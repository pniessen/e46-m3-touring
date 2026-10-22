// Measure per-character advance widths for each text class, twice: with the site's page.css
// (Google fonts, as the page loads them) and with the SVG's own <style> block (standalone file).
//   NODE_PATH=$(npm root -g) node measure_chars.js chars.json
// Output: {"page": {cls: {char: w}}, "std": {...}, "check": {...}}
const { chromium } = require('playwright');
const fs = require('fs');
const CLASSES = ['t', 't t-b', 't-sm', 't-sm t-b', 't-xs', 't-xs t-b', 't-h',
  't t-mono', 't t-b t-mono', 't-sm t-mono', 't-sm t-b t-mono', 't-xs t-mono', 't-xs t-b t-mono'];
const CHARS = [];
for (let c = 32; c < 127; c++) CHARS.push(String.fromCharCode(c));
for (const c of '–—→←↑↓·±°×≈≤≥’‘“”…²³½µΩ•✕✓') CHARS.push(c);
(async () => {
  const out = process.argv[2];
  const css = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/tools/page.css', 'utf8');
  const svgSrc = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/diagrams/04-fuel-pressure.svg', 'utf8');
  const style = svgSrc.match(/<style>[\s\S]*?<\/style>/)[0];
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  // each char measured as "x" + c*10 + "x" - "xx" to get a clean advance (and spaces survive)
  const items = [];
  for (const cls of CLASSES) for (const ch of CHARS) items.push([cls, ch]);
  const texts = items.map(([c, ch], i) => `<text class="${c}" x="0" y="${20 + i * 20}" xml:space="preserve">${esc('x' + ch.repeat(10) + 'x')}</text>`).join('')
    + CLASSES.map((c, i) => `<text class="${c}" x="0" y="${20 + (items.length + i) * 20}">xx</text>`).join('');
  const H = (items.length + CLASSES.length) * 20 + 40;
  const probe = `<text class="t-h" x="0" y="${H + 20}">PROBE</text><text class="t t-b" x="0" y="${H + 40}">probe</text><text class="t t-mono" x="0" y="${H + 60}">probe</text><text class="t t-mono t-b" x="0" y="${H + 80}">probe</text>`;
  const fonts = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">`;
  const pageHtml = `${fonts}<style>${css}</style><figure class="diagram"><div class="diagram-scroll"><svg viewBox="0 0 3000 ${H + 100}" style="width:3000px;min-width:0;max-width:none">${texts}${probe}</svg></div></figure>`;
  const stdHtml = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3000 ${H}" width="3000" height="${H}" color="#1b2128">${style}${texts}</svg>`;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage();
  const measure = async html => {
    await page.setContent(html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(400);
    return page.evaluate(n => [...document.querySelectorAll('svg text')].slice(0, n).map(t => t.getComputedTextLength()), items.length + CLASSES.length);
  };
  const res = {};
  for (const [mode, html] of [['page', pageHtml], ['std', stdHtml]]) {
    const w = await measure(html);
    if (mode === 'page') {
      const ok = await page.evaluate(() => document.fonts.check("13px 'IBM Plex Sans'") && document.fonts.check("13px 'IBM Plex Mono'") && document.fonts.check("700 15px 'Saira Condensed'"));
      if (!ok) { console.error('FONTS NOT LOADED'); process.exit(2); }
    }
    const xx = {};
    CLASSES.forEach((c, i) => { xx[c] = w[items.length + i]; });
    const tab = {};
    items.forEach(([c, ch], i) => { (tab[c] = tab[c] || {})[ch] = Math.round((w[i] - xx[c]) / 10 * 1000) / 1000; });
    res[mode] = tab;
  }
  fs.writeFileSync(out, JSON.stringify(res));
  console.log('measured', items.length, 'chars x 2 modes');
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
