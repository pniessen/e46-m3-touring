// Screenshot landscape test pages at 1440x900 (light, dark) and 390 wide (light, dark), and check
// every diagram's text (adapted from ../shoot.js).
//   NODE_PATH=$(npm root -g) node shoot.js OUTDIR page1.html [page2.html ...]
// Checks (in SVG user units): text outside the viewBox, text overlapping text, any stroke
// (lines, paths, box outlines, arrowheads) crossing text, text spilling out of the box it sits in,
// broken marker references, and the smallest font size.
const { chromium } = require('playwright');
const path = require('path');

function checks() {
  const svg = document.querySelector('figure.diagram svg');
  const vb = svg.viewBox.baseVal;
  const r = svg.getBoundingClientRect();
  const out = { issues: [], rendered: `${r.width.toFixed(0)}x${r.height.toFixed(0)}` };
  const texts = [...svg.querySelectorAll('text')];
  const boxes = texts.map(t => {
    const b = t.getBBox();
    const fs = parseFloat(getComputedStyle(t).fontSize);
    const y = parseFloat(t.getAttribute('y'));
    return { t, txt: t.textContent.trim(), x0: b.x, x1: b.x + b.width, y0: y - 0.72 * fs, y1: y + 0.2 * fs, fs, ax: b.x + 1, ay: y - 0.3 * fs };
  });
  const f = n => n.toFixed(1);
  for (const b of boxes) {
    if (b.x0 < vb.x + 2 || b.x1 > vb.x + vb.width - 2 || b.y0 < vb.y + 1 || b.y1 > vb.y + vb.height - 1)
      out.issues.push(`OUT OF VIEWBOX "${b.txt}" x ${f(b.x0)}..${f(b.x1)} y ${f(b.y0)}..${f(b.y1)}`);
  }
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], c = boxes[j];
    const ox = Math.min(a.x1, c.x1) - Math.max(a.x0, c.x0), oy = Math.min(a.y1, c.y1) - Math.max(a.y0, c.y0);
    if (ox > -2.5 && oy > -1) out.issues.push(`TEXT/TEXT "${a.txt}" vs "${c.txt}" (ox ${f(ox)}, oy ${f(oy)})`);
  }
  const geoms = [...svg.querySelectorAll('line,path,polyline,polygon,rect,circle,ellipse')]
    .filter(g => !g.closest('defs') && !(g.getAttribute('class') || '').split(/\s+/).includes('bg'));
  const seen = new Set();
  for (const g of geoms) {
    const cs = getComputedStyle(g);
    const sw = cs.stroke && cs.stroke !== 'none' ? parseFloat(cs.strokeWidth) || 0 : 0;
    const filled = cs.fill && cs.fill !== 'none' && cs.fill !== 'transparent';
    const pts = [];
    let len = 0;
    try { len = g.getTotalLength(); } catch (e) { len = 0; }
    if (sw > 0 && len > 0) for (let s = 0; s <= len; s += 0.75) pts.push(g.getPointAtLength(s));
    for (const which of ['marker-end', 'marker-start']) {
      const m = g.getAttribute(which);
      if (!m || m === 'none' || len === 0) continue;
      const atEnd = which === 'marker-end';
      const tip = g.getPointAtLength(atEnd ? len : 0), back = g.getPointAtLength(atEnd ? Math.max(0, len - 1) : Math.min(len, 1));
      let dx = tip.x - back.x, dy = tip.y - back.y; const d = Math.hypot(dx, dy) || 1; dx /= d; dy /= d;
      // house marker: viewBox 8x8 drawn at 7x7 stroke widths, refX 7.5: tip 0.5u past the end, base 7.5u behind, half-width 4u
      const sc = 7 * (sw || 1) / 8, nx = -dy, ny = dx;
      const T = { x: tip.x + dx * 0.5 * sc, y: tip.y + dy * 0.5 * sc };
      const B = { x: tip.x - dx * 7.5 * sc, y: tip.y - dy * 7.5 * sc };
      for (let u = 0; u <= 1; u += 0.1) for (let v = -1; v <= 1; v += 0.1) {
        const w = 4 * sc * (1 - u) * v;
        pts.push({ x: B.x + (T.x - B.x) * u + nx * w, y: B.y + (T.y - B.y) * u + ny * w });
      }
    }
    const bb = g.getBBox();
    const small = filled && bb.width * bb.height < 700 && g.tagName !== 'line';
    for (const b of boxes) {
      // a pin cell (or any box) holding its own label is fine
      if (g.tagName === 'rect' && b.x0 >= bb.x + 1 && b.x1 <= bb.x + bb.width - 1 && b.y0 >= bb.y - 0.5 && b.y1 <= bb.y + bb.height + 0.5) continue;
      const pad = sw / 2 + 0.6;
      let hit = pts.some(p => p.x > b.x0 - pad && p.x < b.x1 + pad && p.y > b.y0 - pad && p.y < b.y1 + pad);
      if (!hit && small) {
        const ox = Math.min(bb.x + bb.width, b.x1) - Math.max(bb.x, b.x0), oy = Math.min(bb.y + bb.height, b.y1) - Math.max(bb.y, b.y0);
        hit = ox > 0 && oy > 0;
      }
      if (hit) {
        const key = g.outerHTML.slice(0, 80) + '|' + b.txt;
        if (!seen.has(key)) { seen.add(key); out.issues.push(`SHAPE/TEXT <${g.tagName} class="${g.getAttribute('class') || ''}" ${g.tagName === 'rect' ? `x=${g.getAttribute('x')} y=${g.getAttribute('y')}` : ''}> crosses "${b.txt}"`); }
      }
    }
  }
  const rects = [...svg.querySelectorAll('rect')].filter(r => !(r.getAttribute('class') || '').includes('bg') && !r.closest('defs'))
    .map(r => ({ r, b: r.getBBox(), cls: r.getAttribute('class') || '' })).filter(o => o.b.width * o.b.height > 500);
  for (const b of boxes) {
    const hosts = rects.filter(o => b.ax >= o.b.x && b.ax <= o.b.x + o.b.width && b.ay >= o.b.y && b.ay <= o.b.y + o.b.height)
      .sort((p, q) => p.b.width * p.b.height - q.b.width * q.b.height);
    if (!hosts.length) continue;
    const h = hosts[0].b;
    if (b.x0 < h.x + 3 || b.x1 > h.x + h.width - 3 || b.y0 < h.y + 1.5 || b.y1 > h.y + h.height - 1.5)
      out.issues.push(`SPILLS OUT OF BOX "${b.txt}" (box ${f(h.x)},${f(h.y)} ${f(h.width)}x${f(h.height)}; text x ${f(b.x0)}..${f(b.x1)} y ${f(b.y0)}..${f(b.y1)})`);
  }
  const ids = new Set([...svg.querySelectorAll('[id]')].map(e => e.id));
  for (const e of svg.querySelectorAll('[marker-end],[marker-start]')) for (const a of ['marker-end', 'marker-start']) {
    const u = e.getAttribute(a); if (u && !ids.has(u.slice(5, -1))) out.issues.push(`BROKEN MARKER ${u}`);
  }
  out.minFont = Math.min(...boxes.map(b => b.fs));
  out.hasStyle = !!svg.querySelector('style'); out.hasBg = !!svg.querySelector('rect.bg');
  return out;
}

