# English Homepage Study Progress — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add mark-complete toggle and stats panel to english7/8/9 index pages

**Architecture:** Pure inline JS + CSS in each grade's index.html. Grade 7 migrates from 24 hardcoded `<a>` cards to JS-generated (matching Grade 8/9 pattern). Progress stored in localStorage. No backend, no external dependencies.

**Tech Stack:** Vanilla JS, CSS custom properties, localStorage

**Design Doc:** `docs/plans/2026-07-21-english-index-progress-design.md`

---

### Task 1: CSS — Stats panel + toggle button styles in all 3 grade CSS files

**Files:**
- Modify: `english7/css/english.css`
- Modify: `english8/css/english8.css`
- Modify: `english9/css/english9.css`

Add the following new section before `/* ── Responsive ── */`:

```css
/* ── Index: Progress Panel ── */
.progress-panel { background: var(--bg-secondary); border-radius: var(--radius); padding: 20px 24px; margin-bottom: 28px; }
.progress-panel .pp-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 6px; }
.progress-panel .pp-header h2 { font-size: 16px; font-weight: 700; }
.progress-panel .pp-header .pp-date { font-size: 12px; color: var(--text-secondary); }
.pp-bar-bg { background: var(--border); border-radius: 8px; height: 10px; overflow: hidden; margin-bottom: 16px; }
.pp-bar-fill { height: 100%; border-radius: 8px; background: var(--accent); transition: width 0.3s ease; }
.pp-bar-label { font-size: 13px; font-weight: 600; margin-bottom: 4px; display: flex; justify-content: space-between; }
.pp-semester { margin-top: 12px; }
.pp-semester .pp-bar-bg { height: 6px; }
.pp-semester .pp-bar-fill { background: linear-gradient(90deg, var(--accent), var(--eng-green)); }

/* ── Index: Unit Cards ── */
.unit-card .toggle-btn {
  position: absolute; top: 8px; right: 8px; width: 24px; height: 24px; display: flex;
  align-items: center; justify-content: center; border-radius: 50%; border: none;
  cursor: pointer; font-size: 14px; background: transparent; z-index: 2;
}
.unit-card .toggle-btn:hover { background: var(--bg-secondary); }
.unit-card.completed { border-color: var(--eng-green); }
.unit-card.completed::before { background: var(--eng-green) !important; }
```

Add responsive inside `@media (max-width: 640px)`:
```css
.progress-panel { padding: 14px 16px; }
.progress-panel .pp-header h2 { font-size: 14px; }
.pp-bar-bg { height: 8px; }
```

After adding to `english.css`, repeat identically in `english8.css` and `english9.css`.

Add also the responsive rule for `.progress-panel` to the `@media (max-width: 640px)` block at the end of the responsive section (the existing one near the bottom of each file).

**Step 1: Edit each CSS file to add the new styles**

Edit `english7/css/english.css`:
- Before `/* ── Responsive ── */`, insert the progress-panel + toggle-btn block
- Inside `@media (max-width: 640px)` block, add: `.progress-panel { padding: 14px 16px; }`
- Repeat for `english8/css/english8.css` and `english9/css/english9.css`

**Step 2: Commit**

```bash
git add english7/css/english.css english8/css/english8.css english9/css/english9.css
git commit -m "feat: add progress-panel and toggle-btn CSS for index study progress"
```

---

### Task 2: Grade 7 index — migrate to JS-driven cards + add progress system

**Files:**
- Modify: `english7/index.html`

**Step 1: Replace unit card HTML with empty grids**

Remove the 24 hardcoded `<a class="unit-card done">...</a>` elements inside the two `.semester` divs (s1 and s2).

Replace with:
```html
<div class="unit-grid" id="s1-grid"></div>
```
and:
```html
<div class="unit-grid" id="s2-grid"></div>
```

**Step 2: Add progress panel HTML below hero, above nav-links**

Insert between `.hero` and `.nav-links`:
```html
<div class="progress-panel" id="progressPanel" style="display:none">
  <div class="pp-header">
    <h2>📊 学习进度</h2>
    <span class="pp-date" id="ppDate"></span>
  </div>
  <div class="pp-bar-label"><span>总进度</span><span id="ppTotalLabel">0 / 0</span></div>
  <div class="pp-bar-bg"><div class="pp-bar-fill" id="ppTotalBar" style="width:0%"></div></div>
  <div id="ppSemesters"></div>
</div>
```

