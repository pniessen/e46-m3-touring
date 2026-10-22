const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const page_ = path.resolve('e2e/guide.html');
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 900 }, deviceScaleFactor: 2, colorScheme: scheme });
    const page = await ctx.newPage();
    await page.goto('file://' + page_, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const figs = await page.$$('figure.diagram');
    for (const f of figs) {
      const cap = await f.$eval('figcaption', c => c.textContent.trim().slice(0, 12));
      const m = cap.match(/Figure (T1\d|6)\./);
      if (!m) continue;
      await f.scrollIntoViewIfNeeded();
      await f.screenshot({ path: `e2e/fig${m[1]}-${scheme}.png` });
      const info = await f.evaluate(el => { const s = el.querySelector('svg'); const r = s.getBoundingClientRect();
        const markers = [...s.querySelectorAll('[marker-end]')].map(e => e.getAttribute('marker-end'));
        const ids = new Set([...s.querySelectorAll('[id]')].map(e => e.id));
        const broken = markers.filter(u => !ids.has(u.slice(5, -1)));
        return `${Math.round(r.width)}x${Math.round(r.height)} markers=${markers.length} broken=${broken.length} hasStyle=${!!s.querySelector('style')} hasBg=${!!s.querySelector('rect.bg')}`; });
      console.log(scheme, m[1], info);
    }
    await ctx.close();
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
