#!/usr/bin/env python3
"""Generate unit HTML files for each unit from u03.html template."""

import re, json

# Load template
with open("u03.html", encoding="utf-8") as f:
    TEMPLATE = f.read()

# Load unit data from separate JSON files
import os, sys

def load_unit_data():
    """Return dict of unit_key -> data dict."""
    with open("english7_units.json", encoding="utf-8") as f:
        return json.load(f)

def gen_html(unit_key, u):
    h = TEMPLATE
    
    # Unit number & title
    num = str(u["num"])
    title = u["title"]
    subtitle = u["subtitle"]
    topic = u["topic"]
    func = u["func"]
    grammar_tag = u["grammar"]
    writing = u["writing"]
    can_do = u["can_do"]
    scene = u["scene"]
    dialogue = u["dialogue"]
    translation = u["translation"]
    key_points = u["key_points"]
    reading_title = u["reading_title"]
    reading_paras = u["reading_paras"]
    gloss = u["gloss"]
    vocab = u["vocab"]
    patterns = u["patterns"]
    grammar_tables = u["grammar_tables"]
    exercises = u["exercises"]
    micro_task = u["micro_task"]
    model_paras = u["model_paras"]
    model_trans = u["model_trans"]
    checklist = u["checklist"]
    feynman = u["feynman"]
    review = u["review"]
    next_unit = str(u["next_unit"])
    next_title = u["next_title"]
    next_desc = u["next_desc"]
    
    # -- Title --
    h = h.replace(
        "Unit 3 Is this your pencil? | \u521d\u4e2d\u82f1\u8bed\u4e03\u5e74\u7ea7",
        f"Unit {num} {title} | \u521d\u4e2d\u82f1\u8bed\u4e03\u5e74\u7ea7"
    )
    
    # -- Cover --
    h = h.replace('<div class="sub-en">Unit 3</div>', f'<div class="sub-en">Unit {num}</div>')
    h = h.replace("<h1>Is this your pencil?</h1>", f"<h1>{title}</h1>")
    h = h.replace(
        "<p>\u786e\u8ba4\u7269\u54c1\u5f52\u5c5e \u00b7 \u7269\u4e3b\u4ee3\u8bcd\u5165\u95e8 \u00b7 \u5931\u7269\u62db\u9886</p>",
        f"<p>{subtitle}</p>"
    )
    
    # -- Unit meta --
    h = h.replace(
        '<span>\U0001f4d6 \u8bdd\u9898\uff1aSchool things</span>',
        f'<span>\U0001f4d6 \u8bdd\u9898\uff1a{topic}</span>'
    )
    h = h.replace(
        '<span>\U0001f4ac \u529f\u80fd\uff1aIdentify ownership</span>',
        f'<span>\U0001f4ac \u529f\u80fd\uff1a{func}</span>'
    )
    h = h.replace(
        '<span>\U0001f4da \u8bed\u6cd5\uff1a\u6307\u793a\u4ee3\u8bcd \u00b7 \u7269\u4e3b\u4ee3\u8bcd</span>',
        f'<span>\U0001f4da \u8bed\u6cd5\uff1a{grammar_tag}</span>'
    )
    h = h.replace(
        '<span>\U0001f4dd \u5199\u4f5c\uff1aLost &amp; Found</span>',
        f'<span>\U0001f4dd \u5199\u4f5c\uff1a{writing}</span>'
    )
    
    # -- Can-do --
    cb_lines = "\n".join(f'  <label><input type="checkbox"> {item}</label>' for item in can_do)
    # Replace the entire can-do block
    can_do_pattern = r'<label><input type="checkbox"> I can ask "Is this/that[^"]*?" and answer[^<]*</label>[\s\S]*?<label><input type="checkbox"> I can write a simple lost / found notice\.</label>'
    h = re.sub(can_do_pattern, cb_lines, h)
    
    # -- Scene --
    h = h.replace(
        '\u573a\u666f\uff1aAnn \u548c Tom \u5728\u6559\u5ba4\u6361\u5230\u4e00\u4e9b\u6587\u5177\uff0c\u6b63\u5728\u5bfb\u627e\u5931\u4e3b\u3002',
        f'\u573a\u666f\uff1a{scene}'
    )
    
    # -- Dialogue --
    dia_lines = []
    for speaker, text in dialogue:
        ds = text.replace("<em>", "").replace("</em>", "")
        dia_lines.append(
            f'      <div class="dialogue-line">\n'
            f'        <span class="speaker">{speaker}:</span>\n'
            f'        <span class="en-text wotd-say" data-speak="{ds}">{text}</span>\n'
            f'      </div>'
        )
    dia_block = "\n".join(dia_lines)
    dia_re = r'<div class="dialogue" id="dialogueText">[\s\S]*?</div>\n\n    <details style="margin-top:12px;">'
    h = re.sub(dia_re, f'<div class="dialogue" id="dialogueText">\n{dia_block}\n    </div>\n\n    <details style="margin-top:12px;">', h)
    
    # -- Translation --
    trans_block = "\n".join(f'        <p>{t}</p>' for t in translation)
    trans_re = r'<p>Tom: \u563b Ann\uff01\u770b\uff01<em>\u8fd9\u662f\u4f60\u7684\u5c3a\u5b50\u5417\uff1f</em></p>[\s\S]*?<p>Ann: \u4e0d\uff0c\u4e0d\u662f\u3002<em>\u6211\u7684\u662f\u9ec4\u8272\u7684</em>\u3002\u90a3\u4e9b\u662f\u7ea2\u8272\u7684\u3002</p>'
    h = re.sub(trans_re, trans_block, h)
    
    # -- Key points --
    kp_lines = []
    for kp_title, kp_desc in key_points:
        kp_lines.append(f'      <p><strong>{kp_title}</strong> \u2192 {kp_desc}</p>')
    kp_block = "\n".join(kp_lines)
    kp_re = r'<p><strong>1\.</strong> <em>Is this your ruler\?</em> \u2192 "\u8fd9\u662f\u4f60\u7684\u5c3a\u5b50\u5417\?" \u4e00\u822c\u7591\u95ee\u53e5\uff0c\u628a <strong>be \u52a8\u8bcd \(is/are\)</strong> \u63d0\u5230\u53e5\u9996\..*?<p><strong>4\.</strong> <em>You\'re welcome\.</em> \u2192 "\u4e0d\u5ba2\u6c14" \u56fa\u5b9a\u642d\u914d\uff0c\u56de\u5e94 Thank you / Thanks\.</p>'
    h = re.sub(kp_re, kp_block, h, flags=re.DOTALL)
    
    # -- Reading title --
    h = h.replace(
        '<h3 style="font-size:15px;color:var(--accent);margin:0;">\U0001f4d6 Reading: Lost &amp; Found Notice</h3>',
        f'<h3 style="font-size:15px;color:var(--accent);margin:0;">\U0001f4d6 Reading: {reading_title}</h3>'
    )
    
    # -- Reading paragraphs --
    rp_lines = []
    for p in reading_paras:
        rp_lines.append(f'      <p class="en-text" data-speak="{p}">{p}</p>')
    rp_block = "\n".join(rp_lines)
    rp_re = r'<div id="readingEnglish">\n      <div class="notice">\n        <div class="title en-text" data-speak="Found">Found</div>[\s\S]*?</div>\n      </div>'
    h = re.sub(rp_re, f'<div id="readingEnglish">\n{rp_block}\n      </div>', h)
    
    # -- Gloss --
    gl_lines = []
    for word, ipa, pos, defn in gloss:
        gl_lines.append(f'        <span class="gloss-item wotd-say" data-speak="{word}">\U0001f4d8 {word} {ipa} {pos} {defn}</span>')
    gl_block = "\n".join(gl_lines)
    gl_re = r'<span class="gloss-item wotd-say" data-speak="schoolbag">\U0001f4d8 schoolbag /ˈskuːlbæɡ/ n\. \u4e66\u5305</span>[\s\S]*?<span class="gloss-item wotd-say" data-speak="a set of">\U0001f4d8 a set of \u4e00\u4e32 / \u4e00\u5957</span>'
    h = re.sub(gl_re, gl_block, h)
    
    # -- Vocabulary --
    vc_lines = []
    for word, ipa, pos, defn, example, trans in vocab:
        vc_lines.append(
            f'      <div class="vocab-card">\n'
            f'        <span class="headword wotd-say" data-speak="{word}">{word}</span><span class="headword-speak-indicator">\U0001f50a</span>\n'
            f'        <span class="ipa">{ipa}</span>\n'
            f'        <span class="pos">{pos}</span>\n'
            f'        <div class="definition">{defn}</div>\n'
            f'        <div class="example"><span class="wotd-say" data-speak="{example}">{example}</span><span class="trans">{trans}</span></div>\n'
            f'      </div>'
        )
    vc_block = "\n".join(vc_lines)
    vc_re = r'<div class="vocab-grid" id="vocabGrid">[\s\S]*?</div>\n\n    </div>\n  </div>\n</details>'
    h = re.sub(vc_re, f'<div class="vocab-grid" id="vocabGrid">\n{vc_block}\n    </div>\n\n    </div>\n  </div>\n</details>', h)
    
    # -- Patterns --
    pt_lines = []
    for i, (structure, desc, substitution) in enumerate(patterns, 1):
        pt_lines.append(
            f'      <div class="pattern-card">\n'
            f'        <div class="structure">{structure}</div> <button class="speak-btn" data-target="sp{i}" title="\u6717\u8bfb\u53e5\u578b">\U0001f50a</button>\n'
            f'        <div>{desc}</div>\n'
            f'        <div class="substitution"><span class="q-speak-wrap" id="sp{i}">{substitution}</span></div>\n'
            f'      </div>'
        )
    pt_block = "\n    \n".join(pt_lines)
    pt_re = r'<div class="pattern-grid">[\s\S]*?</div>\n\n    </div>\n</details>'
    h = re.sub(pt_re, f'<div class="pattern-grid">\n    \n{pt_block}\n\n    </div>\n\n    </div>\n</details>', h)
    
    # -- Grammar --
    gm_modules = []
    for gt in grammar_tables:
        gtitle = gt[0]
        table_rows = gt[1]
        gnote = gt[2] if len(gt) > 2 else ""
        gerrors = gt[3] if len(gt) > 3 else []
        
        tbl = '      <table class="grammar-table">\n'
        for ri, row in enumerate(table_rows):
            tag = "th" if ri == 0 else "td"
            tbl += '        <tr>' + "".join(f'<{tag}>{c}</{tag}>' for c in row) + '</tr>\n'
        tbl += '      </table>'
        
        err_html = ""
        if gerrors:
            err_html = '\n      <div class="chinese-error">\n        <strong>\u26a0\ufe0f \u4e2d\u5f0f\u82f1\u8bed\u7ea0\u9519\uff1a</strong><br>\n'
            for wrong, correct in gerrors:
                err_html += f'        \u274c <span class="wrong wotd-say" data-speak="{wrong}">{wrong}</span><br>\n'
                err_html += f'        \u2705 <span class="correct wotd-say" data-speak="{correct}">{correct}</span><br><br>\n'
            err_html += '      </div>'
        
        gm_modules.append(
            f'    <div class="grammar-module">\n'
            f'      <h3>{gtitle}</h3>\n'
            f'{tbl}\n'
            f'      <p style="font-size:14px;margin-top:8px;">{gnote}</p>\n'
            f'{err_html}\n'
            f'    </div>'
        )
    
    gm_block = "\n\n".join(gm_modules)
    gm_re = r'<div class="grammar-module">\n      <h3>1\u20e3 \u6307\u793a\u4ee3\u8bcd\uff1athis / that / these / those</h3>[\s\S]*?</div>\n\n  </div>\n</details>'
    h = re.sub(gm_re, f'{gm_block}\n\n  </div>\n</details>', h)
    
    # -- Exercises --
    ex_lines = []
    tier_map = {"\u57fa\u7840": '\U0001f949 \u57fa\u7840\u5173 \u00b7 \u6982\u5ff5\u8bc6\u8bb0',
                "\u63d0\u5347": '\U0001f948 \u63d0\u5347\u5173 \u00b7 \u8bed\u5883\u8fd0\u7528',
                "\u6311\u6218": '\U0001f947 \u6311\u6218\u5173 \u00b7 \u7efc\u5408\u8fd0\u7528'}
    current_tier = None
    for idx, (tier, diff, q_body, answer, explanation) in enumerate(exercises, 1):
        if current_tier != tier:
            current_tier = tier
            ex_lines.append(f'\n    <h3 style="color:var(--accent);margin:{"0" if tier == "\u57fa\u7840" else "20"}px 0 10px;">{tier_map[tier]}</h3>\n')
        ex_lines.append(
            f'    <div class="exam-q">\n'
            f'      <span class="q-tag">{tier}</span>\n'
            f'      <span class="q-diff">{diff}</span>\n'
            f'      <div class="q-body"><span class="q-speak-wrap" id="q{idx}">{q_body}</span> <button class="speak-btn" data-target="q{idx}" title="\u6717\u8bfb\u9898\u76ee">\U0001f50a</button></div>\n'
            f'      <span class="q-toggle">\U0001f4dd \u67e5\u770b\u7b54\u6848</span>\n'
            f'      <div class="q-solution"><strong>\u7b54\u6848\uff1a</strong>{answer}<br><strong>\u89e3\u6790\uff1a</strong>{explanation}</div>\n'
            f'    </div>'
        )
    ex_block = "\n".join(ex_lines)
    ex_re = r'<h3 style="color:var\(--accent\);margin:0 0 10px;">\U0001f949 \u57fa\u7840\u5173 \u00b7 \u6982\u5ff5\u8bc6\u8bb0</h3>[\s\S]*?</div>\n\n</details>'
    h = re.sub(ex_re, f'{ex_block}\n\n  </div>\n\n</details>', h)
    
    # -- Micro-writing --
    h = h.replace(
        '<p>\u5047\u8bbe\u4f60\u4e22\u5931\u4e86\u5b66\u751f\u8bc1\uff0c\u8bf7\u7528\u82f1\u6587\u5199\u4e00\u5219\u5bfb\u7269\u542f\u4e8b\u3002\u6ce8\u610f\u683c\u5f0f\uff1a\u6807\u9898 Lost\uff0c\u63cf\u8ff0\u7269\u54c1\u7279\u5f81\uff0c\u7559\u4e0b\u8054\u7cfb\u65b9\u5f0f\u3002</p>',
        f'<p>{micro_task}</p>'
    )
    
    mp_lines = []
    for p in model_paras:
        ps = p.replace("<strong>", "").replace("</strong>", "")
        mp_lines.append(f'    <p class="en"><span class="wotd-say" data-speak="{ps}">{p}</span></p>')
    mp_block = "\n".join(mp_lines)
    
    mp_re = r'<p class="en"><span class="wotd-say" data-speak="Lost:"><strong>Lost:</strong></span></p>[\s\S]*?<span class="trans">\u6211\u4e22\u5931\u4e86\u5b66\u751f\u8bc1\u3002\u5b83\u662f\u84dd\u767d\u8272\u7684\uff0c\u4e0a\u9762\u6709\u6211\u7684\u540d\u5b57"\u5f20\u4f1f"\u3002\u6211\u5fc5\u987b\u627e\u5230\u5b83\u3002\u8bf7\u81f4\u7535 139-1234-5678\u3002\u8c22\u8c22\uff01</span>'
    h = re.sub(mp_re, f'{mp_block}\n    <span class="trans">{model_trans}</span>', h)
    
    # -- Checklist --
    cl_lines = "\n".join(f'  <label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> {item}</label>' for item in checklist)
    cl_re = r'<label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> \u6211\u80fd\u5206\u6e05 this/that/these/those \u7684\u533a\u522b\uff0c\u5e76\u6b63\u786e\u4f7f\u7528</label>[\s\S]*?<label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> \u6211\u80fd\u5199\u4e00\u5219\u82f1\u6587\u5931\u7269\u62db\u9886\u542f\u4e8b</label>'
    h = re.sub(cl_re, cl_lines, h)
    
    # -- Feynman --
    h = h.replace(
        '<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>\u7528\u82f1\u8bed\u6307\u7740\u8eab\u8fb9\u7684\u7269\u54c1\uff0c\u81ea\u95ee\u81ea\u7b54\u2014\u2014"\'Is this my pen? No, it isn\'t. It\'s Tom\'s pen.\'"',
        f'<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>{feynman}'
    )
    # Try alternate pattern
    alt_feynman = '<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>\u7528\u82f1\u8bed\u6307\u7740\u8eab\u8fb9\u7684\u7269\u54c1\uff0c\u81ea\u95ee\u81ea\u7b54\u2014\u2014'
    h = h.replace(alt_feynman, f'<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>{feynman}')
    
    # -- Review schedule --
    rv_block = "\n".join(f'  <span class="review-dot">{r}</span>' for r in review)
    rv_re = r'<span class="review-dot">\U0001f535 1\u5929\u540e\uff1a\u91cd\u505a\u9519\u9898</span>\n  <span class="review-dot">\U0001f7e2 3\u5929\u540e\uff1a\u53e3\u5934\u81ea\u95ee\u81ea\u7b54\u7269\u4e3b\u4ee3\u8bcd</span>\n  <span class="review-dot">\U0001f7e1 1\u5468\u540e\uff1a\u5199\u4e00\u5219\u5b8c\u6574\u7684\u5931\u7269\u62db\u9886</span>\n  <span class="review-dot">\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60\u6240\u6709\u7269\u4e3b\u4ee3\u8bcd\u8868\u683c</span>'
    h = re.sub(rv_re, rv_block, h)
    
    # -- Next stop --
    h = h.replace(
        '<strong>\u27a1\ufe0f \u4e0b\u4e00\u5355\u5143\uff1aUnit 4 Where\'s my schoolbag?</strong><br>\n  \u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u7528 <strong>Where</strong> \u95ee\u7269\u54c1\u7684\u4f4d\u7f6e\uff0c\u4f7f\u7528\u4ecb\u8bcd <strong>in / on / under</strong> \u63cf\u8ff0\u65b9\u4f4d\u2014\u2014\u8fd9\u5728\u5931\u7269\u62db\u9886\u573a\u666f\u4e2d\u4e5f\u4f1a\u7528\u5230\uff01',
        f'<strong>\u27a1\ufe0f \u4e0b\u4e00\u5355\u5143\uff1aUnit {next_unit} {next_title}</strong><br>\n  {next_desc}'
    )
    
    # -- Sidebar active --
    h = h.replace('href="u03.html" class="active"', 'href="u03.html"')
    h = h.replace(f'href="{unit_key}.html"', f'href="{unit_key}.html" class="active"')
    
    return h


def main():
    data = load_unit_data()
    for key in sorted(data.keys()):
        u = data[key]
        html = gen_html(key, u)
        fname = f"{key}.html"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"{fname} \u2705 ({len(html)} bytes) \u2014 Unit {u['num']}: {u['title']}")
    print(f"\n\U0001f389 All {len(data)} files generated!")

if __name__ == "__main__":
    main()
