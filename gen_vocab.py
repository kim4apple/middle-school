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
        
        # Write output
        output_path = os.path.join(prefix, 'appendix-vocab.html')
        with open(output_path, 'w') as f:
            f.write(html)
        
        print(f'✅ {output_path} ({total_units} units, {total_words} words, {len(html)} chars)')
