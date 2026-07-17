#!/usr/bin/env python3
"""Generate appendix-vocab.html for english8 and english9."""
import re, os, json, sys

CARD_PATTERN = r'<div class="vocab-card">(.*?)(?=</div>\s*(?:<div class="vocab-card"|</div>\s*</div>\s*</details>))'

def extract_vocab(html_path):
    with open(html_path) as f:
        html = f.read()
    fn = os.path.splitext(os.path.basename(html_path))[0]
    m = re.search(r'<title>(.+?)</title>', html)
    title = m.group(1) if m else fn
    cards = []
    for card_html in re.findall(CARD_PATTERN, html, re.DOTALL):
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
            cards.append({'w': w.strip(), 'ipa': mi.group(1) if mi else '',
                'pos': mp.group(1) if mp else '', 'def': md.group(1) if md else '',
                'ex': me.group(1) if me else '', 'trans': mt.group(1) if mt else ''})
    return dict(label=fn, title=title, words=cards)

def make_sidebar(prefix, units_a, units_b, grade_label):
    lines = [
        '    <a href="index.html" style="font-weight:600;">🏠 返回首页</a>',
        '    <a href="appendix-grammar.html" style="font-size:13px;">📌 语法全景图</a>',
        '    <a href="appendix-vocab.html" style="font-size:13px;font-weight:600;color:var(--accent);">📖 单词专项</a>',
        f'    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ {grade_label} 上 ━━</a>',
    ]
    for fn in units_a:
        path = os.path.join(prefix, fn)
        with open(path) as fp:
            ct = fp.read()
        mt = re.search(r'<title>(.+?)</title>', ct)
        t = mt.group(1).split('|')[0].strip() if mt else fn
        lines.append(f'    <a href="{fn}">{t}</a>')
    lines.append(f'    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ {grade_label} 下 ━━</a>')
    for fn in units_b:
        path = os.path.join(prefix, fn)
        with open(path) as fp:
            ct = fp.read()
        mt = re.search(r'<title>(.+?)</title>', ct)
        t = mt.group(1).split('|')[0].strip() if mt else fn
        lines.append(f'    <a href="{fn}">{t}</a>')
    return '\n'.join(lines)

