#!/usr/bin/env python3
"""Extract vocabulary data from all 24 unit files, merge with supplement,
and inject into appendix-vocab.html template (preserving all UI/JS features)."""

import re
import json
from pathlib import Path

BASE = Path(__file__).parent
TEMPLATE_PATH = BASE / "appendix-vocab.html"
UNIT_FILES = [
    "st01.html", "st02.html", "st03.html",
    "u01.html", "u02.html", "u03.html", "u04.html", "u05.html",
    "u06.html", "u07.html",
    "b2u01.html", "b2u02.html", "b2u03.html", "b2u04.html", "b2u05.html",
    "b2u06.html", "b2u07.html", "b2u08.html",
]


def build_level_map(html):
    boundaries = [(0, 'basic')]
    for m in re.finditer(r'<summary>[^<]*词汇[^<]*</summary>', html):
        s = m.group()
        if '学霸' in s:
            boundaries.append((m.start(), 'expert'))
        elif '掌握' in s:
            boundaries.append((m.start(), 'master'))
        elif '基础' in s:
            boundaries.append((m.start(), 'basic'))
    return boundaries


def get_level_for_card(pos, boundaries):
    level = 'basic'
    for b_pos, b_level in boundaries:
        if b_pos < pos:
            level = b_level
        else:
            break
    return level


def extract_units():
    units = []
    for fname in UNIT_FILES:
        path = BASE / fname
        html = path.read_text(encoding="utf-8")
        level_map = build_level_map(html)

        title_m = re.search(r'<title>(.+?)</title>', html)
        title = title_m.group(1) if title_m else fname

        unit_label = fname.replace(".html", "")
        words = []

        for m_card in re.finditer(
            r'<div class="vocab-card">(.*?)(?=</div>\s*(?:<div class="vocab-card"|</div>\s*</div>\s*</details>|</div>\s*</div>\s*</div>\s*</details>))',
            html, re.DOTALL
        ):
            card = m_card.group(1)
            pos = m_card.start()
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

            trans_m = re.search(r'<span class="trans">([^<]*)</span>', card)

            level = get_level_for_card(pos, level_map)

            words.append({
                "w": word,
                "ipa": ipa_m.group(1) if ipa_m else "",
                "pos": pos_m.group(1) if pos_m else "",
                "def": defn_m.group(1).strip() if defn_m else "",
                "ex": example,
                "trans": trans_m.group(1) if trans_m else "",
                "level": level,
            })

        units.append({"label": unit_label, "title": title, "words": words})
    return units


def merge_supplement(units):
    supp_path = BASE / "vocab-supplement.json"
    if not supp_path.exists():
        return units
    supp = json.loads(supp_path.read_text(encoding="utf-8"))
    for unit in units:
        label = unit["label"]
        extra = supp.get(label, [])
        if not extra:
            continue
        existing_words = {w["w"] for w in unit["words"]}
        for w in extra:
            if w["w"] not in existing_words:
                if "level" not in w:
                    w["level"] = "basic"
                unit["words"].append(w)
                existing_words.add(w["w"])
    return units


def inject_data(units, template_path):
    html = template_path.read_text(encoding="utf-8")
    data_json = json.dumps(units, ensure_ascii=False)

    # Replace VOCAB_DATA — find start/end by bracket depth
    marker = "var VOCAB_DATA = "
    start = html.find(marker)
    if start == -1:
        raise ValueError("VOCAB_DATA marker not found in template")
    data_start = start + len(marker)

    depth = 0
    in_str = False
    end = data_start
    for i in range(data_start, len(html)):
        ch = html[i]
        if ch == '"' and (i == data_start or html[i - 1] != "\\"):
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

    # Update word count in tagline
    total = sum(len(u["words"]) for u in units)
    html = re.sub(r"(\d+) 词集中突破", f"{total} 词集中突破", html)

    template_path.write_text(html, encoding="utf-8")
    print(f"Injected {total} words across {len(units)} units into {template_path}")


if __name__ == "__main__":
    units = extract_units()
    units = merge_supplement(units)
    total_words = sum(len(u["words"]) for u in units)
    print(f"Extracted + supplemented: {total_words} words across {len(units)} units")
    inject_data(units, TEMPLATE_PATH)
