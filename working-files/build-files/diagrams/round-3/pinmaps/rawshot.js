// Render raw SVG files as an <img> in a bare page (no site CSS, no web fonts), as a file viewer would.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const [outDir, ...files] = process.argv.slice(2);
  const page = await browser.newPage({ viewport: { width: 900, height: 800 }, deviceScaleFactor: 1.5 });
  for (const f of files) {
    const html = path.resolve(outDir, path.basename(f, '.svg') + '-raw.html');
    const w = /viewBox="0 0 (\d+)/.exec(fs.readFileSync(f, 'utf8'))[1];
    fs.writeFileSync(html, `<!doctype html><body style="margin:0;background:#fff"><img src="file://${path.resolve(f)}" style="width:${w}px;display:block"></body>`);
    await page.goto('file://' + html);
    await page.waitForTimeout(400);
    const img = await page.$('img');
    await img.screenshot({ path: path.join(outDir, path.basename(f, '.svg') + '-raw.png') });
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
