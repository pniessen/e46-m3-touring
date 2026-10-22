// Zoomed crop of a region of the inlined figure, in SVG user units.  node zoom.js page.html out.png x y w h [dark]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [page_, out, x, y, w, h, dark] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 3, colorScheme: dark ? 'dark' : 'light' });
  const page = await ctx.newPage();
  await page.goto('file://' + path.resolve(page_), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const r = await page.evaluate(([x, y, w, h]) => {
    const svg = document.querySelector('figure.diagram svg');
    svg.scrollIntoView();
    const b = svg.getBoundingClientRect(); const vb = svg.viewBox.baseVal; const s = b.width / vb.width;
    return { x: b.x + x * s, y: b.y + y * s, width: w * s, height: h * s };
  }, [+x, +y, +w, +h]);
  await page.screenshot({ path: out, clip: r });
  await browser.close();
})();
