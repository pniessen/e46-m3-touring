// Zoomed crop of a figure region in SVG units:  node zoom.js page.html out.png x y w h [dark]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [pg, out, x, y, w, h, dark] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2.5, colorScheme: dark ? 'dark' : 'light' });
  const page = await ctx.newPage();
  await page.goto('file://' + path.resolve(pg), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const r = await page.evaluate(() => { const s = document.querySelector('figure.diagram svg'); const b = s.getBoundingClientRect(); return { x: b.x + scrollX, y: b.y + scrollY, k: b.width / s.viewBox.baseVal.width }; });
  await page.screenshot({ path: out, fullPage: true, clip: { x: r.x + x * r.k, y: r.y + y * r.k, width: w * r.k, height: h * r.k } });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
