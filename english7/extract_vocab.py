#!/usr/bin/env python3
"""Extract vocabulary data from all 24 unit files and generate appendix-vocab.html"""

import re
import json
import html as html_mod
from pathlib import Path

BASE = Path(__file__).parent
UNIT_FILES = [
    "st01.html", "st02.html", "st03.html",
    "u01.html", "u02.html", "u03.html", "u04.html", "u05.html",
    "u06.html", "u07.html", "u08.html", "u09.html",
    "b2u01.html", "b2u02.html", "b2u03.html", "b2u04.html", "b2u05.html",
    "b2u06.html", "b2u07.html", "b2u08.html", "b2u09.html", "b2u10.html",
    "b2u11.html", "b2u12.html",
]

def extract_units():
    units = []
    for fname in UNIT_FILES:
        path = BASE / fname
        html = path.read_text(encoding="utf-8")

        title_m = re.search(r'<title>(.+?)</title>', html)
        title = title_m.group(1) if title_m else fname

        unit_label = fname.replace(".html", "")
        words = []

        cards = re.findall(
            r'<div class="vocab-card">(.*?)</div>\s*</div>', html, re.DOTALL
        )
        for card in cards:
            headword_m = re.search(r'data-speak="([^"]*)"', card)
            if not headword_m:
                continue
            word = headword_m.group(1)

            ipa_m = re.search(r'<span class="ipa">([^<]+)</span>', card)
            pos_m = re.search(r'<span class="pos">([^<]+)</span>', card)
            defn_m = re.search(
                r'<div class="definition">(.*?)</div>', card, re.DOTALL
            )

            speaks = re.findall(r'data-speak="([^"]*)"', card)
            example = speaks[1] if len(speaks) > 1 else ""

            trans_m = re.search(
                r'<span class="trans">([^<]*)</span>', card
            )

            words.append({
                "w": word,
                "ipa": ipa_m.group(1) if ipa_m else "",
                "pos": pos_m.group(1) if pos_m else "",
                "def": defn_m.group(1).strip() if defn_m else "",
                "ex": example,
                "trans": trans_m.group(1) if trans_m else "",
            })

        units.append({"label": unit_label, "title": title, "words": words})
    return units


def generate_html(units):
    data_json = json.dumps(units, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>单词专项 · 初中英语七年级</title>
<link rel="stylesheet" href="css/english.css">
<style>
body {{ display: block; min-height: 100vh; padding: 0; }}
.wrapper {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 60px; }}
.hero {{ text-align: center; padding: 40px 0 32px; }}
.hero h1 {{ font-size: 28px; font-weight: 800; margin-bottom: 6px; }}
.hero .tagline {{ color: var(--text-secondary); font-size: 14px; }}
.hero .badge {{ display: inline-block; font-size: 11px; padding: 3px 12px; border-radius: 20px; background: var(--accent-light); color: var(--accent); font-weight: 600; margin-top: 8px; }}
.back-link {{ display: inline-block; margin-bottom: 24px; font-size: 13px; color: var(--accent); text-decoration: none; }}
.back-link:hover {{ text-decoration: underline; }}

