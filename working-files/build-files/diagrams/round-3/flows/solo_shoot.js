// Render each SVG file on its own (its own <style> block, no page CSS) and report text spilling out of boxes.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [outDir, ...files] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
  const page = await browser.newPage({ viewport: { width: 820, height: 1000 } });
  for (const f of files) {
    const raw = require('fs').readFileSync(path.resolve(f), 'utf8');
    await page.setContent(`<!doctype html><html><body style="margin:0;background:#fff">${raw}</body></html>`);
    await page.evaluate(() => { const s = document.querySelector('svg'); s.setAttribute('width', '800'); });
    const r = await page.evaluate(() => {
      const svg = document.querySelector('svg');
      const vb = svg.viewBox.baseVal;
      const rects = [...svg.querySelectorAll('rect')].filter(r => r.getAttribute('class') !== 'bg').map(r => r.getBBox()).filter(b => b.width * b.height > 500);
      const issues = [];
      let fam = getComputedStyle(svg.querySelector('text')).fontFamily;
      for (const t of svg.querySelectorAll('text')) {
        const b = t.getBBox();
        if (b.x < 1 || b.x + b.width > vb.width - 1) issues.push('OUT ' + t.textContent.slice(0, 40));
        const ax = b.x + 1, ay = b.y + b.height / 2;
        const host = rects.filter(h => ax >= h.x && ax <= h.x + h.width && ay >= h.y && ay <= h.y + h.height).sort((p, q) => p.width * p.height - q.width * q.height)[0];
        if (host && (b.x + b.width > host.x + host.width - 1)) issues.push(`SPILL by ${(b.x + b.width - host.x - host.width).toFixed(1)}: ${t.textContent.slice(0, 50)}`);
      }
      return { fam, issues };
    });
    await (await page.$('svg')).screenshot({ path: path.join(outDir, path.basename(f, '.svg') + '-solo.png') });
    console.log(path.basename(f), 'font:', r.fam, '|', r.issues.length, 'issue(s)');
    r.issues.slice(0, 12).forEach(i => console.log('   ' + i));
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
