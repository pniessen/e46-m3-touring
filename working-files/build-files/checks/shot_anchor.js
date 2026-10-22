// Screenshot a page at phone width, scrolled to an element, in light and dark.
const { chromium } = require('playwright');
(async () => {
  const [,, file, selector, outPrefix, extraScroll] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: scheme });
    const p = await ctx.newPage();
    await p.goto('file://' + file, { waitUntil: 'load', timeout: 120000 });
    await p.evaluate(() => document.fonts.ready);
    const ok = await p.evaluate((sel) => { const e = document.querySelector(sel); if (!e) return false; e.scrollIntoView({ block: 'start', behavior: 'instant' }); return true; }, selector);
    if (!ok) { console.log('not found', selector); break; }
    if (extraScroll) await p.evaluate((d) => window.scrollBy({ top: +d, behavior: 'instant' }), extraScroll);
    await p.waitForTimeout(300);
    await p.screenshot({ path: `${outPrefix}-${scheme}.png` });
    await ctx.close();
  }
  await browser.close();
})();