/* === Top bar === */
.top-bar {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 24px; }}
.view-toggle {{ display: flex; gap: 4px; background: var(--bg-secondary); border-radius: 8px; padding: 3px; }}
.view-toggle button {{ padding: 6px 16px; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; background: transparent; color: var(--text-secondary); transition: 0.15s; }}
.view-toggle button.active {{ background: var(--bg); color: var(--text); box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
.filter-bar {{ display: flex; gap: 6px; flex-wrap: wrap; }}
.filter-bar button {{ font-size: 12px; padding: 4px 14px; border-radius: 20px; border: 1px solid var(--border); background: var(--bg); color: var(--text); cursor: pointer; }}
.filter-bar button.active {{ border-color: var(--accent); background: var(--accent-light); color: var(--accent); font-weight: 600; }}
#unitFilter {{ font-size: 13px; padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--bg); color: var(--text); }}

/* === Table view === */
.vocab-unit {{ margin-bottom: 20px; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }}
.vocab-unit summary {{ padding: 14px 18px; cursor: pointer; font-size: 15px; font-weight: 600; background: var(--bg-secondary); user-select: none; list-style: none; display: flex; align-items: center; justify-content: space-between; }}
.vocab-unit summary::-webkit-details-marker {{ display: none; }}
.vocab-unit summary .unit-progress {{ font-size: 12px; font-weight: 400; color: var(--text-secondary); }}
.vocab-unit summary .unit-progress strong {{ color: var(--accent); }}
.vocab-unit[open] summary {{ border-bottom: 1px solid var(--border); }}
.vocab-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
.vocab-table th {{ padding: 8px 12px; text-align: left; font-size: 11px; color: var(--text-secondary); font-weight: 600; border-bottom: 1px solid var(--border); }}
.vocab-table td {{ padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: middle; }}
.vocab-table tr:last-child td {{ border-bottom: none; }}
.vocab-table tr:hover {{ background: var(--bg-secondary); }}
.vocab-table .cb-cell {{ width: 32px; text-align: center; }}
.vocab-table .cb-cell input {{ width: 16px; height: 16px; cursor: pointer; accent-color: var(--accent); }}
.vocab-table .word-cell {{ min-width: 100px; }}
.vocab-table .word-cell .headword {{ font-weight: 600; cursor: pointer; }}
.vocab-table .word-cell .headword:hover {{ color: var(--accent); }}
.vocab-table .word-cell .speak-indicator {{ font-size: 11px; margin-left: 4px; cursor: pointer; opacity: 0.5; }}
.vocab-table .word-cell .speak-indicator:hover {{ opacity: 1; }}
.vocab-table .ipa-cell {{ font-family: Menlo, "SF Mono", Consolas, monospace; font-size: 13px; color: var(--text-secondary); }}
.vocab-table .pos-cell {{ color: var(--text-secondary); font-size: 12px; }}
.vocab-table .def-cell {{ color: var(--text); }}
.vocab-table .ex-cell {{ font-size: 13px; color: var(--text-secondary); max-width: 200px; }}
.vocab-table .ex-cell .ex-en {{ cursor: pointer; }}
.vocab-table .ex-cell .ex-en:hover {{ color: var(--accent); }}
.vocab-table .ex-cell .ex-zh {{ font-size: 12px; color: var(--text-secondary); }}
.vocab-table .mastered td {{ color: var(--text-secondary); }}
.vocab-table .mastered .headword {{ text-decoration: line-through; text-decoration-color: var(--text-secondary); }}

/* === Flashcard view === */
.flashcard-view {{ display: none; }}
.flashcard-header {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; flex-wrap: wrap; gap: 10px; }}
.flashcard-header .stats {{ font-size: 13px; color: var(--text-secondary); }}
.flashcard-header .stats strong {{ color: var(--accent); }}
.flashcard-area {{ max-width: 500px; margin: 0 auto; perspective: 1000px; }}
.flashcard {{ position: relative; width: 100%; min-height: 280px; cursor: pointer; transition: transform 0.4s; transform-style: preserve-3d; }}
.flashcard.flipped {{ transform: rotateY(180deg); }}
.flashcard .front, .flashcard .back {{ position: absolute; top: 0; left: 0; width: 100%; min-height: 280px; backface-visibility: hidden; border-radius: 16px; padding: 32px 28px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }}
.flashcard .front {{ background: var(--bg); border: 2px solid var(--border); box-shadow: 0 4px 20px rgba(0,0,0,0.06); }}
.flashcard .front .big-word {{ font-size: 32px; font-weight: 700; cursor: pointer; }}
.flashcard .front .big-word:hover {{ color: var(--accent); }}
.flashcard .front .front-ipa {{ font-size: 15px; color: var(--text-secondary); margin-top: 8px; font-family: Menlo, "SF Mono", Consolas, monospace; }}
.flashcard .front .front-hint {{ font-size: 12px; color: var(--text-secondary); margin-top: 24px; }}
.flashcard .back {{ background: var(--bg-secondary); border: 2px solid var(--border); transform: rotateY(180deg); }}
.flashcard .back .back-def {{ font-size: 24px; font-weight: 600; margin-bottom: 8px; }}
.flashcard .back .back-pos {{ font-size: 13px; color: var(--text-secondary); }}
.flashcard .back .back-ex {{ font-size: 14px; color: var(--text-secondary); margin-top: 16px; max-width: 360px; cursor: pointer; }}
.flashcard .back .back-ex:hover {{ color: var(--accent); }}
.flashcard .back .back-extrans {{ font-size: 13px; color: var(--text-secondary); margin-top: 4px; }}
.flashcard-nav {{ display: flex; justify-content: center; gap: 8px; margin-top: 20px; flex-wrap: wrap; }}
.flashcard-nav button {{ padding: 10px 24px; border-radius: 8px; border: none; cursor: pointer; font-size: 14px; font-weight: 600; transition: 0.15s; }}
.btn-green {{ background: #16a34a; color: #fff; }}
.btn-green:hover {{ background: #15803d; }}
.btn-yellow {{ background: #ca8a04; color: #fff; }}
.btn-yellow:hover {{ background: #a16207; }}
.btn-red {{ background: #dc2626; color: #fff; }}
.btn-red:hover {{ background: #b91c1c; }}
.btn-reset {{ background: var(--bg); color: var(--accent); border: 1px solid var(--border) !important; }}
.btn-reset:hover {{ background: var(--accent-light); }}
.no-card {{ text-align: center; padding: 60px; color: var(--text-secondary); font-size: 16px; }}

[data-theme="dark"] .flashcard .front {{ background: #1e293b; border-color: #334155; }}
[data-theme="dark"] .flashcard .back {{ background: #1e1b4b; border-color: #334155; }}
[data-theme="dark"] .view-toggle {{ background: #1e293b; }}
[data-theme="dark"] .view-toggle button.active {{ background: #0f172a; }}

@media (max-width: 640px) {{
  .wrapper {{ padding: 20px 14px 40px; }}
  .top-bar {{ flex-direction: column; align-items: stretch; }}
  .vocab-table {{ font-size: 13px; }}
  .vocab-table th, .vocab-table td {{ padding: 6px 8px; }}
  .vocab-table .ex-cell {{ max-width: 120px; }}
  .flashcard .front .big-word {{ font-size: 26px; }}
  .flashcard .back .back-def {{ font-size: 20px; }}
  .flashcard .front, .flashcard .back {{ min-height: 220px; padding: 24px 20px; }}
}}
</style>
</head>
<body>

<div class="wrapper">
  <a href="index.html" class="back-link">← 返回单元列表</a>

  <div class="hero">
    <h1>📖 单词专项</h1>
    <p class="tagline">人教版七年级全册词汇 · 240 词集中突破</p>
    <span class="badge">24 单元 · 可朗读 · 可标记掌握 · 可自测</span>
  </div>

  <div class="top-bar">
    <div class="view-toggle">
      <button class="active" data-view="table">📋 单词表</button>
      <button data-view="flashcard">🃏 自测卡</button>
    </div>
    <div class="filter-bar" id="filterBar">
      <button class="active" data-filter="all">全部</button>
      <button data-filter="unmastered">未掌握</button>
      <button data-filter="mastered">已掌握</button>
    </div>
    <select id="unitFilter">
      <option value="all">全部单元</option>
    </select>
  </div>

  <div id="tableView"></div>
  <div class="flashcard-view" id="flashcardView"></div>
</div>

<script>
var VOCAB_DATA = {data_json};

/* === State === */
var state = {{
  view: 'table',
  filter: 'all',
  unitFilter: 'all',
  mastered: {{}},
  cardIndex: 0,
  cardQueue: [],
  isFlipped: false,
}};

try {{
  var saved = JSON.parse(localStorage.getItem('eng7-vocab-mastered'));
  if (saved) state.mastered = saved;
}} catch(e) {{}}

function saveMastered() {{
  localStorage.setItem('eng7-vocab-mastered', JSON.stringify(state.mastered));
}}

/* === Speak === */
function speak(text) {{
  if ('speechSynthesis' in window) {{
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US'; u.rate = 0.85;
    window.speechSynthesis.speak(u);
  }}
}}

/* === Table View === */
function renderTable() {{
  var container = document.getElementById('tableView');
  var html = '';
  VOCAB_DATA.forEach(function(unit, ui) {{
    var total = unit.words.length;
    var done = unit.words.filter(function(w, wi) {{
      return state.mastered[unit.label + '-' + wi];
    }}).length;

    var showUnit = state.unitFilter === 'all' || state.unitFilter === unit.label;
    if (!showUnit) return;

    var filteredWords = unit.words.filter(function(w, wi) {{
      var key = unit.label + '-' + wi;
      if (state.filter === 'mastered') return state.mastered[key];
      if (state.filter === 'unmastered') return !state.mastered[key];
      return true;
    }});
    if (filteredWords.length === 0) return;

    html += '<details class="vocab-unit"' + (state.unitFilter !== 'all' ? ' open' : '') + '>';
    html += '<summary><span>' + unit.label + ' ' + unit.title.split('|')[0].trim() + '</span>';
    html += '<span class="unit-progress"><strong>' + done + '</strong> / ' + total + ' 掌握</span></summary>';
    html += '<table class="vocab-table"><thead><tr>';
    html += '<th class="cb-cell"></th><th>单词</th><th>音标</th><th>词性</th><th>释义</th><th>例句</th>';
    html += '</tr></thead><tbody>';

    filteredWords.forEach(function(w, wi) {{
      var origIdx = unit.words.indexOf(w);
      var key = unit.label + '-' + origIdx;
      var mastered = state.mastered[key];
      html += '<tr class="' + (mastered ? 'mastered' : '') + '">';
      html += '<td class="cb-cell"><input type="checkbox" ' + (mastered ? 'checked' : '') + ' data-key="' + key + '"></td>';
      html += '<td class="word-cell"><span class="headword" data-speak="' + htmlEncode(w.w) + '">' + htmlEncode(w.w) + '</span><span class="speak-indicator" data-speak="' + htmlEncode(w.w) + '">🔊</span></td>';
      html += '<td class="ipa-cell">' + htmlEncode(w.ipa) + '</td>';
      html += '<td class="pos-cell">' + htmlEncode(w.pos) + '</td>';
      html += '<td class="def-cell">' + htmlEncode(w.def) + '</td>';
      html += '<td class="ex-cell">';
      if (w.ex) html += '<div class="ex-en" data-speak="' + htmlEncode(w.ex) + '">' + htmlEncode(w.ex) + '</div>';
      if (w.trans) html += '<div class="ex-zh">' + htmlEncode(w.trans) + '</div>';
      html += '</td></tr>';
    }});

    html += '</tbody></table></details>';
  }});

  if (!html) {{
    html = '<div class="no-card">当前筛选条件下没有单词</div>';
  }}

  container.innerHTML = html;

  /* Bind checkbox */
  container.querySelectorAll('input[type=checkbox]').forEach(function(cb) {{
    cb.addEventListener('change', function() {{
      var key = this.dataset.key;
      if (this.checked) state.mastered[key] = true;
      else delete state.mastered[key];
      saveMastered();
      renderTable();
    }});
  }});

  /* Bind speak */
  container.querySelectorAll('[data-speak]').forEach(function(el) {{
    el.addEventListener('click', function() {{ speak(this.dataset.speak); }});
  }});
}}

function htmlEncode(s) {{
  var d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}}

/* === Flashcard View === */
function buildQueue() {{
  var queue = [];
  VOCAB_DATA.forEach(function(unit, ui) {{
    if (state.unitFilter !== 'all' && state.unitFilter !== unit.label) return;
    unit.words.forEach(function(w, wi) {{
      var key = unit.label + '-' + wi;
      if (state.filter === 'mastered' && !state.mastered[key]) return;
      if (state.filter === 'unmastered' && state.mastered[key]) return;
      queue.push({{ unit: unit.label, idx: wi, word: w, key: key }});
    }});
  }});
  /* Shuffle */
  for (var i = queue.length - 1; i > 0; i--) {{
    var j = Math.floor(Math.random() * (i + 1));
    var t = queue[i]; queue[i] = queue[j]; queue[j] = t;
  }}
  return queue;
}}

function renderFlashcard() {{
  var container = document.getElementById('flashcardView');
  container.style.display = 'block';

  if (state.cardQueue.length === 0) {{
    container.innerHTML = '<div class="no-card">✨ 全部掌握！太棒了！<br><br><button class="btn-reset" onclick="resetFlashcard()">🔄 重新开始</button></div>';
    return;
  }}

  var item = state.cardQueue[state.cardIndex];
  if (!item) {{ state.cardIndex = 0; item = state.cardQueue[0]; if (!item) return; }}
  var w = item.word;
  var mastered = state.mastered[item.key];

  var total = state.cardQueue.length;
  var remain = total - state.cardIndex;

  var html = '';
  html += '<div class="flashcard-header">';
  html += '<div class="stats">剩余 <strong>' + remain + '</strong> / ' + total + ' 词 · ' + item.unit + '</div>';
  html += '<div class="stats">已掌握 <strong>' + Object.keys(state.mastered).length + '</strong> 词</div>';
  html += '</div>';

  html += '<div class="flashcard-area">';
  html += '<div class="flashcard' + (state.isFlipped ? ' flipped' : '') + '" id="flashcard">';
  html += '<div class="front">';
  html += '<div class="big-word" data-speak="' + htmlEncode(w.w) + '">' + htmlEncode(w.w) + '</div>';
  html += '<div class="front-ipa">' + htmlEncode(w.ipa) + '</div>';
  html += '<div class="front-hint">点击卡片 / 空格键 翻转</div>';
  html += '</div>';
  html += '<div class="back">';
  html += '<div class="back-def">' + htmlEncode(w.def) + '</div>';
  html += '<div class="back-pos">' + htmlEncode(w.pos) + '</div>';
  if (w.ex) html += '<div class="back-ex" data-speak="' + htmlEncode(w.ex) + '">📖 ' + htmlEncode(w.ex) + '</div>';
  if (w.trans) html += '<div class="back-extrans">' + htmlEncode(w.trans) + '</div>';
  html += '</div>';
  html += '</div></div>';

  html += '<div class="flashcard-nav" id="cardNav">';
  if (state.isFlipped) {{
    html += '<button class="btn-green" data-action="remember">✅ 记住了</button>';
    html += '<button class="btn-yellow" data-action="blurry">🤔 模糊</button>';
    html += '<button class="btn-red" data-action="forgot">❌ 忘记</button>';
  }} else {{
    html += '<button class="btn-reset" id="flipBtn">👆 翻转</button>';
  }}
  html += '<button class="btn-reset" data-action="restart" style="margin-left:8px;">🔄 重新洗牌</button>';
  html += '</div>';

  container.innerHTML = html;

  /* Bind card click flip */
  var card = document.getElementById('flashcard');
  if (card) {{
    card.addEventListener('click', function(e) {{
      if (e.target.closest('[data-speak]')) return;
      flipCard();
    }});
  }}

  /* Bind speak */
  container.querySelectorAll('[data-speak]').forEach(function(el) {{
    el.addEventListener('click', function() {{ speak(this.dataset.speak); }});
  }});

  /* Bind action buttons */
  container.querySelectorAll('[data-action]').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var action = this.dataset.action;
      if (action === 'restart') resetFlashcard();
      else if (action === 'remember') handleCard('remember');
      else if (action === 'blurry') handleCard('blurry');
      else if (action === 'forgot') handleCard('forgot');
    }});
  }});

  var flipBtn = document.getElementById('flipBtn');
  if (flipBtn) flipBtn.addEventListener('click', flipCard);
}}

function flipCard() {{
  state.isFlipped = !state.isFlipped;
  renderFlashcard();
}}

function handleCard(action) {{
  var item = state.cardQueue[state.cardIndex];

  if (action === 'remember') {{
    state.mastered[item.key] = true;
    state.cardQueue.splice(state.cardIndex, 1);
  }} else if (action === 'blurry') {{
    state.cardIndex++;
  }} else if (action === 'forgot') {{
    state.cardIndex++;
  }}

  state.isFlipped = false;
  saveMastered();

  if (state.cardIndex >= state.cardQueue.length) {{
    state.cardIndex = 0;
  }}

  renderFlashcard();
}}

function resetFlashcard() {{
  state.cardQueue = buildQueue();
  state.cardIndex = 0;
  state.isFlipped = false;
  renderFlashcard();
}}

/* === Switch view === */
function switchView(view) {{
  state.view = view;
  document.querySelectorAll('.view-toggle button').forEach(function(b) {{
    b.classList.toggle('active', b.dataset.view === view);
  }});
  document.getElementById('tableView').style.display = view === 'table' ? 'block' : 'none';
  document.getElementById('flashcardView').style.display = view === 'flashcard' ? 'block' : 'none';
  if (view === 'table') renderTable();
  else resetFlashcard();
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
    else resetFlashcard();
  }});
}});

/* Unit filter */
var sel = document.getElementById('unitFilter');
VOCAB_DATA.forEach(function(u) {{
  var opt = document.createElement('option');
  opt.value = u.label;
  opt.textContent = u.label + ' ' + u.title.split('|')[0].trim();
  sel.appendChild(opt);
}});
sel.addEventListener('change', function() {{
  state.unitFilter = this.value;
  if (state.view === 'table') renderTable();
  else resetFlashcard();
}});

/* Keyboard */
document.addEventListener('keydown', function(e) {{
  if (state.view !== 'flashcard') return;
  if (e.key === ' ' || e.key === 'Enter') {{
    e.preventDefault();
    if (!state.isFlipped) flipCard();
    else handleCard('blurry');
  }}
}});

switchView('table');
</script>

</body>
</html>"""


if __name__ == "__main__":
    units = extract_units()
    total_words = sum(len(u["words"]) for u in units)
    print(f"Extracted {total_words} words from {len(units)} units")

    html = generate_html(units)
    output_path = BASE / "appendix-vocab.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"Generated {output_path}")
