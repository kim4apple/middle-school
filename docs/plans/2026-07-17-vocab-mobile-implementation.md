# 单词专项 · 移动端重设计 — 实施计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 将 english8/9 appendix-vocab.html 从 5 Tab 平铺改为 4 Tab（主页/单词表/学习/统计）+ 全新移动端体验

**Architecture:** 单 HTML 页面，所有模块通过 JS 动态渲染。CSS 嵌入 `<style>` 块。修改 `gen_vocab.py` 确保未来可重新生成。

**Tech Stack:** 原生 JS + CSS（无框架）、localStorage、VisualViewport API、Web Speech API

---

### Task 1: 重构全局导航 — 4 Tab + 滑动切换

**Files:**
- Modify: `gen_vocab.py` (CSS + HTML 模板替换)
- Result: `english8/appendix-vocab.html` (重新生成)

**Step 1: 修改顶部栏**

将现有的 `.hero` + `.top-bar` 改为固定顶部栏：
```html
<header class="app-header">
  <button class="back-btn" onclick="location.href='index.html'">←</button>
  <h1 class="app-title" id="appTitle">🏠 主页</h1>
  <div class="header-right"></div>
</header>
```

**Step 2: 新增底部 Tab Bar**

```html
<nav class="tab-bar" id="tabBar">
  <button class="tab-item active" data-tab="home">🏠<span>主页</span></button>
  <button class="tab-item" data-tab="table">📋<span>单词</span></button>
  <button class="tab-item" data-tab="learn">🎯<span>学习</span></button>
  <button class="tab-item" data-tab="stats">📊<span>统计</span></button>
</nav>
```

**Step 3: 添加底部 Tab 安全区域**

```css
.tab-bar {
  padding-bottom: env(safe-area-inset-bottom, 0);
  height: calc(56px + env(safe-area-inset-bottom, 0));
}
```

**Step 4: 实现滑动切换**

```javascript
let touchStartX = 0;
let touchEndX = 0;
const tabs = ['home', 'table', 'learn', 'stats'];

document.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; });
document.addEventListener('touchend', e => {
  touchEndX = e.changedTouches[0].screenX;
  const diff = touchStartX - touchEndX;
  if (Math.abs(diff) > 50) {
    const current = tabs.indexOf(state.view);
    const next = diff > 0 ? current + 1 : current - 1;
    if (next >= 0 && next < tabs.length) switchView(tabs[next]);
  }
});
```

**Step 5: 重写 switchView**

合并原来的 5 个 view 为 4 个，学习模块在内部子选择。

**Step 6: 重新生成**

```bash
python3 gen_vocab.py
```

**Step 7: 提交**

```bash
git add gen_vocab.py english8/appendix-vocab.html english9/appendix-vocab.html
git commit -m "vocab: 4 Tab 导航 + 滑动切换"
```

---

### Task 2: 🏠 主页 Dashboard

**Files:**
- Modify: `gen_vocab.py` (添加 homeView 渲染函数)

**Step 1: 新增 HomeView 渲染函数**

```javascript
function renderHome() {
  const total = VOCAB_DATA.reduce((s, u) => s + u.words.length, 0);
  const mastered = Object.keys(state.mastered).length;
  const dueCount = getDueCount();  // SRS 到期数
  const streak = getStreak();      // 连续学习天数
  const todayCount = getTodayCount();

  document.getElementById('homeView').innerHTML = `...`;
}
```

**Step 2: 实现快速开始按钮**

- 「继续上次」→ 跳到最后使用的模块和单元
- 「随机 10 词」→ 切换到自测卡模式，随机抽 10 词

**Step 3: 保存学习记录**

```javascript
function recordStudy(count) {
  const today = new Date().toDateString();
  let log = JSON.parse(localStorage.getItem('vocab-study-log') || '{}');
  log[today] = (log[today] || 0) + count;
  localStorage.setItem('vocab-study-log', JSON.stringify(log));
}
```

**Step 4: 提交**

```bash
git commit -m "vocab: 主页 Dashboard"
```

---

### Task 3: 📋 单词表 — 搜索 + 卡片布局

**Files:**
- Modify: `gen_vocab.py` (renderTable 函数)

**Step 1: 添加搜索框**

在筛选栏下方添加：
```html
<div class="search-bar">
  <input type="text" id="searchInput" placeholder="🔍 搜索单词..." oninput="renderTable()">
</div>
```

**Step 2: 修改 renderTable 的筛选逻辑**

```javascript
function getFilteredWords() {
  const query = (document.getElementById('searchInput')?.value || '').toLowerCase();
  // ... existing filter logic ...
  if (query) {
    out = out.filter(w => w.word.w.toLowerCase().includes(query) || 
      w.word.def.includes(query));
  }
  return out;
}
```

**Step 3: 提交**

```bash
git commit -m "vocab: 单词表搜索框"
```

---

### Task 4: 🎯 学习 — 模式选择页

**Files:**
- Modify: `gen_vocab.py`

**Step 1: 新增学习模式选择视图**

```html
<div id="learnHome" class="view-panel">
  <div class="learn-mode-grid">
    <button class="learn-mode-card" onclick="startFlashcard()">
      <span class="mode-icon">🃏</span>
      <span class="mode-title">自测卡</span>
      <span class="mode-desc">翻卡记忆，掌握进度</span>
    </button>
    <button class="learn-mode-card" onclick="startDictation()">
      <span class="mode-icon">✍️</span>
      <span class="mode-title">听写</span>
      <span class="mode-desc">拼写训练</span>
    </button>
    <button class="learn-mode-card" onclick="startQuiz()">
      <span class="mode-icon">📝</span>
      <span class="mode-title">选择题</span>
      <span class="mode-desc">四选一练习</span>
    </button>
  </div>
</div>
```

