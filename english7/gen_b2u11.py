#!/usr/bin/env python3
"""Generate b2u11.html."""
import re

def q(s):
    return s

TEMPLATE = open("b2u09.html", encoding="utf-8").read()

def gen(fname, num, title, subtitle, unit_meta, can_dos,
         scene_short, dialogue, dialogue_trans, key_points,
         reading_title, reading_sentences, gloss,
         vocab, patterns, grammar_sections,
         exercises, micro_task, model_paras, model_trans,
         checklist, feynman, review_dots, next_unit, next_desc):
    h = TEMPLATE
    h = h.replace("\u4e03\u4e0b Unit 9 What does he look like? | \u521d\u4e2d\u82f1\u8bed\u4e03\u5e74\u7ea7", f"\u4e03\u4e0b Unit {num} {title} | \u521d\u4e2d\u82f1\u8bed\u4e03\u5e74\u7ea7")
    h = h.replace('\u4e03\u4e0b \u00b7 Unit 9', f'\u4e03\u4e0b \u00b7 Unit {num}')
    h = h.replace('What does he look like?', title)
    h = h.replace('\u5916\u8c8c\u63cf\u8ff0 \u00b7 \u8eab\u9ad8\u4f53\u578b \u00b7 \u53d1\u578b\u914d\u9970', subtitle)

    h = h.replace('class="active"', 'class="active-DISABLE"')
    h = h.replace(f'href="{fname}.html"', f'href="{fname}.html" class="active"')
    h = h.replace('class="active-DISABLE"', '')

    h = h.replace('\U0001f4d6 \u8bdd\u9898\uff1aPhysical appearance', unit_meta[0])
    h = h.replace('\U0001f4ac \u529f\u80fd\uff1aDescribe people\'s looks \u00b7 Ask "What does he look like?"', unit_meta[1])
    h = h.replace('\U0001f4da \u8bed\u6cd5\uff1ahas/have \u63cf\u8ff0\u5916\u8c8c \u00b7 be + \u5f62\u5bb9\u8bcd\u63cf\u8ff0\u6574\u4f53\u5f62\u8c61', unit_meta[2])
    h = h.replace('\U0001f4dd \u5199\u4f5c\uff1a\u63cf\u8ff0\u4e00\u4e2a\u4eba\uff08\u670b\u53cb/\u5bb6\u4eba\uff09\u7684\u5916\u8c8c', unit_meta[3])

    cb = '\n'.join(f'  <label><input type="checkbox"> {c}</label>' for c in can_dos)
    h = re.sub(r'<label><input type="checkbox"> I can ask "What does he/she look like\?"</label>[\s\S]*?<label><input type="checkbox"> I can write a short paragraph describing someone\'s appearance\.</label>', cb, h)

    h = h.replace(
        '\u573a\u666f\uff1aMike \u548c Sarah \u5728\u8c08\u8bba\u65b0\u6765\u7684\u540c\u5b66 David\uff0c\u76f8\u4e92\u63cf\u8ff0\u4ed6\u7684\u957f\u76f8\u3002',
        f'\u573a\u666f\uff1a{scene_short}')

    dia_lines = []
    for speaker, text, trans in dialogue:
        clean = text.replace('<em>', '').replace('</em>', '')
        dia_lines.append(f'      <div class="dialogue-line">\n        <span class="speaker">{speaker}:</span>\n        <span class="en-text wotd-say" data-speak="{clean}">{text}</span>\n      </div>')
    dia_block = '\n'.join(dia_lines)
    h = re.sub(r'<div class="dialogue" id="dialogueText">[\s\S]*?</div>\n\n    <details style="margin-top:12px;">',
               f'<div class="dialogue" id="dialogueText">\n{dia_block}\n    </div>\n\n    <details style="margin-top:12px;">', h)

    trans_block = '\n'.join(f'        <p>{t}</p>' for t in dialogue_trans)
    h = re.sub(r'<p>Sarah: Mike\uff0c\u4f60\u8ba4\u8bc6\u65b0\u6765\u7684\u540c\u5b66 David \u5417\uff1f</p>[\s\S]*?<p>Mike: \u77e5\u9053\u4e86\u3002\u6211\u5f85\u513f\u53ef\u53bb\u8ddf\u4ed6\u6253\u4e2a\u62db\u547c\u3002</p>', trans_block, h)

    kp_lines = []
    for title_kp, desc in key_points:
        kp_lines.append(f'      <p><strong>{title_kp}</strong> {desc}</p>')
    kp_block = '\n'.join(kp_lines)
    h = re.sub(r'<p><strong>1\.</strong> <em>What does he look like\?</em> \u2192 "\u4ed6\u957f\u4ec0\u4e48\u6837\?" \u56fa\u5b9a\u53e5\u578b\uff0c\u8be2\u95ee\u5916\u8c8c\..*?<p><strong>4\.</strong> <em>Does he wear glasses\?</em> \u2192 \u7528 <strong>wear</strong> \u8868\u793a"\u7a7f\u6234\uff08\u773c\u955c\u3001\u8863\u670d\u7b49\uff09"\.</p>', kp_block, h, flags=re.DOTALL)

    rp_lines = []
    for p in reading_sentences:
        rp_lines.append(f'      <p class="en-text" data-speak="{p}">{p}</p>')
    rp_block = '\n'.join(rp_lines)
    h = re.sub(r'<div id="readingEnglish">\n      <p class="en-text" data-speak="My best friend is Li Ming\. He is of medium height but a little heavy\.">[\s\S]*?</div>',
               f'<div id="readingEnglish">\n{rp_block}\n      </div>', h)
    h = h.replace('<h3 style="font-size:15px;color:var(--accent);margin:0;">\U0001f4d6 Reading: My Best Friend</h3>',
                  f'<h3 style="font-size:15px;color:var(--accent);margin:0;">\U0001f4d6 Reading: {reading_title}</h3>')

    gl_lines = []
    for word, ipa, defn in gloss:
        gl_lines.append(f'        <span class="gloss-item wotd-say" data-speak="{word}">\U0001f4d8 {word} {ipa} {defn}</span>')
    gl_block = '\n'.join(gl_lines)
    h = re.sub(r'<span class="gloss-item wotd-say" data-speak="medium">[\s\S]*?</span>', gl_block, h)

    vc_lines = []
    for word, ipa, pos, defn, example, ex_html, trans in vocab:
        vc_lines.append(f'      <div class="vocab-card">\n        <span class="headword wotd-say" data-speak="{word}">{word}</span><span class="headword-speak-indicator">\U0001f50a</span>\n        <span class="ipa">{ipa}</span>\n        <span class="pos">{pos}</span>\n        <div class="definition">{defn}</div>\n        <div class="example"><span class="wotd-say" data-speak="{example}">{ex_html}</span><span class="trans">{trans}</span></div>\n      </div>')
    vc_block = '\n'.join(vc_lines)
    h = re.sub(r'<div class="vocab-grid" id="vocabGrid">[\s\S]*?</div>\n\n    </div>\n  </div>\n</details>',
               f'<div class="vocab-grid" id="vocabGrid">\n{vc_block}\n    </div>\n\n    </div>\n  </div>\n</details>', h)

    pt_lines = []
    for i, (struct, desc, sub) in enumerate(patterns, 1):
        pt_lines.append(f'      <div class="pattern-card">\n        <div class="structure">{struct}</div> <button class="speak-btn" data-target="sp{i}" title="\u6717\u8bfb\u53e5\u578b">\U0001f50a</button>\n        <div>{desc}</div>\n        <div class="substitution"><span class="q-speak-wrap" id="sp{i}">{sub}</span></div>\n      </div>')
    pt_block = '\n    \n'.join(pt_lines)
    h = re.sub(r'<div class="pattern-grid">[\s\S]*?</div>\n\n    </div>\n</details>',
               f'<div class="pattern-grid">\n    \n{pt_block}\n\n    </div>\n\n    </div>\n</details>', h)

    gm_mods = []
    for gtitle, gcontent in grammar_sections:
        gm_mods.append(f'    <div class="grammar-module">\n      <h3>{gtitle}</h3>\n{gcontent}\n    </div>')
    gm_block = '\n\n'.join(gm_mods)
    h = re.sub(r'<div class="grammar-module">\n      <h3>1\u20e3 be \u63cf\u8ff0 vs\. have \u63cf\u8ff0</h3>[\s\S]*?</div>\n\n  </div>\n</details>',
               f'{gm_block}\n\n  </div>\n</details>', h)

    ex_lines = []
    for idx, (tier, diff, qid, qbody, answer, expl) in enumerate(exercises, 1):
        if idx == 1 or tier != exercises[idx-2][0] if idx > 1 else True:
            tier_map = {'\u57fa\u7840': f'\n    <h3 style="color:var(--accent);margin:{"0" if tier == "\u57fa\u7840" else "20"}px 0 10px;">\U0001f949 \u57fa\u7840\u5173 \u00b7 \u6982\u5ff5\u8bc6\u8bb0</h3>\n', '\u63d0\u5347': '\n    <h3 style="color:var(--accent);margin:20px 0 10px;">\U0001f948 \u63d0\u5347\u5173 \u00b7 \u8bed\u5883\u8fd0\u7528</h3>\n', '\u6311\u6218': '\n    <h3 style="color:var(--accent);margin:20px 0 10px;">\U0001f947 \u6311\u6218\u5173 \u00b7 \u7efc\u5408\u8fd0\u7528</h3>\n'}
            ex_lines.append(tier_map[tier])
        ex_lines.append(f'    <div class="exam-q">\n      <span class="q-tag">{tier}</span>\n      <span class="q-diff">{diff}</span>\n      <div class="q-body"><span class="q-speak-wrap" id="q{qid}">{qbody}</span> <button class="speak-btn" data-target="q{qid}" title="\u6717\u8bfb\u9898\u76ee">\U0001f50a</button></div>\n      <span class="q-toggle">\U0001f4dd \u67e5\u770b\u7b54\u6848</span>\n      <div class="q-solution"><strong>\u7b54\u6848\uff1a</strong>{answer}<br><strong>\u89e3\u6790\uff1a</strong>{expl}</div>\n    </div>')
    ex_block = '\n'.join(ex_lines)
    h = re.sub(r'<h3 style="color:var\(--accent\);margin:0px 0 10px;">\U0001f949 \u57fa\u7840\u5173 \u00b7 \u6982\u5ff5\u8bc6\u8bb0</h3>[\s\S]*?</div>\n\n</details>',
               f'{ex_block}\n\n  </div>\n\n</details>', h)

    h = h.replace('\u7528\u82f1\u8bed\u5199\u4e00\u6bb5\u5173\u4e8e\u4f60\u670b\u53cb\u6216\u5bb6\u4eba\u5916\u8c8c\u7684\u63cf\u8ff0\u3002\u6ce8\u610f\u5148\u7528 There be \u63cf\u8ff0\u6574\u4f53\uff0c\u518d\u7528 has \u63cf\u8ff0\u7ec6\u8282\u3002', micro_task)

    mp_lines = []
    for p in model_paras:
        mp_lines.append(f'    <p class="en"><span class="wotd-say" data-speak="{p}">{p}</span></p>')
    mp_block = '\n'.join(mp_lines)
    writing_template = '''    <p class="en"><span class="wotd-say" data-speak="I want to tell you about my best friend, Wang Fang.">I want to tell you about my best friend, Wang Fang.</span></p>
    <p class="en"><span class="wotd-say" data-speak="She is of medium height and a little thin. She has long straight black hair.">She is of medium height and a little thin. She has long straight black hair.</span></p>
    <p class="en"><span class="wotd-say" data-speak="She has big bright eyes and a small mouth. She always wears a nice smile.">She has big bright eyes and a small mouth. She always wears a nice smile.</span></p>
    <p class="en"><span class="wotd-say" data-speak="She likes to wear a white T-shirt and blue jeans. She looks very pretty.">She likes to wear a white T-shirt and blue jeans. She looks very pretty.</span></p>
    <p class="en"><span class="wotd-say" data-speak="Everyone says she is kind and friendly. I'm lucky to have her as my friend.">Everyone says she is kind and friendly. I'm lucky to have her as my friend.</span></p>'''
    h = h.replace(writing_template, mp_block)
    h = h.replace('\u6211\u60f3\u5411\u4f60\u4ecb\u7ecd\u6211\u6700\u597d\u7684\u670b\u53cb\u738b\u82b3\u3002\u5979\u4e2d\u7b49\u8eab\u9ad8\uff0c\u6709\u70b9\u7626\u3002\u5979\u6709\u4e00\u5934\u9ed1\u8272\u7684\u957f\u76f4\u53d1\u3002\u5979\u6709\u4e00\u53cc\u660e\u4eae\u7684\u5927\u773c\u775b\u548c\u4e00\u5f20\u5c0f\u5634\u3002\u5979\u603b\u662f\u5e26\u7740\u751c\u751c\u7684\u5fae\u7b11\u3002\u5979\u559c\u6b22\u7a7f\u767d T \u6064\u548c\u84dd\u8272\u725b\u4ed4\u88e4\u3002\u5979\u770b\u8d77\u6765\u975e\u5e38\u6f02\u4eae\u3002\u6bcf\u4e2a\u4eba\u90fd\u8bf4\u5979\u5f88\u5584\u826f\u53cb\u597d\u3002\u6211\u5f88\u5e78\u8fd0\u6709\u5979\u505a\u6211\u7684\u670b\u53cb\u3002', model_trans)

    cl_lines = '\n'.join(f'  <label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> {c}</label>' for c in checklist)
    h = re.sub(r'<label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> \u6211\u80fd\u7528 What does he/she look like\? \u8be2\u95ee\u5916\u8c8c</label>[\s\S]*?<label><span class="self-score">\U0001f7e1\u2192\U0001f7e2</span><input type="checkbox"> \u6211\u80fd\u5199\u4e00\u6bb5\u5b8c\u6574\u7684\u5916\u8c8c\u63cf\u8ff0</label>', cl_lines, h)

    h = h.replace('<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>\u60f3\u8c61\u4e00\u4e2a\u4f60\u559c\u6b22\u7684\u7535\u5f71\u89d2\u8272\u6216\u660e\u661f\uff0c\u7528\u82f1\u8bed\u63cf\u8ff0\u5979\u7684\u5916\u8c8c\u3002\u8ba9\u540c\u5b66\u6839\u636e\u4f60\u7684\u63cf\u8ff0\u731c\u51fa\u662f\u8c01\u3002"He is tall and strong\. He has short black hair and a round face\. He always wears a black suit\. Who is he\?"',
                  f'<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>{feynman}')

    rv_block = '\n    '.join(f'<span class="review-dot">{r}</span>' for r in review_dots)
    h = re.sub(r'<span class="review-dot">\U0001f535 1\u5929\u540e\uff1a\u7528\u82f1\u8bed\u63cf\u8ff0\u4f60\u7684\u82f1\u8bed\u8001\u5e08\u7684\u5916\u8c8c</span>\n    <span class="review-dot">\U0001f7e2 3\u5929\u540e\uff1a\u5199\u51fa\u4f60\u548c\u540c\u684c\u7684\u5916\u8c8c\u5bf9\u6bd4</span>\n    <span class="review-dot">\U0001f7e1 1\u5468\u540e\uff1a\u719f\u8bb0\u5934\u53d1\u63cf\u8ff0\u8bcd\uff08\u957f\u77ed/\u76f4\u5377/\u989c\u8272\uff09\u7ec4\u5408</span>\n    <span class="review-dot">\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60 has/have \u548c be \u5728\u5916\u8c8c\u63cf\u8ff0\u4e2d\u7684\u7528\u6cd5</span>', rv_block, h)

    h = h.replace('<strong>\u27a1\ufe0f \u4e0b\u4e00\u5355\u5143\uff1aUnit 10 I\'d like some noodles.</strong>', f'<strong>\u27a1\ufe0f \u4e0b\u4e00\u5355\u5143\uff1a{next_unit}</strong>')
    h = h.replace('\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u5982\u4f55\u7528\u82f1\u8bed\u70b9\u9910\u2014\u2014would like \u7684\u7528\u6cd5\u3001\u98df\u7269\u8bcd\u6c47\u548c\u9910\u5385\u5bf9\u8bdd\u3002', next_desc)

    open(f"{fname}.html", "w", encoding="utf-8").write(h)
    print(f"{fname}.html written ({len(h)} bytes)")

