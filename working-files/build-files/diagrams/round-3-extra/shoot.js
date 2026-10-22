// Screenshot a test page's figure at phone width in light and dark, and report text problems.
//   NODE_PATH=$(npm root -g) node shoot.js page.html outprefix [width]
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [page_html, prefix, widthArg] = process.argv.slice(2);
  const width = parseInt(widthArg || '390', 10);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width, height: 900 }, deviceScaleFactor: 2, colorScheme: scheme });
    const page = await ctx.newPage();
    await page.goto('file://' + path.resolve(page_html));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const fig = await page.$('figure.diagram');
    await fig.screenshot({ path: `${prefix}-${scheme}-${width}.png` });
    if (scheme === 'light') {
      const report = await page.evaluate(() => {
        const svg = document.querySelector('figure.diagram svg');
        const vb = svg.viewBox.baseVal;
        const texts = Array.from(svg.querySelectorAll('text'));
        // Map each text's bbox from its own user space into the root viewBox space (handles <g transform>).
        const rootInv = svg.getScreenCTM().inverse();
        const boxes = texts.map((t) => {
          const b = t.getBBox();
          const m = rootInv.multiply(t.getScreenCTM());
          const pts = [[b.x, b.y], [b.x + b.width, b.y], [b.x, b.y + b.height], [b.x + b.width, b.y + b.height]].map(([x, y]) => {
            const p = new DOMPoint(x, y).matrixTransform(m);
            return [p.x, p.y];
          });
          const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]);
          const x0 = Math.min(...xs), y0 = Math.min(...ys);
          return { s: t.textContent.trim(), x: x0, y: y0, w: Math.max(...xs) - x0, h: Math.max(...ys) - y0, cls: t.getAttribute('class') || '' };
        });
        const out = [];
        for (const b of boxes) {
          if (b.x < vb.x - 0.5 || b.y < vb.y - 0.5 || b.x + b.w > vb.x + vb.width + 0.5 || b.y + b.h > vb.y + vb.height + 0.5) {
            out.push(`OUTSIDE viewBox: "${b.s}" x=${b.x.toFixed(1)}..${(b.x + b.w).toFixed(1)} y=${b.y.toFixed(1)}..${(b.y + b.h).toFixed(1)}`);
          } else if (b.x < vb.x + 7.5 || b.x + b.w > vb.x + vb.width - 7.5) {
            out.push(`MARGIN (<8px): "${b.s}" x=${b.x.toFixed(1)}..${(b.x + b.w).toFixed(1)}`);
          }
        }
        const widest = boxes.slice().sort((a, b) => (b.x + b.w) - (a.x + a.w)).slice(0, 4)
          .map((b) => `${(b.x + b.w).toFixed(1)} "${b.s}"`);
        out.push('rightmost text edges: ' + widest.join(' | '));
        // Text-on-text overlaps (shrink boxes slightly: glyph boxes include line gap).
        for (let i = 0; i < boxes.length; i++) {
          for (let j = i + 1; j < boxes.length; j++) {
            const a = boxes[i], c = boxes[j];
            const ix = Math.min(a.x + a.w, c.x + c.w) - Math.max(a.x, c.x);
            const iy = Math.min(a.y + a.h, c.y + c.h) - Math.max(a.y, c.y);
            if (ix > 0.5 && iy > 2.0) out.push(`OVERLAP: "${a.s}" / "${c.s}" (${ix.toFixed(1)} x ${iy.toFixed(1)})`);
          }
        }
        const sizes = {};
        for (const t of texts) {
          const fs = parseFloat(getComputedStyle(t).fontSize);
          sizes[fs] = (sizes[fs] || 0) + 1;
        }
        const r = svg.getBoundingClientRect();
        return { svgWidthPx: r.width.toFixed(1), svgHeightPx: r.height.toFixed(1), fontSizes: sizes, problems: out,
                 fontsLoaded: Array.from(document.fonts).filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight) };
      });
      console.log(JSON.stringify(report, null, 1));
    }
    await ctx.close();
  }
  await browser.close();
})();
