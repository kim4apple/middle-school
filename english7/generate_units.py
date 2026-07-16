#!/usr/bin/env python3
"""
Generate unit HTML files for the English 7 textbook.

Usage:
    python generate_units.py [--data DATA_FILE]

Reads unit data from a JSON file, renders against an embedded template
(preserving all CSS/JS/structure from u03.html), and writes each unit's .html.
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, 'english7_units.json')
TEMPLATE_FILENAME = 'u03.html'

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def esc_attr(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')


def strip_html(s):
    return re.sub(r'<[^>]+>', '', s)


# ---------------------------------------------------------------------------
# Master template  (mirrors u03.html exactly)
# ---------------------------------------------------------------------------

MASTER_CSS_STYLE = """\
.speak-btn {
  display: inline-flex; align-items: center; gap: 4px;
  font-size: 12px; cursor: pointer; color: var(--accent);
  border: 1px solid var(--border); border-radius: 4px;
  padding: 2px 8px; background: var(--bg);
  transition: background 0.15s;
}
.speak-btn:hover { background: var(--accent-light); }
.speak-btn.speaking { background: var(--eng-amber-light); color: var(--eng-amber); border-color: var(--eng-amber); }
.headword-speak-indicator { font-size: 11px; margin-left: 3px; opacity: 0.55; cursor: pointer; vertical-align: super; line-height: 1; }
.headword-speak-indicator:hover { opacity: 1; }
.wotd-say {
  cursor: pointer; transition: color 0.15s;
}
.wotd-say:hover { color: var(--accent); }
.wotd-say.speaking { color: var(--eng-pink); }
.speech-panel {
  position: fixed; bottom: 80px; right: 24px; z-index: 999;
  background: var(--bg); border: 1px solid var(--border);
  border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.12);
  padding: 14px 18px; display: none; min-width: 180px;
}
.speech-panel.open { display: block; }
.speech-panel .row { display: flex; align-items: center; gap: 8px; margin: 4px 0; font-size: 13px; }
.speech-panel .row label { color: var(--text-secondary); font-size: 12px; min-width: 36px; }
.speech-panel select, .speech-panel input[type="range"] { flex: 1; }
.speech-panel button {
  padding: 4px 12px; border-radius: 6px; border: 1px solid var(--border);
  background: var(--bg); color: var(--text); cursor: pointer; font-size: 12px;
}
.speech-panel button:hover { background: var(--accent-light); }
.speech-toggle-btn {
  position: fixed; bottom: 24px; right: 76px; z-index: 999;
  width: 44px; height: 44px; border-radius: 50%;
  border: 1px solid var(--border); background: var(--bg);
  color: var(--accent); cursor: pointer; font-size: 18px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
  display: flex; align-items: center; justify-content: center;
}
.speech-toggle-btn:hover { background: var(--accent-light); }
.en-text.speaking { background: var(--eng-amber-light); border-radius: 4px; padding: 2px 4px; transition: background 0.2s; }
[data-theme="dark"] .speech-panel { box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
[data-theme="dark"] .en-text.speaking { background: #452a08; }
/* Lazy render below-the-fold sections */
.detail-module { content-visibility: auto; contain-intrinsic-size: 300px; }
.reading { content-visibility: auto; contain-intrinsic-size: 400px; }"""


def build_full_html(title, sidebar_html, cover_html, meta_html, can_do_html,
                    dialogue_html, vocab_html, patterns_html, grammar_html,
                    exercises_html, writing_html, checklist_html,
                    review_html, next_stop_html):
    return f'''<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="css/english.css">
<style>
{MASTER_CSS_STYLE}
</style>
</head>
<body>

<button id="sidebarShowBtn">☰ 侧栏</button>
<button class="back-to-top" id="backToTop">↑</button>

<nav id="sidebar">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
    <h2 style="margin-bottom:0;">英语七年级</h2>
    <button id="sidebarHideBtn" style="background:none;border:none;cursor:pointer;font-size:16px;color:var(--text-secondary);padding:2px 6px;border-radius:4px;">✕</button>
  </div>
{sidebar_html}
  <button class="expand-btn" id="expandAllBtn">📂 展开全部模块</button>
  <button id="theme-toggle" class="theme-toggle">🌙 暗色模式</button>
  <button class="print-btn" onclick="window.print()">🖨️ 打印 / 存 PDF</button>
</nav>

<main id="content">

{cover_html}

{meta_html}

{can_do_html}

{dialogue_html}

{vocab_html}

{patterns_html}

{grammar_html}

{exercises_html}

{writing_html}

{checklist_html}

{review_html}

{next_stop_html}

</main>

<div class="speech-panel" id="speechPanel">
  <div style="font-weight:700;font-size:13px;margin-bottom:6px;">🔊 语音控制</div>
  <div class="row">
    <label>语速</label>
    <input type="range" id="speechRate" min="0.5" max="1.5" step="0.1" value="0.9">
    <span id="speechRateLabel" style="font-size:12px;min-width:32px;text-align:right;">0.9</span>
  </div>
  <div class="row">
    <label>口音</label>
    <select id="speechVoice">
      <option value="en-US">🇺🇸 美式</option>
      <option value="en-GB">🇬🇧 英式</option>
    </select>
  </div>
  <div class="row" style="justify-content:space-between;">
    <button id="speechStopBtn" title="停止朗读">⏹ 停止</button>
    <button id="speechCloseBtn" title="关闭面板">✕ 关闭</button>
  </div>
</div>
<button class="speech-toggle-btn" id="speechToggleBtn" title="语音设置">🔊</button>

<script>
(function() {{
  // ===== SpeechManager =====
  var SpeechManager = {{
    synthesis: window.speechSynthesis,
    currentUtterance: null,
    speaking: false,
    rate: 0.9,
    voiceURI: 'en-US',

    init: function() {{
      var self = this;
      var rateInput = document.getElementById('speechRate');
      var rateLabel = document.getElementById('speechRateLabel');
      var voiceSelect = document.getElementById('speechVoice');
      var stopBtn = document.getElementById('speechStopBtn');
      var closeBtn = document.getElementById('speechCloseBtn');
      var toggleBtn = document.getElementById('speechToggleBtn');
      var panel = document.getElementById('speechPanel');

      var saved = localStorage.getItem('speech-rate');
      if (saved) {{ this.rate = parseFloat(saved); rateInput.value = this.rate; rateLabel.textContent = this.rate; }}
      var savedVoice = localStorage.getItem('speech-voice');
      if (savedVoice) {{ this.voiceURI = savedVoice; voiceSelect.value = savedVoice; }}

      rateInput.addEventListener('input', function() {{
        self.rate = parseFloat(this.value);
        rateLabel.textContent = this.value;
        localStorage.setItem('speech-rate', this.value);
      }});
      voiceSelect.addEventListener('change', function() {{
        self.voiceURI = this.value;
        localStorage.setItem('speech-voice', this.value);
      }});

      stopBtn.addEventListener('click', function() {{ self.stop(); }});
      closeBtn.addEventListener('click', function() {{ panel.classList.remove('open'); }});

      toggleBtn.addEventListener('click', function() {{
        panel.classList.toggle('open');
      }});
    }},

    speak: function(text, callback) {{
      var self = this;
      if (!text) return;
      this.stop();
      var utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = this.voiceURI;
      utterance.rate = this.rate;
      utterance.onstart = function() {{ self.speaking = true; }};
      utterance.onend = function() {{
        self.speaking = false;
        if (callback) callback();
      }};
      utterance.onerror = function() {{ self.speaking = false; }};
      this.currentUtterance = utterance;
      this.synthesis.speak(utterance);
    }},

    speakText: function(el) {{
      var text = el.getAttribute('data-speak') || el.textContent;
      this.speak(text);
    }},

    speakDialogue: function(containerId, callback) {{
      var self = this;
      var container = document.getElementById(containerId);
      if (!container) return;
      var lines = container.querySelectorAll('.en-text');
      var index = 0;
      this.stop();
      function speakNext() {{
        if (index >= lines.length) {{ self.speaking = false; if (callback) callback(); return; }}
        var el = lines[index];
        var text = el.getAttribute('data-speak') || el.textContent.replace(/<[^>]+>/g, '').trim();
        if (!text) {{ index++; speakNext(); return; }}
        el.classList.add('speaking');
        var utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = self.voiceURI;
        utterance.rate = self.rate;
        utterance.onend = function() {{
          el.classList.remove('speaking');
          index++;
          setTimeout(speakNext, 500);
        }};
        utterance.onerror = function() {{ el.classList.remove('speaking'); index++; setTimeout(speakNext, 200); }};
        self.currentUtterance = utterance;
        self.synthesis.speak(utterance);
      }}
      speakNext();
    }},

    speakVocabSection: function(containerId, callback) {{
      var self = this;
      var container = document.getElementById(containerId);
      if (!container) return;
      var cards = container.querySelectorAll('.vocab-card');
      var index = 0;
      this.stop();
      function speakNext() {{
        if (index >= cards.length) {{ self.speaking = false; if (callback) callback(); return; }}
        var card = cards[index];
        var headword = card.querySelector('.headword');
        var def = card.querySelector('.definition');
        var example = card.querySelector('.example .wotd-say');
        var textParts = [];
        if (headword) {{
          textParts.push(headword.getAttribute('data-speak') || headword.textContent);
        }}
        if (example) {{
          textParts.push(example.getAttribute('data-speak') || example.textContent.replace(/<[^>]+>/g, '').trim());
        }}
        var fullText = textParts.join('. ');
        if (!fullText) {{ index++; speakNext(); return; }}
        headword.classList.add('speaking');
        var utterance = new SpeechSynthesisUtterance(fullText);
        utterance.lang = self.voiceURI;
        utterance.rate = self.rate;
        utterance.onend = function() {{
          headword.classList.remove('speaking');
          index++;
          setTimeout(speakNext, 600);
        }};
        utterance.onerror = function() {{ headword.classList.remove('speaking'); index++; setTimeout(speakNext, 300); }};
        self.currentUtterance = utterance;
        self.synthesis.speak(utterance);
      }}
      speakNext();
    }},

    stop: function() {{
      this.synthesis.cancel();
      this.speaking = false;
    }}
  }};

  SpeechManager.init();

  // Bind click-to-speak on .wotd-say
  document.querySelectorAll('.wotd-say').forEach(function(el) {{
    el.addEventListener('click', function() {{
      var text = this.getAttribute('data-speak') || this.textContent;
      SpeechManager.speak(text);
    }});
  }});

  // Bind speak buttons
  document.querySelectorAll('.speak-btn').forEach(function(btn) {{
    btn.addEventListener('click', function(e) {{
      e.stopPropagation();
      var dialogueId = this.getAttribute('data-dialogue');
      var vocabId = this.getAttribute('data-vocab');
      var targetId = this.getAttribute('data-target');
      if (this.classList.contains('speaking')) {{ SpeechManager.stop(); this.classList.remove('speaking'); return; }}
      this.classList.add('speaking');
      var done = function() {{ btn.classList.remove('speaking'); }};
      if (dialogueId) {{
        SpeechManager.speakDialogue(dialogueId, done);
      }} else if (vocabId) {{
        SpeechManager.speakVocabSection(vocabId, done);
      }} else if (targetId) {{
        var target = document.getElementById(targetId);
        if (!target) {{ btn.classList.remove('speaking'); return; }}
        SpeechManager.speak(target.textContent.replace(/<[^>]+>/g, ''), done);
      }} else {{
        btn.classList.remove('speaking');
      }}
    }});
  }});

  // Bind headword speaker indicator clicks
  document.querySelectorAll('.headword-speak-indicator').forEach(function(el) {{
    el.addEventListener('click', function(e) {{
      e.stopPropagation();
      var headword = this.previousElementSibling;
      if (headword && headword.classList.contains('wotd-say')) {{
        var text = headword.getAttribute('data-speak') || headword.textContent;
        SpeechManager.speak(text);
      }}
    }});
  }});
  // ===== Theme toggle =====
  var toggle = document.getElementById('theme-toggle');
  var html = document.documentElement;
  var saved = localStorage.getItem('site-theme');
  if (saved === 'dark') {{ html.setAttribute('data-theme', 'dark'); toggle.textContent = '☀️ 亮色模式'; }}
  toggle.addEventListener('click', function() {{
    var isDark = html.getAttribute('data-theme') === 'dark';
    html.setAttribute('data-theme', isDark ? 'light' : 'dark');
    toggle.textContent = isDark ? '🌙 暗色模式' : '☀️ 亮色模式';
    localStorage.setItem('site-theme', isDark ? 'light' : 'dark');
  }});

  // ===== Expand all / collapse all =====
  (function() {{
    var btn = document.getElementById('expandAllBtn');
    if (!btn) return;
    btn.addEventListener('click', function() {{
      var allDetails = document.querySelectorAll('.module, .exam-module');
      var allOpen = true;
      for (var i = 0; i < allDetails.length; i++) {{
        if (!allDetails[i].hasAttribute('open')) {{ allOpen = false; break; }}
      }}
      for (var i = 0; i < allDetails.length; i++) {{
        if (allOpen) allDetails[i].removeAttribute('open');
        else allDetails[i].setAttribute('open', '');
      }}
      btn.textContent = allOpen ? '📂 展开全部模块' : '📖 收起全部模块';
    }});
  }})();

  // ===== Back to top =====
  window.addEventListener('scroll', function() {{
    var btn = document.getElementById('backToTop');
    if (btn) btn.style.display = window.scrollY > 400 ? 'flex' : 'none';
  }}, {{ passive: true }});
  document.getElementById('backToTop').addEventListener('click', function() {{
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});

  // ===== Sidebar =====
  var sidebar = document.getElementById('sidebar');
  document.getElementById('sidebarHideBtn').addEventListener('click', function() {{ sidebar.classList.add('hidden'); }});
  document.getElementById('sidebarShowBtn').addEventListener('click', function() {{ sidebar.classList.remove('hidden'); }});

  // ===== Solution toggle =====
  document.querySelectorAll('.q-toggle').forEach(function(b){{
    b.addEventListener('click', function(e) {{ e.stopPropagation(); this.parentElement.classList.toggle('show-solution'); }});
  }});
}})();
</script>

</body>
</html>'''


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def build_sidebar_nav(all_sections, current_id):
    lines = []
    lines.append('  <nav>')
    lines.append('    <a href="index.html" style="font-weight:600;">🏠 返回首页</a>')
    for section in all_sections:
        label = section.get('label', '')
        lines.append(f'    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ {label} ━━</a>')
        for u in section['units']:
            uid = u['id']
            href = u.get('href', f'{uid}.html')
            title = u['title']
            active = ' class="active"' if uid == current_id else ''
            style = ' style="opacity:0.6;"' if u.get('status') == 'pending' else ''
            lines.append(f'    <a href="{href}"{style}{active}>{title}</a>')
    lines.append('  </nav>')
    return '\n'.join(lines)


def build_cover(u):
    return f'''<div class="cover">
  <div class="sub-en">Unit {u["num"]}</div>
  <h1>{u["title_en"]}</h1>
  <p>{u.get("title_sub", "")}</p>
</div>'''


def build_meta(u):
    m = u.get('meta', {})
    parts = [
        f'<span>📖 话题：{m.get("topic", "")}</span>',
        f'<span>💬 功能：{m.get("function", "")}</span>',
        f'<span>📚 语法：{m.get("grammar", "")}</span>',
        f'<span>📝 写作：{m.get("writing", "")}</span>',
    ]
    return f'''<div class="unit-meta">
  {'  '.join(parts)}
</div>'''


def build_can_do(items):
    labels = '\n'.join(f'  <label><input type="checkbox"> {item}</label>' for item in items)
    return f'''<div class="can-do">
  <h3>🎯 我能做到</h3>
{labels}
</div>'''


def build_dialogue_module(u):
    d = u.get('dialogue', {})
    scene = d.get('scene', '')
    cid = d.get('speak_btn_id', 'dialogueText')

    lines_html = []
    for line in d.get('lines', []):
        spk = line['speaker']
        en = line['en']
        speak = esc_attr(line.get('speak', en))
        lines_html.append(
            f'''      <div class="dialogue-line">
        <span class="speaker">{spk}:</span>
        <span class="en-text wotd-say" data-speak="{speak}">{en}</span>
      </div>'''
        )
    dialogue_body = '\n'.join(lines_html)

    trans_ps = '\n'.join(f'        <p>{l["cn"]}</p>' for l in d.get('lines', []) if l.get('cn'))

    expls = d.get('explanations', [])
    expl_block = ''
    if expls:
        expl_block = '    <div class="dialogue-annotation">\n      <p><strong>🔑 重点讲解：</strong></p>\n'
        for e in expls:
            expl_block += f'      <p>{e}</p>\n'
        expl_block += '    </div>'

    reading = u.get('reading', {})
    reading_title = reading.get('title', '')
    read_cid = reading.get('speak_btn_id', 'readingEnglish')

    notices = []
    glossary = []
    for sec in reading.get('sections', []):
        t = sec.get('type', '')
        if t == 'notice':
            title_text = sec.get('title', '')
            title_speak = sec.get('speak_title', '')
            title_attr = f' data-speak="{esc_attr(title_speak)}"' if title_speak else ''
            title_html = f'<div class="title en-text"{title_attr}>{title_text}</div>' if title_text else ''
            paras = '\n'.join(
                f'          <p class="en-text" data-speak="{esc_attr(p.get("speak", p["en"]))}">{p["en"]}</p>'
                for p in sec.get('paragraphs', [])
            )
            notices.append(
                f'''      <div class="notice">
        {title_html}
{paras}
      </div>'''
            )
        elif t == 'glossary':
            for item in sec.get('items', []):
                text = item['text']
                speak = esc_attr(item.get('speak', ''))
                if speak:
                    glossary.append(
                        f'        <span class="gloss-item wotd-say" data-speak="{speak}">{text}</span>'
                    )
                else:
                    glossary.append(f'        <span class="gloss-item">{text}</span>')

    notices_block = '\n'.join(notices)
    glossary_block = ''
    if glossary:
        glossary_block = '\n      <div class="read-glossary">\n' + '\n'.join(glossary) + '\n      </div>'

    return f'''<!-- ====== 课文精讲 ====== -->
<details class="module" open>
  <summary>📖 课文精讲 · {reading_title}</summary>
  <div class="content">

    <div style="display:flex;gap:8px;align-items:center;margin-bottom:12px;">
      <span style="font-size:13px;color:var(--text-secondary);">场景：{scene}</span>
      <button class="speak-btn" data-dialogue="{cid}" title="朗读整段对话（含间隔）">🔊 朗读对话</button>
    </div>

    <div class="dialogue" id="{cid}">
{dialogue_body}
    </div>

    <details style="margin-top:12px;">
      <summary style="cursor:pointer;font-size:13px;color:var(--accent);font-weight:600;user-select:none;">📖 查看翻译</summary>
      <div class="dialogue-annotation">
        <p><strong>逐句翻译：</strong></p>
{trans_ps}
      </div>
    </details>

    {expl_block}

    <div style="display:flex;gap:8px;align-items:center;margin:20px 0 10px;">
      <h3 style="font-size:15px;color:var(--accent);margin:0;">📖 Reading: {reading_title}</h3>
      <button class="speak-btn" data-dialogue="{read_cid}" title="朗读英文正文（逐句连读）">🔊 朗读课文</button>
    </div>

    <div class="reading" id="readingText">
      <div id="{read_cid}">
{notices_block}
      </div>
{glossary_block}
    </div>

  </div>
</details>'''


def build_vocab_module(u):
    vocab = u.get('vocab', {})
    items = vocab.get('items', [])
    cid = vocab.get('speak_btn_id', 'vocabGrid')
    summary_title = vocab.get('title', '重点词汇')
    topic = vocab.get('topic_label', '')

    cards = []
    for v in items:
        hw = v['headword']
        hw_speak = esc_attr(v.get('speak', hw))
        ex_speak = esc_attr(v.get('example_speak', strip_html(v.get('example', ''))))
        cards.append(
            f'''      <div class="vocab-card">
        <span class="headword wotd-say" data-speak="{hw_speak}">{hw}</span><span class="headword-speak-indicator">🔊</span>
        <span class="ipa">{v.get("ipa", "")}</span>
        <span class="pos">{v.get("pos", "")}</span>
        <div class="definition">{v.get("def", "")}</div>
        <div class="example"><span class="wotd-say" data-speak="{ex_speak}">{v.get("example", "")}</span><span class="trans">{v.get("trans", "")}</span></div>
      </div>'''
        )

    topic_html = f' · {topic}' if topic else ''
    return f'''<!-- ====== 重点词汇 ====== -->
<details class="module" open>
   <summary>📝 {summary_title}{topic_html} <button class="speak-btn" data-vocab="{cid}" title="朗读全部词汇（含例句）">🔊 朗读全部词汇</button></summary>
  <div class="content">

    <div class="vocab-grid" id="{cid}">

{chr(10).join(cards)}

    </div>

  </div>
</details>'''


def build_patterns_module(u):
    patterns = u.get('patterns', [])
    cards = []
    for i, p in enumerate(patterns):
        sp = p.get('speak_id', f'sp{i+1}')
        cards.append(
            f'''      <div class="pattern-card">
        <div class="structure">{p['structure']}</div> <button class="speak-btn" data-target="{sp}" title="朗读句型">🔊</button>
        <div>{p.get('description', '')}</div>
        <div class="substitution"><span class="q-speak-wrap" id="{sp}">{'<br>'.join(p['examples'])}</span></div>
      </div>'''
        )
    return f'''<!-- ====== 重点句型 ====== -->
<details class="module" open>
  <summary>🔤 重点句型 · Sentence Patterns</summary>
  <div class="content">

    <div class="pattern-grid">

{chr(10).join(cards)}

    </div>

  </div>
</details>'''


def build_grammar_module(u):
    blocks = u.get('grammar', [])
    modules = []

    for g in blocks:
        gtype = g.get('type', '')

        if gtype == 'table':
            title = g['title']
            headers = g.get('headers', [])
            rows = g.get('rows', [])
            tip = g.get('tip', '')

            thead = '<tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr>'
            tbody = ''
            for row in rows:
                cells = ''
                for cell in row:
                    if isinstance(cell, dict):
                        speak = esc_attr(cell.get('speak', ''))
                        text = cell.get('text', '')
                        tag = cell.get('tag', '')
                        fmt = f'<{tag}>' if tag else ''
                        fmt_end = f'</{tag}>' if tag else ''
                        if speak:
                            cells += f'<td><span class="wotd-say" data-speak="{speak}">{fmt}{text}{fmt_end}</span></td>'
                        else:
                            cells += f'<td>{fmt}{text}{fmt_end}</td>'
                    else:
                        cells += f'<td>{cell}</td>'
                tbody += f'        <tr>{cells}</tr>\n'

            tip_html = f'<p style="font-size:14px;margin-top:8px;">📌 <strong>{tip}</strong></p>' if tip else ''
            modules.append(
                f'''    <div class="grammar-module">
      <h3>{title}</h3>
      <table class="grammar-table">
        {thead}
{tbody}      </table>
      {tip_html}
    </div>'''
            )

        elif gtype == 'possessive':
            title = g['title']
            rows = g.get('rows', [])
            tip = g.get('tip', '')
            comparisons = g.get('comparisons', [])
            errors = g.get('error_correction', [])

            tbody = ''
            for row in rows:
                cells = ''
                for cell in row:
                    if cell is None:
                        cells += '<td></td>'
                    elif isinstance(cell, dict):
                        speak = esc_attr(cell.get('speak', ''))
                        text = cell.get('text', '')
                        tag = cell.get('tag', '')
                        fmt = f'<{tag}>' if tag else ''
                        fmt_end = f'</{tag}>' if tag else ''
                        if speak:
                            cells += f'<td><span class="wotd-say" data-speak="{speak}">{fmt}{text}{fmt_end}</span></td>'
                        else:
                            cells += f'<td>{fmt}{text}{fmt_end}</td>'
                    else:
                        cells += f'<td>{cell}</td>'
                tbody += f'        <tr>{cells}</tr>\n'

            html = f'''    <div class="grammar-module">
      <h3>{title}</h3>
      <table class="grammar-table">
        <tr><th>人称</th><th>形容词性物主代词<br><span style="font-weight:400;">(后面必须跟名词)</span></th><th>名词性物主代词<br><span style="font-weight:400;">(后面不能跟名词)</span></th></tr>
{tbody}      </table>'''

            if comparisons:
                html += '\n      <p style="font-size:14px;margin-top:8px;">📌 <strong>对比：</strong></p>\n'
                for c in comparisons:
                    en1 = c.get('en1', '')
                    en2 = c.get('en2', '')
                    html += f'      <p style="font-size:14px;">{c.get("text", "")}<br>\n      {en1} = {en2}</p>\n'

            if errors:
                html += '\n\n      <div class="chinese-error">\n        <strong>⚠️ 中式英语纠错：</strong><br>\n'
                for e in errors:
                    wrong = e['wrong']
                    c1 = e['correct1']
                    c2 = e.get('correct2', '')
                    ws = esc_attr(e.get('wrong_speak', wrong))
                    cs1 = esc_attr(e.get('c1_speak', c1))
                    cs2 = esc_attr(e.get('c2_speak', c2)) if c2 else ''
                    html += f'        ❌ <span class="wrong wotd-say" data-speak="{ws}">{wrong}</span><br>\n'
                    html += f'        ✅ <span class="correct wotd-say" data-speak="{cs1}">{c1}</span>'
                    if c2:
                        html += f' 或 <span class="correct wotd-say" data-speak="{cs2}">{c2}</span>'
                    html += '<br><br>\n'
                html += '      </div>'

            if tip:
                html += f'\n      <p style="font-size:14px;margin-top:8px;">📌 <strong>{tip}</strong></p>'

            html += '\n    </div>'
            modules.append(html)

        elif gtype == 'genitive':
            title = g['title']
            rows = g.get('rows', [])
            tip = g.get('tip', '')
            comparison = g.get('comparison', '')

            tbody = ''
            for row in rows:
                rule = row['rule']
                ex = row['example']
                if isinstance(ex, dict):
                    speak = esc_attr(ex['speak'])
                    text = ex['text']
                    tbody += f'<tr><td>{rule}</td><td><span class="wotd-say" data-speak="{speak}">{text}</span></td></tr>\n        '
                else:
                    tbody += f'<tr><td>{rule}</td><td>{ex}</td></tr>\n        '

            html = f'''    <div class="grammar-module">
      <h3>{title}</h3>
      <table class="grammar-table">
        <tr><th>规则</th><th>示例</th></tr>
        {tbody}
      </table>'''

            if comparison:
                html += f'\n      <div class="grammar-tip">\n        <strong>💡 对比：</strong><br>\n        {comparison}\n      </div>'

            if tip:
                html += f'\n      <p style="font-size:14px;margin-top:8px;">📌 <strong>{tip}</strong></p>'

            html += '\n    </div>'
            modules.append(html)

    return f'''<!-- ====== 语法聚焦 ====== -->
<details class="module detail-module" open>
  <summary>📚 语法聚焦 · Demonstratives & Possessives <button class="speak-btn" data-target="grammarContainer" title="朗读全部语法例句">🔊 朗读语法</button></summary>
  <div class="content">

{chr(10).join(modules)}

  </div>
</details>'''


def build_exercises_module(u):
    exercises = u.get('exercises', [])
    level_labels = {'基础': '🥉 基础关 · 概念识记', '提升': '🥈 提升关 · 语境运用', '挑战': '🏆 挑战关 · 综合运用'}
    level_colors = {'基础': 'var(--accent)', '提升': 'var(--accent)', '挑战': 'var(--eng-pink)'}
    level_diff = {'基础': 'easy', '提升': 'mid', '挑战': 'hard'}
    level_stars = {'基础': '★☆☆', '提升': '★★☆', '挑战': '★★★'}

    parts = []
    current = None
    first = True
    for ex in exercises:
        tag = ex.get('tag', '基础')
        if tag != current:
            current = tag
            m = '0 0 10px' if first else '20px 0 10px'
            first = False
            parts.append(f'\n    <h3 style="color:{level_colors.get(tag, "var(--accent)")};margin:{m};">{level_labels.get(tag, tag)}</h3>\n')

        eid = ex.get('id', f'q{hash(str(ex)) % 10000}')
        diff = ex.get('difficulty', level_stars.get(tag, '★☆☆'))
        dc = ex.get('diff_class', level_diff.get(tag, 'easy'))
        body = ex.get('body', '')
        answer = ex.get('answer', '')
        analysis = ex.get('analysis', '')

        parts.append(
            f'''    <div class="exam-q">
      <span class="q-tag">{tag}</span>
      <span class="q-diff {dc}">{diff}</span>
      <div class="q-body"><span class="q-speak-wrap" id="{eid}">{body}</span> <button class="speak-btn" data-target="{eid}" title="朗读题目">🔊</button></div>
      <span class="q-toggle">📝 查看答案</span>
      <div class="q-solution"><strong>答案：</strong>{answer}<br><strong>解析：</strong>{analysis}</div>
    </div>'''
        )

    return f'''<!-- ====== 三级闯关 ====== -->
<details class="exam-module" open>
  <summary>📝 三级闯关 · 实战练习</summary>
  <div class="content">
{chr(10).join(parts)}

  </div>

</details>'''


def build_writing(u):
    w = u.get('writing', {})
    task = w.get('task', '')
    cid = w.get('speak_btn_id', 'microModel')
    translation = w.get('translation', '')

    model_parts = []
    for line in w.get('model_en', []):
        if isinstance(line, dict):
            if line.get('tag'):
                speak = esc_attr(line.get('speak', line['tag']))
                model_parts.append(
                    f'''    <p class="en"><span class="wotd-say" data-speak="{speak}"><strong>{line['tag']}:</strong></span></p>'''
                )
            else:
                en = line['en']
                speak = esc_attr(line.get('speak', en))
                model_parts.append(
                    f'''    <p class="en{' ' + line.get('class', '') if line.get('class') else ''}"><span class="wotd-say" data-speak="{speak}">{en}</span></p>'''
                )
        else:
            model_parts.append(
                f'''    <p class="en"><span class="wotd-say" data-speak="{esc_attr(line)}">{line}</span></p>'''
            )

    return f'''<div class="micro-writing detail-module">
  <h3>✍️ 微写作：{task}</h3>
  <p>{task}</p>
  <div class="model" id="{cid}">
{chr(10).join(model_parts)}
    <span class="trans">{translation}</span>
  </div>
</div>'''


def build_checklist(u):
    items = u.get('checklist', [])
    feynman = u.get('feynman_challenge', '')
    labels = '\n'.join(
        f'  <label><span class="self-score">🟡→🟢</span><input type="checkbox"> {item}</label>'
        for item in items
    )
    feynman_html = ''
    if feynman:
        feynman_html = (
            '  <p style="margin-top:12px;font-size:14px;color:var(--text-secondary);'
            'border-top:1px solid var(--border);padding-top:12px;">\n'
            f'    <strong>🧑‍🏫 费曼挑战：</strong>{feynman}\n  </p>'
        )
    return f'''<div class="checklist detail-module">
  <h3>✅ 章节自查清单</h3>
{labels}
{feynman_html}
</div>'''


def build_review(u):
    items = u.get('review', [])
    dots = '\n'.join(
        f'  <span class="review-dot">{item.get("icon", "🔵")} {item["time"]}：{item["task"]}</span>'
        for item in items
    )
    return f'''<div class="review-schedule">
  <strong>📅 间隔复习</strong>
{dots}
</div>'''


def build_next_stop(u):
    ns = u.get('next_stop', {})
    return f'''<div class="next-stop">
  <strong>➡️ 下一单元：{ns.get("label", "")} {ns.get("title", "")}</strong><br>
  {ns.get("desc", "")}
</div>'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate unit HTML files for English 7 textbook')
    parser.add_argument('--data', default=DATA_FILE, help='JSON data file path')
    parser.add_argument('--outdir', default=SCRIPT_DIR, help='Output directory (default: same as script)')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files (including template)')
    parser.add_argument('--dry-run', action='store_true', help='Print what would be generated without writing')
    args = parser.parse_args()

    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)
    data = json.loads(read_file(args.data))
    sections = data.get('sidebar', [])
    units = data.get('units', [])
    for u in units:
        uid = u['id']
        filename = f'{uid}.html'
        outpath = os.path.join(outdir, filename)

        # Safety check: don't overwrite the template file without --force
        base = os.path.basename(outpath)
        if base == TEMPLATE_FILENAME and not args.force:
            print(f'  SKIP {filename} (is the template file; use --force to overwrite)')
            continue

        print(f'  {"[DRY RUN] " if args.dry_run else ""}Generating {filename}...')

        title = f'Unit {u["num"]} {u["title_en"]} | 初中英语七年级'
        sidebar_html = build_sidebar_nav(sections, uid)
        cover_html = build_cover(u)
        meta_html = build_meta(u)
        can_do_html = build_can_do(u.get('can_do', []))
        dialogue_html = build_dialogue_module(u)
        vocab_html = build_vocab_module(u)
        patterns_html = build_patterns_module(u)
        grammar_html = build_grammar_module(u)
        exercises_html = build_exercises_module(u)
        writing_html = build_writing(u)
        checklist_html = build_checklist(u)
        review_html = build_review(u)
        next_stop_html = build_next_stop(u)

        html = build_full_html(
            title, sidebar_html, cover_html, meta_html, can_do_html,
            dialogue_html, vocab_html, patterns_html, grammar_html,
            exercises_html, writing_html, checklist_html,
            review_html, next_stop_html
        )

        if not args.dry_run:
            write_file(outpath, html)

    print(f'\nDone — {len(units)} file(s) processed.')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    main()
