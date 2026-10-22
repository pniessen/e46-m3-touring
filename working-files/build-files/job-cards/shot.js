// Screenshot given cards in print layout at a given width.
const { chromium } = require('playwright');
(async () => {
  const [,, file, widthPx, outPrefix, ...ids] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: Number(widthPx), height: 1000 }, deviceScaleFactor: 1 });
  await page.goto('file://' + file, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  for (const id of ids) {
    const el = await page.$('#' + id);
    await el.screenshot({ path: `${outPrefix}-${id}.png` });
    console.log(`${outPrefix}-${id}.png`);
  }
  await browser.close();
})();
