const { chromium } = require('playwright');
(async () => {
  const [,, file, outDir] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  const page = await ctx.newPage();
  await page.goto('file://' + file, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: outDir + '/phone-top2.png' });
  const t = await page.$('#card-12d-alignment-and-final-coding .table-wrap:nth-of-type(2)');
  await page.evaluate(() => document.querySelector('#card-12d-alignment-and-final-coding').scrollIntoView({behavior: 'instant'}));
  await page.evaluate(() => window.scrollBy({top: 760, behavior: 'instant'}));
  await page.waitForTimeout(400); await page.screenshot({ path: outDir + '/phone-12d.png' });
  await browser.close();
})();
