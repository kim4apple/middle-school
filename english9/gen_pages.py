#!/usr/bin/env python3
"""Generate Grade 9 English unit pages from content data."""

import os, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))

GRADE = "english9"
THEME_KEY = "eng9-theme"
CSS_FILE = "css/english9.css"

CONTENT_MODULES = ["content_9"]

ALL_UNITS = [
    ("u01","U1","How can we become good learners?", "学习方法",None,"u02.html"),
    ("u02","U2","I think that mooncakes are delicious!", "节日与文化","u01.html","u03.html"),
    ("u03","U3","Could you please tell me where the restrooms are?", "问路与请求","u02.html","u04.html"),
    ("u04","U4","I used to be afraid of the dark.", "变化与成长","u03.html","u05.html"),
    ("u05","U5","What are the shirts made of?", "产品与材料","u04.html","u06.html"),
    ("u06","U6","When was it invented?", "发明历史","u05.html","u07.html"),
    ("u07","U7","Teenagers should be allowed to choose their own clothes.", "规则与许可","u06.html","u08.html"),
    ("u08","U8","It must belong to Carla.", "推测与判断","u07.html","u09.html"),
    ("u09","U9","I like music that I can dance to.", "偏好与定从","u08.html","u10.html"),
    ("u10","U10","You're supposed to shake hands.", "礼仪与文化","u09.html","u11.html"),
    ("u11","U11","Sad movies make me cry.", "情感与感受","u10.html","u12.html"),
    ("u12","U12","Life is full of the unexpected.", "意外与经历","u11.html","u13.html"),
    ("u13","U13","We're trying to save the earth!", "环保与行动","u12.html","u14.html"),
    ("u14","U14","I remember meeting all of you in Grade 7.", "回忆与毕业","u13.html",None),
]

def load_content():
    merged = {}
    for mod_name in CONTENT_MODULES:
        try:
            mod = importlib.import_module(mod_name)
            import_key = f"UNITS_{mod_name.split('_')[1]}"
            for key, val in getattr(mod, import_key).items():
                merged[key] = val
            print(f"  Loaded {mod_name}")
        except (ImportError, AttributeError) as e:
            print(f"  ⚠ {mod_name}: {e}")
    return merged

def build_sidebar(current_id):
    lines = ['    <nav id="sidebar">']
    lines.append('      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">')
    lines.append('        <h2 style="margin-bottom:0;">英语九年级</h2>')
    lines.append('        <button id="sidebarHideBtn" style="background:none;border:none;cursor:pointer;font-size:16px;color:var(--text-secondary);padding:2px 6px;border-radius:4px;">✕</button>')
    lines.append('      </div><nav>')
    lines.append('        <a href="index.html" style="font-weight:600;">🏠 返回首页</a>')
    lines.append('        <a href="../grammar.html" style="font-size:13px;">📌 语法全景图</a>')
    lines.append('        <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ 九年级全一册 ━━</a>')
    for uid, num, title, _, _, _ in ALL_UNITS:
        active_mark = ' class="active"' if uid == current_id else ''
        lines.append(f'        <a href="{uid}.html"{active_mark}>{num} {title}</a>')
    lines.append('      </nav>')
    lines.append('      <button class="expand-btn" id="expandAllBtn">📂 展开全部模块</button>')
    lines.append('      <button class="theme-toggle" id="themeToggle" onclick="toggleTheme()" title="切换主题">🌙</button>')
    lines.append('    </nav>')
    return '\n'.join(lines)

def build_vocab(vocab):
    cards = []
    for hw, ipa, pos, defn, ex, trans in vocab:
        cards.append(f'''      <div class="vocab-card">
        <span class="headword wotd-say" data-speak="{hw}">{hw}</span><span class="headword-speak-indicator">🔊</span>
        <span class="ipa">/{ipa}/</span><span class="pos">{pos}</span>
        <div class="definition">{defn}</div>
        <div class="example"><span class="wotd-say" data-speak="{ex}">{ex}</span><span class="trans">{trans}</span></div>
      </div>''')
    return '\n'.join(cards)