if __name__ == '__main__':
    for grade in [8, 9]:
        prefix = f'english{grade}'
        grade_cn = '八年级' if grade == 8 else '九年级'
        grade_label = '八' if grade == 8 else '九'
        theme_key = f'eng{grade}-vocab'
        css_file = f'english{grade}.css' if grade > 7 else 'english.css'
        
        if grade == 8:
            units_a = [f'u{i:02d}.html' for i in range(1,9)]
            units_b = [f'b2u{i:02d}.html' for i in range(1,9)]
        else:
            units_a = [f'u{i:02d}.html' for i in range(1,15)]
            units_b = []
        
        # Extract vocab data
        vocab_data = []
        for fn in units_a + units_b:
            path = os.path.join(prefix, fn)
            if os.path.exists(path):
                data = extract_vocab(path)
                if data['words']:
                    vocab_data.append(data)
        
        data_json = json.dumps(vocab_data, ensure_ascii=False)
        total_words = sum(len(u['words']) for u in vocab_data)
        total_units = len(vocab_data)
        
        # Read english7 template
        with open('english7/appendix-vocab.html') as f:
            html = f.read()
        
        # 1. Replace VOCAB_DATA
        start = html.find('var VOCAB_DATA = [')
        end = html.find('\n\n', start)  # Find the blank line after the array
        if end == -1:
            end = html.find('];', start) + 2
        html = html[:start] + f'var VOCAB_DATA = {data_json};' + html[end:]
        
        # 2. Replace theme key
        html = html.replace("'eng7-vocab'", f"'{theme_key}'")
        html = html.replace('eng7-', f'eng{grade}-')
        
        # 3. Replace grade name
        html = html.replace('七年级', grade_cn)
        html = html.replace('eng7-', f'eng{grade}-')
        
        # 4. Replace CSS link
        html = html.replace('css/english.css', f'css/{css_file}')
        
        # 5. Replace badge count
        html = re.sub(r'(\d+) 单元 · (\d+) 词', f'{total_units} 单元 · {total_words} 词', html)
        
        # 6. Replace shortUnitLabel for new grade format
        sl_map = {}
        for u in vocab_data:
            m = re.match(r'u(\d+)', u['label'])
            if m:
                if grade == 8:
                    sl_map[u['label']] = f"8A-U{int(m.group(1))}"
                else:
                    sl_map[u['label']] = f"9A-U{int(m.group(1))}"
            m = re.match(r'b2u(\d+)', u['label'])
            if m:
                if grade == 8:
                    sl_map[u['label']] = f"8B-U{int(m.group(1))}"
        sl_js = json.dumps(sl_map)
        html = html.replace(
            "function shortUnitLabel(label) {",
            f"""function shortUnitLabel(label) {{
    var map = {sl_js};
    return map[label] || label;
  }}
  
  function shortUnitLabel_old(label) {{"""
        )
        # Remove old implementation
        html = re.sub(
            r'function shortUnitLabel_old\(label\) \{.*?^  \}',
            '',
            html,
            count=1,
            flags=re.DOTALL | re.MULTILINE
        )
        
        # 7. Replace sidebar nav
        sidebar_html = make_sidebar(prefix, units_a, units_b, grade_label)
        # Find the <nav> section in the sidebar
        nav_match = re.search(r'(<nav>\s*\n\s*<a href="index\.html".*?</nav>)', html, re.DOTALL)
        if nav_match:
            html = html.replace(nav_match.group(1), f'<nav>\n{sidebar_html}\n      </nav>', 1)
        
        # 8. Update back link
        html = html.replace('返回七年级', f'返回{grade_cn}')
        
        # 9. Fix duplicate engX- that might have happened
        html = html.replace(f'eng{grade}-' * 2, f'eng{grade}-')
        
        # 10. Replace mobile responsive CSS with enhanced version
        # Find the 2nd 640px block and replace it with card layout version
        second = html.find('@media (max-width: 640px) {', html.find('@media (max-width: 640px) {') + 10)
        if second >= 0:
            style_end = html.find('</style>', second)
            mob_css = '''  .wrapper { padding: 16px 10px 40px; }
  #sidebarShowBtn { z-index: 100; }
  .hero h1 { font-size: 22px; }
  .hero .tagline { font-size: 12px; }
  .hero .badge { font-size: 10px; padding: 3px 10px; }
  .top-bar { flex-direction: column; align-items: stretch; gap: 8px; }
  .view-toggle { justify-content: center; }
  .view-toggle button { font-size: 11px; padding: 5px 10px; }
  #unitFilter { font-size: 12px; padding: 6px 10px; }
  .back-link { font-size: 12px; margin-bottom: 16px; }

  /* ── Vocab units ── */
  .vocab-unit summary { font-size: 13px; padding: 8px 10px; }
  .vocab-unit summary .unit-progress { font-size: 10px; white-space: nowrap; }
  .vocab-unit summary .unit-progress .pct { min-width: 20px; }
  .vocab-unit summary .unit-progress .srs-due { font-size: 9px; padding: 1px 5px; }
  .vocab-unit summary .sum-content span { max-width: 55%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; display: inline-block; vertical-align: middle; }

  /* ── Table → Card layout for mobile ── */
  .vocab-table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 14px; }
  .vocab-table thead { display: none; }
  .vocab-table tbody { display: block; }
  .vocab-table tr { display: block; padding: 12px 14px; margin-bottom: 6px; border: 1px solid var(--border); border-radius: 10px; background: var(--bg); }
  .vocab-table td { display: inline; padding: 0; border: none; white-space: normal; font-size: 14px; }
  .vocab-table .cb-cell { display: inline-block; float: left; margin: 3px 10px 0 0; width: auto; }
  .vocab-table .cb-cell input { width: 18px; height: 18px; }
  .vocab-table .word-cell { display: inline; font-size: 16px; font-weight: 700; color: var(--accent); }
  .vocab-table .word-cell .speak-indicator { font-size: 12px; }
  .vocab-table .word-cell .wrong-tag { font-size: 10px; padding: 1px 6px; vertical-align: middle; }
  .vocab-table .ipa-cell { display: inline; font-size: 12px; color: var(--text-secondary); margin-left: 6px; }
  .vocab-table .pos-cell { display: inline; font-size: 11px; color: var(--accent); text-transform: uppercase; margin-left: 4px; }
  .vocab-table .def-cell { display: block; font-size: 14px; color: var(--text); margin-top: 6px; padding-left: 0 !important; white-space: normal; }
  .vocab-table .ex-cell { display: none; }
  .vocab-table .mastered td { opacity: 0.55; }
  .vocab-table .wrong-row { background: #fef2f2; border-color: #fecaca; }
  [data-theme="dark"] .vocab-table .wrong-row { background: #2d0a0a; border-color: #7f1d1d; }

  /* ── Other views ── */
  .flashcard .front .big-word { font-size: 24px; }
  .flashcard .back .back-def { font-size: 20px; }
  .flashcard .front, .flashcard .back { padding: 24px 16px; min-height: 240px; }
  .flashcard-nav button { padding: 8px 16px; font-size: 13px; min-height: 44px; }
  .flashcard-header { flex-direction: column; align-items: flex-start; }
  .dictation-card .dict-chinese { font-size: 22px; }
  .dictation-input-wrap input { font-size: 16px; padding: 10px 12px; }
  .dictation-input-wrap { max-width: 100%; }
  .dictation-nav button { padding: 8px 16px; font-size: 13px; }
  .quiz-question { font-size: 20px; }
  .quiz-option { font-size: 14px; padding: 10px 12px; }
  .quiz-header .q-progress { font-size: 12px; }
  .stats-grid { grid-template-columns: 1fr 1fr; gap: 8px; }
  .stat-card .stat-value { font-size: 22px; }
  .stat-card { padding: 14px; }
  .stats-wrong-list { max-height: 200px; }
  .stats-units .su-row { padding: 6px 8px; }
  .stats-units .su-label { font-size: 11px; min-width: 0; }
}'''
            html = html[:second] + '@media (max-width: 640px) {' + mob_css + html[style_end:]
        
        # Also replace the 700px block
        old_700 = '''@media (max-width: 700px) {
  .vocab-table .ipa-cell, .vocab-table .ex-cell { display: none; }
  .vocab-table th:nth-child(3), .vocab-table th:nth-child(6) { display: none; }
}'''
        new_700 = '''@media (max-width: 700px) {
  .vocab-table th:nth-child(3), .vocab-table th:nth-child(6) { display: none; }
  .vocab-table .ipa-cell, .vocab-table .ex-cell { display: none; }
  .vocab-unit summary .sum-content span { font-size: 13px; }
}'''
        html = html.replace(old_700, new_700)
        
        # Add 320px/360px blocks before </style>
        extra_mob = '''
@media (max-width: 360px) {
  .hero h1 { font-size: 18px; }
  .view-toggle button { font-size: 9px; padding: 3px 6px; }
  .vocab-table tr { padding: 10px 8px; }
  .vocab-table .word-cell { font-size: 15px; }
  .vocab-table .ipa-cell { display: none; }
  .vocab-table .pos-cell { font-size: 10px; }
  .vocab-table .def-cell { font-size: 13px; }
  .vocab-table .cb-cell input { width: 16px; height: 16px; }
  .vocab-unit summary { font-size: 12px; padding: 6px 8px; }
  .vocab-unit summary .sum-content span { max-width: 50%; font-size: 11px; }
  .vocab-unit summary .unit-progress .srs-due { display: none; }
}
@media (max-width: 320px) {
  .wrapper { padding: 12px 6px 30px; }
  .hero h1 { font-size: 16px; }
  .view-toggle button { font-size: 8px; padding: 3px 5px; }
  .vocab-unit summary { font-size: 11px; padding: 6px; }
  .vocab-unit summary .sum-content span { max-width: 45%; font-size: 10px; }
  .vocab-table tr { padding: 8px 6px; }
  .vocab-table .word-cell { font-size: 14px; }
  .vocab-table .pos-cell { display: none; }
  .vocab-table .def-cell { font-size: 12px; }
  .vocab-table .cb-cell { float: none; display: inline-block; margin-right: 6px; }
  .flashcard .front .big-word { font-size: 20px; }
  .flashcard .back .back-def { font-size: 17px; }
  .flashcard .front, .flashcard .back { padding: 16px 12px; min-height: 200px; }
  .dictation-card .dict-chinese { font-size: 18px; }
  .dictation-input-wrap input { font-size: 14px; padding: 8px 10px; }
  .quiz-question { font-size: 17px; }
  .quiz-option { font-size: 13px; padding: 8px 10px; }
  .stat-card .stat-value { font-size: 18px; }
  .stat-card { padding: 10px; }
}'''
        html = html.replace('</style>', extra_mob + '\n</style>')
        
        # Write output
        output_path = os.path.join(prefix, 'appendix-vocab.html')
        with open(output_path, 'w') as f:
            f.write(html)
        
        print(f'✅ {output_path} ({total_units} units, {total_words} words, {len(html)} chars)')
