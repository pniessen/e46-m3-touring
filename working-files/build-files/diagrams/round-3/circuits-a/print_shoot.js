const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await browser.newContext({ viewport: { width: 740, height: 1000 }, deviceScaleFactor: 1.5 });
  const page = await ctx.newPage();
  await page.goto('file://' + path.resolve('e2e/wiring.html'), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  for (const f of await page.$$('figure.diagram')) {
    const cap = await f.$eval('figcaption', c => c.textContent.trim());
    const key = cap.includes('Sport button') ? '20' : cap.includes('brake-light switch and the clutch') ? '21' : cap.includes('three warning lamps') ? '22' : null;
    if (!key) continue;
    await f.scrollIntoViewIfNeeded();
    await f.screenshot({ path: `e2e/fig${key}-print.png` });
    const w = await f.evaluate(el => { const s = el.querySelector('svg'); const r = s.getBoundingClientRect(); return `${Math.round(r.width)}x${Math.round(r.height)} scale ${(r.width / 800).toFixed(2)}`; });
    console.log('print', key, w);
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
