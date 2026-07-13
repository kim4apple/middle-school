# 初中理科自学教材设计模板

> 适用学科：数学、物理、化学、生物
> 设计风格：极简现代 · 完全离线 · 自学优先 · 单页多章或多文件

---

## 一、文件结构决策

### 方案A：单文件（适合内容较少）

```
subject.html
katex/                    ← KaTeX 本地文件
```

**适用**: 学科信息量较少（如 6-8 章），数学可用此方案
**参考**: `math7.html` (10章, ~2000行), `math8.html` (12章, ~1100行)

### 方案B：多文件目录（推荐，适合内容多、SVG 图多）

```
subject/
├── index.html             ← 导航页（各章摘要 + 附录全部内容）
├── css/
│   └── subject.css        ← 共享样式（基于 math 系列样式模板）
├── ch01.html ~ ch12.html  ← 每章独立页面
├── appendix.html          ← 附录独立页
katex/                     ← 共享 KaTeX 本地文件
```

**适用**: 学科信息量大（10+ 章），含大量 SVG 示意图
**参考**: `physics8/` (12章 + 附录, 共 14 个 HTML 文件)

---

## 二、HTML 单页模板

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>学科 · 完全总结</title>
  <link rel="stylesheet" href="katex/katex.min.css">
  <link rel="stylesheet" href="css/subject.css">
</head>
<body>
  <!-- 侧边栏 -->
  <nav id="sidebar">
    <h2>学科名称</h2>
    <nav>
      <a href="#ch01">第1章 · 标题</a>
    </nav>
    <button class="expand-btn" id="expandAllBtn">📂 展开全部章节</button>
    <button id="theme-toggle" class="theme-toggle">🌙 暗色模式</button>
  </nav>

  <!-- 内容区 -->
  <main id="content">
    <!-- 每章结构见下方 模块模板 -->
  </main>

  <script src="katex/katex.min.js"></script>
  <script src="katex/auto-render.min.js"></script>
  <script>
    /* 暗色模式切换 + 侧栏高亮 + 侧栏隐藏 + 一键展开 */
  </script>
</body>
</html>
```

---

## 三、CSS 设计系统

### 配色

```css
:root {
  --bg: #ffffff;                  /* 背景 */
  --bg-secondary: #f1f5f9;        /* 侧栏/模块标题背景 */
  --text: #1a1a2e;               /* 正文 */
  --text-secondary: #64748b;      /* 辅助文字 */
  --accent: #4f46e5;              /* 靛蓝强调色 */
  --accent-light: #eef2ff;        /* 强调色浅版 */
  --border: #e2e8f0;             /* 边框 */
  --shadow: 0 1px 3px rgba(0,0,0,0.08);      /* 卡片阴影 */
  --shadow-hover: 0 4px 12px rgba(0,0,0,0.12);
  --radius: 8px;                  /* 圆角 */
  --sidebar-width: 280px;         /* 侧栏宽度 */
}
```

### 暗色模式

`[data-theme="dark"]` 覆盖所有 `--var`，用 `#0f172a` 深蓝底 + `#e2e8f0` 浅文字。

### 关键 CSS 类

| 类名 | 用途 | 特征 |
|------|------|------|
| `.module` | 可折叠内容区块 | 灰色边框 + 阴影 |
| `.card-grid` | 卡片网格容器 | `grid-template-columns: repeat(auto-fill, minmax(260px, 1fr))` |
| `.concept-card` | 概念卡片 | 白底 + 边栏 + 阴影，鼠标悬浮加深 |
| `.formula-card` | 公式卡片 | 灰底 + 靛蓝左边框 |
| `.technique-card` | 技巧/解题卡片 | 白底 + `step-num` 圆形编号 |
| `.technique-card .pitfall` | 易错提示 | 红底 + 红左边框 |
| `.technique-card .principle` | 原理讲解 | 靛蓝浅底 |
| `.technique-card .variant` | 变式题 | 灰底 + 上分割线 |
| `.technique-card .exam-hint` | 中考怎么考 | 红底 |
| `.experiment-card` | 物理实验卡片 | 橙左边框 |
| `.learning-goals` | 学习目标 | 靛蓝浅底 |
| `.knowledge-link` | 前置知识链接 | 虚线边框 |
| `.thought-method` | 思维方法 | 橙渐变左边框 |
| `.checklist` | 自查清单 | checkbox 列表 |
| `.exam-module` | 中考真题区域 | 红色模块标题 |
| `.exam-q` | 单道真题 | 黄色底 + 红色标签 |
| `.exam-q .diagram` | 配图容器 | 居中, SVG 自动缩放 |
| `.mindmap` | 思维导图 | 树形缩进 + 连接线 |
| `.expand-btn` | 展开/收起按钮 | 靛蓝主题 |
| `.sidebar-toggle` / `#sidebar.hidden` | 侧栏隐藏 | 固定左上位置 |
| `#sidebarShowBtn` | 显示侧栏按钮 | 侧栏隐藏时出现 |

