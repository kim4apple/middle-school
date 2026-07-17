import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const browser = await chromium.launch({ headless: true });

for (const prefix of ['english8']) {
  const url = 'file://' + path.join(__dirname, prefix, 'appendix-vocab.html');
  const page = await browser.newPage();

  for (const width of [360, 900, 1200]) {
    await page.setViewportSize({ width, height: 800 });
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(800);

    await page.screenshot({ path: `/tmp/${prefix}_${width}_home.png`, fullPage: false });

    for (const tab of ['table', 'learn', 'stats']) {
      await page.evaluate((t) => switchView(t), tab);
      await page.waitForTimeout(400);
      await page.screenshot({ path: `/tmp/${prefix}_${width}_${tab}.png`, fullPage: false });
    }
  }

  await page.close();
}

await browser.close();
console.log('Done');