gen("b2u11", 11,
    "How was your school trip?",
    "\u5b66\u6821\u65c5\u884c \u00b7 \u8fc7\u53bb\u7ecf\u5386 \u00b7 \u8fc7\u53bb\u5f0f",
    ["\U0001f4d6 \u8bdd\u9898\uff1aSchool trip &amp; Past events",
     "\U0001f4ac \u529f\u80fd\uff1aTalk about past events \u00b7 Ask \"How was...?\" \u00b7 Describe experiences",
     "\U0001f4da \u8bed\u6cd5\uff1aSimple past tense (was/were) \u00b7 Regular &amp; irregular past verbs",
     "\U0001f4dd \u5199\u4f5c\uff1a\u7528\u8fc7\u53bb\u65f6\u63cf\u8ff0\u4e00\u6b21\u5b66\u6821\u65c5\u884c"],
    ['I can ask "How was your school trip?"',
     'I can say "It was great / boring / interesting."',
     "I can use regular past tense verbs (e.g. visited, played).",
     "I can write about a past trip using past tense."],
    "Tom\u3001Sarah \u548c\u8001\u5e08\u5728\u5b66\u6821\u7ec4\u7ec7\u7684\u519c\u573a\u5c55\u89c8\u540e\u56de\u5fc6\u8fc7\u53bb\u7684\u7ecf\u5386\u3002",
    [["Teacher", "How was your school trip, everyone?", "\u8001\u5e08: \u5927\u5bb6\u597d\uff0c\u5b66\u6821\u65c5\u884c\u600e\u4e48\u6837\uff1f"],
     ["Tom", "It was great! I went to the farm with my classmates.", "Tom: \u592a\u68d2\u4e86\uff01\u6211\u548c\u540c\u5b66\u4eec\u53bb\u4e86\u519c\u573a\u3002"],
     ["Teacher", "What did you do there?", "\u8001\u5e08: \u4f60\u4eec\u5728\u90a3\u91cc\u505a\u4e86\u4ec0\u4e48\uff1f"],
     ["Tom", "I rode a horse and milked a cow. It was so much fun!", "Tom: \u6211\u9a91\u4e86\u9a6c\uff0c\u8fd8\u7ed9\u725b\u64a0\u5976\u3002\u975e\u5e38\u6709\u8da3\uff01"],
     ["Sarah", "I went to the museum. I saw some old things. They were cool.", "Sarah: \u6211\u53bb\u4e86\u535a\u7269\u9986\u3002\u6211\u770b\u5230\u4e86\u5f88\u591a\u53e4\u8463\u3002\u597d\u9177\u554a\uff01"],
     ["Teacher", "Did you have a good time?", "\u8001\u5e08: \u4f60\u4eec\u73a9\u5f97\u5f00\u5fc3\u5417\uff1f"],
     ["Tom", "Yes, I did. I learned a lot about farming!", "Tom: \u5f53\u7136\u4e86\u3002\u6211\u5b66\u5230\u4e86\u5f88\u591a\u5173\u4e8e\u519c\u4e1a\u7684\u77e5\u8bc6\uff01"],
     ["Sarah", "Well... I got lost in the museum. It was a little scary!", "Sarah: \u55ef... \u6211\u5728\u535a\u7269\u9986\u91cc\u8ff7\u8def\u4e86\u3002\u6709\u70b9\u53ef\u6015\uff01"]],
    ["\u8001\u5e08: \u5927\u5bb6\u597d\uff0c\u5b66\u6821\u65c5\u884c\u600e\u4e48\u6837\uff1f",
     "Tom: \u592a\u68d2\u4e86\uff01\u6211\u548c\u540c\u5b66\u4eec\u53bb\u4e86\u519c\u573a\u3002",
     "\u8001\u5e08: \u4f60\u4eec\u5728\u90a3\u91cc\u505a\u4e86\u4ec0\u4e48\uff1f",
     "Tom: \u6211\u9a91\u4e86\u9a6c\uff0c\u8fd8\u7ed9\u725b\u64a0\u5976\u3002\u975e\u5e38\u6709\u8da3\uff01",
     "Sarah: \u6211\u53bb\u4e86\u535a\u7269\u9986\u3002\u6211\u770b\u5230\u4e86\u5f88\u591a\u53e4\u8463\u3002\u597d\u9177\u554a\uff01",
     "\u8001\u5e08: \u4f60\u4eec\u73a9\u5f97\u5f00\u5fc3\u5417\uff1f",
     "Tom: \u5f53\u7136\u4e86\u3002\u6211\u5b66\u5230\u4e86\u5f88\u591a\u5173\u4e8e\u519c\u4e1a\u7684\u77e5\u8bc6\uff01",
     "Sarah: \u55ef... \u6211\u5728\u535a\u7269\u9986\u91cc\u8ff7\u8def\u4e86\u3002\u6709\u70b9\u53ef\u6015\uff01"],
    [("1. ", "How was...? \u2192 \u201c\u2026\u2026\u600e\u4e48\u6837\uff1f\u201d\u8be2\u95ee\u5bf9\u67d0\u4e8b\u7684\u770b\u6cd5\u3002How was your trip? It was great! \u56fa\u5b9a\u642d\u914d\u3002"),
     ("2. ", "What did you do? \u2192 \u201c\u4f60\u505a\u4e86\u4ec0\u4e48\uff1f\u201d did + \u52a8\u8bcd\u539f\u5f62\u6784\u6210\u8fc7\u53bb\u65f6\u7591\u95ee\u53e5\u3002"),
     ("3. ", "Go \u2192 went / see \u2192 saw / ride \u2192 rode / milk \u2192 milked / learn \u2192 learned \u2014 \u8fc7\u53bb\u5f0f\u7684\u89c4\u5219\u4e0e\u4e0d\u89c4\u5219\u53d8\u5316\u3002"),
     ("4. ", "Did you...? \u2192 Yes, I did. / No, I didn't. \u8fc7\u53bb\u65f6\u7591\u95ee\u53e5\u7684\u56de\u7b54\u3002")],
    "A Great Day at the Farm",
    ["Last Monday, our class went to a farm for a school trip. The weather was warm and sunny.",
     "We arrived at the farm at nine o'clock. First, my friend Mike and I rode horses. It was exciting!",
     "Then we milked cows and fed chickens. The farmer taught us how to grow vegetables.",
     "We also picked some apples and tomatoes. They were very fresh and delicious.",
     "At noon we had lunch on the grass. I ate a big sandwich and drank some orange juice.",
     "In the afternoon we visited the cowshed and took many photos. I learned a lot about farm life.",
     "I think the school trip was really wonderful. I want to go there again!"],
    [["went", "/went/", "v. (go\u7684\u8fc7\u53bb\u5f0f) \u53bb"],
     ["milk", "/m\u026alk/", "v. \u64a0\u5976"],
     ["ride", "/ra\u026ad/", "v. \u9a91\uff08\u9a6c\u3001\u81ea\u884c\u8f66\uff09"],
     ["feed", "/fi\u02d0d/", "v. \u5582\u98df"],
     ["farm", "/f\u0251\u02d0rm/", "n. \u519c\u573a"]],
    [("cow", "/ka\u028a/", "n.", "\u5976\u725b", "I milked the cow on the farm.", "I milked the <strong>cow</strong> on the farm.", "\u6211\u5728\u519c\u573a\u7ed9\u5976\u725b\u64a0\u5976\u3002"),
     ("horse", "/h\u0254\u02d0rs/", "n.", "\u9a6c", "She rode a horse yesterday.", "She <strong>rode</strong> a <strong>horse</strong> yesterday.", "\u5979\u6628\u5929\u9a91\u4e86\u9a6c\u3002"),
     ("farm", "/f\u0251\u02d0rm/", "n.", "\u519c\u573a\uff1bv. \u79cd\u5730", "My uncle works on the farm.", "My uncle works on the <strong>farm</strong>.", "\u6211\u53d4\u53d4\u5728\u519c\u573a\u5de5\u4f5c\u3002"),
     ("milk", "/m\u026alk/", "v.", "\u64a0\u5976\uff1bn. \u5976", "The farmer milks the cows every morning.", "The farmer <strong>milks</strong> the cows every morning.", "\u519c\u6c11\u6bcf\u5929\u65e9\u4e0a\u64a0\u725b\u5976\u3002"),
     ("ride", "/ra\u026ad/", "v.", "\u9a91\uff08\u9a6c\u3001\u81ea\u884c\u8f66\uff09", "Can you ride a horse?", "Can you <strong>ride</strong> a horse?", "\u4f60\u4f1a\u9a91\u9a6c\u5417\uff1f"),
     ("feed", "/fi\u02d0d/", "v.", "\u5582\u98df\uff1b\u4f9b\u517b", "We fed the chickens on the farm.", "We <strong>fed</strong> the chickens on the farm.", "\u6211\u4eec\u5728\u519c\u573a\u5582\u4e86\u9e21\u3002"),
     ("grow", "/\u0261ro\u028a/", "v.", "\u79cd\u690d\uff1b\u751f\u957f", "The farmer grows rice and vegetables.", "The farmer <strong>grows</strong> rice and vegetables.", "\u519c\u6c11\u79cd\u690d\u6c34\u7a3b\u548c\u852c\u83dc\u3002"),
     ("pick", "/p\u026ak/", "v.", "\u6458\uff1b\u6311\u9009", "We picked apples on the farm.", "We <strong>picked</strong> apples on the farm.", "\u6211\u4eec\u5728\u519c\u573a\u6458\u4e86\u82f9\u679c\u3002"),
     ("excellent", "/\u02c8\u025bks\u0259l\u0259nt/", "adj.", "\u4f18\u79c0\u7684\uff1b\u68d2\u6781\u4e86", "The trip was excellent!", "The trip was <strong>excellent</strong>!", "\u8fd9\u6b21\u65c5\u884c\u68d2\u6781\u4e86\uff01"),
     ("museum", "/mju\u02d0\u02c8zi\u02d0\u0259m/", "n.", "\u535a\u7269\u9986", "We visited the history museum.", "We visited the history <strong>museum</strong>.", "\u6211\u4eec\u53c2\u89c2\u4e86\u5386\u53f2\u535a\u7269\u9986\u3002")],
    [(q("How was...? / It was..."), q("\u8be2\u95ee\u5bf9\u67d0\u4e8b\u7684\u770b\u6cd5"),
      q('''\u2705 <strong>How was</strong> <span class="slot">your school trip</span>?<br>
      \u2705 It <strong>was</strong> <span class="slot">great / wonderful / fun / boring</span>.<br>
      \u2705 How <strong>were</strong> <span class="slot">the people</span>? They <strong>were</strong> very nice.''')),
     (q("What did you do...?"), q("\u7591\u95ee\u53e5\uff1adid + \u52a8\u8bcd\u539f\u5f62"),
      q('''\u2705 <strong>What did</strong> you <strong>do</strong> <span class="slot">on the farm</span>?<br>
      \u2705 I <strong>rode</strong> a horse and <strong>milked</strong> a cow.<br>
      \u2705 <strong>Did</strong> you <strong>see</strong> any animals? Yes, I <strong>did</strong>. / No, I <strong>didn't</strong>.''')),
     (q("\u52a8\u8bcd\u8fc7\u53bb\u5f0f\u89c4\u5219"), q("\u52a0 -ed / \u4e0d\u89c4\u5219\u53d8\u5316"),
      q('''\u2705 \u89c4\u5219\uff1avisit -> <strong>visited</strong>, play -> <strong>played</strong>, milk -> <strong>milked</strong><br>
      \u2705 -e\u7ed3\u5c3e\uff1alive -> <strong>lived</strong>, like -> <strong>liked</strong><br>
      \u2705 \u8f85\u97f3+y\u7ed3\u5c3e\uff1astudy -> <strong>studied</strong>, carry -> <strong>carried</strong><br>
      \u2705 \u91cd\u8bfb\u95ed\u97f3\u8282\uff1astop -> <strong>stopped</strong>, plan -> <strong>planned</strong>''')),
     (q("\u5e38\u89c1\u4e0d\u89c4\u5219\u8fc7\u53bb\u5f0f"), q("\u9700\u8981\u5355\u72ec\u8bb0\u5fc6\u7684\u5e38\u7528\u8bcd"),
      q('''\u2705 go -> <strong>went</strong>, see -> <strong>saw</strong>, have -> <strong>had</strong><br>
      \u2705 eat -> <strong>ate</strong>, drink -> <strong>drank</strong>, ride -> <strong>rode</strong><br>
      \u2705 feed -> <strong>fed</strong>, grow -> <strong>grew</strong>, pick -> <strong>picked</strong>\uff08\u89c4\u5219\uff09'''))],
    [(q("1\u20e3 \u4e00\u822c\u8fc7\u53bb\u65f6\uff1awas / were"),
      q('''<p><strong>was / were</strong> \u662f is / am / are \u7684\u8fc7\u53bb\u5f0f\uff0c\u7528\u4e8e\u63cf\u8ff0\u8fc7\u53bb\u72b6\u6001\u3002</p>
      <table class="grammar-table">
        <tr><th>\u4e3b\u8bed</th><th>\u8fc7\u53bb\u5f0f</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>I / He / She / It</td><td>was</td><td><span class="wotd-say" data-speak="The trip was great.">The trip <strong>was</strong> great.</span></td></tr>
        <tr><td>You / We / They</td><td>were</td><td><span class="wotd-say" data-speak="The people were friendly.">The people <strong>were</strong> friendly.</span></td></tr>
        <tr><td>\u7591\u95ee\u53e5</td><td>Was/Were \u63d0\u524d</td><td><span class="wotd-say" data-speak="Was the trip interesting?">Was the trip interesting?</span></td></tr>
        <tr><td>\u5426\u5b9a\u53e5</td><td>wasn't / weren't</td><td><span class="wotd-say" data-speak="The food wasn't very good.">The food <strong>wasn't</strong> very good.</span></td></tr>
      </table>''')),
     (q("2\u20e3 \u4e00\u822c\u8fc7\u53bb\u65f6\uff1a\u884c\u4e3a\u52a8\u8bcd"),
      q('''<p>\u7528\u4e8e\u63cf\u8ff0\u8fc7\u53bb\u53d1\u751f\u7684\u52a8\u4f5c\u3002\u7591\u95ee\u53e5\u7528 did\uff0c\u52a8\u8bcd\u56de\u590d\u539f\u5f62\u3002</p>
      <table class="grammar-table">
        <tr><th>\u53e5\u578b</th><th>\u7ed3\u6784</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>\u80af\u5b9a\u53e5</td><td>\u4e3b + \u52a8\u8bcd\u8fc7\u53bb\u5f0f</td><td><span class="wotd-say" data-speak="I visited the museum.">I <strong>visited</strong> the museum.</span></td></tr>
        <tr><td>\u5426\u5b9a\u53e5</td><td>\u4e3b + didn't + \u52a8\u8bcd\u539f\u5f62</td><td><span class="wotd-say" data-speak="I didn't see any cows.">I <strong>didn't see</strong> any cows.</span></td></tr>
        <tr><td>\u7591\u95ee\u53e5</td><td>Did + \u4e3b + \u52a8\u8bcd\u539f\u5f62?</td><td><span class="wotd-say" data-speak="Did you ride a horse?">Did you ride a horse?</span></td></tr>
      </table>''')),
     (q("3\u20e3 \u5e38\u89c1\u4e0d\u89c4\u5219\u52a8\u8bcd\u8fc7\u53bb\u5f0f"),
      q('''<table class="grammar-table">
        <tr><th>\u73b0\u5728\u5f62\u5f0f</th><th>\u8fc7\u53bb\u5f0f</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>go</td><td>went</td><td><span class="wotd-say" data-speak="I went to the park.">I <strong>went</strong> to the park.</span></td></tr>
        <tr><td>see</td><td>saw</td><td><span class="wotd-say" data-speak="I saw a big cow.">I <strong>saw</strong> a big cow.</span></td></tr>
        <tr><td>eat</td><td>ate</td><td><span class="wotd-say" data-speak="We ate lunch on the farm.">We <strong>ate</strong> lunch on the farm.</span></td></tr>
        <tr><td>have</td><td>had</td><td><span class="wotd-say" data-speak="We had a great time.">We <strong>had</strong> a great time.</span></td></tr>
        <tr><td>take</td><td>took</td><td><span class="wotd-say" data-speak="I took many photos.">I <strong>took</strong> many photos.</span></td></tr>
      </table>
      <div class="chinese-error">
        <strong>\u26a0\ufe0f \u4e2d\u5f0f\u82f1\u8bed\u7ea0\u9519\uff1a</strong><br>
        \u274c <span class="wrong wotd-say" data-speak="I go to the farm yesterday.">I go to the farm yesterday.</span><br>
        \u2705 <span class="correct wotd-say" data-speak="I went to the farm yesterday.">I <strong>went</strong> to the farm yesterday.</span><br><br>
        \u274c <span class="wrong wotd-say" data-speak="Did you went to the museum?">Did you went to the museum?</span><br>
        \u2705 <span class="correct wotd-say" data-speak="Did you go to the museum?">Did you <strong>go</strong> to the museum?</span>
      </div>'''))],
    [("\u57fa\u7840", "\u2605\u2606\u2606", 1, 'How ____ your school trip? \u2014 It was great! (is / was / were)', "was", "How was...? \u8be2\u95ee\u5bf9\u67d0\u4e8b\u7684\u770b\u6cd5\uff0c\u56de\u7b54\u7528 It was..."),
     ("\u57fa\u7840", "\u2605\u2606\u2606", 2, 'I ____ to the farm yesterday. (go / goes / went)', "went", "yesterday \u8868\u793a\u8fc7\u53bb\uff0c\u7528 go \u7684\u8fc7\u53bb\u5f0f went\u3002"),
     ("\u57fa\u7840", "\u2605\u2606\u2606", 3, 'Did you ____ a horse? \u2014 Yes, I did. (rode / ride / riding)', "ride", "Did \u540e\u52a8\u8bcd\u7528\u539f\u5f62\u3002"),
     ("\u63d0\u5347", "\u2605\u2605\u2606", 4, '\u6539\u9519\uff1aI didn\'t went to the museum yesterday.', "I didn't go to the museum yesterday.", "didn't \u540e\u52a8\u8bcd\u7528\u539f\u5f62 go\uff0c\u4e0d\u80fd\u7528\u8fc7\u53bb\u5f0f went\u3002"),
     ("\u63d0\u5347", "\u2605\u2605\u2606", 5, '\u8fde\u8bcd\u6210\u53e5\uff1adid / you / what / do / on / farm / the', "What did you do on the farm?", "\u7591\u95ee\u53e5\uff1aWhat + did + \u4e3b\u8bed + do + \u5176\u4ed6\uff1f"),
     ("\u63d0\u5347", "\u2605\u2605\u2606", 6, '\u7528\u8fc7\u53bb\u5f0f\u586b\u7a7a\uff1aWe ____ (see) a lot of cows and ____ (feed) the chickens.', "saw; fed", "see\u2192saw\uff08\u4e0d\u89c4\u5219\uff09\uff0cfeed\u2192fed\uff08\u4e0d\u89c4\u5219\uff09\u3002"),
     ("\u6311\u6218", "\u2605\u2605\u2605", 7, '\u6c49\u8bd1\u82f1\uff1a\u4f60\u7684\u5b66\u6821\u65c5\u884c\u600e\u4e48\u6837\uff1f\u592a\u68d2\u4e86\uff01\u6211\u9a91\u4e86\u9a6c\u8fd8\u6458\u4e86\u82f9\u679c\u3002', "How was your school trip? It was excellent! I rode a horse and picked apples.", "\u7efc\u5408\u8fc7\u53bb\u65f6\u8868\u8fbe\uff1awas \u63cf\u8ff0\u611f\u53d7\uff0c\u8fc7\u53bb\u5f0f\u52a8\u8bcd\u63cf\u8ff0\u5177\u4f53\u6d3b\u52a8\u3002"),
     ("\u6311\u6218", "\u2605\u2605\u2605", 8, '\u7f16\u5199\u5bf9\u8bdd\uff1a<br>A: ____ was your ____?<br>B: It was ____.<br>A: What ____ you ____?<br>B: I ____ a horse and ____ a cow.', "How; trip; wonderful; did; do; rode; milked", "\u8336\u8336\u5f0f\u63d0\u95ee\uff1aHow was...? What did you do? \u9010\u6b65\u8be2\u95ee\u7ec6\u8282\u3002")],
    "\u7528\u4e00\u822c\u8fc7\u53bb\u65f6\u5199\u4e00\u6bb5\u5173\u4e8e\u4f60\u7684\u5b66\u6821\u65c5\u884c\u7684\u7ecf\u5386\u3002\u81f3\u5c116\u53e5\u8bdd\uff0c\u5305\u62ec\u4f60\u4ec0\u4e48\u65f6\u5019\u53bb\u7684\u3001\u548c\u8c01\u53bb\u7684\u3001\u505a\u4e86\u4ec0\u4e48\u3001\u611f\u53d7\u5982\u4f55\u3002",
    ["Last Friday, I went on a school trip to the science museum with my classmates.",
     "The bus ride was long but very interesting. We saw many tall buildings on the way.",
     "At the museum, I saw a robot that could play chess. It was so cool!",
     "I also tried a 3D game. The experience was amazing and I learned a lot.",
     "We took many photos and bought some souvenirs. The gift shop was not expensive.",
     "I think the trip was really educational and fun. I want to visit again."],
    "\u4e0a\u5468\u4e94\uff0c\u6211\u548c\u540c\u5b66\u4eec\u53bb\u79d1\u5b66\u535a\u7269\u9986\u53c2\u89c2\u3002\u5ea7\u516c\u5171\u6c7d\u8f66\u5f88\u957f\u65f6\u95f4\u4f46\u5f88\u6709\u8da3\u3002\u6211\u4eec\u5728\u8def\u4e0a\u770b\u5230\u4e86\u8bb8\u591a\u9ad8\u697c\u3002\u5728\u535a\u7269\u9986\u91cc\uff0c\u6211\u770b\u5230\u4e86\u4e00\u4e2a\u4f1a\u4e0b\u68cb\u7684\u673a\u5668\u4eba\uff0c\u975e\u5e38\u9177\uff01\u6211\u8fd8\u5c1d\u8bd5\u4e86 3D \u6e38\u620f\uff0c\u90a3\u79cd\u4f53\u9a8c\u592a\u60ca\u4eba\u4e86\uff0c\u6211\u5b66\u5230\u4e86\u5f88\u591a\u3002\u6211\u4eec\u62cd\u4e86\u5f88\u591a\u7167\u7247\uff0c\u4e70\u4e86\u7eaa\u5ff5\u54c1\u3002\u79ae\u54c1\u5e97\u4e5f\u4e0d\u8d35\u3002\u6211\u89c9\u5f97\u8fd9\u6b21\u65c5\u884c\u65e2\u6709\u6559\u80b2\u610f\u4e49\u53c8\u5f88\u6709\u8da3\uff0c\u6211\u8fd8\u60f3\u518d\u53bb\u4e00\u6b21\u3002",
    ["\u6211\u80fd\u7528 How was...? \u8be2\u95ee\u5bf9\u67d0\u4e8b\u7684\u770b\u6cd5",
     "\u6211\u80fd\u7528 What did you do? \u8be2\u95ee\u8fc7\u53bb\u7684\u6d3b\u52a8",
     "\u6211\u80fd\u6b63\u786e\u4f7f\u7528\u8fc7\u53bb\u5f0f\u52a8\u8bcd",
     "\u6211\u80fd\u533a\u5206\u89c4\u5219\u548c\u4e0d\u89c4\u5219\u52a8\u8bcd\u7684\u8fc7\u53bb\u5f0f",
     "\u6211\u80fd\u7528\u4e00\u822c\u8fc7\u53bb\u65f6\u5199\u4e00\u6bb5\u7ecf\u5386"],
    "\u60f3\u8c61\u4f60\u6628\u5929\u53bb\u4e86\u4e00\u4e2a\u6709\u8da3\u7684\u5730\u65b9\uff08\u52a8\u7269\u56ed\u3001\u6d77\u6ee9\u3001\u516c\u56ed\u7b49\uff09\uff0c\u7528\u82f1\u8bed\u5411\u540c\u5b66\u63cf\u8ff0\u4f60\u53bb\u4e86\u54ea\u91cc\u3001\u505a\u4e86\u4ec0\u4e48\u3001\u611f\u89c9\u600e\u4e48\u6837\u3002\u7ec3\u4e60\uff1a\u201cHow was your trip? \u2014 It was great! What did you do? \u2014 I saw... Did you...? \u2014 Yes, I did.\u201d",
    ["\U0001f535 1\u5929\u540e\uff1a\u590d\u4e60 How was / What did \u7591\u95ee\u53e5\u578b",
     "\U0001f7e2 3\u5929\u540e\uff1a\u5199\u51fa is/am/are/go/see/have \u7684\u8fc7\u53bb\u5f0f",
     "\U0001f7e1 1\u5468\u540e\uff1a\u80cc\u8bf5\u8fc7\u53bb\u5f0f\u89c4\u5219\u53ca\u5e38\u89c1\u4e0d\u89c4\u5219\u52a8\u8bcd",
     "\U0001f534 1\u6708\u540e\uff1a\u7528\u8fc7\u53bb\u65f6\u53e3\u8ff0\u4e00\u6b21\u65c5\u884c\u7ecf\u5386"],
    "\u4e0b\u4e00\u5355\u5143\uff1aUnit 12 What did you do last weekend?",
    "\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u7ee7\u7eed\u5b66\u4e60\u4e00\u822c\u8fc7\u53bb\u65f6\uff0c\u8bdd\u9898\u805a\u7126\u5728\u5468\u672b\u6d3b\u52a8\uff0c\u5b66\u4e60\u66f4\u591a\u4e0d\u89c4\u5219\u52a8\u8bcd\u7684\u8fc7\u53bb\u5f0f\u3002"
)
