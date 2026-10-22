const { chromium } = require('playwright');
(async () => {
  const [,, file, widthPx, ...ids] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: Number(widthPx), height: 1000 } });
  await page.goto('file://' + file, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  const out = await page.evaluate((ids) => ids.map(id => {
    const s = document.getElementById(id);
    return [id, [...s.children].map(c => {
      const b = c.getBoundingClientRect();
      let extra = '';
      if (c.classList.contains('table-wrap')) extra = ' rows:' + [...c.querySelectorAll('tr')].map(r => Math.round(r.getBoundingClientRect().height)).join(',');
      if (c.tagName === 'UL') extra = ' items:' + [...c.querySelectorAll('li')].map(r => Math.round(r.getBoundingClientRect().height)).join(',');
      return `${c.tagName}${c.className ? '.' + c.className : ''} h=${Math.round(b.height)}${extra} | ${(c.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50)}`;
    })];
  }), ids);
  for (const [id, kids] of out) { console.log('##', id); kids.forEach(k => console.log('  ', k)); }
  await browser.close();
})();