### SVG 示意图样式

```css
.exam-q .diagram { margin: 10px 0; text-align: center; }
.exam-q .diagram svg { max-width: 280px; height: auto; }
/* 暗色模式下反转线条颜色 */
[data-theme="dark"] .exam-q .diagram svg line,
[data-theme="dark"] .exam-q .diagram svg path { stroke: #94a3b8; }
[data-theme="dark"] .exam-q .diagram svg text { fill: #e2e8f0; }
```

### 打印支持

```css
@media print {
  * { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  #sidebar { display: none; }
  #sidebarShowBtn, .expand-btn { display: none; }
  details .content { display: block !important; } /* 强制展开 */
  details[open] .content { display: block !important; }
  .module { box-shadow: none; border: 1px solid #ccc; page-break-inside: avoid; }
  body { display: block; }
}
```

---

## 四、每章模块模板（10 个模块，严格顺序）

```
┌─ 🎯 学习目标（.learning-goals）
├─ 🔗 前置知识（.knowledge-link）
├─ 🧭 学科思维方法（.thought-method）
├─ 🧠 思维导图（.mindmap）
├─ 📖 核心概念（.card-grid > .concept-card × 4-8 张）
├─ 📐 公式速查（.formula-card × 3-6 张）
├─ 🔬 实验探究（.experiment-card — 仅物理/化学/生物）
│   ├─ .exp-step（步骤，带 .exp-step-num 圆形编号）
│   ├─ .exp-principle（实验原理）
│   └─ .exp-tip（注意事项）
├─ 💡 解题技巧（.technique-card × 2-4 张）
│   ├─ .method（方法概述）
│   ├─ .example（例题）
│   ├─ .pitfall（易错点）
│   ├─ .principle（原理讲解）
│   ├─ .variant（变式题）
│   └─ .exam-hint（中考怎么考）
├─ 🎯 中考真题（.exam-module > .exam-q × 3-5 道）
│   ├─ .q-tag（年份+城市标签）
│   ├─ .q-body（题目，可含 .diagram > svg）
│   └─ .q-solution（答案+解析）
└─ ✅ 自查清单 + 费曼挑战（.checklist）
```

### 模块数量参考

| 学科 | 概念卡/章 | 公式卡/章 | 技巧卡/章 | 真题/章 | SVG/章 |
|------|----------|----------|----------|--------|-------|
| 数学 | 4-6 | 3-5 | 2-3 | 3-5 | 1-3 |
| 物理 | 4-8 | 3-6 | 2-4 | 3-5 | 2-4 |
| 化学 | 4-6 | 3-5 | 2-3 | 3-4 | 1-3 |
| 生物 | 4-6 | 0-2 | 2-3 | 2-3 | 1-3 |

---

## 五、附录模块（完整总结）

1. **全年级知识体系思维导图** — 所有章节总览
2. **核心公式速查表** — 按主题分组（约 20-30 条公式）
3. **学科方法汇总** — 数学思想方法 / 物理实验方法 / 化学实验方法
4. **高频易错陷阱总览** — 按类别分组（符号/概念/公式/审题/计算）
5. **科学教学法·零基础到精通** — 学习路径 + 教学节奏参考（40天计划）
6. **快速自学与提升技巧** — 费曼挑战法 / 三遍刷题法 / 每日一练

---

## 六、JavaScript 功能清单

### 1. 暗色模式切换

```javascript
(function() {
  var key = 'subject-theme';
  function setTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    localStorage.setItem(key, t);
    var btn = document.getElementById('theme-toggle');
    if (btn) btn.textContent = t === 'dark' ? '☀ 亮色模式' : '🌙 暗色模式';
  }
  setTheme(localStorage.getItem(key) ||
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  document.getElementById('theme-toggle').addEventListener('click', function() {
    var cur = document.documentElement.getAttribute('data-theme');
    setTheme(cur === 'dark' ? 'light' : 'dark');
  });
})();
```

### 2. 侧边栏滚动高亮

```javascript
(function() {
  var links = document.querySelectorAll('#sidebar nav a');
  var chapters = document.querySelectorAll('.chapter');
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        links.forEach(function(l) { l.classList.remove('active'); });
        var active = document.querySelector('#sidebar nav a[href="#' + entry.target.id + '"]');
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-20% 0px -70% 0px' });
  chapters.forEach(function(ch) { observer.observe(ch); });
})();
```

