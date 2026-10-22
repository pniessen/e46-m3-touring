const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage();
  const html = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap"><p style="font-family:'IBM Plex Sans'">Hello</p><p style="font-family:'Saira Condensed';font-weight:700">HELLO</p>`;
  await page.setContent(html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const r = await page.evaluate(() => [...document.fonts].map(f => f.family + ' ' + f.weight + ' ' + f.status).filter(s => !s.includes('unloaded')));
  console.log(r.join('\n'));
  console.log(await page.evaluate(() => document.fonts.check("13px 'IBM Plex Sans'") + ' ' + document.fonts.check("700 15px 'Saira Condensed'")));
  await browser.close();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
