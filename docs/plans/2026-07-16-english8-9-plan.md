# English Grade 8 & 9 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create fully functional Grade 8 and Grade 9 English learning pages (30 units total) following the Grade 7 structure with new modules.

**Architecture:** Python generator script creates page skeletons from a template (english7/u03.html). New CSS extends english7 design system. Each unit page has 10 modules with TTS, dark mode, sidebar. Content filled per-unit manually.

**Tech Stack:** HTML/CSS/JS (no framework), SpeechSynthesis API, localStorage, Python 3 for generation.

**Design doc:** `docs/plans/2026-07-16-english8-9-design.md`

---

### Task 1: Create directory structure + base CSS

**Files:**
- Create: `english8/css/english8.css`
- Create: `english9/css/english9.css`

**Step 1: Create directories**

Run:
```bash
mkdir -p /Users/kim/Documents/workspace/claudecode/math/english8/css
mkdir -p /Users/kim/Documents/workspace/claudecode/math/english9/css
```

Expected: directories exist, ls shows css/ subdirs.

**Step 2: Copy and extend css from Grade 7**

English 8 CSS (`english8/css/english8.css`):
- Copy `english7/css/english.css` as base
- Add new module styles:

```css
/* ===== 阅读专项 ===== */
.reading-module { ... }
.reading-passage { ... }
.reading-question { ... }

/* ===== 中考题型专练 ===== */
.exam-section { ... }
.cloze { ... }
.grammar-fill { ... }

/* ===== 写作进阶 ===== */
.writing-module { ... }
.writing-prompt { ... }
.writing-framework { ... }

/* ===== Project ===== */
.project-module { ... }
.project-steps { ... }
.project-rubric { ... }
```

English 9 CSS (`english9/css/english9.css`): Same as 8.

**Step 3: Commit**

```bash
git add english8/css/ english9/css/
git commit -m "feat: create english8/9 dirs + base CSS"
```

---

### Task 2: Create index pages for Grade 8 and Grade 9

**Files:**
- Create: `english8/index.html`
- Create: `english9/index.html`

**Step 1: Create index page for Grade 8**

Based on `english7/index.html`, adapt:
- Hero title: "初中英语八年级"
- Two semesters: 八上 (8 units), 八下 (8 units)
- Unit cards with: Happy Holiday, Home Sweet Home, Same or Different?, Amazing Plants and Animals, What a Delicious Meal!, Plan for Yourself, When Tomorrow Comes, Let's Communicate! (八上) and the 8 八下 units
- Theme key: `eng8-theme`
- Sidebar link points to grade 8 only
- Nav links: 返回首页 · appendix-grammar (english8/)

**Step 2: Create index page for Grade 9**

Same pattern:
- Title: "初中英语九年级"
- Single semester: 全一册 (14 units)
- Units: How can we become good learners? through I remember meeting all of you in Grade 7.
- Theme key: `eng9-theme`

**Step 3: Commit**

```bash
git add english8/index.html english9/index.html
git commit -m "feat: add Grade 8 & 9 index pages"
```

---

### Task 3: Write Python generator script for page skeletons

**Files:**
- Create: `english8/gen_pages.py`
- Create: `english9/gen_pages.py`

**Step 1: Write gen_pages.py for Grade 8**

The script:
1. Reads `english7/u03.html` as a template
2. Extracts the structural parts (head, sidebar modules, SpeechManager, theme toggle, etc.)
3. Replaces unit-specific content with placeholders
4. Generates 16 files (8 上 + 8 下) with correct titles, sidebar links, unit meta

Key replacement logic:
- `<title>Unit X ... | 初中英语八年级</title>`
- `<h1>Unit title</h1>`
- `<span>Unit subtitle / topic</span>`
- `.unit-meta` spans with topic info
- `.can-do` checkboxes with unit-specific objectives
- Sidebar active class on current unit
- Dialogue text, vocab cards, example sentences — leave as descriptive comments for manual fill

**Step 2: Write gen_pages.py for Grade 9**

Same pattern, generates 14 files.

**Step 3: Run generators**

```bash
cd english8 && python3 gen_pages.py
cd english9 && python3 gen_pages.py
```

Verify: 30 files exist, each is valid HTML.

**Step 4: Commit**

```bash
git add english8/gen_pages.py english9/gen_pages.py english8/u0*.html english8/b2u0*.html english9/u0*.html
git commit -m "feat: generate Grade 8 & 9 page skeletons"
```

---

### Task 4: Fill unit content — Grade 8 上册 (8 units)

**Files:**
- Modify: `english8/u01.html` through `english8/u08.html`

**Step 1-8: Per unit (repeat for each)**

