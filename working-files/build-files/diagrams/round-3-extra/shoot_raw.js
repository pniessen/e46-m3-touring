// Screenshot an SVG file on its own (as GitHub shows it: own <style>, no web fonts) and report text problems.
//   NODE_PATH=$(npm root -g) node shoot_raw.js file.svg out.png
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const [svgFile, outPng] = process.argv.slice(2);
  const svgText = fs.readFileSync(svgFile, 'utf8');
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await browser.newContext({ viewport: { width: 400, height: 800 }, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  await page.setContent(`<!doctype html><html><body style="margin:0;background:#fff">${svgText}</body></html>`);
  await page.waitForTimeout(200);
  const svg = await page.$('svg');
  await svg.screenshot({ path: outPng });
  const report = await page.evaluate(() => {
    const svg = document.querySelector('svg');
    svg.style.width = '400px';
    const vb = svg.viewBox.baseVal;
    const rootInv = svg.getScreenCTM().inverse();
    const boxes = Array.from(svg.querySelectorAll('text')).map((t) => {
      const b = t.getBBox();
      const m = rootInv.multiply(t.getScreenCTM());
      const pts = [[b.x, b.y], [b.x + b.width, b.y + b.height]].map(([x, y]) => new DOMPoint(x, y).matrixTransform(m));
      return { s: t.textContent.trim(), x: pts[0].x, y: pts[0].y, w: pts[1].x - pts[0].x, h: pts[1].y - pts[0].y };
    });
    const out = [];
    for (const b of boxes) {
      if (b.x < 0 || b.x + b.w > vb.width || b.y < 0 || b.y + b.h > vb.height) out.push(`OUTSIDE: "${b.s}" ${b.x.toFixed(1)}..${(b.x + b.w).toFixed(1)}`);
    }
    for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
      const a = boxes[i], c = boxes[j];
      const ix = Math.min(a.x + a.w, c.x + c.w) - Math.max(a.x, c.x);
      const iy = Math.min(a.y + a.h, c.y + c.h) - Math.max(a.y, c.y);
      if (ix > 0.5 && iy > 2.0) out.push(`OVERLAP: "${a.s}" / "${c.s}"`);
    }
    const widest = boxes.slice().sort((a, b) => (b.x + b.w) - (a.x + a.w)).slice(0, 3).map((b) => `${(b.x + b.w).toFixed(1)} "${b.s}"`);
    out.push('rightmost: ' + widest.join(' | '));
    return out;
  });
  console.log(report.join('\n'));
  await browser.close();
})();
