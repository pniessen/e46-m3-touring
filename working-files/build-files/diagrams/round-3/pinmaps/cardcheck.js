const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  for (const p of process.argv.slice(2)) {
    await page.goto('file://' + path.resolve(p), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate(() => {
      const svg = document.querySelector('figure.diagram svg');
      const out = [];
      for (const t of svg.querySelectorAll('text')) {
        const b = t.getBBox();
        const x = parseFloat(t.getAttribute('x'));
        if (x < 400 && b.x + b.width > 380) out.push(`${(b.x + b.width).toFixed(1)}  ${t.textContent.slice(0, 70)}`);
        if (b.x + b.width > 785) out.push(`RIGHT EDGE ${(b.x + b.width).toFixed(1)}  ${t.textContent.slice(0, 70)}`);
      }
      return out;
    });
    console.log('==', path.basename(p)); r.forEach(l => console.log('  ', l));
  }
  await browser.close();
})();
