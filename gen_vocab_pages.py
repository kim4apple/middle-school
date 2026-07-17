#!/usr/bin/env python3
"""Generate appendix-vocab.html for english8 and english9 from unit pages."""
import re, os, json, sys

UNIT_PATTERN = r'<div class="vocab-card">(.*?)(?=</div>\s*(?:<div class="vocab-card"|</div>\s*</div>\s*</details>))'

def extract_vocab(html_path):
    with open(html_path) as f:
        html = f.read()
    fn = os.path.splitext(os.path.basename(html_path))[0]
    m = re.search(r'<title>(.+?)</title>', html)
    title = m.group(1) if m else fn
    cards = []
    for card_html in re.findall(UNIT_PATTERN, html, re.DOTALL):
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
            cards.append(dict(w=w.strip(), ipa=mi.group(1) if mi else '',
                pos=mp.group(1) if mp else '', defn=md.group(1) if md else '',
                ex=me.group(1) if me else '', trans=mt.group(1) if mt else ''))
    return dict(label=fn, title=title, words=cards)

def short_label(label):
    m = re.match(r'u(\d+)', label)
    if m:
        n = int(m.group(1))
        if n <= 8: return f'8A-U{n}'
        return f'9A-U{n-8}'
    m = re.match(r'b2u(\d+)', label)
    if m: return f'8B-U{int(m.group(1))}'
    return label

def gen_sidebar_links(prefix, grade_label, units_1, units_2):
    """Generate sidebar nav links HTML."""
    lines = []
    lines.append(f'    <a href="index.html" style="font-weight:600;">🏠 返回首页</a>')
    lines.append(f'    <a href="appendix-grammar.html" style="font-size:13px;">📌 语法全景图</a>')
    lines.append(f'    <a href="appendix-vocab.html" style="font-size:13px;font-weight:600;color:var(--accent);">📖 单词专项</a>')
    lines.append(f'    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ {grade_label} 上 ━━</a>')
    for f in units_1:
        path = os.path.join(prefix, f)
        with open(path) as fp:
            content = fp.read()
        m = re.search(r'<title>(.+?)</title>', content)
        title = m.group(1).split('|')[0].strip() if m else f
        lines.append(f'    <a href="{f}">{title}</a>')
    lines.append(f'    <a href="#" style="font-size:12px;color:var(--text-secondary);margin:4px 0;">━━ {grade_label} 下 ━━</a>')
    for f in units_2:
        path = os.path.join(prefix, f)
        with open(path) as fp:
            content = fp.read()
        m = re.search(r'<title>(.+?)</title>', content)
        title = m.group(1).split('|')[0].strip() if m else f
        lines.append(f'    <a href="{f}">{title}</a>')
    return '\n'.join(lines)

def generate_page(prefix, grade_label, theme_key, units_1, units_2, sidebar_links):
    """Generate appendix-vocab.html by extracting data from unit pages."""
    vocab_data = []
    for f in units_1 + units_2:
        path = os.path.join(prefix, f)
        if os.path.exists(path):
            data = extract_vocab(path)
            if data['words']:
                vocab_data.append(data)
    
    data_json = json.dumps(vocab_data, ensure_ascii=False)
    
    # Copy english7 template and customize
    template_path = 'english7/appendix-vocab.html'
    with open(template_path) as f:
        html = f.read()
    
    # Replace the VOCAB_DATA
    # Find the existing VOCAB_DATA and replace with ours
    html = re.sub(
        r'var VOCAB_DATA = \[.*?\];\s*$',
        f'var VOCAB_DATA = {data_json};',
        html,
        count=1,
        flags=re.DOTALL | re.MULTILINE
    )
    
    return html

if __name__ == '__main__':
    # Generate for english8
    prefix = 'english8'
    units_1 = sorted([f'u{i:02d}.html' for i in range(1,9)])
    units_2 = sorted([f'b2u{i:02d}.html' for i in range(1,9)])
    
    vocab_data = []
    for f in units_1 + units_2:
        path = os.path.join(prefix, f)
        if os.path.exists(path):
            data = extract_vocab(path)
            if data['words']:
                vocab_data.append(data)
                print(f"  {data['label']}: {len(data['words'])} words")
    
    data_json = json.dumps(vocab_data, ensure_ascii=False)
    total_words = sum(len(u['words']) for u in vocab_data)
    print(f"\nEnglish8 total: {len(vocab_data)} units, {total_words} words")
    print(f"JSON length: {len(data_json)} chars")
    
    # Write data file for reference
    output_path = os.path.join(prefix, 'vocab-data.json')
    with open(output_path, 'w') as f:
        f.write(data_json)
    print(f"Data written to {output_path}")
