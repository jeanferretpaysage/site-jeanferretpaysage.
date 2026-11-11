const { chromium } = require('playwright'); const fs = require('fs');
// node render.js dir : rend chaque .svg en .png à sa taille
(async () => {
  const dir = process.argv[2]; const b = await chromium.launch();
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(dir + '/' + f, 'utf8');
    const w = +svg.match(/width="(\d+)"/)[1], h = +svg.match(/height="(\d+)"/)[1];
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await p.screenshot({ path: dir + '/' + f.replace('.svg', '.png'), clip: { x: 0, y: 0, width: w, height: h } });
    await p.close();
  }
  await b.close();
})();
