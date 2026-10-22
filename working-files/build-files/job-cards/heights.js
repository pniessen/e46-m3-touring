// Print-layout height of each card (section) at a given content width; flags cards taller than the page box.
const { chromium } = require('playwright');
(async () => {
  const [,, file, widthPx = '739', limitPx = '979'] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: Number(widthPx), height: 1000 } });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  await page.goto('file://' + file, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  const rows = await page.evaluate(() => [...document.querySelectorAll('main section')].map(s => {
    const kids = [...s.children];
    const first = kids[0].getBoundingClientRect().top - parseFloat(getComputedStyle(kids[0]).marginTop);
    const last = kids[kids.length - 1].getBoundingClientRect().bottom;
    return [s.querySelector('h2').textContent.trim(), Math.round(last - first)];
  }));
  const limit = Number(limitPx);
  for (const [t, h] of rows) console.log(String(h).padStart(5), h > limit ? 'OVER ' + (h - limit) : '     ', t);
  if (errors.length) console.log('ERRORS', errors);
  await browser.close();
})();
