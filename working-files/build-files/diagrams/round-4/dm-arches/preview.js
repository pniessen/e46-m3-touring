// Render SVG files at their own size (x2) through the site's page CSS, light or dark, for layout checks.
//   NODE_PATH=$(npm root -g) node preview.js OUTDIR light|dark file.svg [...]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [outDir, scheme, ...files] = process.argv.slice(2);
  const css = fs.readFileSync('/home/user/archeyon/e46-m3-touring-conversion/tools/page.css', 'utf8');
  const fonts = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">';
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await browser.newContext({ viewport: { width: 1000, height: 1200 }, deviceScaleFactor: 2, colorScheme: scheme });
  const page = await ctx.newPage();
  for (const f of files) {
    let svg = fs.readFileSync(f, 'utf8');
    const vb = svg.match(/viewBox="0 0 (\d+) (\d+)"/);
    const W = +vb[1];
    svg = svg.replace(/<style>[\s\S]*?<\/style>/, '').replace(/<rect class="bg"[^>]*\/>/, '').replace(/\scolor="[^"]*"/, '');
    const html = `<!doctype html><html><head><meta charset="utf-8">${fonts}<style>${css}
      body{margin:0;padding:8px;background:var(--surface)} .diagram-scroll svg{min-width:0;width:${W}px;max-width:none}</style></head>
      <body><figure class="diagram"><div class="diagram-scroll">${svg}</div></figure></body></html>`;
    await page.setContent(html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const fig = await page.$('figure.diagram svg');
    const name = path.basename(f, '.svg');
    await fig.screenshot({ path: path.join(outDir, `${name}-${scheme}-full.png`) });
    console.log('wrote', path.join(outDir, `${name}-${scheme}-full.png`));
  }
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
