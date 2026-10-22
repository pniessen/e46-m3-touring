// List near-misses: text closer than MIN px (SVG units) to another text, a stroke, or a box edge it isn't inside.
//   NODE_PATH=$(npm root -g) node audit.js page.html [MIN]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [p, minArg] = process.argv.slice(2);
  const MIN = parseFloat(minArg || '3');
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await page.goto('file://' + path.resolve(p), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const out = await page.evaluate((MIN) => {
    const svg = document.querySelector('figure.diagram svg');
    const res = [];
    const T = [...svg.querySelectorAll('text')].map(t => { const b = t.getBBox(); const fs = parseFloat(getComputedStyle(t).fontSize); const y = parseFloat(t.getAttribute('y'));
      return { txt: t.textContent, x0: b.x, x1: b.x + b.width, y0: y - 0.70 * fs, y1: y + 0.05 * fs }; });
    const gap = (a, b) => { const dx = Math.max(a.x0 - b.x1, b.x0 - a.x1, 0), dy = Math.max(a.y0 - b.y1, b.y0 - a.y1, 0); return Math.hypot(dx, dy); };
    for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const g = gap(T[i], T[j]); if (g < MIN) res.push(`text~text ${g.toFixed(1)}: "${T[i].txt}" / "${T[j].txt}"`); }
    const G = [...svg.querySelectorAll('line,path,rect,circle')].filter(g => !g.closest('defs') && !(g.getAttribute('class') || '').includes('bg'));
    for (const g of G) {
      const cs = getComputedStyle(g); const sw = cs.stroke !== 'none' ? parseFloat(cs.strokeWidth) : 0; const bb = g.getBBox();
      let len = 0; try { len = g.getTotalLength(); } catch (e) {}
      const pts = []; for (let s = 0; s <= len; s += 1) pts.push(g.getPointAtLength(s));
      for (const which of ['marker-end', 'marker-start']) {
        const m = g.getAttribute(which); if (!m || len === 0) continue;
        const atEnd = which === 'marker-end';
        const tip = g.getPointAtLength(atEnd ? len : 0), back = g.getPointAtLength(atEnd ? Math.max(0, len - 1) : Math.min(len, 1));
        let dx = tip.x - back.x, dy = tip.y - back.y; const dd = Math.hypot(dx, dy) || 1; dx /= dd; dy /= dd;
        const sc = 7 * (sw || 1) / 8, nx = -dy, ny = dx;
        const T = { x: tip.x + dx * 0.5 * sc, y: tip.y + dy * 0.5 * sc }, B = { x: tip.x - dx * 7.5 * sc, y: tip.y - dy * 7.5 * sc };
        for (let u = 0; u <= 1; u += 0.1) for (let v = -1; v <= 1; v += 0.1) { const w = 4 * sc * (1 - u) * v; pts.push({ x: B.x + (T.x - B.x) * u + nx * w, y: B.y + (T.y - B.y) * u + ny * w }); }
      }
      for (const t of T) {
        if (g.tagName === 'rect' && t.x0 >= bb.x && t.x1 <= bb.x + bb.width && t.y0 >= bb.y && t.y1 <= bb.y + bb.height) {
          // inside a box: check distance to its edges
          const m = Math.min(t.x0 - bb.x, bb.x + bb.width - t.x1, t.y0 - bb.y, bb.y + bb.height - t.y1);
          if (m < MIN - 0.5 && bb.width * bb.height > 600) res.push(`in-box ${m.toFixed(1)}: "${t.txt}" in <rect ${g.getAttribute('class')} ${bb.x},${bb.y}>`);
          continue;
        }
        let best = 1e9; for (const q of pts) { const dx = Math.max(t.x0 - q.x, q.x - t.x1, 0), dy = Math.max(t.y0 - q.y, q.y - t.y1, 0); best = Math.min(best, Math.hypot(dx, dy) - sw / 2); }
        if (best < MIN) res.push(`text~${g.tagName}.${g.getAttribute('class')} ${best.toFixed(1)}: "${t.txt}"`);
      }
    }
    return res;
  }, MIN);
  console.log(out.length ? out.join('\n') : 'no near-misses');
  await browser.close();
})();
