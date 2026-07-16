#!/usr/bin/env python3
"""Generate b2u10-12 unit files from b2u09.html template."""
import re, json

def load_template():
    with open("b2u09.html", encoding="utf-8") as f:
        return f.read()

def q(s):
    """Replace smart quotes with \u201c \u201d to avoid Python parsing issues"""
    return s

def gen(fname, num, title, subtitle, unit_meta, can_dos,
         scene_short, dialogue, dialogue_trans, key_points,
         reading_title, reading_sentences, gloss,
         vocab, patterns, grammar_sections,
         exercises, micro_task, model_paras, model_trans,
         checklist, feynman, review_dots, next_unit, next_desc):
    h = load_template()

    # Title
    h = h.replace(
        "\u4e03\u4e0b Unit 9 What does he look like? | \u521d\u4e2d\u82f1\u8bed\u4e03\u5e74\u7ea7",
        f"\u4e03\u4e0b Unit {num} {title} | \u521d\u4e2d\u82f1\u8bed\u4e03\u5e74\u7ea7"
    )

    # Cover
    h = h.replace('\u4e03\u4e0b \u00b7 Unit 9', f'\u4e03\u4e0b \u00b7 Unit {num}')
    h = h.replace('What does he look like?', title)
    h = h.replace(
        '\u5916\u8c8c\u63cf\u8ff0 \u00b7 \u8eab\u9ad8\u4f53\u578b \u00b7 \u53d1\u578b\u914d\u9970',
        subtitle
    )

    # Sidebar active
    h = h.replace('class="active"', 'class="active-DISABLE"')
    h = h.replace(f'href="{fname}.html"', f'href="{fname}.html" class="active"')
    h = h.replace('class="active-DISABLE"', '')

    # Meta
    h = h.replace('\U0001f4d6 \u8bdd\u9898\uff1aPhysical appearance', unit_meta[0])
    h = h.replace(
        '\U0001f4ac \u529f\u80fd\uff1aDescribe people\'s looks \u00b7 Ask "What does he look like?"',
        unit_meta[1]
    )
    h = h.replace(
        '\U0001f4da \u8bed\u6cd5\uff1ahas/have \u63cf\u8ff0\u5916\u8c8c \u00b7 be + \u5f62\u5bb9\u8bcd\u63cf\u8ff0\u6574\u4f53\u5f62\u8c61',
        unit_meta[2]
    )
    h = h.replace(
        '\U0001f4dd \u5199\u4f5c\uff1a\u63cf\u8ff0\u4e00\u4e2a\u4eba\uff08\u670b\u53cb/\u5bb6\u4eba\uff09\u7684\u5916\u8c8c',
        unit_meta[3]
    )

    # Can-do
    cb = '\n'.join(f'  <label><input type="checkbox"> {c}</label>' for c in can_dos)
    cb_re = r'<label><input type="checkbox"> I can ask "What does he/she look like\?"</label>[\s\S]*?<label><input type="checkbox"> I can write a short paragraph describing someone\'s appearance\.</label>'
    h = re.sub(cb_re, cb, h)

    # Scene
    h = h.replace(
        '\u573a\u666f\uff1aMike \u548c Sarah \u5728\u8c08\u8bba\u65b0\u6765\u7684\u540c\u5b66 David\uff0c\u76f8\u4e92\u63cf\u8ff0\u4ed6\u7684\u957f\u76f8\u3002',
        f'\u573a\u666f\uff1a{scene_short}'
    )

    # Dialogue
    dia_lines = []
    for speaker, text, trans in dialogue:
        clean = text.replace('<em>', '').replace('</em>', '')
        dia_lines.append(
            f'      <div class="dialogue-line">\n'
            f'        <span class="speaker">{speaker}:</span>\n'
            f'        <span class="en-text wotd-say" data-speak="{clean}">{text}</span>\n'
            f'      </div>'
        )
    dia_block = '\n'.join(dia_lines)
    dia_re = r'<div class="dialogue" id="dialogueText">[\s\S]*?</div>\n\n    <details style="margin-top:12px;">'
    h = re.sub(dia_re, f'<div class="dialogue" id="dialogueText">\n{dia_block}\n    </div>\n\n    <details style="margin-top:12px;">', h)

    # Translation
    trans_block = '\n'.join(f'        <p>{t}</p>' for t in dialogue_trans)
    trans_re = r'<p>Sarah: Mike\uff0c\u4f60\u8ba4\u8bc6\u65b0\u6765\u7684\u540c\u5b66 David \u5417\uff1f</p>[\s\S]*?<p>Mike: \u77e5\u9053\u4e86\u3002\u6211\u5f85\u513f\u53ef\u53bb\u8ddf\u4ed6\u6253\u4e2a\u62db\u547c\u3002</p>'
    h = re.sub(trans_re, trans_block, h)

    # Key points
    kp_lines = []
    for title_kp, desc in key_points:
        kp_lines.append(f'      <p><strong>{title_kp}</strong> {desc}</p>')
    kp_block = '\n'.join(kp_lines)
    kp_re = r'<p><strong>1\.</strong> <em>What does he look like\?</em> \u2192 "\u4ed6\u957f\u4ec0\u4e48\u6837\?" \u56fa\u5b9a\u53e5\u578b\uff0c\u8be2\u95ee\u5916\u8c8c\..*?<p><strong>4\.</strong> <em>Does he wear glasses\?</em> \u2192 \u7528 <strong>wear</strong> \u8868\u793a"\u7a7f\u6234\uff08\u773c\u955c\u3001\u8863\u670d\u7b49\uff09"\.</p>'
    h = re.sub(kp_re, kp_block, h, flags=re.DOTALL)

    # Reading
    rp_lines = []
    for p in reading_sentences:
        rp_lines.append(f'      <p class="en-text" data-speak="{p}">{p}</p>')
    rp_block = '\n'.join(rp_lines)
    rp_re = r'<div id="readingEnglish">\n      <p class="en-text" data-speak="My best friend is Li Ming\. He is of medium height but a little heavy\.">[\s\S]*?</div>'
    h = re.sub(rp_re, f'<div id="readingEnglish">\n{rp_block}\n      </div>', h)

    h = h.replace(
        '<h3 style="font-size:15px;color:var(--accent);margin:0;">\U0001f4d6 Reading: My Best Friend</h3>',
        f'<h3 style="font-size:15px;color:var(--accent);margin:0;">\U0001f4d6 Reading: {reading_title}</h3>'
    )

    # Gloss
    gl_lines = []
    for word, ipa, defn in gloss:
        gl_lines.append(f'        <span class="gloss-item wotd-say" data-speak="{word}">\U0001f4d8 {word} {ipa} {defn}</span>')
    gl_block = '\n'.join(gl_lines)
    gl_re = r'<span class="gloss-item wotd-say" data-speak="medium">[\s\S]*?</span>'
    h = re.sub(gl_re, gl_block, h)

    # Vocab
    vc_lines = []
    for word, ipa, pos, defn, example, ex_html, trans in vocab:
        vc_lines.append(
            f'      <div class="vocab-card">\n'
            f'        <span class="headword wotd-say" data-speak="{word}">{word}</span><span class="headword-speak-indicator">\U0001f50a</span>\n'
            f'        <span class="ipa">{ipa}</span>\n'
            f'        <span class="pos">{pos}</span>\n'
            f'        <div class="definition">{defn}</div>\n'
            f'        <div class="example"><span class="wotd-say" data-speak="{example}">{ex_html}</span><span class="trans">{trans}</span></div>\n'
            f'      </div>'
        )
    vc_block = '\n'.join(vc_lines)
    vc_re = r'<div class="vocab-grid" id="vocabGrid">[\s\S]*?</div>\n\n    </div>\n  </div>\n</details>'
    h = re.sub(vc_re, f'<div class="vocab-grid" id="vocabGrid">\n{vc_block}\n    </div>\n\n    </div>\n  </div>\n</details>', h)

    # Patterns
    pt_lines = []
    for i, (struct, desc, sub) in enumerate(patterns, 1):
        pt_lines.append(
            f'      <div class="pattern-card">\n'
            f'        <div class="structure">{struct}</div> <button class="speak-btn" data-target="sp{i}" title="\u6717\u8bfb\u53e5\u578b">\U0001f50a</button>\n'
            f'        <div>{desc}</div>\n'
            f'        <div class="substitution"><span class="q-speak-wrap" id="sp{i}">{sub}</span></div>\n'
            f'      </div>'
        )
    pt_block = '\n    \n'.join(pt_lines)
    pt_re = r'<div class="pattern-grid">[\s\S]*?</div>\n\n    </div>\n</details>'
    h = re.sub(pt_re, f'<div class="pattern-grid">\n    \n{pt_block}\n\n    </div>\n\n    </div>\n</details>', h)

    # Grammar
    gm_mods = []
    for gtitle, gcontent in grammar_sections:
        gm_mods.append(
            f'    <div class="grammar-module">\n'
            f'      <h3>{gtitle}</h3>\n'
            f'{gcontent}\n'
            f'    </div>'
        )
    gm_block = '\n\n'.join(gm_mods)
    gm_re = r'<div class="grammar-module">\n      <h3>1\u20e3 be \u63cf\u8ff0 vs\. have \u63cf\u8ff0</h3>[\s\S]*?</div>\n\n  </div>\n</details>'
    h = re.sub(gm_re, f'{gm_block}\n\n  </div>\n</details>', h)

    # Exercises
    ex_lines = []
    for idx, (tier, diff, qid, qbody, answer, expl) in enumerate(exercises, 1):
        if idx == 1 or tier != exercises[idx-2][0] if idx > 1 else True:
            tier_map = {
                '\u57fa\u7840': f'\n    <h3 style="color:var(--accent);margin:{"0" if tier == "\u57fa\u7840" else "20"}px 0 10px;">\U0001f949 \u57fa\u7840\u5173 \u00b7 \u6982\u5ff5\u8bc6\u8bb0</h3>\n',
                '\u63d0\u5347': f'\n    <h3 style="color:var(--accent);margin:20px 0 10px;">\U0001f948 \u63d0\u5347\u5173 \u00b7 \u8bed\u5883\u8fd0\u7528</h3>\n',
                '\u6311\u6218': f'\n    <h3 style="color:var(--accent);margin:20px 0 10px;">\U0001f947 \u6311\u6218\u5173 \u00b7 \u7efc\u5408\u8fd0\u7528</h3>\n',
            }
            ex_lines.append(tier_map[tier])
        ex_lines.append(
            f'    <div class="exam-q">\n'
            f'      <span class="q-tag">{tier}</span>\n'
            f'      <span class="q-diff">{diff}</span>\n'
            f'      <div class="q-body"><span class="q-speak-wrap" id="q{qid}">{qbody}</span> <button class="speak-btn" data-target="q{qid}" title="\u6717\u8bfb\u9898\u76ee">\U0001f50a</button></div>\n'
            f'      <span class="q-toggle">\U0001f4dd \u67e5\u770b\u7b54\u6848</span>\n'
            f'      <div class="q-solution"><strong>\u7b54\u6848\uff1a</strong>{answer}<br><strong>\u89e3\u6790\uff1a</strong>{expl}</div>\n'
            f'    </div>'
        )
    ex_block = '\n'.join(ex_lines)
    ex_re = r'<h3 style="color:var\(--accent\);margin:0px 0 10px;">\U0001f949 \u57fa\u7840\u5173 \u00b7 \u6982\u5ff5\u8bc6\u8bb0</h3>[\s\S]*?</div>\n\n</details>'
    h = re.sub(ex_re, f'{ex_block}\n\n  </div>\n\n</details>', h)

    # Micro-writing task
    h = h.replace(
        '\u7528\u82f1\u8bed\u5199\u4e00\u6bb5\u5173\u4e8e\u4f60\u670b\u53cb\u6216\u5bb6\u4eba\u5916\u8c8c\u7684\u63cf\u8ff0\u3002\u6ce8\u610f\u5148\u7528 There be \u63cf\u8ff0\u6574\u4f53\uff0c\u518d\u7528 has \u63cf\u8ff0\u7ec6\u8282\u3002',
        micro_task
    )

    # Writing model
    mp_lines = []
    for p in model_paras:
        mp_lines.append(f'    <p class="en"><span class="wotd-say" data-speak="{p}">{p}</span></p>')
    mp_block = '\n'.join(mp_lines)
    mp_re = r'<p class="en"><span class="wotd-say" data-speak="I want to tell you about my best friend, Wang Fang\.">[\s\S]*?<span class="trans">[\s\S]*?/span>'
    # Use a more specific replacement
    writing_template = '''    <p class="en"><span class="wotd-say" data-speak="I want to tell you about my best friend, Wang Fang.">I want to tell you about my best friend, Wang Fang.</span></p>
    <p class="en"><span class="wotd-say" data-speak="She is of medium height and a little thin. She has long straight black hair.">She is of medium height and a little thin. She has long straight black hair.</span></p>
    <p class="en"><span class="wotd-say" data-speak="She has big bright eyes and a small mouth. She always wears a nice smile.">She has big bright eyes and a small mouth. She always wears a nice smile.</span></p>
    <p class="en"><span class="wotd-say" data-speak="She likes to wear a white T-shirt and blue jeans. She looks very pretty.">She likes to wear a white T-shirt and blue jeans. She looks very pretty.</span></p>
    <p class="en"><span class="wotd-say" data-speak="Everyone says she is kind and friendly. I'm lucky to have her as my friend.">Everyone says she is kind and friendly. I'm lucky to have her as my friend.</span></p>'''
    h = h.replace(writing_template, mp_block)

    # Model translation
    h = h.replace(
        '\u6211\u60f3\u5411\u4f60\u4ecb\u7ecd\u6211\u6700\u597d\u7684\u670b\u53cb\u738b\u82b3\u3002\u5979\u4e2d\u7b49\u8eab\u9ad8\uff0c\u6709\u70b9\u7626\u3002\u5979\u6709\u4e00\u5934\u9ed1\u8272\u7684\u957f\u76f4\u53d1\u3002\u5979\u6709\u4e00\u53cc\u660e\u4eae\u7684\u5927\u773c\u775b\u548c\u4e00\u5f20\u5c0f\u5634\u3002\u5979\u603b\u662f\u5e26\u7740\u751c\u751c\u7684\u5fae\u7b11\u3002\u5979\u559c\u6b22\u7a7f\u767d T \u6064\u548c\u84dd\u8272\u725b\u4ed4\u88e4\u3002\u5979\u770b\u8d77\u6765\u975e\u5e38\u6f02\u4eae\u3002\u6bcf\u4e2a\u4eba\u90fd\u8bf4\u5979\u5f88\u5584\u826f\u53cb\u597d\u3002\u6211\u5f88\u5e78\u8fd0\u6709\u5979\u505a\u6211\u7684\u670b\u53cb\u3002',
        model_trans
    )

    # Checklist
    cl_lines = '\n'.join(f'  <label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> {c}</label>' for c in checklist)
    cl_re = r'<label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> \u6211\u80fd\u7528 What does he/she look like\? \u8be2\u95ee\u5916\u8c8c</label>[\s\S]*?<label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> \u6211\u80fd\u5199\u4e00\u6bb5\u5b8c\u6574\u7684\u5916\u8c8c\u63cf\u8ff0</label>'
    h = re.sub(cl_re, cl_lines, h)

    # Feynman
    h = h.replace(
        '<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>\u60f3\u8c61\u4e00\u4e2a\u4f60\u559c\u6b22\u7684\u7535\u5f71\u89d2\u8272\u6216\u660e\u661f\uff0c\u7528\u82f1\u8bed\u63cf\u8ff0\u5979\u7684\u5916\u8c8c\u3002\u8ba9\u540c\u5b66\u6839\u636e\u4f60\u7684\u63cf\u8ff0\u731c\u51fa\u662f\u8c01\u3002"He is tall and strong\. He has short black hair and a round face\. He always wears a black suit\. Who is he\?"',
        f'<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>{feynman}'
    )

    # Review
    rv_block = '\n    '.join(f'<span class="review-dot">{r}</span>' for r in review_dots)
    rv_re = r'<span class="review-dot">\U0001f535 1\u5929\u540e\uff1a\u7528\u82f1\u8bed\u63cf\u8ff0\u4f60\u7684\u82f1\u8bed\u8001\u5e08\u7684\u5916\u8c8c</span>\n    <span class="review-dot">\U0001f7e2 3\u5929\u540e\uff1a\u5199\u51fa\u4f60\u548c\u540c\u684c\u7684\u5916\u8c8c\u5bf9\u6bd4</span>\n    <span class="review-dot">\U0001f7e1 1\u5468\u540e\uff1a\u719f\u8bb0\u5934\u53d1\u63cf\u8ff0\u8bcd\uff08\u957f\u77ed/\u76f4\u5377/\u989c\u8272\uff09\u7ec4\u5408</span>\n    <span class="review-dot">\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60 has/have \u548c be \u5728\u5916\u8c8c\u63cf\u8ff0\u4e2d\u7684\u7528\u6cd5</span>'
    h = re.sub(rv_re, rv_block, h)

    # Next
    h = h.replace(
        '<strong>\u27a1\ufe0f \u4e0b\u4e00\u5355\u5143\uff1aUnit 10 I\'d like some noodles.</strong>',
        f'<strong>\u27a1\ufe0f \u4e0b\u4e00\u5355\u5143\uff1a{next_unit}</strong>'
    )
    h = h.replace(
        '\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u5982\u4f55\u7528\u82f1\u8bed\u70b9\u9910\u2014\u2014would like \u7684\u7528\u6cd5\u3001\u98df\u7269\u8bcd\u6c47\u548c\u9910\u5385\u5bf9\u8bdd\u3002',
        next_desc
    )

    with open(f"{fname}.html", "w", encoding="utf-8") as f:
        f.write(h)
    print(f"{fname}.html written ({len(h)} bytes)")

