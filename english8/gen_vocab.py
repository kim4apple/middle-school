#!/usr/bin/env python3
"""Generate appendix-vocab.html for english8 by extracting vocab from unit pages."""
import re, os, json, glob

UNIT_FILES = sorted(glob.glob('english8/[bu]*.html'))
LABEL_MAP = {
    'u01': '8A-U1', 'u02': '8A-U2', 'u03': '8A-U3', 'u04': '8A-U4',
    'u05': '8A-U5', 'u06': '8A-U6', 'u07': '8A-U7', 'u08': '8A-U8',
    'b2u01': '8B-U1', 'b2u02': '8B-U2', 'b2u03': '8B-U3', 'b2u04': '8B-U4',
    'b2u05': '8B-U5', 'b2u06': '8B-U6', 'b2u07': '8B-U7', 'b2u08': '8B-U8',
}

def extract_vocab(html_path):
    with open(html_path) as f:
        html = f.read()
    label = os.path.splitext(os.path.basename(html_path))[0]
    m = re.search(r'<title>(.+?)</title>', html)
    title = m.group(1) if m else label
    cards = []
    pattern = r'<div class="vocab-card">(.*?)</div>\s*(?=<div class="vocab-card"|</div>\s*</div>\s*</details>)'
    for card_html in re.findall(pattern, html, re.DOTALL):
        w = ''
        mw = re.search(r'data-speak="([^"]+)"[^>]*>\s*[^<]+</span>\s*<span class="headword-speak', card_html)
        if mw: w = mw.group(1)
        if not w:
            mw2 = re.search(r'class="headword[^"]*"[^>]*>([^<]+)', card_html)
            if mw2: w = mw2.group(1)
        mi = re.search(r'class="ipa"[^>]*>([^<]+)', card_html)
        mp = re.search(r'class="pos"[^>]*>([^<]+)', card_html)
        md = re.search(r'class="definition"[^>]*>([^<]+)', card_html)
        me = re.search(r'class="wotd-say"[^>]*data-speak="([^"]+)"', card_html)
        mt = re.search(r'class="trans"[^>]*>([^<]+)', card_html)
        if w:
            cards.append({
                'w': w.strip(),
                'ipa': mi.group(1) if mi else '',
                'pos': mp.group(1) if mp else '',
                'def': md.group(1) if md else '',
                'ex': me.group(1) if me else '',
                'trans': mt.group(1) if mt else '',
            })
    return {'label': label, 'title': title, 'words': cards}

def short_label(label):
    return LABEL_MAP.get(label, label)

