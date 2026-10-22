const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const scheme of ['light', 'dark']) {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 1000 }, deviceScaleFactor: 2, colorScheme: scheme });
    const page = await ctx.newPage();
    await page.goto('file://' + path.resolve('e2e/page.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(400);
    for (const [key, start] of [['14', 'Two plan views'], ['15', 'A typical 24-month']]) {
      const handle = await page.evaluateHandle((s) => {
        const svg = Array.from(document.querySelectorAll('figure.diagram svg')).find((e) => (e.getAttribute('aria-label') || '').startsWith(s));
        return svg.closest('figure');
      }, start);
      await handle.asElement().scrollIntoViewIfNeeded();
      await handle.asElement().screenshot({ path: `e2e-desk-${key}-${scheme}.png` });
      const info = await handle.asElement().evaluate((fig) => {
        const s = fig.querySelector('svg').getBoundingClientRect();
        const sc = fig.querySelector('.diagram-scroll');
        return { svgW: s.width, svgH: Math.round(s.height), scrollW: sc.scrollWidth, clientW: sc.clientWidth,
                 sectionId: fig.closest('section') ? fig.closest('section').id : null };
      });
      console.log(scheme, key, JSON.stringify(info));
    }
    await ctx.close();
  }
  await browser.close();
})();