**Step 2: 提交**

```bash
git commit -m "vocab: 学习模式选择页"
```

---

### Task 5: 🃏 自测卡 — 按钮固定+手势

**Files:**
- Modify: `gen_vocab.py`

**Step 1: 按钮固定布局**

翻面后，卡片和按钮区域分离：
```css
.flashcard-wrapper { display: flex; flex-direction: column; height: calc(100vh - 48px - 56px); }
.flashcard-area { flex: 1; display: flex; align-items: center; justify-content: center; }
.flashcard-actions { padding: 12px 16px; padding-bottom: calc(12px + env(safe-area-inset-bottom)); }
```

**Step 2: 左右滑动切换单词**

同全局滑动逻辑，但自测卡激活时拦截左右滑动。

**Step 3: 自动朗读**

进入新词时自动调用 `speak()`，用一个扬声器图标表示当前正在朗读。

**Step 4: 提交**

```bash
git commit -m "vocab: 自测卡手势+按钮固定"
```

---

### Task 6: ✍️ 听写 — 键盘适配

**Files:**
- Modify: `gen_vocab.py`

**Step 1: 输入框+提示固定布局**

```css
.dict-fixed-top { position: fixed; top: 48px; left: 0; right: 0; z-index: 10; }
.dict-input-area { position: fixed; bottom: 0; left: 0; right: 0; 
  padding: 12px 16px; padding-bottom: calc(12px + env(safe-area-inset-bottom));
  background: var(--bg); }
```

**Step 2: `visualViewport` 监听**

```javascript
if (window.visualViewport) {
  window.visualViewport.addEventListener('resize', () => {
    const diff = window.innerHeight - window.visualViewport.height;
    if (diff > 100) {
      // 键盘弹出
      document.getElementById('tabBar').style.display = 'none';
      document.querySelector('.dict-input-area').style.bottom = '0';
    } else {
      document.getElementById('tabBar').style.display = '';
    }
  });
}
```

**Step 3: 错误答案对比**

高亮用户拼写与正确答案的差异字母。

**Step 4: 提交**

```bash
git commit -m "vocab: 听写键盘适配"
```

---

### Task 7: 📊 统计 — 可视图表

**Files:**
- Modify: `gen_vocab.py`

**Step 1: 学习记录图表**

显示过去 7 天的学习量柱状图（纯 CSS，无第三方库）。

**Step 2: SRS 复习列表**

展示所有待复习词汇，按到期时间排序。

**Step 3: 提交**

```bash
git commit -m "vocab: 统计模块增强"
```

---

### Task 8: 全局状态共享 + 骨架屏

**Files:**
- Modify: `gen_vocab.py`

**Step 1: 跨模块状态同步**

`unitFilter` 和 `filter` 状态全局变量，切换模块不丢失。

**Step 2: 骨架屏**

```html
<div class="skeleton-screen" id="skeleton">
  <div class="skeleton-line w-80"></div>
  <div class="skeleton-line w-60"></div>
  <div class="skeleton-line w-90"></div>
</div>
```

JS 渲染完成后隐藏骨架屏。

**Step 3: 提交**

```bash
git commit -m "vocab: 全局状态+骨架屏"
```

---

### Task 9: CSS 间距/字体系统统一

**Files:**
- Modify: `gen_vocab.py` (CSS 部分)

**Step 1: 建立间距变量**

```css
:root {
  --space-xs: 4px; --space-sm: 8px; --space-md: 12px;
  --space-lg: 16px; --space-xl: 20px; --space-2xl: 24px;
}
```

**Step 2: 建立字体层级**

```css
.text-h1 { font-size: 22px; font-weight: 800; }
.text-h2 { font-size: 18px; font-weight: 700; }
.text-h3 { font-size: 16px; font-weight: 700; }
.text-body { font-size: 14px; font-weight: 400; }
.text-caption { font-size: 12px; font-weight: 400; }
```

**Step 3: 提交**

```bash
git commit -m "vocab: 间距/字体系统统一"
```

---

### Task 10: 微交互动画

**Files:**
- Modify: `gen_vocab.py`

**Step 1: Tab 切换动画**

```css
.view-panel { position: absolute; width: 100%; transition: opacity 0.25s, transform 0.25s; }
.view-panel.active { opacity: 1; transform: translateX(0); }
.view-panel.exit-left { opacity: 0; transform: translateX(-30px); }
.view-panel.exit-right { opacity: 0; transform: translateX(30px); }
```

**Step 2: 勾选动画**

```css
.vocab-table tr { transition: opacity 0.3s, transform 0.3s; }
.vocab-table .mastered { opacity: 0.4; transform: scale(0.98); }
```

**Step 3: 按钮点击反馈**

```css
button:active { transform: scale(0.94); transition: transform 0.1s; }
```

**Step 4: 提交**

```bash
git commit -m "vocab: 微交互动画"
```

---

## 执行方式

设计文档：`docs/plans/2026-07-17-vocab-mobile-redesign.md`

Plan 分 10 个任务，按 P0→P3 顺序执行。每个任务独立可提交。

**建议的执行方式：** 子代理驱动（Subagent-Driven），当前会话中逐任务分派。
