// Render SVG files standalone (their own <style>, no page CSS) at 2x and check headings fit.
//   NODE_PATH=$(npm root -g) node shoot_std.js OUTDIR a.svg [b.svg ...]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [outDir, ...files] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: 800, height: 900 }, deviceScaleFactor: 1.5 });
  for (const f of files) {
    const fs = require('fs');
    const raw = fs.readFileSync(path.resolve(f), 'utf8');
    await page.setContent(`<!doctype html><html><body style="margin:0;background:#fff">${raw.replace(/<svg /, '<svg width="800" ')}</body></html>`);
    const r = await page.evaluate(() => {
      const svg = document.querySelector('svg'); const vb = svg.viewBox.baseVal; const out = [];
      for (const t of svg.querySelectorAll('text')) { const b = t.getBBox(); if (b.x < 1 || b.x + b.width > vb.width - 1) out.push(`OUT "${t.textContent}" ${b.x.toFixed(1)}..${(b.x + b.width).toFixed(1)}`); }
      const fam = getComputedStyle(svg.querySelector('text')).fontFamily;
      return { out, fam };
    });
    console.log(path.basename(f), 'font:', r.fam, r.out.length ? r.out.join('; ') : 'all text inside');
    await (await page.$('svg')).screenshot({ path: path.join(outDir, path.basename(f, '.svg') + '-standalone.png') });
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