def build_patterns(patterns):
    cards = []
    for i, (title, note, body) in enumerate(patterns):
        cards.append(f'''      <div class="pattern-card">
        <div class="structure">{title}</div> <button class="speak-btn" data-target="sp{i+1}" title="朗读句型">🔊</button>
        <div>{note}</div>
        <div class="substitution"><span class="q-speak-wrap" id="sp{i+1}">{body}</span></div>
      </div>''')
    return '\n'.join(cards)

def build_grammar_table(rows):
    html = '<table class="grammar-table">\n'
    for i, row in enumerate(rows):
        tag = 'th' if i == 0 else 'td'
        html += '<tr>' + ''.join(f'<{tag}>{" ".join(cell.split())}</{tag}>' for cell in row) + '</tr>\n'
    html += '</table>'
    return html

def build_grammar(data):
    sections = ""
    for title, table_rows in data:
        sections += f'<h3>{title}</h3>\n' + build_grammar_table(table_rows) + '\n'
    return sections

def build_exam_qs(qs):
    questions = []
    for item in qs:
        t, diff, body, answer = item[:4]
        questions.append(f'''    <div class="exam-q">
      <span class="q-tag">{t}</span><span class="q-diff">{diff}</span>
      <div class="q-body">{body}</div>
      <span class="q-toggle">📝 查看答案</span>
      <div class="q-solution"><strong>答案：</strong>{answer}</div>
    </div>''')
    return '\n'.join(questions)

def build_reading_gloss(gloss):
    return ''.join(f'<span>{w} {d}</span> ' for w, d in gloss)

def build_reading_qs(qs):
    return '\n'.join(f'''    <div class="exam-q reading-q">
      <span class="q-tag">{q[0]}</span><span class="q-diff">{q[1]}</span>
      <div class="q-body">{q[2]}</div>
      <span class="q-toggle">📝 查看答案</span>
      <div class="q-solution"><strong>答案：</strong>{q[3]}</div>
    </div>''' for q in qs)

def build_exam_options(options):
    html = ''
    for num, choices in options:
        html += f'<div style="margin:4px 0;font-size:13px;"><strong>{num}</strong> '
        for letter, text in choices.items():
            html += f'<span style="margin-right:12px;"><input type="radio" name="exam_{num}" disabled> {letter}. {text}</span> '
        html += '</div>\n'
    return html