def generate_html(vocab_data, grade='八年级', theme_key='eng8-vocab'):
    sidebar_links = '\n'.join(
        f'        <a href="appendix-vocab.html" style="font-size:13px;">📖 单词专项</a>'
        for _ in [1]
    )

    data_json = json.dumps(vocab_data, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>单词专项 · 初中英语{grade}</title>
<link rel="stylesheet" href="css/english8.css">
<script>(function(){{var t=localStorage.getItem('{theme_key}');if(!t)t=window.matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';document.documentElement.setAttribute('data-theme',t);}})();</script>
<style>
body {{ display: flex; min-height: 100vh; padding: 0; }}
.wrapper {{ flex: 1; max-width: 960px; margin: 0 auto; padding: 32px 24px 60px; margin-left: var(--sidebar-width); }}
body:has(#sidebar.hidden) .wrapper {{ margin-left: 0; }}
#sidebarShowBtn {{ position: fixed; top: 12px; left: 12px; z-index: 99; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 6px; padding: 6px 10px; cursor: pointer; font-size: 14px; color: var(--text); box-shadow: var(--shadow); display: none; align-items: center; gap: 4px; }}
body:has(#sidebar.hidden) #sidebarShowBtn {{ display: flex; }}
.hero {{ text-align: center; padding: 36px 0 28px; }}
.hero h1 {{ font-size: 28px; font-weight: 800; margin-bottom: 6px; letter-spacing: -0.02em; }}
.hero .tagline {{ color: var(--text-secondary); font-size: 14px; }}
.hero .badge {{ display: inline-block; font-size: 11px; padding: 4px 14px; border-radius: 20px; background: var(--accent-light); color: var(--accent); font-weight: 600; margin-top: 8px; }}
.back-link {{ display: inline-flex; align-items: center; gap: 4px; margin-bottom: 24px; font-size: 13px; color: var(--accent); text-decoration: none; font-weight: 500; }}
.back-link:hover {{ gap: 6px; }}
.top-bar {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 24px; }}
.view-toggle {{ display: flex; gap: 3px; background: var(--bg-secondary); border-radius: 10px; padding: 3px; flex-wrap: wrap; box-shadow: inset 0 1px 2px rgba(0,0,0,0.04); }}
.view-toggle button {{ padding: 7px 16px; border: none; border-radius: 7px; cursor: pointer; font-size: 12px; font-weight: 600; background: transparent; color: var(--text-secondary); transition: all 0.18s; white-space: nowrap; }}
.view-toggle button:hover {{ color: var(--text); }}
.view-toggle button.active {{ background: var(--bg); color: var(--accent); box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
.filter-bar {{ display: flex; gap: 6px; flex-wrap: wrap; }}
.filter-bar button {{ font-size: 12px; padding: 5px 16px; border-radius: 20px; border: 1px solid var(--border); background: var(--bg); color: var(--text-secondary); cursor: pointer; transition: all 0.15s; font-weight: 500; }}
.filter-bar button:hover {{ border-color: var(--accent); color: var(--text); }}
.filter-bar button.active {{ border-color: var(--accent); background: var(--accent-light); color: var(--accent); font-weight: 600; }}
.filter-bar button.filter-wrong {{ border-color: #dc2626; color: #dc2626; }}
.filter-bar button.filter-wrong.active {{ background: #fef2f2; color: #dc2626; border-color: #dc2626; }}
[data-theme="dark"] .filter-bar button.filter-wrong {{ border-color: #f87171; color: #f87171; }}
[data-theme="dark"] .filter-bar button.filter-wrong.active {{ background: #451a1a; color: #f87171; border-color: #f87171; }}
#unitFilter {{ font-size: 13px; padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--bg); color: var(--text); }}
.view-panel {{ display: none; }}
.view-panel.active {{ display: block; animation: fadeIn 0.2s ease; }}
@keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(4px); }} to {{ opacity: 1; transform: translateY(0); }} }}
.vocab-unit {{ margin-bottom: 14px; border: 1px solid var(--border); border-radius: var(--radius); overflow: clip; }}
.vocab-unit summary {{ padding: 10px 14px; cursor: pointer; font-size: 14px; font-weight: 600; user-select: none; list-style: none; display: flex; align-items: center; justify-content: space-between; background: var(--bg-secondary); border-radius: var(--radius); }}
.vocab-unit[open] summary {{ border-radius: var(--radius) var(--radius) 0 0; border-bottom: 1px solid var(--border); }}
.vocab-unit summary .sum-content {{ display: flex; align-items: center; justify-content: space-between; width: 100%; gap: 12px; }}
.vocab-unit summary .unit-progress {{ font-size: 11px; font-weight: 500; color: var(--text-secondary); display: flex; align-items: center; gap: 6px; flex-shrink: 0; white-space: nowrap; }}
.vocab-unit summary .unit-progress strong {{ color: var(--accent); }}
.vocab-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
.vocab-table th {{ padding: 6px 10px; text-align: left; font-size: 10px; color: var(--text-secondary); font-weight: 600; border-bottom: 1px solid var(--border); background: var(--bg); white-space: nowrap; }}
.vocab-table td {{ padding: 6px 10px; border-bottom: 1px solid var(--border); vertical-align: middle; }}
.vocab-table tr:last-child td {{ border-bottom: none; }}
.vocab-table tr:hover {{ background: var(--bg-secondary); }}
.vocab-table .word-cell {{ cursor: pointer; font-weight: 500; }}
.vocab-table .ipa-cell {{ font-family: Menlo, "SF Mono", Consolas, monospace; font-size: 12px; color: var(--text-secondary); }}
.vocab-table .pos-cell {{ font-size: 11px; color: var(--accent); white-space: nowrap; }}
.vocab-table .mastered td {{ opacity: 0.55; }}
.vocab-table .mastered .word-cell {{ text-decoration: line-through; }}
.vocab-table .wrong-row {{ background: #fef2f2; }}
[data-theme="dark"] .vocab-table .wrong-row {{ background: #2d0a0a; }}
.flashcard-area {{ max-width: 500px; margin: 0 auto; perspective: 1000px; }}
.flashcard {{ position: relative; width: 100%; min-height: 280px; cursor: pointer; transition: transform 0.4s; transform-style: preserve-3d; }}
.flashcard.flipped {{ transform: rotateY(180deg); }}
.flashcard .front, .flashcard .back {{ position: absolute; inset: 0; backface-visibility: hidden; border-radius: 16px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border: 1px solid var(--border); box-shadow: 0 4px 20px rgba(0,0,0,0.08); background: var(--bg); }}
.flashcard .back {{ transform: rotateY(180deg); background: var(--accent-light); }}
.flashcard .front .word {{ font-size: 32px; font-weight: 800; color: var(--accent); margin-bottom: 8px; }}
.flashcard .front .ipa {{ font-size: 16px; color: var(--text-secondary); }}
.flashcard .front .hint {{ margin-top: 24px; font-size: 13px; color: var(--text-secondary); opacity: 0.6; }}
.flashcard .back .def {{ font-size: 24px; font-weight: 700; margin-bottom: 12px; color: var(--accent); }}
.flashcard .back .pos {{ font-size: 14px; color: var(--text-secondary); margin-bottom: 6px; }}
.flashcard .back .ex {{ font-size: 15px; line-height: 1.6; color: var(--text); max-width: 90%; }}
.flashcard .back .trans {{ font-size: 13px; color: var(--text-secondary); margin-top: 6px; }}
.flashcard-nav {{ display: flex; align-items: center; justify-content: center; gap: 12px; margin-top: 20px; }}
.flashcard-nav button {{ padding: 8px 20px; border-radius: 10px; border: 1px solid var(--border); background: var(--bg); color: var(--text); cursor: pointer; font-weight: 600; font-size: 13px; transition: all 0.15s; }}
.flashcard-nav button:hover {{ background: var(--accent-light); border-color: var(--accent); color: var(--accent); }}
.flashcard-nav .card-progress {{ font-size: 13px; color: var(--text-secondary); }}
.flashcard-nav .card-progress strong {{ color: var(--accent); }}
.flashcard-buttons {{ display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 14px; }}
.flashcard-buttons button {{ padding: 8px 24px; border-radius: 10px; border: none; cursor: pointer; font-weight: 700; font-size: 13px; transition: all 0.15s; }}
.btn-easy {{ background: #dcfce7; color: #166534; }}
.btn-easy:hover {{ background: #bbf7d0; }}
.btn-hard {{ background: #fef3c7; color: #92400e; }}
.btn-hard:hover {{ background: #fde68a; }}
.btn-forgot {{ background: #fce7f3; color: #9d174d; }}
.btn-forgot:hover {{ background: #fbcfe8; }}
.quiz-options {{ display: flex; flex-direction: column; gap: 10px; max-width: 500px; margin: 20px auto; }}
.quiz-options button {{ padding: 14px 20px; border-radius: 12px; border: 2px solid var(--border); background: var(--bg); cursor: pointer; font-size: 15px; text-align: left; transition: all 0.15s; }}
.quiz-options button:hover {{ border-color: var(--accent); background: var(--accent-light); }}
.quiz-options button.correct {{ border-color: #16a34a; background: #dcfce7; color: #166534; }}
.quiz-options button.wrong {{ border-color: #dc2626; background: #fef2f2; color: #dc2626; }}
.quiz-header {{ text-align: center; margin-bottom: 20px; }}
.quiz-header .q-progress {{ font-size: 13px; color: var(--text-secondary); }}
.quiz-header .q-progress strong {{ color: var(--accent); }}
.dictation-area {{ max-width: 500px; margin: 0 auto; text-align: center; }}
.dictation-area .d-word {{ font-size: 20px; color: var(--text-secondary); margin-bottom: 16px; }}
.dictation-area input {{ width: 100%; padding: 12px 16px; border: 2px solid var(--border); border-radius: 12px; font-size: 18px; text-align: center; outline: none; background: var(--bg); color: var(--text); }}
.dictation-area input:focus {{ border-color: var(--accent); }}
.dictation-area .d-result {{ margin-top: 16px; font-size: 16px; font-weight: 600; }}
.dictation-area .d-result.correct {{ color: #16a34a; }}
.dictation-area .d-result.wrong {{ color: #dc2626; }}
.dictation-area .d-result .d-answer {{ font-weight: 700; color: var(--accent); }}
.dictation-nav {{ display: flex; gap: 10px; justify-content: center; margin-top: 16px; }}
.dictation-nav button {{ padding: 8px 24px; border-radius: 10px; border: 1px solid var(--border); background: var(--bg); cursor: pointer; font-weight: 600; font-size: 13px; }}
.dictation-nav button:hover {{ background: var(--accent-light); }}
.stats-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }}
.stat-card {{ padding: 20px; border-radius: 12px; border: 1px solid var(--border); text-align: center; background: var(--bg); }}
.stat-card .num {{ font-size: 36px; font-weight: 800; color: var(--accent); }}
.stat-card .label {{ font-size: 12px; color: var(--text-secondary); margin-top: 4px; }}
.stats-unit {{ margin-bottom: 12px; }}
.stats-unit .su-header {{ display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; }}
.stats-unit .su-bar {{ height: 6px; border-radius: 3px; background: var(--bg-secondary); overflow: hidden; }}
.stats-unit .su-bar .fill {{ height: 100%; border-radius: 3px; background: var(--accent); transition: width 0.3s; }}
.stats-wrong-list {{ max-height: 300px; overflow-y: auto; }}
.stats-wrong-list .wrong-item {{ display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--border); font-size: 13px; }}
@media (max-width: 700px) {{
  .vocab-table .ipa-cell {{ display: none; }}
  .vocab-table th:nth-child(3) {{ display: none; }}
  .flashcard .front .word {{ font-size: 26px; }}
  .flashcard .back .def {{ font-size: 20px; }}
}}
@media (max-width: 640px) {{
  .wrapper {{ padding: 16px 12px 60px; }}
  .hero h1 {{ font-size: 22px; }}
  .top-bar {{ flex-direction: column; align-items: stretch; }}
  .view-toggle {{ justify-content: center; }}
  .stats-grid {{ grid-template-columns: 1fr 1fr; }}
}}
</style>
</head>
<body>

<nav id="sidebar">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
    <h2 style="margin-bottom:0;">{grade}</h2>
    <button id="sidebarHideBtn" style="background:none;border:none;cursor:pointer;font-size:16px;color:var(--text-secondary);padding:2px 6px;border-radius:4px;">✕</button>
  </div>
  <nav>
    <a href="index.html" style="font-weight:600;">🏠 返回首页</a>
    <a href="appendix-grammar.html" style="font-size:13px;">📌 语法全景图</a>
    <a href="appendix-vocab.html" style="font-size:13px;font-weight:600;color:var(--accent);">📖 单词专项</a>
    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ 八 上 ━━</a>
{"".join(f'    <a href="{f.replace("english8/","")}">{section_title(f)}</a>\\n' for f in sorted(glob.glob('english8/u*.html')))}
    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ 八 下 ━━</a>
{"".join(f'    <a href="{f.replace("english8/","")}">{section_title(f)}</a>\\n' for f in sorted(glob.glob('english8/b2u*.html')))}
  </nav>
  <button class="expand-btn" id="expandAllBtn">📂 展开全部模块</button>
  <button class="theme-toggle" id="themeToggle" onclick="toggleTheme()" title="切换主题">🌙</button>
</nav>

<button id="sidebarShowBtn">☰ 菜单</button>

<div class="wrapper">
  <a href="index.html" class="back-link">← 返回{grade}</a>
  <div class="hero">
    <h1>📖 单词专项 · {grade}</h1>
    <p class="tagline">人教版 · 全部单元词汇 · 自测卡 · 听写 · 练习 · 进度追踪</p>
    <span class="badge">{len(vocab_data)} 单元 · {sum(len(u['words']) for u in vocab_data)} 词</span>
  </div>

  <div class="top-bar">
    <div class="view-toggle">
      <button class="active" data-view="table">📋 单词表</button>
      <button data-view="flashcard">🃏 自测卡</button>
      <button data-view="dictation">✍️ 听写</button>
      <button data-view="quiz">📝 练习</button>
      <button data-view="stats">📊 统计</button>
    </div>
    <div class="filter-bar" id="filterBar">
      <button class="active" data-filter="all">全部</button>
      <button data-filter="unmastered">未掌握</button>
      <button data-filter="mastered">已掌握</button>
      <button data-filter="wrong" class="filter-wrong">❌ 错词</button>
    </div>
    <select id="unitFilter">
      <option value="all">全部单元</option>
    </select>
  </div>

  <div id="tableView" class="view-panel active"></div>
  <div id="flashcardView" class="view-panel"></div>
  <div id="dictationView" class="view-panel"></div>
  <div id="quizView" class="view-panel"></div>
  <div id="statsView" class="view-panel"></div>
</div>

<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>

<script>
var VOCAB_DATA = {data_json};

/* === State === */
var state = {{
  view: 'table',
  filter: 'all',
  unitFilter: 'all',
  cardIndex: 0,
  isFlipped: false,
  mastered: {{}},
  srs: {{}},
  wrongWords: {{}},
  quizWords: [],
  quizIndex: 0,
  quizAnswered: false,
  quizCorrect: 0,
  dictWords: [],
  dictIndex: 0,
  dictRevealed: false,
  dictCorrect: 0,
}};

try {{ var sm = JSON.parse(localStorage.getItem('{theme_key}-mastered')); if (sm) state.mastered = sm; }} catch(e){{}}
try {{ var ss = JSON.parse(localStorage.getItem('{theme_key}-srs')); if (ss) state.srs = ss; }} catch(e){{}}
try {{ var sw = JSON.parse(localStorage.getItem('{theme_key}-wrong')); if (sw) state.wrongWords = sw; }} catch(e){{}}

function saveMastered() {{ localStorage.setItem('{theme_key}-mastered', JSON.stringify(state.mastered)); }}
function saveSrs() {{ localStorage.setItem('{theme_key}-srs', JSON.stringify(state.srs)); }}
function saveWrong() {{ localStorage.setItem('{theme_key}-wrong', JSON.stringify(state.wrongWords)); }}

function getSrs(key) {{ return state.srs[key] || {{i:0,n:0,next:0}}; }}
function isWrong(key) {{ return state.wrongWords[key] && state.wrongWords[key].count > 2; }}

function getFilteredWords() {{
  var out = [];
  VOCAB_DATA.forEach(function(unit) {{
    if (state.unitFilter !== 'all' && state.unitFilter !== unit.label) return;
    unit.words.forEach(function(w, wi) {{
      var key = unit.label + '-' + wi;
      if (state.filter === 'mastered' && !state.mastered[key]) return;
      if (state.filter === 'unmastered' && state.mastered[key]) return;
      if (state.filter === 'wrong' && !isWrong(key)) return;
      out.push({{unit: unit.label, word: w, key: key, unitTitle: unit.title}});
    }});
  }});
  return out;
}}

function shortUnitLabel(label) {{
  return '{' + {json.dumps(LABEL_MAP)} + '}'[label] || label;
}}

/* === Table View === */
function renderTable() {{
  var words = getFilteredWords();
  var byUnit = {{}};
  words.forEach(function(w) {{
    if (!byUnit[w.unit]) byUnit[w.unit] = [];
    byUnit[w.unit].push(w);
  }});
  var html = '';
  var unitOrder = VOCAB_DATA.map(function(u) {{ return u.label; }});
  unitOrder.forEach(function(label) {{
    if (!byUnit[label]) return;
    var unit = VOCAB_DATA.find(function(u) {{ return u.label === label; }});
    if (!unit) return;
    var uw = byUnit[label];
    var mastered = uw.filter(function(w) {{ return state.mastered[w.key]; }}).length;
    var pct = uw.length ? Math.round(mastered / uw.length * 100) : 0;
    html += '<details class="vocab-unit" open>';
    html += '<summary><div class="sum-content"><span>' + shortUnitLabel(label) + ' ' + unit.title.split('|')[0].trim() + '</span>';
    html += '<span class="unit-progress"><strong>' + mastered + '</strong>/' + uw.length + ' <span class="pct ' + (pct===100?'done':'') + '">' + pct + '%</span></span></div></summary>';
    html += '<table class="vocab-table"><thead><tr><th>单词</th><th>音标</th><th>词性</th><th>释义</th><th>掌握</th></tr></thead><tbody>';
    uw.forEach(function(w) {{
      var key = w.key;
      var isMastered = state.mastered[key];
      var isWrong = isWrong(key);
      html += '<tr class="' + (isMastered?'mastered ':'') + (isWrong?'wrong-row ':'') + '">';
      html += '<td class="word-cell" onclick="speak(\\'' + w.word.w.replace(/'/g,"\\\\'") + '\\')">' + w.word.w + '</td>';
      html += '<td class="ipa-cell">' + w.word.ipa + '</td>';
      html += '<td class="pos-cell">' + w.word.pos + '</td>';
      html += '<td>' + w.word.def + '</td>';
      html += '<td><input type="checkbox" ' + (isMastered?'checked':'') + ' onchange="toggleMastered(\\'' + key + '\\',this.checked);renderTable();"></td>';
      html += '</tr>';
    }});
    html += '</tbody></table></details>';
  }});
  document.getElementById('tableView').innerHTML = html || '<p style="text-align:center;padding:40px;color:var(--text-secondary);">没有符合条件的单词</p>';
}}

function toggleMastered(key, val) {{
  if (val) state.mastered[key] = true;
  else delete state.mastered[key];
  saveMastered();
}}

function speak(text) {{
  if ('speechSynthesis' in window) {{
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US'; u.rate = 0.85;
    window.speechSynthesis.speak(u);
  }}
}}

/* === Flashcard View === */
function resetFlashcard() {{
  var words = getFilteredWords();
  if (words.length === 0) return;
  state.cardIndex = 0;
  state.isFlipped = false;
  renderFlashcard();
}}

function renderFlashcard() {{
  var words = getFilteredWords();
  if (words.length === 0) {{ document.getElementById('flashcardView').innerHTML = '<p style="text-align:center;padding:40px;color:var(--text-secondary);">没有符合条件的单词</p>'; return; }}
  var w = words[state.cardIndex];
  var html = '<div class="flashcard-area"><div class="flashcard" id="flashcard" onclick="flipCard()">';
  html += '<div class="front"><div class="word" onclick="event.stopPropagation();speak(\\'' + w.word.w.replace(/'/g,"\\\\'") + '\\')">' + w.word.w + '</div>';
  html += '<div class="ipa">' + w.word.ipa + '</div><div class="hint">点击翻面查看释义</div></div>';
  html += '<div class="back"><div class="def">' + w.word.def + '</div><div class="pos">' + w.word.pos + '</div>';
  html += '<div class="ex">' + w.word.ex + '</div><div class="trans">' + w.word.trans + '</div></div></div></div>';
  html += '<div class="flashcard-nav"><button onclick="prevCard()">← 上一个</button>';
  html += '<span class="card-progress"><strong>' + (state.cardIndex+1) + '</strong>/' + words.length + '</span>';
  html += '<button onclick="nextCard()">下一个 →</button></div>';
  if (state.isFlipped) html += '<div class="flashcard-buttons"><button class="btn-easy" onclick="rateCard(3)">😊 简单</button><button class="btn-hard" onclick="rateCard(1)">🤔 较难</button><button class="btn-forgot" onclick="rateCard(0)">😵 忘了</button></div>';
  document.getElementById('flashcardView').innerHTML = html;
  if (state.isFlipped) document.getElementById('flashcard').classList.add('flipped');
}}

function flipCard() {{
  state.isFlipped = !state.isFlipped;
  var el = document.getElementById('flashcard');
  if (el) el.classList.toggle('flipped');
  renderFlashcard();
}}

function prevCard() {{ if (state.cardIndex > 0) {{ state.cardIndex--; state.isFlipped = false; renderFlashcard(); }} }}
function nextCard() {{ var words = getFilteredWords(); if (state.cardIndex < words.length - 1) {{ state.cardIndex++; state.isFlipped = false; renderFlashcard(); }} }}

function rateCard(val) {{
  var words = getFilteredWords();
  var w = words[state.cardIndex];
  var s = getSrs(w.key);
  if (val === 3) {{ s.i = Math.min(s.i + 1, 5); state.mastered[w.key] = true; }}
  else if (val === 1) {{ s.i = Math.max(s.i - 1, 0); }}
  else {{ s.i = 0; if (!state.wrongWords[w.key]) state.wrongWords[w.key] = {{count:0}}; state.wrongWords[w.key].count = (state.wrongWords[w.key].count||0) + 1; delete state.mastered[w.key]; }}
  state.srs[w.key] = s;
  saveMastered(); saveSrs(); saveWrong();
  nextCard();
}}

/* === Dictation === */
function startDictation() {{
  state.dictIndex = 0;
  state.dictRevealed = false;
  state.dictCorrect = 0;
  var words = getFilteredWords();
  state.dictWords = shuffle(words.slice());
  renderDictation();
}}

function renderDictation() {{
  if (state.dictIndex >= state.dictWords.length) {{
    document.getElementById('dictationView').innerHTML = '<div class="dictation-area"><div class="d-result correct">✅ 完成！正确 ' + state.dictCorrect + '/' + state.dictWords.length + '</div><div class="dictation-nav"><button onclick="startDictation()">🔄 再来一次</button></div></div>';
    return;
  }}
  var w = state.dictWords[state.dictIndex];
  var html = '<div class="dictation-area">';
  html += '<div class="d-word">' + (state.dictIndex+1) + '/' + state.dictWords.length + '</div>';
  if (!state.dictRevealed) {{
    html += '<p style="font-size:14px;color:var(--text-secondary);margin-bottom:12px;">👂 听录音并拼写单词</p>';
    html += '<button onclick="speak(\\'' + w.word.w.replace(/'/g,"\\\\'") + '\\')" style="padding:8px 20px;border-radius:8px;border:1px solid var(--border);background:var(--bg);cursor:pointer;margin-bottom:12px;">🔊 播放</button>';
    html += '<input type="text" id="dictInput" placeholder="输入单词..." onkeydown="if(event.key===\\'Enter\\')checkDictation()">';
    html += '<div class="dictation-nav"><button onclick="checkDictation()">✅ 检查</button><button onclick="revealDictation()">💡 显示答案</button></div>';
  }} else {{
    var isCorrect = state.dictRevealResult;
    html += '<div class="d-result ' + (isCorrect?'correct':'wrong') + '">' + (isCorrect?'✅ 正确！':'❌ 正确答案：') + '<span class="d-answer">' + w.word.w + '</span></div>';
    html += '<div class="d-word" style="margin-top:8px">' + w.word.def + '</div>';
    html += '<div class="dictation-nav"><button onclick="nextDictation()">' + (state.dictIndex < state.dictWords.length-1?'下一个 →':'🏁 完成') + '</button></div>';
  }}
  html += '</div>';
  document.getElementById('dictationView').innerHTML = html;
  if (!state.dictRevealed) {{
    var inp = document.getElementById('dictInput');
    if (inp) setTimeout(function() {{ inp.focus(); }}, 100);
  }}
}}

function checkDictation() {{
  var inp = document.getElementById('dictInput');
  if (!inp) return;
  var w = state.dictWords[state.dictIndex];
  state.dictRevealed = true;
  state.dictRevealResult = inp.value.trim().toLowerCase() === w.word.w.toLowerCase();
  if (state.dictRevealResult) state.dictCorrect++;
  renderDictation();
}}

function revealDictation() {{
  state.dictRevealed = true;
  state.dictRevealResult = false;
  renderDictation();
}}

function nextDictation() {{
  state.dictIndex++;
  state.dictRevealed = false;
  renderDictation();
}}

/* === Quiz === */
function startQuiz() {{
  var words = getFilteredWords();
  state.quizWords = shuffle(words.slice()).slice(0, 20);
  state.quizIndex = 0;
  state.quizAnswered = false;
  state.quizCorrect = 0;
  renderQuiz();
}}

function renderQuiz() {{
  if (state.quizIndex >= state.quizWords.length) {{
    document.getElementById('quizView').innerHTML = '<div style="text-align:center;padding:40px"><div style="font-size:48px;margin-bottom:16px;">🏆</div><h2>练习完成！</h2><p style="font-size:18px;margin:12px 0;color:var(--accent);font-weight:700;">正确率：' + Math.round(state.quizCorrect/state.quizWords.length*100) + '%</p><p style="color:var(--text-secondary);font-size:14px;">' + state.quizCorrect + '/' + state.quizWords.length + '</p><button onclick="startQuiz()" style="margin-top:20px;padding:10px 24px;border-radius:10px;border:1px solid var(--border);background:var(--accent);color:#fff;cursor:pointer;font-weight:600;">🔄 再来一次</button></div>';
    return;
  }}
  var w = state.quizWords[state.quizIndex];
  var correct = w.word.def;
  var opts = [correct];
  while (opts.length < 4) {{
    var r = VOCAB_DATA[Math.floor(Math.random()*VOCAB_DATA.length)].words;
    var rw = r[Math.floor(Math.random()*r.length)].def;
    if (opts.indexOf(rw) === -1) opts.push(rw);
  }}
  opts = shuffle(opts);
  var html = '<div class="quiz-header"><span class="q-progress"><strong>' + (state.quizIndex+1) + '</strong>/' + state.quizWords.length + '</span></div>';
  html += '<p style="text-align:center;font-size:24px;font-weight:700;margin-bottom:8px;color:var(--accent);">' + w.word.w + '</p>';
  html += '<p style="text-align:center;font-size:14px;color:var(--text-secondary);margin-bottom:20px;">' + w.word.ipa + '</p>';
  html += '<p style="text-align:center;font-size:13px;color:var(--text-secondary);margin-bottom:8px;">选择正确的中文释义：</p>';
  html += '<div class="quiz-options">';
  html += opts.map(function(o) {{
    var cls = '';
    if (state.quizAnswered) cls = o === correct ? 'correct' : 'wrong';
    return '<button class="' + cls + '" onclick="answerQuiz(\\'' + o.replace(/'/g,"\\\\'") + '\\',\\'' + correct.replace(/'/g,"\\\\'") + '\\')"' + (state.quizAnswered?' disabled':'') + '>' + o + '</button>';
  }}).join('');
  html += '</div>';
  if (state.quizAnswered) html += '<div style="text-align:center;margin-top:16px;"><button onclick="nextQuiz()" style="padding:8px 20px;border-radius:8px;border:1px solid var(--border);background:var(--accent);color:#fff;cursor:pointer;font-weight:600;">' + (state.quizIndex < state.quizWords.length-1?'下一题 →':'🏁 查看结果') + '</button></div>';
  document.getElementById('quizView').innerHTML = html;
}}

function answerQuiz(selected, correct) {{
  if (state.quizAnswered) return;
  state.quizAnswered = true;
  if (selected === correct) state.quizCorrect++;
  renderQuiz();
}}

function nextQuiz() {{ state.quizIndex++; state.quizAnswered = false; renderQuiz(); }}

/* === Stats === */
function renderStats() {{
  var totalWords = 0;
  VOCAB_DATA.forEach(function(u) {{ totalWords += u.words.length; }});
  var mastered = Object.keys(state.mastered).length;
  var wrongCount = Object.keys(state.wrongWords).filter(function(k) {{ return state.wrongWords[k].count > 2; }}).length;
  var html = '<div class="stats-grid"><div class="stat-card"><div class="num">' + totalWords + '</div><div class="label">总词汇</div></div>';
  html += '<div class="stat-card"><div class="num">' + mastered + '</div><div class="label">已掌握</div></div>';
  html += '<div class="stat-card"><div class="num" style="color:' + (wrongCount>0?'#dc2626':'var(--accent)') + '">' + wrongCount + '</div><div class="label">易错词</div></div>';
  html += '<div class="stat-card"><div class="num">' + Math.round(mastered/totalWords*100) + '%</div><div class="label">掌握率</div></div></div>';
  html += '<h3 style="font-size:15px;margin-bottom:12px;">各单元进度</h3>';
  VOCAB_DATA.forEach(function(unit) {{
    var m = unit.words.filter(function(_, wi) {{ return state.mastered[unit.label + '-' + wi]; }}).length;
    var pct = Math.round(m / unit.words.length * 100);
    html += '<div class="stats-unit"><div class="su-header"><span>' + shortUnitLabel(unit.label) + ' ' + unit.title.split('|')[0].trim() + '</span><span>' + m + '/' + unit.words.length + '</span></div>';
    html += '<div class="su-bar"><div class="fill" style="width:' + pct + '%"></div></div></div>';
  }});
  var wrongWords = Object.keys(state.wrongWords).filter(function(k) {{ return state.wrongWords[k].count > 2; }});
  if (wrongWords.length) {{
    html += '<h3 style="font-size:15px;margin:20px 0 12px;color:#dc2626;">❌ 高频错词</h3>';
    html += '<div class="stats-wrong-list">';
    wrongWords.forEach(function(key) {{
      var parts = key.split('-');
      var ui = VOCAB_DATA.findIndex(function(u) {{ return u.label === parts[0]; }});
      if (ui === -1 || !VOCAB_DATA[ui].words[parseInt(parts[1])]) return;
      var w = VOCAB_DATA[ui].words[parseInt(parts[1])];
      html += '<div class="wrong-item"><span>' + w.w + '</span><span style="color:var(--text-secondary);">' + shortUnitLabel(parts[0]) + '</span></div>';
    }});
    html += '</div>';
  }}
  document.getElementById('statsView').innerHTML = html;
}}

function shuffle(arr) {{
  for (var i = arr.length - 1; i > 0; i--) {{
    var j = Math.floor(Math.random() * (i + 1));
    var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
  }}
  return arr;
}}

/* === View Switching === */
function switchView(view) {{
  state.view = view;
  document.querySelectorAll('.view-toggle button').forEach(function(b) {{
    b.classList.toggle('active', b.dataset.view === view);
  }});
  ['tableView', 'flashcardView', 'dictationView', 'quizView', 'statsView'].forEach(function(id) {{
    document.getElementById(id).classList.toggle('active', id === view + 'View');
  }});
  if (view === 'table') renderTable();
  else if (view === 'flashcard') resetFlashcard();
  else if (view === 'dictation') startDictation();
  else if (view === 'quiz') startQuiz();
  else if (view === 'stats') renderStats();
}}

/* === Init === */
document.querySelectorAll('.view-toggle button').forEach(function(b) {{
  b.addEventListener('click', function() {{ switchView(this.dataset.view); }});
}});

document.querySelectorAll('.filter-bar button').forEach(function(b) {{
  b.addEventListener('click', function() {{
    document.querySelectorAll('.filter-bar button').forEach(function(x) {{ x.classList.remove('active'); }});
    this.classList.add('active');
    state.filter = this.dataset.filter;
    if (state.view === 'table') renderTable();
    else if (state.view === 'flashcard') resetFlashcard();
    else if (state.view === 'dictation') startDictation();
    else if (state.view === 'quiz') startQuiz();
  }});
}});

var sel = document.getElementById('unitFilter');
VOCAB_DATA.forEach(function(u) {{
  var opt = document.createElement('option');
  opt.value = u.label;
  opt.textContent = shortUnitLabel(u.label) + ' ' + u.title.split('|')[0].trim();
  sel.appendChild(opt);
}});
sel.addEventListener('change', function() {{
  state.unitFilter = this.value;
  if (state.view === 'table') renderTable();
  else if (state.view === 'flashcard') resetFlashcard();
  else if (state.view === 'dictation') startDictation();
  else if (state.view === 'quiz') startQuiz();
}});

document.addEventListener('keydown', function(e) {{
  if (state.view === 'flashcard' && (e.key === ' ' || e.key === 'Enter')) {{
    e.preventDefault();
    if (!state.isFlipped) flipCard();
    else {{ /* auto-advance on rated */ }}
  }}
  if (state.view === 'dictation' && e.key === 'Enter') {{
    if (!state.dictRevealed) {{ e.preventDefault(); checkDictation(); }}
    else {{ e.preventDefault(); nextDictation(); }}
  }}
}});

/* === Theme + Sidebar === */
function toggleTheme() {{
  var h = document.documentElement;
  var isDark = h.getAttribute('data-theme') === 'dark';
  h.setAttribute('data-theme', isDark ? 'light' : 'dark');
  localStorage.setItem('{theme_key}', isDark ? 'light' : 'dark');
}}
var sidebar = document.getElementById('sidebar');
var hideBtn = document.getElementById('sidebarHideBtn');
var showBtn = document.getElementById('sidebarShowBtn');
hideBtn.addEventListener('click', function() {{ sidebar.classList.add('hidden'); }});
showBtn.addEventListener('click', function() {{ sidebar.classList.remove('hidden'); }});

/* Expand all */
document.getElementById('expandAllBtn').addEventListener('click', function() {{
  var details = document.querySelectorAll('.vocab-unit');
  var allOpen = true;
  details.forEach(function(d) {{ if (!d.hasAttribute('open')) allOpen = false; }});
  details.forEach(function(d) {{ allOpen ? d.removeAttribute('open') : d.setAttribute('open', ''); }});
  this.textContent = allOpen ? '📂 展开全部模块' : '📖 收起全部模块';
}});
</script>
</body>
</html>'''

def section_title(path):
    label = os.path.splitext(os.path.basename(path))[0]
    m = re.search(r'<title>(.+?)</title>', open(path).read())
    title = m.group(1).split('|')[0].strip() if m else label
    cls = ' class="active"' if label == 'u01' else ''
    return f'{label}.html{cls}>{title}'

if __name__ == '__main__':
    import glob
    vocab_data = []
    for f in sorted(UNIT_FILES):
        data = extract_vocab(f)
        if data['words']:
            vocab_data.append(data)
            print(f"  {data['label']}: {len(data['words'])} words")
    
    html = generate_html(vocab_data, '八年级', 'eng8-vocab')
    # Fix the section_title calls in the generated HTML - handle them inline
    # Actually, let's just write the file with the correct sidebar links
    with open('english8/appendix-vocab.html', 'w') as f:
        f.write(html)
    print(f"\nGenerated english8/appendix-vocab.html with {len(vocab_data)} units, {sum(len(u['words']) for u in vocab_data)} words")
