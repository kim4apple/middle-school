import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FILE = 'file://' + path.join(__dirname, 'english8/appendix-vocab.html');
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function run() {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({ viewport: { width: 390, height: 844 } })).newPage();

  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });

  console.log('📱 打开页面...');
  await page.goto(FILE, { waitUntil: 'networkidle', timeout: 15000 });
  await sleep(1000);

  // 隐藏侧栏（移动端覆盖 Tab bar）
  // Ensure light mode for consistent testing
  await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  await page.evaluate(() => document.getElementById('sidebar')?.classList.add('hidden'));
  await sleep(300);

  const R = []; // results
  const ok = (label, cond, msg) => R.push({ label, ok: !!cond, msg });

  // === 1. 结构检查 ===
  ok('DOCTYPE', await page.evaluate(() => document.doctype?.name === 'html'), '✅');
  ok('app-header', await page.$('.app-header'), '顶部栏');
  ok('view-container', await page.$('.view-container'), '内容容器');
  ok('tab-bar', await page.$('.tab-bar'), '底部 Tab');
  ok('4 tabs', (await page.$$('.tab-item')).length === 4, '4个Tab');
  ok('homeView', await page.$('#homeView'), '主页面板');
  ok('tableView', await page.$('#tableView'), '单词表面板');
  ok('learnView', await page.$('#learnView'), '学习面板');
  ok('statsView', await page.$('#statsView'), '统计面板');
  ok('VOCAB_DATA', await page.evaluate(() => typeof VOCAB_DATA !== 'undefined'), '词汇数据');

  // === 2. Tab 切换 ===
  for (const tab of ['table', 'learn', 'stats', 'home']) {
    await page.click(`[data-tab="${tab}"]`, { force: true });
    await sleep(300);
    const active = await page.$eval('.tab-item.active', el => el.getAttribute('data-tab'));
    ok(`tab-${tab}`, active === tab, `切换到 ${tab}`);
  }

  // === 3. 主页 ===
  await page.click('[data-tab="home"]', { force: true });
  await sleep(300);
  ok('home-greet', await page.$('.greet-text'), '问候语');
  ok('home-stats', await page.$('.home-stats'), '统计卡片');
  const haBtns = await page.$$('.ha-btn');
  ok('ha-btn-count', haBtns.length === 2, `快速开始按钮数: ${haBtns.length}`);
  if (haBtns.length >= 2) {
    const btn1Text = await haBtns[0].textContent();
    const btn2Text = await haBtns[1].textContent();
    ok('ha-btn1-text', btn1Text.includes('浏览'), `按钮1: ${btn1Text.trim()}`);
    ok('ha-btn2-text', btn2Text.includes('学习'), `按钮2: ${btn2Text.trim()}`);
    // Click "📋 浏览单词表" via evaluate to avoid viewport issues
    await page.evaluate(() => document.querySelector('.ha-btn').click());
    await sleep(300);
    const at1 = await page.$eval('.tab-item.active', el => el.getAttribute('data-tab'));
    ok('ha-btn1-nav', at1 === 'table', '浏览单词表→单词Tab');
    // Back to home
    await page.click('[data-tab="home"]', { force: true }); await sleep(300);
    // Click "🎯 开始学习" (3rd child: label + btn1 + btn2)
    await page.evaluate(() => { const b = document.querySelectorAll('.ha-btn'); if (b[1]) b[1].click(); });
    await sleep(300);
    const at2 = await page.$eval('.tab-item.active', el => el.getAttribute('data-tab'));
    ok('ha-btn2-nav', at2 === 'learn', '开始学习→学习Tab');
    await page.click('[data-tab="home"]', { force: true }); await sleep(300);
  }

  // === 4. 单词表 ===
  await page.click('[data-tab="table"]', { force: true });
  await sleep(300);
  ok('filter-btn', (await page.$$('.filter-bar button')).length >= 3, '筛选按钮');
  ok('search-input', await page.$('#searchInput'), '搜索框');
  // 搜索测试
  const si = await page.$('#searchInput');
  if (si) {
    await si.fill('vacation');
    await sleep(500);
    const cards = await page.$$('.vocab-unit, .vocab-card');
    ok('search', cards.length > 0, `搜索"vacation": ${cards.length} 结果`);
    await page.evaluate(() => { const el = document.getElementById('searchInput'); if (el) el.value = ''; });
  }

  // === 5. 学习模式 ===
  await page.click('[data-tab="learn"]', { force: true });
  await sleep(300);
  ok('learn-cards', (await page.$$('.learn-card')).length === 3, '3种学习模式');

  // 自测卡
  await page.evaluate(() => { const cards = document.querySelectorAll('.learn-card'); if (cards[0]) cards[0].click(); });
  await sleep(500);
  ok('flashcard', await page.$('.flashcard-area, .flashcard'), '自测卡渲染');

  // 回到学习主页
  await page.click('[data-tab="learn"]', { force: true }); await sleep(300);

  // 听写
  await page.evaluate(() => { const cards = document.querySelectorAll('.learn-card'); if (cards[1]) cards[1].click(); });
  await sleep(300);
  ok('dictation', await page.$('.dictation-card, #dictationView'), '听写渲染');

  // 回到学习主页
  await page.click('[data-tab="learn"]', { force: true }); await sleep(300);

  // 选择题
  await page.evaluate(() => { const cards = document.querySelectorAll('.learn-card'); if (cards[2]) cards[2].click(); });
  await sleep(300);
  ok('quiz', await page.$('.quiz-header, .quiz-question, .quiz-options'), '选择题渲染');

  // === 6. 统计 ===
  await page.click('[data-tab="stats"]', { force: true });
  await sleep(500);
  ok('stats', await page.$('.stat-card, .stats-grid'), '统计渲染');

  // === 7. 样式检查 — 亮色模式 ===
  const lightStyles = await page.evaluate(() => {
    const s = getComputedStyle(document.body);
    return {
      bg: s.getPropertyValue('--bg').trim(),
      text: s.getPropertyValue('--text').trim(),
      textSec: s.getPropertyValue('--text-secondary').trim(),
      accent: s.getPropertyValue('--accent').trim(),
    };
  });
  ok('light-bg', lightStyles.bg === '#ffffff', `亮色背景: ${lightStyles.bg}`);
  ok('light-text', lightStyles.text === '#1a1a2e', `亮色文字: ${lightStyles.text}`);
  ok('light-accent', lightStyles.accent === '#7c3aed', `亮色强调色: ${lightStyles.accent}`);

  // === 8. 暗色模式切换 + 样式检查 ===
  await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  await sleep(300);
  const darkAttr = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
  ok('dark-attr', darkAttr === 'dark', 'data-theme=dark');

  const darkStyles = await page.evaluate(() => {
    const s = getComputedStyle(document.body);
    return {
      bg: s.getPropertyValue('--bg').trim(),
      text: s.getPropertyValue('--text').trim(),
      textSec: s.getPropertyValue('--text-secondary').trim(),
      accent: s.getPropertyValue('--accent').trim(),
    };
  });
  ok('dark-bg', darkStyles.bg === '#0f172a', `暗色背景: ${darkStyles.bg}`);
  ok('dark-text', darkStyles.text === '#e2e8f0', `暗色文字: ${darkStyles.text}`);
  ok('dark-accent', darkStyles.accent === '#a78bfa', `暗色强调色: ${darkStyles.accent}`);

  // === 9. 对比度检查（文字 ≠ 背景）===
  ok('contrast-text-bg', lightStyles.text !== lightStyles.bg, '亮色：文字≠背景');
  ok('contrast-textSec-bg', lightStyles.textSec !== lightStyles.bg, '亮色：辅助文字≠背景');
  ok('contrast-accent-bg', lightStyles.accent !== lightStyles.bg, '亮色：强调色≠背景');
  ok('dark-contrast-text-bg', darkStyles.text !== darkStyles.bg, '暗色：文字≠背景');
  ok('dark-contrast-textSec-bg', darkStyles.textSec !== darkStyles.bg, '暗色：辅助文字≠背景');
  ok('dark-contrast-accent-bg', darkStyles.accent !== darkStyles.bg, '暗色：强调色≠背景');

  // 恢复到亮色
  await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));

  // === 8. 控制台错误 ===
  ok('no-errors', errors.length === 0, `控制台错误: ${errors.length}`);
  errors.forEach(e => console.log(`  ⚠️  ${e}`));

  // === 报告 ===
  const pass = R.filter(r => r.ok).length;
  const fail = R.filter(r => !r.ok).length;
  console.log(`\n${'='.repeat(50)}`);
  console.log(`  单词专项 · 自动化验证报告`);
  console.log(`${'='.repeat(50)}`);
  for (const r of R) console.log(`  ${r.ok ? '✅' : '❌'}  ${r.label}: ${r.msg}`);
  console.log(`${'='.repeat(50)}`);
  console.log(`  总计: ${R.length} 项 | ✅ ${pass} | ❌ ${fail}`);
  console.log(`${'='.repeat(50)}`);

  await browser.close();
  process.exit(fail > 0 ? 1 : 0);
}

run().catch(e => { console.error('❌', e.message); process.exit(1); });
