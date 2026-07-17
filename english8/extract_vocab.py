#!/usr/bin/env python3
"""Extract vocab data from english8 unit pages and generate appendix-vocab.html"""
import re, os, json, sys

UNIT_PATTERN = r'<div class="vocab-card">(.*?)(?=</div>\s*(?:<div class="vocab-card"|</div>\s*</div>\s*</details>))'

def extract_vocab(html_path):
    with open(html_path) as f:
        html = f.read()
    label = os.path.splitext(os.path.basename(html_path))[0]
    m = re.search(r'<title>(.+?)</title>', html)
    title = m.group(1) if m else label
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
    return dict(label=label, title=title, words=cards)

if __name__ == '__main__':
    grade = sys.argv[1] if len(sys.argv) > 1 else '8'
    if grade == '8':
        prefix = 'english8'
        theme_key = 'eng8-vocab'
        grade_name = '八年级'
        unit_files = sorted([f'{prefix}/u{i:02d}.html' for i in range(1,9)] + 
                           [f'{prefix}/b2u{i:02d}.html' for i in range(1,9)])
    else:
        prefix = 'english9'
        theme_key = 'eng9-vocab'
        grade_name = '九年级'
        unit_files = sorted([f'{prefix}/u{i:02d}.html' for i in range(1,15)])

    vocab_data = []
    for f in unit_files:
        if os.path.exists(f):
            data = extract_vocab(f)
            if data['words']:
                vocab_data.append(data)
                print(f"  {data['label']}: {len(data['words'])} words")

    data_json = json.dumps(vocab_data, ensure_ascii=False)
    print(f"\nTotal: {len(vocab_data)} units, {sum(len(u['words']) for u in vocab_data)} words")
    print(f"\nVOCAB_DATA = {data_json[:200]}...")
