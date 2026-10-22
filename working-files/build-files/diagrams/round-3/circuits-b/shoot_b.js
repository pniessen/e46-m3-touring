// Screenshot test pages at 1440x900 (light and dark) and 390 px (light), and check every diagram's text.
//   NODE_PATH=$(npm root -g) node shoot_b.js OUTDIR page1.html [page2.html ...]
// Checks run on the 1440 light render (copied from ../shoot.js): text outside the viewBox, text
// overlapping text, strokes crossing text, text spilling out of its box; plus broken marker refs.
const { chromium } = require('playwright');
const path = require('path');
function checks() {
  const svg = document.querySelector('figure.diagram svg');
  const vb = svg.viewBox.baseVal;
  const out = { issues: [], rendered: svg.getBoundingClientRect().width };
  const texts = [...svg.querySelectorAll('text')];
  const boxes = texts.map(t => {
    const b = t.getBBox();
    const fs = parseFloat(getComputedStyle(t).fontSize);
    const y = parseFloat(t.getAttribute('y'));
    return { t, txt: t.textContent.trim(), x0: b.x, x1: b.x + b.width, y0: y - 0.72 * fs, y1: y + 0.2 * fs, fs, ax: parseFloat(t.getAttribute('x')), ay: y - 0.3 * fs };
  });
  const f = n => n.toFixed(1);
  for (const b of boxes) {
    if (b.x0 < vb.x + 2 || b.x1 > vb.x + vb.width - 2 || b.y0 < vb.y + 1 || b.y1 > vb.y + vb.height - 1)
      out.issues.push(`OUT OF VIEWBOX "${b.txt}" x ${f(b.x0)}..${f(b.x1)} y ${f(b.y0)}..${f(b.y1)}`);
  }
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], c = boxes[j];
    const ox = Math.min(a.x1, c.x1) - Math.max(a.x0, c.x0), oy = Math.min(a.y1, c.y1) - Math.max(a.y0, c.y0);
    if (ox > -1.5 && oy > -1) out.issues.push(`TEXT/TEXT "${a.txt}" vs "${c.txt}" (ox ${f(ox)}, oy ${f(oy)})`);
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
    // arrowheads: sample a small disc just behind each marked end
    for (const which of ['marker-end', 'marker-start']) {
      const m = g.getAttribute(which);
      if (!m || m === 'none' || len === 0) continue;
      const atEnd = which === 'marker-end';
      const tip = g.getPointAtLength(atEnd ? len : 0), back = g.getPointAtLength(atEnd ? Math.max(0, len - 1) : Math.min(len, 1));
      let dx = tip.x - back.x, dy = tip.y - back.y; const d = Math.hypot(dx, dy) || 1; dx /= d; dy /= d;
      const cx = tip.x - dx * 4.5, cy = tip.y - dy * 4.5;
      for (let a = 0; a < 6.28; a += 0.5) for (const r of [0, 2, 3.5]) pts.push({ x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) });
    }
    const bb = g.getBBox();
    const small = filled && bb.width * bb.height < 700 && g.tagName !== 'line';
    for (const b of boxes) {
      const pad = sw / 2 + 0.3;
      let hit = pts.some(p => p.x > b.x0 - pad && p.x < b.x1 + pad && p.y > b.y0 - pad && p.y < b.y1 + pad);
      if (!hit && small) {
        const ox = Math.min(bb.x + bb.width, b.x1) - Math.max(bb.x, b.x0), oy = Math.min(bb.y + bb.height, b.y1) - Math.max(bb.y, b.y0);
        hit = ox > 0 && oy > 0;
      }
      // a label that sits wholly inside its own small cell (pin numbers, badges) is not a crossing
      const inside = b.x0 >= bb.x - 0.5 && b.x1 <= bb.x + bb.width + 0.5 && b.y0 >= bb.y - 1.5 && b.y1 <= bb.y + bb.height + 1.5;
      if (hit && small && inside) hit = false;
      if (hit) {
        const covers = [...svg.querySelectorAll('rect')].filter(r => r !== g && !r.closest('defs')
          && (g.compareDocumentPosition(r) & Node.DOCUMENT_POSITION_FOLLOWING)
          && (() => { const f = getComputedStyle(r).fill; return f && f !== 'none' && !f.startsWith('rgba(0, 0, 0, 0)'); })()
          && (() => { const c = r.getBBox(); return b.x0 >= c.x - 0.5 && b.x1 <= c.x + c.width + 0.5 && b.y0 >= c.y - 1.5 && b.y1 <= c.y + c.height + 1.5; })());
        if (covers.length) hit = false;
      }
      if (hit) {
        const key = g.outerHTML.slice(0, 80) + '|' + b.txt;
        if (!seen.has(key)) { seen.add(key); out.issues.push(`SHAPE/TEXT <${g.tagName} class="${g.getAttribute('class') || ''}"> crosses "${b.txt}"`); }
      }
    }
  }
  // text should sit inside the smallest filled box around its anchor
  const rects = [...svg.querySelectorAll('rect')].filter(r => !(r.getAttribute('class') || '').includes('bg') && !r.closest('defs'))
    .map(r => ({ r, b: r.getBBox(), cls: r.getAttribute('class') || '' })).filter(o => o.b.width * o.b.height > 300);
  for (const b of boxes) {
    const hosts = rects.filter(o => b.ax >= o.b.x && b.ax <= o.b.x + o.b.width && b.ay >= o.b.y && b.ay <= o.b.y + o.b.height)
      .sort((p, q) => p.b.width * p.b.height - q.b.width * q.b.height);
    if (!hosts.length) continue;
    const h = hosts[0].b;
    if (b.x0 < h.x + 3 || b.x1 > h.x + h.width - 3 || b.y0 < h.y + 1.5 || b.y1 > h.y + h.height - 1.5)
      out.issues.push(`SPILLS OUT OF BOX "${b.txt}" (box ${f(h.x)},${f(h.y)} ${f(h.width)}x${f(h.height)}; text x ${f(b.x0)}..${f(b.x1)} y ${f(b.y0)}..${f(b.y1)})`);
  }
  out.minFont = Math.min(...boxes.map(b => b.fs));
  return out;
}


