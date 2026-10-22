// Measure text widths with the site's CSS and fonts, in SVG user units at the site's sizes.
//   NODE_PATH=$(npm root -g) node measure_json.js in.json out.json
// in.json: [[cls, text], ...]   out.json: {"cls|text": width, ...} (merged into an existing out.json)
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const outPath = process.argv[3];
  let out = {};
  try { out = JSON.parse(fs.readFileSync(outPath, 'utf8')); } catch (e) { out = {}; }
  const css = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/tools/page.css', 'utf8');
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const texts = items.map(([c, t], i) => `<text class="${c}" x="0" y="${20 + i * 20}">${esc(t)}</text>`).join('');
  const html = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap"><style>${css}</style><figure class="diagram"><div class="diagram-scroll portrait"><svg viewBox="0 0 3000 ${items.length * 20 + 40}" style="width:3000px;min-width:0;max-width:none">${texts}</svg></div></figure>`;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'networkidle' });
  const specs = ["13px 'IBM Plex Sans'", "600 13px 'IBM Plex Sans'", "13px 'IBM Plex Mono'", "500 13px 'IBM Plex Mono'", "700 15px 'Saira Condensed'"];
  await page.evaluate(async (specs) => { for (const f of specs) await document.fonts.load(f, 'Ag0'); }, specs);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const ok = await page.evaluate((specs) => specs.every(f => document.fonts.check(f, 'Ag0')), specs);
  if (!ok) { console.error('FONTS NOT LOADED'); process.exit(2); }
  const w = await page.evaluate(() => [...document.querySelectorAll('svg text')].map(t => t.getBBox().width));
  items.forEach(([c, t], i) => { out[c + '|' + t] = Math.round(w[i] * 10) / 10; });
  fs.writeFileSync(outPath, JSON.stringify(out, null, 0));
  console.log('measured', items.length);
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