**Step 3: Replace the entire `<script>` block at the bottom**

Complete JS logic (replacing both the existing scroll/themetoggle and adding progress):

```html
<script>
(function(){
  var CONFIG = {
    key: 'eng7-progress',
    semesters: [
      { id:'s1', label:'📗 七年级上册', sub:'Starter 1–3 + Unit 1–9' },
      { id:'s2', label:'📘 七年级下册', sub:'Unit 1–12' }
    ],
    units: {
      s1: [
        {id:'st01', label:'S1', title:'Good morning!', topic:'字母·问候'},
        {id:'st02', label:'S2', title:"What's this in English?", topic:'物品·字母'},
        {id:'st03', label:'S3', title:'What color is it?', topic:'颜色·字母'},
        {id:'u01', label:'U1', title:"My name's Gina.", topic:'自我介绍'},
        {id:'u02', label:'U2', title:'This is my sister.', topic:'家庭成员'},
        {id:'u03', label:'U3', title:'Is this your pencil?', topic:'学校物品'},
        {id:'u04', label:'U4', title:"Where's my schoolbag?", topic:'房间物品'},
        {id:'u05', label:'U5', title:'Do you have a soccer ball?', topic:'体育运动'},
        {id:'u06', label:'U6', title:'Do you like bananas?', topic:'饮食偏好'},
        {id:'u07', label:'U7', title:'How much are these socks?', topic:'购物'},
        {id:'u08', label:'U8', title:'When is your birthday?', topic:'日期'},
        {id:'u09', label:'U9', title:'My favorite subject is science.', topic:'学科喜好'}
      ],
      s2: [
        {id:'b2u01', label:'U1', title:'Can you play the guitar?', topic:'才能与俱乐部'},
        {id:'b2u02', label:'U2', title:'What time do you go to school?', topic:'日常作息'},
        {id:'b2u03', label:'U3', title:'How do you get to school?', topic:'交通方式'},
        {id:'b2u04', label:'U4', title:"Don't eat in class.", topic:'校规'},
        {id:'b2u05', label:'U5', title:'Why do you like pandas?', topic:'动物'},
        {id:'b2u06', label:'U6', title:"I'm watching TV.", topic:'日常活动'},
        {id:'b2u07', label:'U7', title:"It's raining!", topic:'天气'},
        {id:'b2u08', label:'U8', title:'Is there a post office near here?', topic:'问路指路'},
        {id:'b2u09', label:'U9', title:'What does he look like?', topic:'外貌描述'},
        {id:'b2u10', label:'U10', title:"I'd like some noodles.", topic:'点餐'},
        {id:'b2u11', label:'U11', title:'How was your school trip?', topic:'学校旅行'},
        {id:'b2u12', label:'U12', title:'What did you do last weekend?', topic:'周末活动'}
      ]
    }
  };

  // ── Progress data ──
  function load() {
    var raw = localStorage.getItem(CONFIG.key);
    return raw ? JSON.parse(raw) : { completed: {}, lastStudyDate: null };
  }
  function save(data) {
    localStorage.setItem(CONFIG.key, JSON.stringify(data));
  }

  // ── Render semester unit grids ──
  function renderUnits(data) {
    CONFIG.semesters.forEach(function(sem) {
      var grid = document.getElementById(sem.id + '-grid');
      if (!grid) return;
      grid.innerHTML = '';
      CONFIG.units[sem.id].forEach(function(u) {
        var isDone = !!data.completed[u.id];
        var card = document.createElement('a');
        card.className = 'unit-card' + (isDone ? ' completed' : '');
        card.href = u.id + '.html';
        card.innerHTML =
          '<button class="toggle-btn" data-unit="' + u.id + '" title="标记完成">' +
          (isDone ? '✅' : '○') + '</button>' +
          '<span class="bg-label">' + u.label + '</span>' +
          '<div class="title">' + u.title + '</div>' +
          '<div class="topic">' + u.topic + '</div>';
        card.querySelector('.toggle-btn').addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          toggleComplete(u.id);
        });
        grid.appendChild(card);
      });
    });
  }

  // ── Toggle completion ──
  function toggleComplete(id) {
    var data = load();
    if (data.completed[id]) {
      delete data.completed[id];
    } else {
      data.completed[id] = new Date().toISOString().slice(0,10);
      data.lastStudyDate = data.completed[id];
    }
    save(data);
    renderUnits(data);
    renderStats(data);
  }

  // ── Count completed in a semester ──
  function semesterCount(data, semId) {
    var list = CONFIG.units[semId] || [];
    var done = 0;
    list.forEach(function(u) { if (data.completed[u.id]) done++; });
    return { done: done, total: list.length };
  }

  // ── Render stats panel ──
  function renderStats(data) {
    var panel = document.getElementById('progressPanel');
    if (!panel) return;
    panel.style.display = '';

    // Overall
    var total = 0, done = 0;
    CONFIG.semesters.forEach(function(sem) {
      var c = semesterCount(data, sem.id);
      total += c.total; done += c.done;
    });
    var pct = total === 0 ? 0 : Math.round(done / total * 100);
    document.getElementById('ppTotalLabel').textContent = done + ' / ' + total + ' (' + pct + '%)';
    document.getElementById('ppTotalBar').style.width = pct + '%';

    // Date
    document.getElementById('ppDate').textContent = data.lastStudyDate ? '最近学习 ' + data.lastStudyDate : '';

    // Per semester
    var html = '';
    CONFIG.semesters.forEach(function(sem) {
      var c = semesterCount(data, sem.id);
      var sp = c.total === 0 ? 0 : Math.round(c.done / c.total * 100);
      html += '<div class="pp-semester">' +
        '<div class="pp-bar-label"><span>' + sem.label + '</span><span>' + c.done + ' / ' + c.total + '</span></div>' +
        '<div class="pp-bar-bg"><div class="pp-bar-fill" style="width:' + sp + '%"></div></div>' +
        '</div>';
    });
    document.getElementById('ppSemesters').innerHTML = html;
  }

  // ── Init ──
  var data = load();
  renderUnits(data);
  renderStats(data);

  // ── Back to top ──
  var btn = document.getElementById('backToTop');
  window.addEventListener('scroll', function() { btn.style.display = window.scrollY > 300 ? 'flex' : 'none'; }, { passive: true });
  btn.addEventListener('click', function() { window.scrollTo({ top: 0, behavior: 'smooth' }); });
})();
function setTheme(t) { document.documentElement.setAttribute("data-theme", t); localStorage.setItem("eng7-theme", t); var btn = document.getElementById("themeToggle"); if (btn) btn.textContent = t === "dark" ? "☀️" : "🌙"; }
function toggleTheme() { setTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark"); }
</script>
```