(async () => {
  const [outDir, ...pages] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const runs = [['desk-light', 1440, 'light'], ['desk-dark', 1440, 'dark'], ['phone-light', 390, 'light']];
  for (const [tag, width, scheme] of runs) {
    const ctx = await browser.newContext({ viewport: { width, height: 900 }, deviceScaleFactor: width > 1000 ? 1 : 2, colorScheme: scheme });
    const page = await ctx.newPage();
    for (const p of pages) {
      await page.goto('file://' + path.resolve(p), { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      const fontsOk = await page.evaluate(() => document.fonts.check("13px 'IBM Plex Sans'") && document.fonts.check("13px 'IBM Plex Mono'"));
      const name = path.basename(p, '.html');
      const fig = await page.$('figure.diagram');
      await fig.screenshot({ path: path.join(outDir, `${name}-${tag}.png`) });
      if (tag === 'desk-light') {
        const r = await page.evaluate(checks);
        const mk = await page.evaluate(() => { const s = document.querySelector('figure.diagram svg');
          const ids = new Set([...s.querySelectorAll('[id]')].map(e => e.id));
          const refs = [...s.querySelectorAll('[marker-end],[marker-start]')].flatMap(e => [e.getAttribute('marker-end'), e.getAttribute('marker-start')]).filter(Boolean);
          return refs.filter(u => !ids.has(u.slice(5, -1))).length; });
        console.log(`== ${name}: rendered ${r.rendered.toFixed(0)} px wide, fonts ${fontsOk ? 'loaded' : 'MISSING'}, smallest text ${r.minFont}px, broken markers ${mk}, ${r.issues.length} issue(s)`);
        for (const i of r.issues) console.log('   ' + i);
      }
    }
    await ctx.close();
  }
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