(async () => {
  const [outDir, ...pages] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const views = [
    { tag: 'desk', w: 1440, h: 900, dsf: 1 },
    { tag: 'phone', w: 390, h: 900, dsf: 2 },
  ];
  for (const v of views) for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: v.w, height: v.h }, deviceScaleFactor: v.dsf, colorScheme: scheme });
    const page = await ctx.newPage();
    for (const p of pages) {
      await page.goto('file://' + path.resolve(p), { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      const fontsOk = await page.evaluate(() => document.fonts.check("13px 'IBM Plex Sans'") && document.fonts.check("13px 'IBM Plex Mono'"));
      const name = path.basename(p, '.html');
      const fig = await page.$('figure.diagram');
      await fig.scrollIntoViewIfNeeded();
      await fig.screenshot({ path: path.join(outDir, `${name}-${v.tag}-${scheme}.png`) });
      if (v.tag === 'phone' && scheme === 'light') {
        await page.$eval('.diagram-scroll', el => { el.scrollLeft = el.scrollWidth; });
        await fig.screenshot({ path: path.join(outDir, `${name}-${v.tag}-${scheme}-right.png`) });
      }
      if (scheme === 'light') {
        const r = await page.evaluate(checks);
        console.log(`== ${name} [${v.tag}]: rendered ${r.rendered}, fonts ${fontsOk ? 'loaded' : 'MISSING'}, smallest text ${r.minFont}px, style ${r.hasStyle} bg ${r.hasBg}, ${r.issues.length} issue(s)`);
        if (v.tag === 'desk') for (const i of r.issues) console.log('   ' + i);
      }
    }
    await ctx.close();
  }
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
