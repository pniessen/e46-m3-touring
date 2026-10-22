// Measure label widths twice: with the site's page.css (fonts from Google Fonts, as the page
// loads them) and with the SVG's own <style> block (as a standalone file renders).
//   node measure_cache.js requests.txt cache.json      (lines: "class|text")
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [reqFile, cacheFile] = process.argv.slice(2);
  const lines = fs.readFileSync(reqFile, 'utf8').split('\n').filter(Boolean).map(l => { const i = l.indexOf('|'); return [l.slice(0, i), l.slice(i + 1)]; });
  const cache = fs.existsSync(cacheFile) ? JSON.parse(fs.readFileSync(cacheFile, 'utf8')) : {};
  const css = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/tools/page.css', 'utf8');
  const svgSrc = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/diagrams/04-fuel-pressure.svg', 'utf8');
  const style = svgSrc.match(/<style>[\s\S]*?<\/style>/)[0];
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const texts = lines.map(([c, t], i) => `<text class="${c}" x="0" y="${20 + i * 20}">${esc(t)}</text>`).join('');
  const H = lines.length * 20 + 40;
  // force every font face the diagrams use to load (unused faces never load)
  const probe = `<text class="t-h" x="0" y="${H + 20}">PROBE</text><text class="t t-b" x="0" y="${H + 40}">probe</text><text class="t t-mono" x="0" y="${H + 60}">probe</text><text class="t t-mono t-b" x="0" y="${H + 80}">probe</text>`;
  const fonts = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">`;
  const pageHtml = `${fonts}<style>${css}</style><figure class="diagram"><div class="diagram-scroll"><svg viewBox="0 0 3000 ${H + 100}" style="width:3000px;min-width:0;max-width:none">${texts}${probe}</svg></div></figure>`;
  const stdHtml = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3000 ${H}" width="3000" height="${H}">${style}${texts}</svg>`;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage();
  const measure = async html => {
    await page.setContent(html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    return page.evaluate(n => [...document.querySelectorAll('svg text')].slice(0, n).map(t => t.getBBox().width), lines.length);
  };
  const wp = await measure(pageHtml);
  const fontsOk = await page.evaluate(() => document.fonts.check("13px 'IBM Plex Sans'") && document.fonts.check("13px 'IBM Plex Mono'") && document.fonts.check("700 15px 'Saira Condensed'"));
  if (!fontsOk) { console.error('FONTS NOT LOADED'); process.exit(2); }
  const ws = await measure(stdHtml);
  lines.forEach(([c, t], i) => { cache[c + '|' + t] = { page: Math.round(wp[i] * 10) / 10, std: Math.round(ws[i] * 10) / 10 }; });
  fs.writeFileSync(cacheFile, JSON.stringify(cache, null, 0));
  console.log(`measured ${lines.length} strings`);
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
