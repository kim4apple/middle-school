import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const url = 'file://' + path.join(__dirname, 'english8', 'appendix-vocab.html');

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();

for (const width of [360, 768, 900, 1025, 1200]) {
  await page.setViewportSize({ width, height: 800 });
  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(500);

  const tabStyle = await page.evaluate(() => {
    const tab = document.querySelector('.tab-item');
    if (!tab) return {};
    const cs = getComputedStyle(tab);
    return { flexDirection: cs.flexDirection, fontSize: cs.fontSize, gap: cs.gap, padding: cs.padding };
  });

  const barPos = await page.evaluate(() => {
    const bar = document.querySelector('.tab-bar');
    if (!bar) return {};
    const cs = getComputedStyle(bar);
    const rect = bar.getBoundingClientRect();
    return { position: cs.position, bottom: cs.bottom, rectBottom: rect.bottom, rectTop: rect.top, innerHeight: window.innerHeight, maxWidth: cs.maxWidth };
  });

  const wrapPad = await page.evaluate(() => {
    const w = document.querySelector('.wrapper');
    if (!w) return {};
    const cs = getComputedStyle(w);
    return { padding: cs.padding, display: cs.display, flexDirection: cs.flexDirection };
  });

  const statsGrid = await page.evaluate(() => {
    switchView('stats');
    const g = document.querySelector('.stats-grid');
    if (!g) return {};
    return { gridTemplateColumns: getComputedStyle(g).gridTemplateColumns };
  });

  console.log(`\n── ${width}px ──`);
  console.log(`tab-item: dir=${tabStyle.flexDirection} font=${tabStyle.fontSize} gap=${tabStyle.gap}`);
  console.log(`tab-bar: pos=${barPos.position} bottom=${barPos.bottom} maxW=${barPos.maxWidth} rectBottom=${barPos.rectBottom}/${barPos.innerHeight}`);
  console.log(`wrapper: disp=${wrapPad.display} dir=${wrapPad.flexDirection} pad=${wrapPad.padding}`);
  console.log(`stats-grid: ${statsGrid.gridTemplateColumns}`);
}

await browser.close();
