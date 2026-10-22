const { chromium } = require('playwright');
(async () => {
  const [,, file, w] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: Number(w), height: 1000 } });
  await page.goto('file://' + file, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  console.log(await page.evaluate(() => {
    const c = document.querySelector('footer.colophon'); const cs = getComputedStyle(c);
    const last = document.querySelector('main section:last-of-type');
    const mainWrap = document.querySelector('main .wrap'); const ws = getComputedStyle(mainWrap);
    return JSON.stringify({ colophon: Math.round(c.getBoundingClientRect().height), mt: cs.marginTop, pt: cs.paddingTop,
      wrapPadBottom: ws.paddingBottom, gapAfterLastCard: Math.round(c.getBoundingClientRect().top - last.getBoundingClientRect().bottom) });
  }));
  await browser.close();
})();
