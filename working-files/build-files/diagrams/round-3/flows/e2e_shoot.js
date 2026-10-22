const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, colorScheme: scheme });
    const page = await ctx.newPage();
    await page.goto('file://' + path.resolve('e2e/wiring.html'), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const figs = await page.$$('figure.diagram');
    let i = 0;
    for (const f of figs) {
      i++;
      await f.scrollIntoViewIfNeeded();
      await f.screenshot({ path: `e2e/fig${i}-${scheme}.png` });
      const info = await f.evaluate(el => { const s = el.querySelector('svg'); const r = s.getBoundingClientRect();
        const refs = [...s.querySelectorAll('[marker-end]')].map(e => e.getAttribute('marker-end'));
        const ids = new Set([...document.querySelectorAll('[id]')].map(e => e.id));
        const broken = refs.filter(u => !ids.has(u.slice(5, -1)));
        return `${Math.round(r.width)}x${Math.round(r.height)} arrows=${refs.length} broken=${broken.length} style=${!!s.querySelector('style')} bg=${!!s.querySelector('rect.bg')} cap="${el.querySelector('figcaption').textContent.slice(0, 50)}"`; });
      console.log(scheme, i, info);
    }
    await ctx.close();
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