### 3. 侧边栏隐藏/显示

```javascript
(function() {
  var sidebar = document.getElementById('sidebar');
  var hideBtn = document.getElementById('sidebarHideBtn');
  var showBtn = document.getElementById('sidebarShowBtn');
  var hidden = localStorage.getItem('subject-sidebar') === 'hidden';
  if (hidden) sidebar.classList.add('hidden');
  hideBtn.addEventListener('click', function() {
    sidebar.classList.add('hidden');
    localStorage.setItem('subject-sidebar', 'hidden');
  });
  showBtn.addEventListener('click', function() {
    sidebar.classList.remove('hidden');
    localStorage.setItem('subject-sidebar', '');
  });
})();
```

### 4. 一键展开/收起全部

```javascript
(function() {
  var btn = document.getElementById('expandAllBtn');
  btn.addEventListener('click', function() {
    var all = document.querySelectorAll('.module, .exam-module');
    var allOpen = true;
    for (var i = 0; i < all.length; i++) {
      if (!all[i].hasAttribute('open')) { allOpen = false; break; }
    }
    for (var i = 0; i < all.length; i++) {
      if (allOpen) all[i].removeAttribute('open');
      else all[i].setAttribute('open', '');
    }
    btn.textContent = allOpen ? '📂 展开全部章节' : '📖 收起全部章节';
  });
})();
```

### 5. KaTeX 渲染

```javascript
document.addEventListener('DOMContentLoaded', function() {
  renderMathInElement(document.body, {
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '$', right: '$', display: false }
    ],
    throwOnError: false
  });
});
```

---

## 七、SVG 示意图规范

### 坐标与样式

```svg
<svg width="XXX" height="YYY" viewBox="0 0 XXX YYY">
  <!-- 主线条 -->
  <line|polygon|path ... stroke="#4f46e5" stroke-width="2" fill="none" />
  <!-- 辅助线/虚线 -->
  <line ... stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5,3" />
  <!-- 标签文字 -->
  <text ... font-size="12" fill="#4f46e5">A</text>
  <!-- 角度弧线 -->
  <path ... fill="none" stroke="#f59e0b" stroke-width="1.5" />
</svg>
```

### 暗色适配

SVG 颜色在 CSS 层面通过 `[data-theme="dark"] .exam-q .diagram svg *` 自动反转。
线条用 `#4f46e5` → 暗色变 `#94a3b8`
文字用 `#4f46e5` → 暗色变 `#e2e8f0`
强调用 `#dc2626` → 暗色自动适配

### 数量参考

| 学科 | 每章 SVG 数量 | 类型 |
|------|-------------|------|
| 数学(几何) | 1-3 | 几何图形、三视图、坐标图 |
| 物理 | 2-4 | 光路图、受力分析、电路图、图像 |
| 化学 | 1-2 | 实验装置图、分子结构 |
| 生物 | 1-3 | 细胞结构、系统示意图 |

---

## 八、教学法模块内容（附录 A4/A5）

### 科学教学法·零基础到精通

每学科包含：
1. **四层递进知识树** — 按认知逻辑重新排列章节顺序
2. **学科专项训练** — 如数学的负数运算、物理的几何证明脚手架
3. **教学节奏参考** — 40天学习计划表（含每日练习要求）
4. **三遍刷题法说明**
5. **优先级建议** — 如果时间有限优先学哪几章

### 快速自学与提升技巧

1. **费曼挑战法** — 每章末尾设"费曼挑战"，用自己的话讲给别人听
2. **三遍刷题法** — 当天做→周末刷错题→考前看陷阱
3. **每日一练** — 针对学科弱点（如负数运算、几何证明）
4. **间隔复习** — 艾宾浩斯遗忘曲线应用于易错陷阱

---

## 九、关键设计决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 公式渲染 | KaTeX 本地文件 | 完全离线，不依赖 CDN |
| 单页 vs 多页 | 按内容量选择 | 6-8 章用单页，10+ 章用多页 |
| 侧边栏 | 固定左侧 | 桌面完整，手机可隐藏 |
| 章节折叠 | `<details>` 原生 | 零 JS 依赖，打印时可展开 |
| 暗色模式 | CSS 变量 + data-attribute | 统一管理，localStorage 持久 |
| 布局 | Flexbox + CSS Grid | 响应式，无框架依赖 |
| 图示 | 内联 SVG | 完全离线，无限缩放 |
| 字体 | 系统无衬线 | 无需额外字体加载 |
