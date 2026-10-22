// Load job-cards.html from the built site: JS errors, phone-width overflow, fields, screenshots and PDFs.
const { chromium } = require('playwright');
(async () => {
  const [,, siteDir, outDir] = process.argv;
  const url = 'file://' + siteDir + '/job-cards.html';
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const errors = [];
  // Phone
  const phone = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  phone.on('pageerror', e => errors.push('pageerror: ' + e));
  phone.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  phone.on('requestfailed', r => errors.push('requestfailed: ' + r.url() + ' ' + (r.failure() || {}).errorText));
  await phone.goto(url, { waitUntil: 'networkidle' });
  await phone.evaluate(() => document.fonts.ready);
  const m = await phone.evaluate(() => {
    const de = document.documentElement;
    const wide = [...document.querySelectorAll('main *')].filter(e => {
      const r = e.getBoundingClientRect(); return r.right > window.innerWidth + 1 && !e.closest('.table-wrap');
    }).map(e => e.tagName + '.' + e.className + ' ' + (e.textContent || '').trim().slice(0, 40)).slice(0, 10);
    return {
      innerWidth: window.innerWidth, scrollWidth: de.scrollWidth, bodyScroll: document.body.scrollWidth,
      sections: document.querySelectorAll('main section').length,
      fields: document.querySelectorAll('input.fill').length,
      emptyCellsLeft: [...document.querySelectorAll('main td')].filter(td => !td.textContent.trim() && !td.children.length).length,
      checkboxes: document.querySelectorAll('ul.task-list input[type=checkbox]').length,
      disabled: document.querySelectorAll('ul.task-list input[type=checkbox]:disabled').length,
      readingHeads: [...document.querySelectorAll('thead th:last-child')].filter(th => th.textContent.trim() === 'Reading').length,
      wideElems: wide,
      tableWraps: [...document.querySelectorAll('.table-wrap')].filter(w => w.scrollWidth > w.clientWidth + 1).length,
    };
  });
  console.log('PHONE', JSON.stringify(m));
  // Interaction: tick a box and type a reading, reload, check it persisted
  await phone.check('ul.task-list input[type=checkbox] >> nth=0');
  await phone.fill('input.fill >> nth=0', '12.1');
  await phone.reload({ waitUntil: 'networkidle' });
  const persisted = await phone.evaluate(() => [document.querySelector('ul.task-list input[type=checkbox]').checked, document.querySelector('input.fill').value]);
  console.log('PERSIST', JSON.stringify(persisted));
  await phone.evaluate(() => localStorage.clear());
  await phone.reload({ waitUntil: 'networkidle' });
  await phone.screenshot({ path: outDir + '/phone-top.png' });
  await (await phone.$('#card-7b-rear-axle-in')).scrollIntoViewIfNeeded();
  await phone.screenshot({ path: outDir + '/phone-7b.png' });
  // Desktop + PDFs
  const desk = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  desk.on('pageerror', e => errors.push('desk pageerror: ' + e));
  desk.on('console', m => { if (m.type() === 'error') errors.push('desk console: ' + m.text()); });
  await desk.goto(url, { waitUntil: 'networkidle' });
  await desk.evaluate(() => document.fonts.ready);
  await desk.screenshot({ path: outDir + '/desk-top.png' });
  for (const [name, fmt, margin] of [['letter-0.4', 'Letter', '0.4in'], ['letter-0.5', 'Letter', '0.5in'], ['a4-0.4', 'A4', '0.4in'], ['letter-0', 'Letter', '0']]) {
    await desk.pdf({ path: `${outDir}/cards-${name}.pdf`, format: fmt, printBackground: true, margin: { top: margin, bottom: margin, left: margin, right: margin } });
    console.log('PDF', name);
  }
  console.log('ERRORS', JSON.stringify(errors));
  await browser.close();
})();
