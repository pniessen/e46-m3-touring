// Measure the advance width of words with the site's CSS and fonts (and with the SVG's own
// <style> block, as a standalone file renders), for the flow generators' line wrapping.
//   NODE_PATH=$(npm root -g) node measure_words.js in.json out.json
// in.json: [[fontKey, text], ...] where fontKey is a space-separated class list (t, t-sm, t-b, t-mono, t-h).
// out.json: {"page": {"fontKey|text": width}, "solo": {...}}
const { chromium } = require('playwright');
const fs = require('fs');
const FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">';
(async () => {
  const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const css = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/tools/page.css', 'utf8');
  const svgSrc = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/diagrams/04-fuel-pressure.svg', 'utf8');
  const soloStyle = svgSrc.match(/<style>[\s\S]*?<\/style>/)[0];
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const texts = items.map(([c, t], i) => `<text class="${c}" x="0" y="${20 + i * 20}" xml:space="preserve">${esc(t)}</text>`).join('');
  const h = items.length * 20 + 40;
  const pageHtml = `${FONTS}<style>${css}</style><figure class="diagram"><div class="diagram-scroll"><svg viewBox="0 0 4000 ${h}" style="width:4000px;min-width:0;max-width:none">${texts}</svg></div></figure>`;
  const soloHtml = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4000 ${h}" width="4000" height="${h}">${soloStyle}${texts}</svg>`;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const out = {};
  for (const [name, html] of [['page', pageHtml], ['solo', soloHtml]]) {
    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: 'networkidle' });
    if (name === 'page') await page.evaluate(() => Promise.all(["13px 'IBM Plex Sans'", "600 13px 'IBM Plex Sans'", "13px 'IBM Plex Mono'", "700 15px 'Saira Condensed'"].map(f => document.fonts.load(f))));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(200);
    if (name === 'page') {
      const ok = await page.evaluate(() => [document.fonts.check("13px 'IBM Plex Sans'"), document.fonts.check("600 13px 'IBM Plex Sans'"), document.fonts.check("13px 'IBM Plex Mono'"), document.fonts.check("700 15px 'Saira Condensed'")]);
      if (ok.includes(false)) { console.error('FONTS NOT LOADED', ok); process.exit(2); }
    }
    const w = await page.evaluate(() => [...document.querySelectorAll('svg text')].map(t => t.getComputedTextLength()));
    out[name] = {};
    items.forEach(([c, t], i) => { out[name][c + '|' + t] = w[i]; });
    await page.close();
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out));
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
