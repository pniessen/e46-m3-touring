const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const page_ = path.resolve('e2e/wiring.html');
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  for (const v of [{ w: 1440, h: 900, tag: 'desk', dsf: 1 }, { w: 390, h: 900, tag: 'phone', dsf: 2 }]) for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: v.w, height: v.h }, deviceScaleFactor: v.dsf, colorScheme: scheme });
    const page = await ctx.newPage();
    await page.goto('file://' + page_, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    for (const f of await page.$$('figure.diagram')) {
      const cap = await f.$eval('figcaption', c => c.textContent.trim());
      const key = cap.includes('Sport button') ? '20' : cap.includes('brake-light switch and the clutch') ? '21' : cap.includes('three warning lamps') ? '22' : null;
      if (!key) continue;
      await f.scrollIntoViewIfNeeded();
      await f.screenshot({ path: `e2e/fig${key}-${v.tag}-${scheme}.png` });
      const info = await f.evaluate(el => { const s = el.querySelector('svg'); const r = s.getBoundingClientRect();
        const markers = [...s.querySelectorAll('[marker-end],[marker-start]')].map(e => e.getAttribute('marker-end') || e.getAttribute('marker-start'));
        const ids = new Set([...document.querySelectorAll('[id]')].map(e => e.id));
        const broken = markers.filter(u => !ids.has(u.slice(5, -1)));
        const hint = el.querySelector('.scroll-hint'); const hs = hint ? getComputedStyle(hint).display : 'none';
        return `${Math.round(r.width)}x${Math.round(r.height)} markers=${markers.length} broken=${broken.length} style=${!!s.querySelector('style')} bg=${!!s.querySelector('rect.bg')} hint=${hs}`; });
      if (scheme === 'light') console.log(v.tag, key, info);
    }
    await ctx.close();
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