For each unit, manually fill in:
- **课文精讲**: Level-appropriate dialogue about the unit topic, with English + translation + key explanations
- **重点词汇**: 10-15 vocab cards with headword, IPA, POS, definition, example sentence
- **重点句型**: 3-4 sentence patterns with substitution drills
- **语法聚焦**: Grammar table + Chinese error correction section matching the unit's grammar focus
- **三级闯关**: 3 basic + 3 intermediate + 2 challenge questions with reveal-able answers
- **阅读专项**: ~250-300 word passage (textbook or adapted) + 5 multiple-choice questions
- **中考题型专练**: 1-2 cloze/grammar fill exercises
- **写作进阶**: Structured writing prompt + framework + model essay
- **Project**: Task description + steps + example
- **自查清单**: 5-6 unit goals

Unit content reference (人教版 2024 八上):
1. Happy Holiday — 一般过去时复习,不定代词
2. Home Sweet Home — 情态动词 can/could (请求/许可)
3. Same or Different? — 形容词比较级
4. Amazing Plants and Animals — can/can't ability
5. What a Delicious Meal! — 可数/不可数名词, how many/much
6. Plan for Yourself — 一般将来时 (be going to)
7. When Tomorrow Comes — 一般将来时 (will)
8. Let's Communicate! — 宾语从句

**After each unit:**
```bash
node -e "new Function(require('fs').readFileSync('english8/uXX.html','utf8').match(/<script>([\s\S]*?)<\/script>/g).slice(-1)[0].replace(/<\/?script>/g,''))" && echo "JS OK"
```

**Commit after all 8:** `git commit -m "feat: fill Grade 8 上册 unit content"`

---

### Task 5: Fill unit content — Grade 8 下册 (8 units)

**Files:**
- Modify: `english8/b2u01.html` through `english8/b2u08.html`

Same pattern as Task 4. Unit topics:

1. Time to Relax — 建议句型 (Why don't you...? / How about...?)
2. Stay Healthy — 情态动词 should
3. Growing Up — 过去进行时
4. The Wonders of Nature — 形容词最高级
5. Nature's Temper — 过去进行时 (续) / when/while
6. Crossing Cultures — 现在完成时
7. A Good Read — 现在完成时 (yet/already)
8. Making a Difference — 一般将来时被动语态

**Commit:** `git commit -m "feat: fill Grade 8 下册 unit content"`

---

### Task 6: Fill unit content — Grade 9 (14 units)

**Files:**
- Modify: `english9/u01.html` through `english9/u14.html`

Same pattern but:
- Reading专项 uses mixed question types (判断正误, 回答问题, 信息匹配)
- 中考题型专练 covers all 5 types
- Grammar is more advanced (被动语态, 定语从句, 虚拟语气)

Unit grammar focus:
1. How can we become good learners? — 介词by + doing
2. I think that mooncakes are delicious! — 宾语从句 (that/if/whether)
3. Could you please tell me where the restrooms are? — 宾语从句 (wh-)
4. I used to be afraid of the dark. — used to
5. What are the shirts made of? — 被动语态 (一般现在时)
6. When was it invented? — 被动语态 (一般过去时)
7. Teenagers should be allowed... — 情态动词被动语态
8. It must belong to Carla. — 情态动词表推测
9. I like music that I can dance to. — 定语从句
10. You're supposed to shake hands. — be supposed to
11. Sad movies make me cry. — make + 宾语 + 宾补
12. Life is full of the unexpected. — 过去完成时
13. We're trying to save the earth! — 综合复习
14. I remember meeting all of you in Grade 7. — 综合复习

**Commit:** `git commit -m "feat: fill Grade 9 unit content"`

---

### Task 7: Create grammar appendix pages

**Files:**
- Create: `english8/appendix-grammar.html`
- Create: `english9/appendix-grammar.html`

**Step 1: Generate grammar appendix for Grade 8**

Based on `english7/appendix-grammar.html`, adapted with:
- Grade 8 grammar topics (comparatives, future tense, present perfect, passive voice, modal verbs, etc.)
- Cross-unit links within Grade 8 only
- Theme key: `eng8-theme`

**Step 2: Generate grammar appendix for Grade 9**

Same pattern. Grade 9 grammar appendix is comprehensive (all 14 units + 中考 grammar review).

**Commit:**
```bash
git add english8/appendix-grammar.html english9/appendix-grammar.html
git commit -m "feat: add grammar appendix for Grade 8 & 9"
```

---

### Task 8: Validate and fix

**Step 1: Validate all JS across all 30 files**

```bash
for f in english8/u*.html english8/b2u*.html english9/u*.html; do
  node -e "
    var m = require('fs').readFileSync('$f','utf8').match(/<script>([\s\S]*?)<\/script>/g);
    m.forEach(function(s,i){
      var c=s.replace(/<\/?script>/g,'');
      if(c.length>20) try{new Function(c)}catch(e){console.log('$f script'+i+': '+e.message)}
    });
  "
done | grep -v '^$'
```

Expected: no output (all JS valid).

**Step 2: Visual spot check**

Open in browser: `english8/u01.html`, `english9/u01.html`
- Sidebar works and toggles
- Dark mode toggles
- Speech reads text
- Expand all works
- Solution toggle works

**Step 3: Final commit**

```bash
git add -A && git commit -m "chore: final validation and fixes"
```