def run():
    print("Module loaded - use gen() function directly")

if __name__ == "__main__":
    gen("b2u10", 10, "I'd like some noodles.",
        "\u70b9\u9910\u7528\u9910 \u00b7 \u98df\u7269\u79cd\u7c7b \u00b7 would like \u7528\u6cd5",
        [
            "\U0001f4d6 \u8bdd\u9898\uff1aFood &amp; Ordering",
            "\U0001f4ac \u529f\u80fd\uff1aOrder food \u00b7 Express preferences \u00b7 Ask about food",
            "\U0001f4da \u8bed\u6cd5\uff1awould like (I'd like) \u00b7 some/any \u00b7 \u53ef\u6570/\u4e0d\u53ef\u6570\u540d\u8bcd",
            "\U0001f4dd \u5199\u4f5c\uff1a\u9910\u5385\u70b9\u9910\u5bf9\u8bdd\u6216\u83dc\u5355\u4ecb\u7ecd"
        ],
        [
            'I can say "I\'d like..." to order food politely.',
            'I can ask "What kind of noodles would you like?"',
            "I can use some/any correctly with food nouns.",
            "I can write a short restaurant ordering dialogue."
        ],
        "\u5728\u4e00\u5bb6\u9762\u9986\u91cc\uff0c\u670d\u52a1\u5458\u548c\u987e\u5ba2\u4e4b\u95f4\u7684\u70b9\u9910\u5bf9\u8bdd\u3002",
        [
            ["Waiter", "Good evening! What would you like?", "\u670d\u52a1\u5458: \u665a\u4e0a\u597d\uff01\u60a8\u60f3\u5403\u4ec0\u4e48\uff1f"],
            ["Tom", "Good evening. I'd like some noodles, please.", "Tom: \u665a\u4e0a\u597d\u3002\u6211\u60f3\u8981\u4e00\u4e9b\u9762\u6761\u3002"],
            ["Waiter", "What kind of noodles would you like?", "\u670d\u52a1\u5458: \u60a8\u60f3\u8981\u4ec0\u4e48\u6837\u7684\u9762\u6761\uff1f"],
            ["Tom", "I'd like beef noodles with some vegetables.", "Tom: \u6211\u60f3\u8981\u725b\u8089\u9762\uff0c\u52a0\u4e00\u4e9b\u852c\u83dc\u3002"],
            ["Waiter", "What size would you like? Large, medium or small?", "\u670d\u52a1\u5458: \u60a8\u8981\u5927\u4efd\u3001\u4e2d\u4efd\u8fd8\u662f\u5c0f\u4efd\u7684\uff1f"],
            ["Tom", "A large bowl, please. I'm very hungry.", "Tom: \u5927\u7897\u7684\uff0c\u8c22\u8c22\u3002\u6211\u5f88\u997f\u3002"],
            ["Waiter", "OK. A large bowl of beef noodles. Would you like a drink?", "\u670d\u52a1\u5458: \u597d\u7684\u3002\u4e00\u5927\u7897\u725b\u8089\u9762\u3002\u60a8\u60f3\u559d\u4ec0\u4e48\u5417\uff1f"],
            ["Tom", "Yes, I'd like a glass of orange juice, please.", "Tom: \u597d\uff0c\u6211\u8981\u4e00\u676f\u6a59\u6c41\u3002"]
        ],
        [
            "\u670d\u52a1\u5458: \u665a\u4e0a\u597d\uff01\u60a8\u60f3\u5403\u70b9\u4ec0\u4e48\uff1f",
            "Tom: \u665a\u4e0a\u597d\u3002\u6211\u60f3\u8981\u4e00\u4e9b\u9762\u6761\u3002",
            "\u670d\u52a1\u5458: \u60a8\u60f3\u8981\u4ec0\u4e48\u6837\u7684\u9762\u6761\uff1f",
            "Tom: \u6211\u60f3\u8981\u725b\u8089\u9762\uff0c\u52a0\u4e00\u4e9b\u852c\u83dc\u3002",
            "\u670d\u52a1\u5458: \u60a8\u8981\u5927\u4efd\u3001\u4e2d\u4efd\u8fd8\u662f\u5c0f\u4efd\u7684\uff1f",
            "Tom: \u5927\u7897\u7684\uff0c\u8c22\u8c22\u3002\u6211\u5f88\u997f\u3002",
            "\u670d\u52a1\u5458: \u597d\u7684\u3002\u4e00\u5927\u7897\u725b\u8089\u9762\u3002\u60a8\u60f3\u559d\u4ec0\u4e48\u5417\uff1f",
            "Tom: \u597d\uff0c\u6211\u8981\u4e00\u676f\u6a59\u6c41\u3002"
        ],
        [
            ("1. ", "I'd like = I would like \u2192 \u201c\u6211\u60f3\u8981\u201d\uff0c\u6bd4 I want \u66f4\u793c\u8c8c\u3002Would you like...? \u63d0\u95ee\u5bf9\u65b9\u60f3\u8981\u4ec0\u4e48\u3002"),
            ("2. ", "What kind of \u2192 \u201c\u4ec0\u4e48\u79cd\u7c7b\u7684\u201d\uff0cWhat size \u2192 \u201c\u4ec0\u4e48\u5927\u5c0f\u201d\u3002"),
            ("3. ", "A bowl of / a glass of \u2192 \u91cf\u8bcd\u7528\u6cd5\u3002\u4e0d\u53ef\u6570\u540d\u8bcd\u9700\u8981\u7528\u91cf\u8bcd\u8868\u8fbe\u6570\u91cf\u3002"),
            ("4. ", "Some \u7528\u4e8e\u80af\u5b9a\u53e5\uff0cany \u7528\u4e8e\u5426\u5b9a\u53e5\u548c\u7591\u95ee\u53e5\u3002\u4f46\u5728\u671f\u671b\u80af\u5b9a\u56de\u7b54\u65f6\u7528 some\u3002")
        ],
        "Noodle House Menu",
        [
            "Welcome to Noodle House! We have many kinds of delicious noodles.",
            "Would you like beef noodles for 12 yuan? Or you can try mutton noodles for 15 yuan.",
            "We also have chicken noodles with cabbage and potato noodles with tomatoes.",
            "You can add eggs or tofu for extra 2 yuan.",
            "If you're thirsty, we have green tea and orange juice. Come and enjoy!"
        ],
        [
            ["delicious", "/d\u026a\u02c8l\u026a\u0283\u0259s/", "adj. \u7f8e\u5473\u7684"],
            ["mutton", "/\u02c8m\u028cntn/", "n. \u7f8a\u8089"],
            ["cabbage", "/\u02c8k\u00e6b\u026ad\u0292/", "n. \u5377\u5fc3\u83dc"],
            ["tofu", "/\u02c8to\u028afu\u02d0/", "n. \u8c46\u8150"],
            ["thirsty", "/\u02c8\u03b8\u025c\u02d0rsti/", "adj. \u53e3\u6e34\u7684"]
        ],
        [
            ("noodle", "/\u02c8nu\u02d0dl/", "n.", "\u9762\u6761\uff08\u5e38\u7528\u590d\u6570 noodles\uff09", "I'd like a large bowl of beef noodles.", "I'd like a large bowl of beef <strong>noodles</strong>.", "\u6211\u60f3\u8981\u4e00\u5927\u7897\u725b\u8089\u9762\u3002"),
            ("beef", "/bi\u02d0f/", "n.", "\u725b\u8089", "Would you like some beef? It's very tender.", "Would you like some <strong>beef</strong>? It's very tender.", "\u4f60\u60f3\u6765\u70b9\u725b\u8089\u5417\uff1f\u975e\u5e38\u5ae9\u3002"),
            ("mutton", "/\u02c8m\u028cntn/", "n.", "\u7f8a\u8089", "I like mutton noodles with some carrots.", "I like <strong>mutton</strong> noodles with some carrots.", "\u6211\u559c\u6b22\u80e1\u841d\u535c\u7f8a\u8089\u9762\u3002"),
            ("cabbage", "/\u02c8k\u00e6b\u026ad\u0292/", "n.", "\u5377\u5fc3\u83dc\uff1b\u6d0b\u767d\u83dc", "There is some cabbage in the soup.", "There is some <strong>cabbage</strong> in the soup.", "\u6c64\u91cc\u6709\u4e00\u4e9b\u5377\u5fc3\u83dc\u3002"),
            ("potato", "/p\u0259\u02c8te\u026ato\u028a/", "n.", "\u571f\u8c46\uff1b\u9a6c\u94c3\u85af", "I'd like some potato noodles.", "I'd like some <strong>potato</strong> noodles.", "\u6211\u60f3\u8981\u571f\u8c46\u9762\u3002"),
            ("special", "/\u02c8spe\u0283l/", "n.", "\u7279\u8272\u83dc\uff1b\u7279\u4ef7", "Today's special is chicken noodles.", "Today's <strong>special</strong> is chicken noodles.", "\u4eca\u65e5\u7279\u4ef7\u662f\u9e21\u8089\u9762\u3002"),
            ("size", "/sa\u026az/", "n.", "\u5927\u5c0f\uff1b\u5c3a\u7801", "What size would you like? Large, medium or small?", "What <strong>size</strong> would you like? Large, medium or small?", "\u60a8\u8981\u5927\u4efd\u3001\u4e2d\u4efd\u8fd8\u662f\u5c0f\u4efd\uff1f"),
            ("bowl", "/bo\u028al/", "n.", "\u7897", "I can eat two bowls of noodles.", "I can eat two <strong>bowls</strong> of noodles.", "\u6211\u53ef\u4ee5\u5403\u4e24\u7897\u9762\u3002"),
            ("juice", "/d\u0292u\u02d0s/", "n.", "\u679c\u6c41\uff1b\u996e\u6599", "I'd like a glass of apple juice.", "I'd like a glass of apple <strong>juice</strong>.", "\u6211\u60f3\u8981\u4e00\u676f\u82f9\u679c\u6c41\u3002"),
            ("would", "/w\u028ad/", "modal v.", "\u60f3\u8981\uff08\u7528\u4e8e\u59a5\u5a49\u63d0\u8bae\uff09", "Would you like some tea?", "Would you like some tea?", "\u4f60\u60f3\u559d\u70b9\u8336\u5417\uff1f")
        ],
        [
            (q("I'd like + \u98df\u7269 / Would you like...?"), q("\u70b9\u9910\u65f6\u6700\u5e38\u7528\u7684\u53e5\u578b\u3002"),
             q('''\u2705 <strong>I'd like</strong> <span class="slot">some noodles</span>, please.<br>
          \u2705 <strong>Would you like</strong> <span class="slot">some tea</span>?<br>
          \u27a1 \u80af\u5b9a\u56de\u7b54\uff1a<strong>Yes, please.</strong> / \u5426\u5b9a\uff1a<strong>No, thanks.</strong>''')),
            (q("What kind of ... would you like?"), q("\u8be2\u95ee\u5177\u4f53\u79cd\u7c7b\u3002"),
             q('''\u2705 <strong>What kind of</strong> <span class="slot">noodles</span> would you like?<br>
          \u27a1 <span class="slot">Beef noodles</span>, please.<br>
          \u2705 <strong>What kind of</strong> <span class="slot">drink</span> would you like?''')),
            (q("What size / How many / How much"), q("\u8be2\u95ee\u6570\u91cf\u548c\u4efd\u91cf\u3002"),
             q('''\u2705 <strong>What size</strong> would you like? <span class="slot">Large / Medium / Small</span>.<br>
          \u2705 <strong>How many</strong> <span class="slot">bowls</span> would you like? (\u53ef\u6570)<br>
          \u2705 <strong>How much</strong> <span class="slot">beef</span> would you like? (\u4e0d\u53ef\u6570)''')),
            (q("\u91cf\u8bcd\uff1aa bowl of / a glass of / a piece of"), q("\u4e0d\u53ef\u6570\u540d\u8bcd\u7528\u91cf\u8bcd\u6765\u8868\u8fbe\u6570\u91cf\u3002"),
             q('''\u2705 <strong>A bowl of</strong> <span class="slot">noodles</span><br>
          \u2705 <strong>A glass of</strong> <span class="slot">milk / juice / water</span><br>
          \u2705 <strong>A piece of</strong> <span class="slot">bread / cake / meat</span><br>
          \u27a1 \u590d\u6570\uff1atwo <strong>bowls of</strong> rice'''))
        ],
        [
            (q("1\u20e3 would like (I'd like) \u7684\u7528\u6cd5"),
             q('''<p><strong>would like</strong> = want \u7684\u793c\u8c8c\u5f62\u5f0f\uff0c\u540e\u9762\u53ef\u8ddf\uff1a</p>
      <table class="grammar-table">
        <tr><th>\u7ed3\u6784</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>would like + \u540d\u8bcd</td><td><span class="wotd-say" data-speak="I would like some noodles.">I <strong>would like</strong> some noodles.</span></td></tr>
        <tr><td>would like + to do</td><td><span class="wotd-say" data-speak="I would like to eat some bread.">I <strong>would like to eat</strong> some bread.</span></td></tr>
        <tr><td>Would you like...? \u63d0\u95ee</td><td><span class="wotd-say" data-speak="Would you like a glass of water?">Would you like a glass of water?</span></td></tr>
        <tr><td>\u80af\u5b9a\u56de\u7b54</td><td><span class="wotd-say" data-speak="Yes, please.">Yes, please.</span></td></tr>
        <tr><td>\u5426\u5b9a\u56de\u7b54</td><td><span class="wotd-say" data-speak="No, thanks.">No, thanks.</span></td></tr>
      </table>''')),
            (q("2\u20e3 some / any \u7684\u533a\u522b"),
             q('''<table class="grammar-table">
        <tr><th></th><th><strong>some</strong></th><th><strong>any</strong></th></tr>
        <tr><td>\u80af\u5b9a\u53e5</td><td>\u2705 I have <span class="wotd-say" data-speak="some">some</span> apples.</td><td>\u274c</td></tr>
        <tr><td>\u5426\u5b9a\u53e5</td><td>\u274c</td><td>\u2705 I don't have <span class="wotd-say" data-speak="any">any</span> apples.</td></tr>
        <tr><td>\u7591\u95ee\u53e5</td><td>\u2705 Would you like <span class="wotd-say" data-speak="some">some</span> tea? (\u671f\u671b\u80af\u5b9a\u56de\u7b54)</td><td>\u2705 Do you have <span class="wotd-say" data-speak="any">any</span> brothers?</td></tr>
      </table>
      <div class="chinese-error">
        <strong>\u26a0\ufe0f \u4e2d\u5f0f\u82f1\u8bed\u7ea0\u9519\uff1a</strong><br>
        \u274c <span class="wrong wotd-say" data-speak="I would like eat noodles.">I would like eat noodles.</span> (\u7f3a\u5c11 to)<br>
        \u2705 <span class="correct wotd-say" data-speak="I would like to eat noodles.">I would like to eat noodles.</span><br><br>
        \u274c <span class="wrong wotd-say" data-speak="I don't have some money.">I don't have some money.</span> (\u5426\u5b9a\u53e5\u7528 any)<br>
        \u2705 <span class="correct wotd-say" data-speak="I don't have any money.">I don't have any money.</span>
      </div>''')),
            (q("3\u20e3 \u53ef\u6570\u540d\u8bcd vs \u4e0d\u53ef\u6570\u540d\u8bcd"),
             q('''<table class="grammar-table">
        <tr><th></th><th>\u53ef\u6570\u540d\u8bcd</th><th>\u4e0d\u53ef\u6570\u540d\u8bcd</th></tr>
        <tr><td>\u7279\u70b9</td><td>\u53ef\u4ee5\u7528\u6570\u5b57\u6570</td><td>\u65e0\u6cd5\u7528\u6570\u5b57\u6570</td></tr>
        <tr><td>\u793a\u4f8b</td><td>noodle, egg, apple</td><td>beef, water, rice</td></tr>
        <tr><td>\u4fee\u9970\u8bcd</td><td>many / a few / some</td><td>much / a little / some</td></tr>
        <tr><td>\u8be2\u91cf</td><td>How many eggs?</td><td>How much beef?</td></tr>
      </table>''')),
        ],
        [
            ("\u57fa\u7840", "\u2605\u2606\u2606", 1, 'I\'d like some noodles, please. (I\'d like / I like / I want)', "I'd like", "I'd like \u662f I would like \u7684\u7f29\u5199\uff0c\u8868\u793a\u201c\u6211\u60f3\u8981\u201d\uff0c\u793c\u8c8c\u8868\u8fbe\u3002"),
            ("\u57fa\u7840", "\u2605\u2606\u2606", 2, '____ size would you like? \u2014 Large, please. (What / How / Which)', "What", "What size \u8be2\u95ee\u5927\u5c0f\u3002"),
            ("\u57fa\u7840", "\u2605\u2606\u2606", 3, 'Would you like ____ (some / any) tea?', "some", "\u63d0\u51fa\u5efa\u8bae\u5e0c\u671b\u5f97\u5230\u80af\u5b9a\u56de\u7b54\u65f6\u7528 some\u3002"),
            ("\u63d0\u5347", "\u2605\u2605\u2606", 4, '\u6539\u9519\uff1aI would like eat a bowl of noodles.', "I would like to eat a bowl of noodles.", "would like \u540e\u8ddf to do\uff0c\u4e0d\u80fd\u76f4\u63a5\u8ddf\u52a8\u8bcd\u539f\u5f62\u3002"),
            ("\u63d0\u5347", "\u2605\u2605\u2606", 5, '\u8fde\u8bcd\u6210\u53e5\uff1akind / what / of / would / noodles / you / like / ?', "What kind of noodles would you like?", "\u7279\u6b8a\u7591\u95ee\u53e5\uff1aWhat kind of + \u540d\u8bcd + would + \u4e3b\u8bed + like?"),
            ("\u63d0\u5347", "\u2605\u2605\u2606", 6, '\u7528 How much \u6539\u5199\uff1aTell me the price of the beef.', 'How much is the beef?', "How much \u8be2\u95ee\u4e0d\u53ef\u6570\u540d\u8bcd\u7684\u4ef7\u683c\u3002"),
            ("\u6311\u6218", "\u2605\u2605\u2605", 7, '\u6c49\u8bd1\u82f1\uff1a\u4f60\u60f3\u8981\u4ec0\u4e48\u79cd\u7c7b\u7684\u9762\u6761\uff1f\u6211\u60f3\u8981\u725b\u8089\u9762\uff0c\u4e2d\u7897\u7684\u3002', "What kind of noodles would you like? I'd like a medium bowl of beef noodles.", "\u70b9\u9910\u4e09\u90e8\u66f2\uff1a\u8be2\u95ee\u79cd\u7c7b\u2192\u8be2\u95ee\u5927\u5c0f\u2192\u786e\u5b9a\u4e0b\u5355\u3002"),
            ("\u6311\u6218", "\u2605\u2605\u2605", 8, '\u8865\u5168\u5bf9\u8bdd\uff1a<br>A: Welcome! ____ can I do ____ you?<br>B: I\'d ____ some dumplings, please.<br>A: What ____ of dumplings?<br>B: Pork and cabbage, please.', "What; for; like; kind", "\u9910\u5385\u5e38\u7528\u8bed\uff1aWhat can I do for you? / I'd like... / What kind of?")
        ],
        "\u7528 would like \u53e5\u578b\u548c\u91cf\u8bcd\u5199\u4e00\u6bb5\u5728\u9910\u5385\u70b9\u9910\u7684\u5bf9\u8bdd\u3002\u81f3\u5c116\u8f6e\u5bf9\u8bdd\uff0c\u5305\u62ec\u95ee\u5019\u3001\u8be2\u95ee\u79cd\u7c7b\u3001\u8be2\u95ee\u5927\u5c0f\u3001\u70b9\u996e\u6599\u7b49\u3002",
        [
            "Waiter: Welcome to Happy Noodle! What would you like?",
            "Customer: I'd like a bowl of noodles, please.",
            "Waiter: What kind of noodles would you like?",
            "Customer: I'd like chicken noodles with some vegetables.",
            "Waiter: What size would you like?",
            "Customer: A small bowl, please. And I'd like a glass of milk, too.",
            "Waiter: OK. A small bowl of chicken noodles and a glass of milk. Anything else?",
            "Customer: No, thanks. That's all."
        ],
        "\u670d\u52a1\u5458\uff1a\u6b22\u8fce\u5149\u4e34\u5feb\u4e50\u9762\u9986\uff01\u60a8\u60f3\u5403\u70b9\u4ec0\u4e48\uff1f\u987e\u5ba2\uff1a\u6211\u60f3\u8981\u4e00\u7897\u9762\u3002\u670d\u52a1\u5458\uff1a\u60a8\u60f3\u8981\u4ec0\u4e48\u6837\u7684\u9762\uff1f\u987e\u5ba2\uff1a\u6211\u60f3\u8981\u9e21\u8089\u9762\u52a0\u852c\u83dc\u3002\u670d\u52a1\u5458\uff1a\u60f3\u8981\u4ec0\u4e48\u5c3a\u5bf8\uff1f\u987e\u5ba2\uff1a\u5c0f\u7897\u7684\u3002\u518d\u8981\u4e00\u676f\u725b\u5976\u3002\u670d\u52a1\u5458\uff1a\u597d\u7684\u3002\u4e00\u5c0f\u7897\u9e21\u8089\u9762\u548c\u4e00\u676f\u725b\u5976\u3002\u8fd8\u8981\u522b\u7684\u5417\uff1f\u987e\u5ba2\uff1a\u4e0d\u4e86\uff0c\u8c22\u8c22\u3002\u5c31\u8fd9\u4e9b\u3002",
        [
            '\u6211\u80fd\u7528 I\'d like... \u793c\u8c8c\u5730\u70b9\u9910',
            '\u6211\u80fd\u7528 What kind of...? \u8be2\u95ee\u79cd\u7c7b',
            '\u6211\u80fd\u533a\u5206 some \u548c any \u7684\u7528\u6cd5',
            '\u6211\u80fd\u533a\u5206\u53ef\u6570\u540d\u8bcd\u548c\u4e0d\u53ef\u6570\u540d\u8bcd',
            '\u6211\u80fd\u5199\u4e00\u6bb5\u9910\u5385\u70b9\u9910\u5bf9\u8bdd'
        ],
        "\u5047\u88c5\u4f60\u5728\u4e00\u5bb6\u9762\u9986\u5f53\u670d\u52a1\u5458\uff0c\u7528\u82f1\u8bed\u5e2e\u987e\u5ba2\u70b9\u9910\u3002\u7ec3\u4e60\uff1a\u201cWhat would you like? What kind of noodles would you like? What size? Would you like a drink?\u201d \u76f4\u5230\u80fd\u6d41\u5229\u5bf9\u8bdd\u3002",
        [
            "\U0001f535 1\u5929\u540e\uff1a\u590d\u4e60 would like \u53e5\u578b\u548c\u70b9\u9910\u7528\u8bed",
            "\U0001f7e2 3\u5929\u540e\uff1a\u9ed8\u5199\u53ef\u6570\u548c\u4e0d\u53ef\u6570\u540d\u8bcd\u54045\u4e2a",
            "\U0001f7e1 1\u5468\u540e\uff1a\u80cc\u8bf5\u5b8c\u6574\u7684\u70b9\u9910\u5bf9\u8bdd",
            "\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60 some/any \u548c\u91cf\u8bcd\u7684\u7528\u6cd5"
        ],
        "\u4e0b\u4e00\u5355\u5143\uff1aUnit 11 How was your school trip?",
        "\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u4e00\u822c\u8fc7\u53bb\u65f6\u2014\u2014\u7528 was/were \u548c\u52a8\u8bcd\u8fc7\u53bb\u5f0f\u63cf\u8ff0\u8fc7\u53bb\u7684\u7ecf\u5386\u3002"
    )