def build_page(uid, num, title, topic, prev, next_, c):
    page_title = f"{num} {title} | 初中英语九年级"
    sidebar = build_sidebar(uid)
    prev_link = f'<a href="{prev}" class="nav-arrow">← 上一单元</a>' if prev else '<span></span>'
    next_link = f'<a href="{next_}" class="nav-arrow">下一单元 →</a>' if next_ else '<span></span>'
    next_unit_text = c.get("next_unit_desc", "")
    next_unit_title = c.get("next_unit_title", "")

    dialogue_lines = '\n'.join(f'      <div class="dialogue-line"><span class="speaker">{s}:</span><span class="en-text wotd-say" data-speak="{en}">{en}</span></div>' for s, en, _ in c["dialogue"])
    dialogue_trans = '\n'.join(f'        <p><strong>{s}:</strong> {cn}</p>' for s, _, cn in c["dialogue"])
    key_points = '\n'.join(f'      <p>{kp}</p>' for kp in c["key_points"])
    grammar_tips = '\n'.join(f'      <p>{t}</p>' for t in c.get("grammar_tips", []))
    reading_text = '\n'.join(f'      <p class="en-text">{p}</p>' for p in c["reading_text"])
    reading_gloss = build_reading_gloss(c["reading_gloss"])
    reading_qs = build_reading_qs(c["reading_qs"])
    exam_passage = '\n'.join(f'      <p>{p}</p>' for p in c["exam_passage"])
    exam_options = build_exam_options(c["exam_options"])
    exam_answers = '；'.join(c["exam_answers"])
    review_items = '\n'.join(f'    <span class="review-dot">{r}</span>' for r in c["review"])
    can_do = '\n'.join(f'  <label><input type="checkbox"> {item}</label>' for item in c["can_do"])

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link rel="stylesheet" href="{CSS_FILE}">
<style>
.speak-btn {{ display:inline-flex;align-items:center;gap:4px;font-size:12px;cursor:pointer;color:var(--accent);border:1px solid var(--border);border-radius:4px;padding:2px 8px;background:var(--bg);transition:background 0.15s; }}
.speak-btn:hover {{ background:var(--accent-light); }}
.speak-btn.speaking {{ background:var(--eng-amber-light);color:var(--eng-amber);border-color:var(--eng-amber); }}
.headword-speak-indicator {{ font-size:11px;margin-left:3px;opacity:0.55;cursor:pointer;vertical-align:super;line-height:1; }}
.headword-speak-indicator:hover {{ opacity:1; }}
.wotd-say {{ cursor:pointer;transition:color 0.15s; }}
.wotd-say:hover {{ color:var(--accent); }}
.wotd-say.speaking {{ color:var(--eng-pink); }}
.speech-panel {{ position:fixed;bottom:80px;right:24px;z-index:999;background:var(--bg);border:1px solid var(--border);border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.12);padding:14px 18px;display:none;min-width:180px; }}
.speech-panel.open {{ display:block; }}
.speech-panel .row {{ display:flex;align-items:center;gap:8px;margin:4px 0;font-size:13px; }}
.speech-panel .row label {{ color:var(--text-secondary);font-size:12px;min-width:36px; }}
.speech-panel select,.speech-panel input[type="range"] {{ flex:1; }}
.speech-panel button {{ padding:4px 12px;border-radius:6px;border:1px solid var(--border);background:var(--bg);color:var(--text);cursor:pointer;font-size:12px; }}
.speech-panel button:hover {{ background:var(--accent-light); }}
.speech-toggle-btn {{ position:fixed;bottom:24px;right:76px;z-index:999;width:44px;height:44px;border-radius:50%;border:1px solid var(--border);background:var(--bg);color:var(--accent);cursor:pointer;font-size:18px;box-shadow:0 2px 8px rgba(0,0,0,0.12);display:flex;align-items:center;justify-content:center; }}
.speech-toggle-btn:hover {{ background:var(--accent-light); }}
.en-text.speaking {{ background:var(--eng-amber-light);border-radius:4px;padding:2px 4px;transition:background 0.2s; }}
[data-theme="dark"] .speech-panel {{ box-shadow:0 4px 20px rgba(0,0,0,0.5); }}
[data-theme="dark"] .en-text.speaking {{ background:#452a08; }}
.detail-module {{ content-visibility:auto;contain-intrinsic-size:300px; }}
.reading {{ content-visibility:auto;contain-intrinsic-size:400px; }}
</style>
<script>(function(){{var t=localStorage.getItem("{THEME_KEY}");if(!t)t=window.matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light";document.documentElement.setAttribute("data-theme",t);}})();</script>
</head>
<body>
<button id="sidebarShowBtn">☰ 侧栏</button>
<button class="back-to-top" id="backToTop">↑</button>
{sidebar}
<main id="content">
<div class="cover"><div class="sub-en">{num}</div><h1>{title}</h1><p>{topic}</p></div>
<div class="unit-meta"><span>📖 话题：{c["en_topic"]}</span><span>💬 功能：{c["functions"]}</span><span>📚 语法：{c["grammar"]}</span><span>📝 写作：{c["writing"]}</span></div>
<div class="can-do"><h3>🎯 我能做到</h3>{can_do}</div>
<details class="module" open><summary>📖 课文精讲 · {title}</summary><div class="content">
<div style="display:flex;gap:8px;align-items:center;margin-bottom:12px;"><span style="font-size:13px;color:var(--text-secondary);">场景：{c["dialogue_scene"]}</span><button class="speak-btn" data-dialogue="dialogueText" title="朗读整段对话">🔊 朗读对话</button></div>
<div class="dialogue" id="dialogueText">{dialogue_lines}</div>
<details style="margin-top:12px;"><summary style="cursor:pointer;font-size:13px;color:var(--accent);font-weight:600;user-select:none;">📖 查看翻译</summary><div class="dialogue-annotation">{dialogue_trans}</div></details>
<div class="dialogue-annotation"><p><strong>🔑 重点讲解：</strong></p>{key_points}</div></div></details>
<details class="module" open><summary>📝 重点词汇 · {topic} <button class="speak-btn" data-vocab="vocabGrid" title="朗读全部词汇">🔊 朗读全部词汇</button></summary><div class="content"><div class="vocab-grid" id="vocabGrid">{build_vocab(c["vocab"])}</div></div></details>
<details class="module" open><summary>🔤 重点句型 · Sentence Patterns</summary><div class="content"><div class="pattern-grid">{build_patterns(c["patterns"])}</div></div></details>
<details class="module detail-module" open><summary>📚 语法聚焦 · {c["grammar_title"]} <button class="speak-btn" data-target="grammarContainer" title="朗读全部语法例句">🔊 朗读语法</button></summary><div class="content"><div class="grammar-module">{build_grammar(c["grammar_sections"])}</div><div class="chinese-error">{grammar_tips}</div></div></details>
<details class="exam-module" open><summary>📝 三级闯关 · 实战练习</summary><div class="content"><h3 class="level-basic">🥉 基础关 · 概念识记</h3>{build_exam_qs(c["basic_qs"])}<h3 class="level-mid">🥈 提升关 · 语境运用</h3>{build_exam_qs(c["mid_qs"])}<h3 class="level-hard">🥇 挑战关 · 综合运用</h3>{build_exam_qs(c["hard_qs"])}</div></details>
<details class="module detail-module" open><summary>📖 阅读专项 · {c["reading_title"]}</summary><div class="content reading-module"><div class="reading-passage">{reading_text}<div class="gloss">{reading_gloss}</div></div>{reading_qs}</div></details>
<details class="module detail-module" open><summary>🏆 中考题型专练 · {c["exam_q_type"]}</summary><div class="content exam-section"><p style="font-size:13px;margin-bottom:8px;">{c["exam_q"]}</p><div class="reading-passage" style="background:var(--bg-secondary);">{exam_passage}</div>{exam_options}<div class="exam-q" style="border-left-color:#f59e0b;"><span class="q-tag" style="background:#f59e0b;color:#fff;">答案</span><div class="q-body">{exam_answers}</div></div></div></details>
<details class="module detail-module" open><summary>✍️ 写作进阶 · {c["writing"]}</summary><div class="content writing-module"><div class="writing-prompt"><div class="prompt-title">📋 写作题目</div><div class="prompt-text">{c["writing_prompt"]}</div></div><div class="writing-framework">{"\n".join(f'      <div class="fw-step">{s}</div>' for s in c["writing_framework"])}</div><div class="writing-model"><div class="en">{c["writing_model_en"]}</div><div class="trans">{c["writing_model_cn"]}</div></div></div></details>
<details class="module detail-module" open><summary>🎯 Project · {c["project_title"]}</summary><div class="content project-module"><div class="project-brief"><div class="project-title">{c["project_title"]}</div><div class="project-desc">{c["project_desc"]}</div></div><div class="project-steps">{"\n".join(f'      <div class="step"><span class="step-num">{i+1}</span><span class="step-text">{s}</span></div>' for i,s in enumerate(c["project_steps"]))}</div><div class="project-rubric"><table><tr><th>#</th><th>评价标准</th></tr>{"\n".join(f'<tr><td>{i+1}.</td><td>{r}</td></tr>' for i,r in enumerate(c["project_rubric"]))}</table></div></div></details>
<div class="checklist detail-module"><h3>✅ 章节自查清单</h3>{"\n".join(f'  <label><span class="self-score">🟡→🟢</span><input type="checkbox"> {item}</label>' for item in c["checklist"])}<p style="margin-top:12px;font-size:14px;color:var(--text-secondary);border-top:1px solid var(--border);padding-top:12px;"><strong>🧑‍🏫 费曼挑战：</strong>{c["feynman"]}</p></div>
<div class="review-schedule"><strong>📅 间隔复习</strong>{review_items}</div>
<div class="next-stop" style="display:flex;justify-content:space-between;align-items:center;margin-top:24px;">{prev_link}{next_link}</div>
<div class="next-stop" style="margin-top:8px;"><strong>➡️ 下一单元：{next_unit_title}</strong><br>{next_unit_text}</div>
</main>
<div class="speech-panel" id="speechPanel"><div style="font-weight:700;font-size:13px;margin-bottom:6px;">🔊 语音控制</div><div class="row"><label>语速</label><input type="range" id="speechRate" min="0.5" max="1.5" step="0.1" value="0.9"><span id="speechRateLabel" style="font-size:12px;min-width:32px;text-align:right;">0.9</span></div><div class="row"><label>口音</label><select id="speechVoice"><option value="en-US">🇺🇸 美式</option><option value="en-GB">🇬🇧 英式</option></select></div><div class="row" style="justify-content:space-between;"><button id="speechStopBtn">⏹ 停止</button><button id="speechCloseBtn">✕ 关闭</button></div></div>
<button class="speech-toggle-btn" id="speechToggleBtn">🔊</button>
<script>
(function() {{
  var SpeechManager = {{
    synthesis: window.speechSynthesis, currentUtterance: null, speaking: false, rate: 0.9, voiceURI: 'en-US',
    init: function(){{var s=this;document.getElementById('speechRate').addEventListener('input',function(){{s.rate=+this.value;document.getElementById('speechRateLabel').textContent=this.value;}});document.getElementById('speechVoice').addEventListener('change',function(){{s.voiceURI=this.value;localStorage.setItem('speech-voice',this.value);}});document.getElementById('speechStopBtn').addEventListener('click',function(){{s.stop();}});document.getElementById('speechCloseBtn').addEventListener('click',function(){{document.getElementById('speechPanel').classList.remove('open');}});document.getElementById('speechToggleBtn').addEventListener('click',function(){{document.getElementById('speechPanel').classList.toggle('open');}});}},
    speak: function(t,c){{if(!t)return;this.stop();var u=new SpeechSynthesisUtterance(t);u.lang=this.voiceURI;u.rate=this.rate;u.onend=function(){{if(c)c();}};this.currentUtterance=u;this.synthesis.speak(u);}},
    speakDialogue: function(id,c){{var s=this,el=document.getElementById(id),ls=el?el.querySelectorAll('.en-text'):[],i=0;this.stop();(function n(){{if(i>=ls.length){{if(c)c();return;}}var e=ls[i],t=e.getAttribute('data-speak')||e.textContent;if(!t){{i++;n();return;}}e.classList.add('speaking');var u=new SpeechSynthesisUtterance(t);u.lang=s.voiceURI;u.rate=s.rate;u.onend=function(){{e.classList.remove('speaking');i++;setTimeout(n,500);}};u.onerror=function(){{e.classList.remove('speaking');i++;setTimeout(n,200);}};s.currentUtterance=u;s.synthesis.speak(u);}})();}},
    speakVocabSection: function(id,c){{var s=this,el=document.getElementById(id),cs=el?el.querySelectorAll('.vocab-card'):[],i=0;this.stop();(function n(){{if(i>=cs.length){{if(c)c();return;}}var e=cs[i],hw=e.querySelector('.headword'),ex=e.querySelector('.example .wotd-say'),t=[];if(hw)t.push(hw.getAttribute('data-speak')||hw.textContent);if(ex)t.push(ex.getAttribute('data-speak')||ex.textContent.replace(/<[^>]+>/g,'').trim());var ft=t.join('. ');if(!ft){{i++;n();return;}}hw.classList.add('speaking');var u=new SpeechSynthesisUtterance(ft);u.lang=s.voiceURI;u.rate=s.rate;u.onend=function(){{hw.classList.remove('speaking');i++;setTimeout(n,600);}};u.onerror=function(){{hw.classList.remove('speaking');i++;setTimeout(n,300);}};s.currentUtterance=u;s.synthesis.speak(u);}})();}},
    stop: function(){{this.synthesis.cancel();this.speaking=false;}}
  }};SpeechManager.init();
  document.querySelectorAll('.wotd-say').forEach(function(el){{el.addEventListener('click',function(){{SpeechManager.speak(this.getAttribute('data-speak')||this.textContent);}});}});
  document.querySelectorAll('.speak-btn').forEach(function(btn){{btn.addEventListener('click',function(e){{e.stopPropagation();var d=this.getAttribute('data-dialogue'),v=this.getAttribute('data-vocab'),t=this.getAttribute('data-target');if(this.classList.contains('speaking')){{SpeechManager.stop();this.classList.remove('speaking');return;}}this.classList.add('speaking');var done=function(){{btn.classList.remove('speaking');}};if(d){{SpeechManager.speakDialogue(d,done);}}else if(v){{SpeechManager.speakVocabSection(v,done);}}else if(t){{var tg=document.getElementById(t);if(!tg){{btn.classList.remove('speaking');return;}}SpeechManager.speak(tg.textContent.replace(/<[^>]+>/g,''),done);}}else{{btn.classList.remove('speaking');}}}});}});
  document.querySelectorAll('.headword-speak-indicator').forEach(function(el){{el.addEventListener('click',function(e){{e.stopPropagation();var hw=this.previousElementSibling;if(hw&&hw.classList.contains('wotd-say')){{var t=hw.getAttribute('data-speak')||hw.textContent;SpeechManager.speak(t);}}}});}});
  (function(){{var btn=document.getElementById('expandAllBtn');if(!btn)return;btn.addEventListener('click',function(){{var ad=document.querySelectorAll('.module,.exam-module');var ao=true;for(var i=0;i<ad.length;i++){{if(!ad[i].hasAttribute('open')){{ao=false;break;}}}};for(var i=0;i<ad.length;i++){{if(ao)ad[i].removeAttribute('open');else ad[i].setAttribute('open','');}};btn.textContent=ao?'📂 展开全部模块':'📖 收起全部模块';}});}})();
  var s=document.getElementById('sidebar'),k='{THEME_KEY}-sidebar';if(!s)return;
  if(localStorage.getItem(k)==='hidden'){{s.classList.add('hidden');document.body.classList.add('sidebar-hidden')}}
  var h=document.getElementById('sidebarHideBtn'),w=document.getElementById('sidebarShowBtn');
  if(h)h.addEventListener('click',function(){{s.classList.add('hidden');document.body.classList.add('sidebar-hidden');localStorage.setItem(k,'hidden')}});
  if(w)w.addEventListener('click',function(){{s.classList.remove('hidden');document.body.classList.remove('sidebar-hidden');localStorage.setItem(k,'')}});
  window.addEventListener('scroll',function(){{var b=document.getElementById('backToTop');if(b)b.style.display=window.scrollY>400?'flex':'none';}},{{passive:true}});
  document.getElementById('backToTop').addEventListener('click',function(){{window.scrollTo({{top:0,behavior:'smooth'}});}});
  document.querySelectorAll('.q-toggle').forEach(function(b){{b.addEventListener('click',function(e){{e.stopPropagation();this.parentElement.classList.toggle('show-solution');}});}});
}})();
function setTheme(t){{document.documentElement.setAttribute("data-theme",t);localStorage.setItem("{THEME_KEY}",t);var btn=document.getElementById("themeToggle");if(btn)btn.textContent=t==="dark"?"☀️":"🌙";}}
function toggleTheme(){{setTheme(document.documentElement.getAttribute("data-theme")==="dark"?"light":"dark");}}
</script></body></html>'''

def generate_all():
    print("Loading content modules...")
    content = load_content()
    print(f"Total units: {len(content)}")
    print("Generating pages...")
    for uid, num, title, topic, prev, next_ in ALL_UNITS:
        c = content.get(uid)
        if not c:
            print(f"  ⏭ {uid}.html (no content)")
            continue
        html = build_page(uid, num, title, topic, prev, next_, c)
        path = os.path.join(os.path.dirname(__file__), f"{uid}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {uid}.html")

if __name__ == "__main__":
    generate_all()
    print("Done!")