Remove the old `class="done"` from any remaining elements. The `done` class is no longer used.

**Step 4: Verify**

Open `english7/index.html` in browser. Check:
- Cards render from JS
- Click ○ → becomes ✅, progress updates
- Click ✅ → becomes ○, progress updates
- Refresh page → state persists
- Stats panel shows correct counts
- Card links still navigate to unit pages

**Step 5: Commit**

```bash
git add english7/index.html
git commit -m "feat(eng7): add study progress toggle and stats panel on index page"
```

---

### Task 3: Grade 8 index — add progress panel + toggle to existing JS

**Files:**
- Modify: `english8/index.html`

**Step 1: Add progress panel HTML below hero**

Same as Task 2 Step 2, insert between `.hero` and `.nav-links`:
```html
<div class="progress-panel" id="progressPanel" style="display:none">
  <div class="pp-header">
    <h2>📊 学习进度</h2>
    <span class="pp-date" id="ppDate"></span>
  </div>
  <div class="pp-bar-label"><span>总进度</span><span id="ppTotalLabel">0 / 0</span></div>
  <div class="pp-bar-bg"><div class="pp-bar-fill" id="ppTotalBar" style="width:0%"></div></div>
  <div id="ppSemesters"></div>
</div>
```

**Step 2: Replace the `<script>` block**

Replace the entire script (lines 104-143) with the same JS structure as Task 2, but with Grade 8 data:

```html
<script>
(function(){
  var CONFIG = {
    key: 'eng8-progress',
    semesters: [
      { id:'s1', label:'📗 八年级上册', sub:'Unit 1–8' },
      { id:'s2', label:'📘 八年级下册', sub:'Unit 1–8' }
    ],
    units: {
      s1: [
        {id:'u01', label:'U1', title:'Happy Holiday!', topic:'假期活动'},
        {id:'u02', label:'U2', title:"How often do you exercise?", topic:'生活习惯'},
        {id:'u03', label:'U3', title:"I'm more outgoing than my sister.", topic:'个人特质'},
        {id:'u04', label:'U4', title:"What's the best movie theater?", topic:'偏好比较'},
        {id:'u05', label:'U5', title:'Do you want to watch a game show?', topic:'媒体偏好'},
        {id:'u06', label:'U6', title:"I'm going to study computer science.", topic:'职业规划'},
        {id:'u07', label:'U7', title:'Will people have robots?', topic:'未来预测'},
        {id:'u08', label:'U8', title:"Let's Communicate!", topic:'沟通表达'}
      ],
      s2: [
        {id:'b2u01', label:'U1', title:'Time to Relax!', topic:'放松与娱乐'},
        {id:'b2u02', label:'U2', title:"Let's clean up!", topic:'环保行动'},
        {id:'b2u03', label:'U3', title:'Could you please clean your room?', topic:'家务劳动'},
        {id:'b2u04', label:'U4', title:"Why don't you talk to your parents?", topic:'人际沟通'},
        {id:'b2u05', label:'U5', title:'What were you doing when the rainstorm came?', topic:'过去进行'},
        {id:'b2u06', label:'U6', title:'An old man tried to move the mountains.', topic:'故事传说'},
        {id:'b2u07', label:'U7', title:"What's the highest mountain in the world?", topic:'世界之最'},
        {id:'b2u08', label:'U8', title:'Making a Difference', topic:'社会责任'}
      ]
    }
  };

  // ── Progress data (same functions as Task 2) ──
  function load() { var raw = localStorage.getItem(CONFIG.key); return raw ? JSON.parse(raw) : { completed: {}, lastStudyDate: null }; }
  function save(data) { localStorage.setItem(CONFIG.key, JSON.stringify(data)); }

  function renderUnits(data) {
    CONFIG.semesters.forEach(function(sem) {
      var grid = document.getElementById(sem.id + '-grid');
      if (!grid) return;
      grid.innerHTML = '';
      CONFIG.units[sem.id].forEach(function(u) {
        var isDone = !!data.completed[u.id];
        var card = document.createElement('a');
        card.className = 'unit-card' + (isDone ? ' completed' : '');
        card.href = u.id + '.html';
        card.innerHTML =
          '<button class="toggle-btn" data-unit="' + u.id + '" title="标记完成">' +
          (isDone ? '✅' : '○') + '</button>' +
          '<span class="bg-label">' + u.label + '</span>' +
          '<div class="title">' + u.title + '</div>' +
          '<div class="topic">' + u.topic + '</div>';
        card.querySelector('.toggle-btn').addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          toggleComplete(u.id);
        });
        grid.appendChild(card);
      });
    });
  }

  function toggleComplete(id) {
    var data = load();
    if (data.completed[id]) { delete data.completed[id]; }
    else { data.completed[id] = new Date().toISOString().slice(0,10); data.lastStudyDate = data.completed[id]; }
    save(data);
    renderUnits(data);
    renderStats(data);
  }

  function semesterCount(data, semId) {
    var list = CONFIG.units[semId] || [];
    var done = 0;
    list.forEach(function(u) { if (data.completed[u.id]) done++; });
    return { done: done, total: list.length };
  }

  function renderStats(data) {
    var panel = document.getElementById('progressPanel');
    if (!panel) return;
    panel.style.display = '';
    var total = 0, done = 0;
    CONFIG.semesters.forEach(function(sem) {
      var c = semesterCount(data, sem.id);
      total += c.total; done += c.done;
    });
    var pct = total === 0 ? 0 : Math.round(done / total * 100);
    document.getElementById('ppTotalLabel').textContent = done + ' / ' + total + ' (' + pct + '%)';
    document.getElementById('ppTotalBar').style.width = pct + '%';
    document.getElementById('ppDate').textContent = data.lastStudyDate ? '最近学习 ' + data.lastStudyDate : '';
    var html = '';
    CONFIG.semesters.forEach(function(sem) {
      var c = semesterCount(data, sem.id);
      var sp = c.total === 0 ? 0 : Math.round(c.done / c.total * 100);
      html += '<div class="pp-semester"><div class="pp-bar-label"><span>' + sem.label + '</span><span>' + c.done + ' / ' + c.total + '</span></div><div class="pp-bar-bg"><div class="pp-bar-fill" style="width:' + sp + '%"></div></div></div>';
    });
    document.getElementById('ppSemesters').innerHTML = html;
  }

  var data = load();
  renderUnits(data);
  renderStats(data);

  var btn = document.getElementById('backToTop');
  window.addEventListener('scroll', function() { btn.style.display = window.scrollY > 300 ? 'flex' : 'none'; }, { passive: true });
  btn.addEventListener('click', function() { window.scrollTo({ top: 0, behavior: 'smooth' }); });
})();
function setTheme(t) { document.documentElement.setAttribute("data-theme", t); localStorage.setItem("eng8-theme", t); var btn = document.getElementById("themeToggle"); if (btn) btn.textContent = t === "dark" ? "☀️" : "🌙"; }
function toggleTheme() { setTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark"); }
</script>
```

