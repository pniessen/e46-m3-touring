// Measure each card's height in print layout at a given content width.
const { chromium } = require('playwright');
(async () => {
  const [,, file, widthPx = '739', outJson] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: Number(widthPx), height: 1000 } });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  await page.goto('file://' + file, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);
  const res = await page.evaluate(() => {
    const out = { fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).slice(0, 12), sections: [] };
    document.querySelectorAll('main section').forEach(s => {
      const r = s.getBoundingClientRect();
      const kids = [...s.children].map(c => { const b = c.getBoundingClientRect(); const cs = getComputedStyle(c); return [c.tagName + (c.className ? '.' + c.className : ''), Math.round(b.height), cs.marginTop, cs.marginBottom, (c.textContent || '').trim().slice(0, 40)]; });
      out.sections.push({ id: s.id, h: Math.round(r.height), kids });
    });
    return out;
  });
  console.log(JSON.stringify({ errors, ...res }, null, 1));
  await browser.close();
})();
