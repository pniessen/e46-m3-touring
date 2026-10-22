// Measure label widths with the site's CSS and fonts.  node measure.js labels.txt
// labels.txt lines: "class|text"
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const lines = fs.readFileSync(process.argv[2], 'utf8').split('\n').filter(Boolean).map(l => { const i = l.indexOf('|'); return [l.slice(0, i), l.slice(i + 1)]; });
  const css = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/tools/page.css', 'utf8');
  const texts = lines.map(([c, t], i) => `<text class="${c}" x="0" y="${20 + i * 20}">${t.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</text>`).join('');
  const html = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap"><style>${css}</style><figure class="diagram"><div class="diagram-scroll portrait"><svg viewBox="0 0 2000 ${lines.length * 20 + 40}" style="width:2000px;min-width:0;max-width:none">${texts}</svg></div></figure>`;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const w = await page.evaluate(() => [...document.querySelectorAll('svg text')].map(t => t.getBBox().width));
  lines.forEach(([c, t], i) => console.log(w[i].toFixed(1).padStart(6), c.padEnd(16), t));
  await browser.close();
})();
