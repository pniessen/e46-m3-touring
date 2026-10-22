// Load every page of the built site at phone width: JS errors, failed requests, sideways overflow, figure counts.
const { chromium } = require('playwright');
(async () => {
  const [,, siteDir, outDir] = process.argv;
  const pages = require('fs').readdirSync(siteDir).filter(f => f.endsWith('.html') && f !== '404.html').sort();
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const name of pages) {
    const errors = [];
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
    const p = await ctx.newPage();
    p.on('pageerror', e => errors.push('pageerror: ' + e));
    p.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
    p.on('requestfailed', r => { if (!r.url().startsWith('http')) errors.push('requestfailed: ' + r.url().slice(-80)); });
    const t0 = Date.now();
    await p.goto('file://' + siteDir + '/' + name, { waitUntil: 'load', timeout: 120000 });
    const loadMs = Date.now() - t0;
    const m = await p.evaluate(() => {
      const de = document.documentElement, W = window.innerWidth;
      const wide = [...document.querySelectorAll('main *')].filter(e => {
        const r = e.getBoundingClientRect();
        return r.width > 0 && r.right > W + 1 && !e.closest('.table-wrap') && !e.closest('.diagram-scroll') && !e.closest('pre');
      }).map(e => e.tagName + '.' + e.className + ' "' + (e.textContent || '').trim().slice(0, 50) + '"').slice(0, 8);
      return {
        scrollWidth: de.scrollWidth, W,
        diagrams: document.querySelectorAll('figure.diagram svg').length,
        figuresNoSvg: [...document.querySelectorAll('figure.diagram')].filter(f => !f.querySelector('svg')).length,
        brokenImgs: [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(-60)),
        leftoverPlaceholders: (document.body.innerHTML.match(/figure: proposed-/g) || []).length,
        rawMd: (document.querySelector('main').innerText.match(/\]\(#|\*\*\w/g) || []).length,
        wide,
      };
    });
    console.log(name, 'load', loadMs + 'ms', JSON.stringify(m), errors.length ? 'ERRORS ' + JSON.stringify(errors.slice(0, 5)) : 'no errors');
    await ctx.close();
  }
  await browser.close();
})();