**Step 3: Remove `class="done"` from any unit cards or old HTML** (none in 8/9 since they were generated). Also remove the old `semester-progress` innerHTML text since that is now handled by JS.

**Step 4: Verify**

Open `english8/index.html` in browser. Same checks as Task 2.

**Step 5: Commit**

```bash
git add english8/index.html
git commit -m "feat(eng8): add study progress toggle and stats panel on index page"
```

---

### Task 4: Grade 9 index — add progress panel + toggle to existing JS

**Files:**
- Modify: `english9/index.html`

Same pattern as Task 3, but Grade 9 data (single semester, u01-u14).

**Step 1: Add progress panel HTML below hero**

Same HTML as Task 2 Step 2.

**Step 2: Replace the `<script>` block**

Replace entire script (lines 91-122) with the same structure. CONFIG:

```js
var CONFIG = {
  key: 'eng9-progress',
  semesters: [
    { id:'s1', label:'📕 九年级全一册', sub:'Unit 1–14' }
  ],
  units: {
    s1: [
      {id:'u01', label:'U1', title:'How can we become good learners?', topic:'学习方法'},
      {id:'u02', label:'U2', title:'I think that mooncakes are delicious!', topic:'节日与文化'},
      {id:'u03', label:'U3', title:'Could you please tell me where the restrooms are?', topic:'问路与请求'},
      {id:'u04', label:'U4', title:'I used to be afraid of the dark.', topic:'变化与成长'},
      {id:'u05', label:'U5', title:'What are the shirts made of?', topic:'产品与材料'},
      {id:'u06', label:'U6', title:'When was it invented?', topic:'发明历史'},
      {id:'u07', label:'U7', title:'Teenagers should be allowed to choose their own clothes.', topic:'规则与许可'},
      {id:'u08', label:'U8', title:'It must belong to Carla.', topic:'推测与判断'},
      {id:'u09', label:'U9', title:'I like music that I can dance to.', topic:'偏好与定从'},
      {id:'u10', label:'U10', title:"You're supposed to shake hands.", topic:'礼仪与文化'},
      {id:'u11', label:'U11', title:'Sad movies make me cry.', topic:'情感与感受'},
      {id:'u12', label:'U12', title:'Life is full of the unexpected.', topic:'意外与经历'},
      {id:'u13', label:'U13', title:"We're trying to save the earth!", topic:'环保与行动'},
      {id:'u14', label:'U14', title:'I remember meeting all of you in Grade 7.', topic:'回忆与毕业'}
    ]
  }
};
```

Render uses `var grid = document.getElementById('s1-grid')` (no semester loop since only one).

**Step 3: Verify**

Open `english9/index.html` in browser. Same checks.

**Step 4: Commit**

```bash
git add english9/index.html
git commit -m "feat(eng9): add study progress toggle and stats panel on index page"
```
