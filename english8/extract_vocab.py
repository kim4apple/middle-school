#!/usr/bin/env python3
"""Extract vocabulary (3-tier: basic/master/expert) from unit pages
and inject into appendix-vocab.html"""

import re
import json
import sys
from pathlib import Path

BASE = Path(__file__).parent
TEMPLATE_PATH = BASE / "appendix-vocab.html"
MARKER = "var VOCAB_DATA = "

UNIT_PATTERN = r'<div class="vocab-card">(.*?)(?=</div>\s*(?:<div class="vocab-card"|</div>\s*</div>\s*</details>|</div>\s*</div>\s*</div>\s*</details>))'


def build_level_map(html):
    """Pre-scan HTML: return list of (pos, level) boundaries for vocab sections."""
    boundaries = [(0, 'basic')]
    for m in re.finditer(r'<summary>[^<]*词汇[^<]*</summary>', html):
        s = m.group()
        pos = m.start()
        if '学霸' in s:
            boundaries.append((pos, 'expert'))
        elif '掌握' in s:
            boundaries.append((pos, 'master'))
        elif '基础' in s:
            boundaries.append((pos, 'basic'))
    return boundaries

def get_level_for_card(pos, boundaries):
    level = 'basic'
    for b_pos, b_level in boundaries:
        if b_pos < pos:
            level = b_level
        else:
            break
    return level


def extract_vocab(html_path):
    html = html_path.read_text(encoding="utf-8")
    label = html_path.stem
    m = re.search(r'<title>(.+?)</title>', html)
    title = m.group(1) if m else label
    level_map = build_level_map(html)
    cards = []
    for m_card in re.finditer(UNIT_PATTERN, html, re.DOTALL):
        card_html = m_card.group(1)
        pos = m_card.start()
        w = ''
        mw = re.search(r'data-speak="([^"]+)"[^>]*>\s*[^<]+</span>\s*<span class="headword-speak', card_html)
        if mw:
            w = mw.group(1)
        if not w:
            mw2 = re.search(r'class="headword[^"]*"[^>]*>([^<]+)', card_html)
            if mw2:
                w = mw2.group(1)
        mi = re.search(r'class="ipa"[^>]*>([^<]+)', card_html)
        mp = re.search(r'class="pos"[^>]*>([^<]+)', card_html)
        md = re.search(r'class="definition"[^>]*>([^<]+)', card_html)
        me = re.search(r'class="wotd-say"[^>]*data-speak="([^"]+)"', card_html)
        mt = re.search(r'class="trans"[^>]*>([^<]+)', card_html)
        level = get_level_for_card(pos, level_map)

        if w:
            cards.append(dict(
                w=w.strip(),
                ipa=mi.group(1) if mi else '',
                pos=mp.group(1) if mp else '',
                defn=md.group(1) if md else '',
                ex=me.group(1) if me else '',
                trans=mt.group(1) if mt else '',
                level=level,
            ))
    return dict(label=label, title=title, words=cards)


def inject_data(vocab_data, template_path):
    html = template_path.read_text(encoding="utf-8")
    data_json = json.dumps(vocab_data, ensure_ascii=False)
    start = html.find(MARKER)
    if start == -1:
        raise ValueError("VOCAB_DATA marker not found")
    data_start = start + len(MARKER)
    depth = 0
    in_str = False
    end = data_start
    for i in range(data_start, len(html)):
        ch = html[i]
        if ch == '"' and (i == data_start or html[i-1] != "\\"):
            in_str = not in_str
        if not in_str:
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
    html = html[:data_start] + data_json + html[end:]
    template_path.write_text(html, encoding="utf-8")


if __name__ == '__main__':
    grade = sys.argv[1] if len(sys.argv) > 1 else '8'
    if grade == '8':
        prefix = 'english8'
        unit_files = sorted([f'{prefix}/u{i:02d}.html' for i in range(1,9)] +
                           [f'{prefix}/b2u{i:02d}.html' for i in range(1,9)])
    elif grade == '9':
        prefix = 'english9'
        unit_files = sorted([f'{prefix}/u{i:02d}.html' for i in range(1,9)] +
                           [f'{prefix}/b2u{i:02d}.html' for i in range(1,6)])
    else:
        print(f"Unknown grade: {grade}")
        sys.exit(1)

    vocab_data = []
    for f in unit_files:
        p = Path(f)
        if p.exists():
            data = extract_vocab(p)
            if data['words']:
                vocab_data.append(data)
                # Count levels
                levels = {'basic':0, 'master':0, 'expert':0}
                for w in data['words']:
                    l = w.get('level', 'basic')
                    levels[l] = levels.get(l, 0) + 1
                print(f"  {data['label']}: {len(data['words'])} words  "
                      f"(基础{levels['basic']} 掌握{levels['master']} 学霸{levels['expert']})")

    total = sum(len(u['words']) for u in vocab_data)
    print(f"\nTotal: {len(vocab_data)} units, {total} words")

    inject_data(vocab_data, Path(f'{prefix}/appendix-vocab.html'))
    print(f"Injected into {prefix}/appendix-vocab.html")
