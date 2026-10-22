// Browser checks for the split guide: old-anchor forwarding, search, chapter bar state.
const { chromium } = require('playwright');
(async () => {
  const [,, site, out] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  const errors = [];
  p.on('pageerror', e => errors.push(String(e)));
  // 1. Old bookmark into the one-page guide forwards to the chapter page.
  for (const id of ['phase-7-fit-the-m3-rear-axle-and-fuel-system', 'massachusetts', '325xi-rear-drive-or-all-wheel-drive', 'torque-values', 'fuel-system']) {
    await p.goto(`file://${site}/index.html#${id}`);
    await p.waitForTimeout(400);
    console.log('forward', id, '->', p.url().split('/').pop());
  }
  // 2. Chapter bar: the current page is marked; the pager is there.
  await p.goto(`file://${site}/fuel-cooling-and-ac.html`);
  console.log('current chip:', await p.$eval('.chapters a[aria-current="page"]', a => a.textContent));
  console.log('pager:', await p.$$eval('.pager a', as => as.map(a => a.textContent + ' -> ' + a.getAttribute('href'))));
  // 3. Search from a chapter page.
  for (const q of ['11137519432', 'strut top nuts', 'K96 pin', 'push rod']) {
    await p.click('.chapters .search-open');
    await p.fill('.search-q', q);
    await p.waitForTimeout(600);
    await p.waitForFunction(() => /result|Nothing/.test(document.querySelector('.search-status').textContent), null, { timeout: 15000 });
    const status = await p.textContent('.search-status');
    const first = await p.$$eval('.search-results a', as => as.slice(0, 3).map(a => a.querySelector('.where').textContent + ' | ' + a.querySelector('.head').textContent + ' | ' + a.getAttribute('href')));
    console.log(`search "${q}": ${status}`, JSON.stringify(first));
    if (q === 'strut top nuts') await p.screenshot({ path: out + '/search-panel.png' });
    await p.click('.search-close');
  }
  // 4. A result takes you to the right place.
  await p.click('.chapters .search-open');
  await p.fill('.search-q', '11137519432');
  await p.waitForTimeout(600);
  await p.waitForSelector('.search-results a');
  await Promise.all([p.waitForLoadState('load'), p.click('.search-results a')]);
  await p.waitForTimeout(500);
  console.log('after click:', p.url().split('/').pop(), 'panel hidden:', await p.$eval('.search-panel', el => el.hidden));
  console.log('page errors:', errors.length ? errors : 'none');
  await b.close();
})();
