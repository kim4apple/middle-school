#!/usr/bin/env python3
"""Update all unit pages to have exactly 3-tier vocab: 基础 + 掌握 + 学霸.

For each page:
  - Find ALL existing vocab sections (details containing <summary>…词汇…)
  - Determine what's already present
  - Add missing sections (掌握, 学霸) with content from vocab-bank.json
  - Deduplicate if needed
"""

import re
import json
from pathlib import Path

BASE = Path(__file__).parent.parent
VOCAB_BANK = json.loads((BASE / "scripts/vocab-bank.json").read_text())

# Regex to find a complete details module
DETAILS_BLOCK = re.compile(
    r'(<!-- ====== [^=]+ ====== -->\s*)?<details class="module" open>.*?</details>\s*',
    re.DOTALL
)

def make_card(w):
    ww = w['w']
    ipa = w['ipa'].strip('/')
    pos = w['pos']
    defn = w['defn']
    ex = w['ex']
    trans = w['trans']
    return f'''      <div class="vocab-card">
        <span class="headword wotd-say" data-speak="{ww}">{ww}</span><span class="headword-speak-indicator">🔊</span>
        <span class="ipa">/{ipa}/</span><span class="pos">{pos}</span>
        <div class="definition">{defn}</div>
        <div class="example"><span class="wotd-say" data-speak="{ex}">{ex}</span><span class="trans">{trans}</span></div>
      </div>'''

def make_section(emoji, label, subtitle, words):
    cards = '\n'.join(make_card(w) for w in words)
    return f'''\n<!-- ====== {label} ====== -->
<details class="module" open>
  <summary>{emoji} {label} · {subtitle}</summary>
  <div class="content">
    <div class="vocab-grid">
{cards}
    </div>
  </div>
</details>'''


def process_file(path, grade):
    html = path.read_text('utf-8')
    stem = path.stem
    if grade == 7:
        bank_key = stem
    elif grade == 8:
        bank_key = stem + '_8'
    else:
        bank_key = stem + '_9'
    bank = VOCAB_BANK.get(bank_key, {})
    master = bank.get('master', [])
    expert = bank.get('expert', [])

    # 1. Find all vocab sections (details whose summary contains 词汇)
    all_details = list(DETAILS_BLOCK.finditer(html))
    vocab_details = [m for m in all_details if '词汇' in m.group()[:200]]

    # 2. Determine what exists
    has_jichu = any('基础词汇' in m.group()[:200] for m in vocab_details)
    has_zhangwo = any('掌握词汇' in m.group()[:200] for m in vocab_details)
    has_xueba = any('学霸词汇' in m.group()[:200] for m in vocab_details)

    # 3. Fix naming: rename 重点→基础, 学霸→掌握 (when needed)
    if not has_jichu:
        # Rename first occurrence of 重点词汇 or 拓展词汇 to 基础词汇
        html = re.sub(
            r'(<summary>)[^<]*重点词汇',
            lambda m: m.group(1) + '📝 基础词汇',
            html, count=1
        )
        html = re.sub(
            r'<!-- ====== 重点词汇 ====== -->',
            '<!-- ====== 基础词汇 ====== -->',
            html
        )
        has_jichu = True

    # For english9: rename existing 学霸→掌握 if there's no 掌握 yet
    if not has_zhangwo and has_xueba:
        html = re.sub(
            r'(<summary>)[^<]*学霸词汇',
            lambda m: m.group(1) + '🥈 掌握词汇',
            html, count=1
        )
        has_zhangwo = True
        has_xueba = False  # It was renamed, so no longer a 学霸 section

    # 4. Re-scan vocab sections after renames
    all_details = list(DETAILS_BLOCK.finditer(html))
    vocab_details = [m for m in all_details if '词汇' in m.group()[:200]]
    has_jichu = any('基础词汇' in m.group()[:200] for m in vocab_details)
    has_zhangwo = any('掌握词汇' in m.group()[:200] for m in vocab_details)
    has_xueba = any('学霸词汇' in m.group()[:200] for m in vocab_details)

    # 5. Find insertion point: end of the last vocab section
    last_vocab_end = vocab_details[-1].end() if vocab_details else None

    # 6. Add 掌握 if missing
    if master and not has_zhangwo:
        sub = '核心应用' if stem.startswith('st') else '阅读拓展'
        ins = make_section('🥈', '掌握词汇', sub, master)
        if last_vocab_end:
            html = html[:last_vocab_end] + ins + '\n' + html[last_vocab_end:]
            last_vocab_end += len(ins) + 1

    # 7. Add 学霸 if missing
    if expert and not has_xueba:
        ins = make_section('🥇', '学霸词汇', '挑战提升', expert)
        # Re-scan to find updated last vocab section
        all_details = list(DETAILS_BLOCK.finditer(html))
        vocab_details = [m for m in all_details if '词汇' in m.group()[:200]]
        insert_at = vocab_details[-1].end() if vocab_details else len(html)
        html = html[:insert_at] + ins + '\n' + html[insert_at:]

    # 8. Deduplicate: if any vocab section appears twice, remove the second
    # Scan again and check
    all_details = list(DETAILS_BLOCK.finditer(html))
    seen_summaries = {}
    to_remove = []
    for m in all_details:
        block = m.group()
        sum_match = re.search(r'<summary>([^<]*)</summary>', block)
        if sum_match:
            s = sum_match.group(1)
            # Normalize: strip speak-btn etc
            s_clean = re.sub(r'<button[^>]*>.*?</button>', '', s).strip()
            # Check if it's a vocab section
            if '词汇' in s_clean:
                label = re.sub(r'[^\u4e00-\u9fff]', '', s_clean)
                if label in seen_summaries:
                    to_remove.append(m)  # This is a duplicate
                else:
                    seen_summaries[label] = m

    # Remove duplicates (in reverse order to preserve positions)
    for m in reversed(to_remove):
        html = html[:m.start()] + html[m.end():]

    return html


def main():
    configs = [
        (7, [f'english7/st{i:02d}.html' for i in range(1,4)] +
            [f'english7/u{i:02d}.html' for i in range(1,8)] +
            [f'english7/b2u{i:02d}.html' for i in range(1,9)]),
        (8, [f'english8/u{i:02d}.html' for i in range(1,9)] +
            [f'english8/b2u{i:02d}.html' for i in range(1,9)]),
        (9, [f'english9/u{i:02d}.html' for i in range(1,9)] +
            [f'english9/b2u{i:02d}.html' for i in range(1,6)]),
    ]

    for grade, files in configs:
        print(f'=== english{grade} ===')
        for f in files:
            path = BASE / f
            if not path.exists():
                print(f'  SKIP: {f}')
                continue
            html = process_file(path, grade)
            path.write_text(html, 'utf-8')
            cards = len(re.findall(r'<div class="vocab-card">', html))
            sections = [m.group(1)[:55] for m in re.finditer(r'<summary>([^<]*)</summary>', html) if '词汇' in m.group(1)]
            sec_str = ' | '.join(sections) if sections else '(none)'
            print(f'  {path.stem}: {cards} cards  [{sec_str}]')


if __name__ == '__main__':
    main()
