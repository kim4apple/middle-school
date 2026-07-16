#!/usr/bin/env python3
"""Generate b2u12.html."""
import re

TEMPLATE = open("b2u09.html", encoding="utf-8").read()

def q(s):
    return s

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

    h = h.replace('\u573a\u666f\uff1aMike \u548c Sarah \u5728\u8c08\u8bba\u65b0\u6765\u7684\u540c\u5b66 David\uff0c\u76f8\u4e92\u63cf\u8ff0\u4ed6\u7684\u957f\u76f8\u3002',
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

gen("b2u12", 12,
    "What did you do last weekend?",
    "\u5468\u672b\u6d3b\u52a8 \u00b7 \u8fc7\u53bb\u7ecf\u5386 \u00b7 \u4e0d\u89c4\u5219\u52a8\u8bcd",
    ["\U0001f4d6 \u8bdd\u9898\uff1aWeekend activities &amp; Past experiences",
     "\U0001f4ac \u529f\u80fd\uff1aAsk \"What did you do?\" \u00b7 Talk about weekend \u00b7 Share feelings",
     "\U0001f4da \u8bed\u6cd5\uff1aSimple past tense (irregular verbs) \u00b7 Wh-questions in past tense",
     "\U0001f4dd \u5199\u4f5c\uff1a\u7528\u8fc7\u53bb\u65f6\u63cf\u8ff0\u4e00\u4e2a\u5468\u672b\u7ecf\u5386"],
    ['I can ask "What did you do last weekend?"',
     'I can answer "I stayed at home / went to the beach / did my homework."',
     "I can use irregular past tense verbs (e.g. went, did, had, flew).",
     "I can write about my last weekend in simple past tense."],
    "\u8bfe\u95f4\uff0c\u540c\u5b66\u4eec\u5728\u8c08\u8bba\u4e0a\u5468\u672b\u505a\u4e86\u4ec0\u4e48\u3002",
    [["Lucy", "Hi, Bob! What did you do last weekend?", "Lucy: \u55e8\uff0cBob\uff01\u4f60\u4e0a\u5468\u672b\u505a\u4e86\u4ec0\u4e48\uff1f"],
     ["Bob", "I went to the beach with my family. We swam in the sea.", "Bob: \u6211\u548c\u5bb6\u4eba\u53bb\u4e86\u6d77\u6ee9\u3002\u6211\u4eec\u5728\u6d77\u91cc\u6e38\u6cf3\u3002"],
     ["Lucy", "Sounds fun! Did you play volleyball?", "Lucy: \u542c\u8d77\u6765\u5f88\u6709\u8da3\uff01\u4f60\u4eec\u6253\u6392\u7403\u4e86\u5417\uff1f"],
     ["Bob", "No, we didn't. But we flew a kite. It was windy.", "Bob: \u6ca1\u6709\u3002\u4f46\u6211\u4eec\u653e\u4e86\u98ce\u7b5d\u3002\u5f53\u65f6\u5f88\u6709\u98ce\u3002"],
     ["Lucy", "What about you, Amy?", "Lucy: \u4f60\u5462\uff0cAmy\uff1f"],
     ["Amy", "I stayed at home and studied for the math test.", "Amy: \u6211\u5f85\u5728\u5bb6\u91cc\u590d\u4e60\u6570\u5b66\u6d4b\u8bd5\u4e86\u3002"],
     ["Lucy", "Did you watch a movie?", "Lucy: \u4f60\u770b\u7535\u5f71\u4e86\u5417\uff1f"],
     ["Amy", "Yes, I did. I watched an interesting documentary about butterflies.", "Amy: \u770b\u4e86\u3002\u6211\u770b\u4e86\u4e00\u90e8\u6709\u8da3\u7684\u5173\u4e8e\u8774\u8776\u7684\u7eaa\u5f55\u7247\u3002"]],
    ["Lucy: \u55e8\uff0cBob\uff01\u4f60\u4e0a\u5468\u672b\u505a\u4e86\u4ec0\u4e48\uff1f",
     "Bob: \u6211\u548c\u5bb6\u4eba\u53bb\u4e86\u6d77\u6ee9\u3002\u6211\u4eec\u5728\u6d77\u91cc\u6e38\u6cf3\u3002",
     "Lucy: \u542c\u8d77\u6765\u5f88\u6709\u8da3\uff01\u4f60\u4eec\u6253\u6392\u7403\u4e86\u5417\uff1f",
     "Bob: \u6ca1\u6709\u3002\u4f46\u6211\u4eec\u653e\u4e86\u98ce\u7b5d\u3002\u5f53\u65f6\u5f88\u6709\u98ce\u3002",
     "Lucy: \u4f60\u5462\uff0cAmy\uff1f",
     "Amy: \u6211\u5f85\u5728\u5bb6\u91cc\u590d\u4e60\u6570\u5b66\u6d4b\u8bd5\u4e86\u3002",
     "Lucy: \u4f60\u770b\u7535\u5f71\u4e86\u5417\uff1f",
     "Amy: \u770b\u4e86\u3002\u6211\u770b\u4e86\u4e00\u90e8\u6709\u8da3\u7684\u5173\u4e8e\u8774\u8776\u7684\u7eaa\u5f55\u7247\u3002"],
    [("1. ", "last weekend / last night / yesterday \u2192 \u8fc7\u53bb\u65f6\u95f4\u6807\u5fd7\u8bcd\uff0c\u5f15\u51fa\u8fc7\u53bb\u65f6\u53f0\u3002"),
     ("2. ", "What did you do...? \u2192 \u201c\u4f60\u505a\u4e86\u4ec0\u4e48\uff1f\u201d Wh- \u7591\u95ee\u53e5 + did + \u52a8\u8bcd\u539f\u5f62\u3002"),
     ("3. ", "go \u2192 went / swim \u2192 swam / fly \u2192 flew / stay \u2192 stayed \u2014 \u4e0d\u89c4\u5219\u52a8\u8bcd\u9700\u8981\u7279\u522b\u8bb0\u5fc6\u3002"),
     ("4. ", "Did you...? \u2192 Yes, I did. / No, I didn't. \u8fc7\u53bb\u65f6\u7591\u95ee\u53e5\u56de\u7b54\u683c\u5f0f\u56fa\u5b9a\u3002")],
    "A Wonderful Weekend",
    ["Last weekend, I had a wonderful time with my family.",
     "On Saturday morning, my father and I went to the park. We flew a kite in the open field.",
     "In the afternoon, my mother made delicious dumplings. I helped her in the kitchen.",
     "On Sunday, we visited my grandparents. My grandpa told me an interesting story.",
     "I also did my homework and read a book about animals. I learned a lot.",
     "I think my weekend was really great. I felt very happy!"],
    [["weekend", "/\u02ccwi\u02d0k\u02c8end/", "n. \u5468\u672b"],
     ["beach", "/bi\u02d0t\u0283/", "n. \u6d77\u6ee9"],
     ["kite", "/ka\u026at/", "n. \u98ce\u7b5d"],
     ["butterfly", "/\u02c8b\u028ct\u0259rfla\u026a/", "n. \u8774\u8776"],
     ["tired", "/ta\u026a\u0259rd/", "adj. \u7d2f\u7684\uff1b\u75b2\u52b3\u7684"]],
    [("camp", "/k\u00e6mp/", "v.", "\u91ce\u8425\uff1bn. \u8425\u5730",
      "We camped by the lake last weekend.", "We <strong>camped</strong> by the lake last weekend.",
      "\u6211\u4eec\u4e0a\u5468\u672b\u5728\u6e56\u8fb9\u91ce\u8425\u3002"),
     ("lake", "/le\u026ak/", "n.", "\u6e56\uff1b\u6e56\u6cca",
      "The lake was very beautiful.", "The <strong>lake</strong> was very beautiful.",
      "\u8fd9\u4e2a\u6e56\u975e\u5e38\u6f02\u4eae\u3002"),
     ("beach", "/bi\u02d0t\u0283/", "n.", "\u6d77\u6ee9\uff1b\u6d77\u6ee8",
      "We went to the beach on Sunday.", "We went to the <strong>beach</strong> on Sunday.",
      "\u6211\u4eec\u5468\u65e5\u53bb\u4e86\u6d77\u6ee9\u3002"),
     ("sheep", "/\u0283i\u02d0p/", "n.", "\u7f8a\uff1b\u7f8a\u7fa4\uff08\u590d\u6570 sheep\uff09",
      "The farmer has many sheep on the hill.", "The farmer has many <strong>sheep</strong> on the hill.",
      "\u519c\u6c11\u5728\u5c71\u4e0a\u6709\u8bb8\u591a\u7f8a\u3002"),
     ("kite", "/ka\u026at/", "n.", "\u98ce\u7b5d",
      "We flew a kite in the park.", "We flew a <strong>kite</strong> in the park.",
      "\u6211\u4eec\u5728\u516c\u56ed\u653e\u4e86\u98ce\u7b5d\u3002"),
     ("fly", "/fla\u026a/", "v.", "\u98de\u884c\uff1b\u653e\uff08\u98ce\u7b5d\uff09",
      "I flew a kite with my brother yesterday.", "I <strong>flew</strong> a kite with my brother yesterday.",
      "\u6211\u6628\u5929\u548c\u5f1f\u5f1f\u653e\u4e86\u98ce\u7b5d\u3002"),
     ("study", "/\u02c8st\u028cdi/", "v.", "\u5b66\u4e60\uff1b\u7814\u7a76",
      "I studied English for two hours last night.", "I <strong>studied</strong> English for two hours last night.",
      "\u6211\u6628\u665a\u5b66\u4e86\u4e24\u4e2a\u5c0f\u65f6\u82f1\u8bed\u3002"),
     ("natural", "/\u02c8n\u00e6t\u0283\u0259r\u0259l/", "adj.", "\u81ea\u7136\u7684",
      "We visited the natural history museum.", "We visited the <strong>natural</strong> history museum.",
      "\u6211\u4eec\u53c2\u89c2\u4e86\u81ea\u7136\u5386\u53f2\u535a\u7269\u9986\u3002"),
     ("visitor", "/\u02c8v\u026az\u026at\u0259r/", "n.", "\u8bbf\u5ba2\uff1b\u6e38\u5ba2",
      "Many visitors came to the museum every day.", "Many <strong>visitors</strong> came to the museum every day.",
      "\u6bcf\u5929\u6709\u8bb8\u591a\u6e38\u5ba2\u6765\u535a\u7269\u9986\u3002"),
     ("tired", "/ta\u026a\u0259rd/", "adj.", "\u7d2f\u7684\uff1b\u75b2\u52b3\u7684",
      "I was tired after the long walk.", "I was <strong>tired</strong> after the long walk.",
      "\u8d70\u4e86\u90a3\u4e48\u8fdc\u7684\u8def\uff0c\u6211\u5f88\u7d2f\u3002")],
    [(q("What did you do...?"), q("\u8be2\u95ee\u8fc7\u53bb\u7684\u6d3b\u52a8"),
      q('''\u2705 <strong>What did</strong> you <strong>do</strong> <span class="slot">last weekend</span>?<br>
      \u2705 I <strong>went</strong> to the beach. / I <strong>stayed</strong> at home.<br>
      \u2705 <strong>What did</strong> he <strong>do</strong> yesterday? He <strong>played</strong> soccer.''')),
     (q("Where / When / Who did...?"), q("\u5176\u4ed6 Wh- \u7591\u95ee\u53e5"),
      q('''\u2705 <strong>Where did</strong> you <strong>go</strong>? I <strong>went</strong> to the park.<br>
      \u2705 <strong>When did</strong> you <strong>get</strong> home? At five o'clock.<br>
      \u2705 <strong>Who did</strong> you <strong>meet</strong>? I <strong>met</strong> my friend Tom.''')),
     (q("\u4e0d\u89c4\u5219\u52a8\u8bcd\u8fc7\u53bb\u5f0f"), q("\u9700\u8981\u7279\u522b\u8bb0\u5fc6"),
      q('''\u2705 go -> <strong>went</strong>, do -> <strong>did</strong>, have -> <strong>had</strong><br>
      \u2705 fly -> <strong>flew</strong>, swim -> <strong>swam</strong>, make -> <strong>made</strong><br>
      \u2705 tell -> <strong>told</strong>, feel -> <strong>felt</strong>, buy -> <strong>bought</strong><br>
      \u2705 \u89c4\u5219\uff1astay -> <strong>stayed</strong>, watch -> <strong>watched</strong>, study -> <strong>studied</strong>''')),
     (q("last \u7528\u6cd5"), q("last + \u65f6\u95f4\u8868\u8fbe\u8fc7\u53bb"),
      q('''\u2705 <strong>last</strong> weekend / <strong>last</strong> night / <strong>last</strong> Friday<br>
      \u2705 <strong>last</strong> month / <strong>last</strong> year / <strong>last</strong> summer<br>
      \u27a1 yesterday / the day before yesterday / ... ago \u4e5f\u662f\u8fc7\u53bb\u65f6\u6807\u5fd7\u8bcd'''))],
    [(q("1\u20e3 \u4e00\u822c\u8fc7\u53bb\u65f6\u7591\u95ee\u53e5\u6982\u89c8"),
      q('''<p>\u7591\u95ee\u53e5\u7528 <strong>did</strong> \u63d0\u524d\uff0c\u52a8\u8bcd\u56de\u590d\u539f\u5f62\u3002</p>
      <table class="grammar-table">
        <tr><th>\u7591\u95ee\u8bcd</th><th>\u7ed3\u6784</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>What</td><td>What + did + \u4e3b + do?</td><td><span class="wotd-say" data-speak="What did you do last weekend?">What did you do last weekend?</span></td></tr>
        <tr><td>Where</td><td>Where + did + \u4e3b + go?</td><td><span class="wotd-say" data-speak="Where did you go?">Where did you go?</span></td></tr>
        <tr><td>Who</td><td>Who + did + \u4e3b + meet?</td><td><span class="wotd-say" data-speak="Who did you meet?">Who did you meet?</span></td></tr>
        <tr><td>When</td><td>When + did + \u4e3b + arrive?</td><td><span class="wotd-say" data-speak="When did you get home?">When did you get home?</span></td></tr>
      </table>''')),
     (q("2\u20e3 \u5e38\u89c1\u4e0d\u89c4\u5219\u52a8\u8bcd\u8fc7\u53bb\u5f0f\u6c47\u603b"),
      q('''<table class="grammar-table">
        <tr><th>\u539f\u5f62</th><th>\u8fc7\u53bb\u5f0f</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>do</td><td>did</td><td><span class="wotd-say" data-speak="I did my homework.">I <strong>did</strong> my homework.</span></td></tr>
        <tr><td>go</td><td>went</td><td><span class="wotd-say" data-speak="We went to the beach.">We <strong>went</strong> to the beach.</span></td></tr>
        <tr><td>fly</td><td>flew</td><td><span class="wotd-say" data-speak="He flew a kite.">He <strong>flew</strong> a kite.</span></td></tr>
        <tr><td>swim</td><td>swam</td><td><span class="wotd-say" data-speak="They swam in the sea.">They <strong>swam</strong> in the sea.</span></td></tr>
        <tr><td>tell</td><td>told</td><td><span class="wotd-say" data-speak="She told me a story.">She <strong>told</strong> me a story.</span></td></tr>
        <tr><td>feel</td><td>felt</td><td><span class="wotd-say" data-speak="I felt very happy.">I <strong>felt</strong> very happy.</span></td></tr>
      </table>
      <div class="chinese-error">
        <strong>\u26a0\ufe0f \u4e2d\u5f0f\u82f1\u8bed\u7ea0\u9519\uff1a</strong><br>
        \u274c <span class="wrong wotd-say" data-speak="I do my homework last night.">I do my homework last night.</span><br>
        \u2705 <span class="correct wotd-say" data-speak="I did my homework last night.">I <strong>did</strong> my homework last night.</span><br><br>
        \u274c <span class="wrong wotd-say" data-speak="Where you went yesterday?">Where you went yesterday?</span><br>
        \u2705 <span class="correct wotd-say" data-speak="Where did you go yesterday?">Where <strong>did</strong> you go yesterday?</span>
      </div>''')),
     (q("3\u20e3 \u65f6\u95f4\u6807\u5fd7\u8bcd\u4e0e\u8fc7\u53bb\u65f6"),
      q('''<p>\u8fc7\u53bb\u65f6\u5e38\u89c1\u7684\u65f6\u95f4\u6807\u5fd7\u8bcd\uff1a</p>
      <table class="grammar-table">
        <tr><th>\u65f6\u95f4\u6807\u5fd7\u8bcd</th><th>\u4f8b\u53e5</th></tr>
        <tr><td>yesterday</td><td><span class="wotd-say" data-speak="I visited the museum yesterday.">I visited the museum <strong>yesterday</strong>.</span></td></tr>
        <tr><td>last night / weekend / week</td><td><span class="wotd-say" data-speak="I watched TV last night.">I watched TV <strong>last night</strong>.</span></td></tr>
        <tr><td>... ago</td><td><span class="wotd-say" data-speak="I came here two years ago.">I came here <strong>two years ago</strong>.</span></td></tr>
        <tr><td>the day before yesterday</td><td><span class="wotd-say" data-speak="I went there the day before yesterday.">I went there <strong>the day before yesterday</strong>.</span></td></tr>
      </table>'''))],
    [("\u57fa\u7840", "\u2605\u2606\u2606", 1, 'What ____ you do last weekend? (do / did / does)', "did", "last weekend \u662f\u8fc7\u53bb\u65f6\u95f4\uff0c\u7591\u95ee\u53e5\u7528 did\u3002"),
     ("\u57fa\u7840", "\u2605\u2606\u2606", 2, 'I ____ (go) to the beach yesterday.', "went", "yesterday \u8868\u793a\u8fc7\u53bb\uff0cuse went\uff08go \u7684\u8fc7\u53bb\u5f0f\uff09\u3002"),
     ("\u57fa\u7840", "\u2605\u2606\u2606", 3, 'Did she ____ (watch) a movie? \u2014 Yes, she did.', "watch", "Did \u540e\u52a8\u8bcd\u7528\u539f\u5f62\u3002"),
     ("\u63d0\u5347", "\u2605\u2605\u2606", 4, '\u6539\u9519\uff1aWhere did you went last Sunday?', "Where did you go last Sunday?", "did \u540e\u5df2\u7ecf\u6807\u8bb0\u8fc7\u53bb\u65f6\uff0c\u52a8\u8bcd\u7528\u539f\u5f62\u3002"),
     ("\u63d0\u5347", "\u2605\u2605\u2606", 5, '\u8fde\u8bcd\u6210\u53e5\uff1adid / what / you / do / weekend / last', "What did you do last weekend?", "\u7591\u95ee\u53e5\u8bcd\u5e8f\uff1aWh- + did + \u4e3b\u8bed + \u52a8\u8bcd\u539f\u5f62\uff1f"),
     ("\u63d0\u5347", "\u2605\u2605\u2606", 6, '\u586b\u5165\u6b63\u786e\u7684\u8fc7\u53bb\u5f0f\uff1aWe ____ (fly) a kite and ____ (swim) in the pool.', "flew; swam", "fly\u2192flew\uff0cswim\u2192swam\uff0c\u90fd\u662f\u4e0d\u89c4\u5219\u52a8\u8bcd\u3002"),
     ("\u6311\u6218", "\u2605\u2605\u2605", 7, '\u6c49\u8bd1\u82f1\uff1a\u4f60\u4e0a\u5468\u672b\u505a\u4e86\u4ec0\u4e48\uff1f\u6211\u548c\u5bb6\u4eba\u53bb\u4e86\u6d77\u6ee9\uff0c\u5728\u6d77\u91cc\u6e38\u4e86\u6cf3\u3002', "What did you do last weekend? I went to the beach with my family and swam in the sea.", "\u7efc\u5408\u8fc7\u53bb\u65f6\u3010\u7591\u95ee\u53e5+ \u80af\u5b9a\u53e5\u3011\u8868\u8fbe\u3002"),
     ("\u6311\u6218", "\u2605\u2605\u2605", 8, '\u5bf9\u5212\u7ebf\u90e8\u5206\u63d0\u95ee\uff1aI went to the park <u>last Saturday</u>.<br>\u2192 ____ ____ you ____ to the park?', "When did; go", "\u5bf9\u65f6\u95f4\u63d0\u95ee\u7528 when\uff0c\u52a8\u8bcd\u7528\u539f\u5f62 go\u3002")],
    "\u7528\u4e00\u822c\u8fc7\u53bb\u65f6\u5199\u4e00\u6bb5\u5173\u4e8e\u4f60\u4e0a\u5468\u672b\u505a\u4e86\u4ec0\u4e48\u7684\u7ecf\u5386\u3002\u81f3\u5c116\u53e5\u8bdd\uff0c\u5305\u62ec\u5468\u516d\u548c\u5468\u65e5\u7684\u6d3b\u52a8\uff0c\u5e76\u8bf4\u8bf4\u4f60\u7684\u611f\u53d7\u3002",
    ["Last weekend, I did many interesting things.",
     "On Saturday morning, I stayed at home and did my homework. It was a little difficult.",
     "In the afternoon, I went to the library with my best friend. We read some storybooks.",
     "On Sunday, my family and I visited the Natural History Museum. I saw many dinosaur fossils.",
     "They were huge and amazing! I took a lot of photos there.",
     "I was tired but very happy. What a wonderful weekend!"],
    "\u4e0a\u5468\u672b\uff0c\u6211\u505a\u4e86\u5f88\u591a\u6709\u8da3\u7684\u4e8b\u60c5\u3002\u5468\u516d\u4e0a\u5348\uff0c\u6211\u5f85\u5728\u5bb6\u91cc\u505a\u4e86\u4f5c\u4e1a\uff0c\u6709\u70b9\u96be\u3002\u4e0b\u5348\uff0c\u6211\u548c\u6700\u597d\u7684\u670b\u53cb\u53bb\u4e86\u56fe\u4e66\u9986\uff0c\u6211\u4eec\u770b\u4e86\u4e00\u4e9b\u6545\u4e8b\u4e66\u3002\u5468\u65e5\uff0c\u6211\u548c\u5bb6\u4eba\u53c2\u89c2\u4e86\u81ea\u7136\u5386\u53f2\u535a\u7269\u9986\uff0c\u6211\u770b\u5230\u4e86\u5f88\u591a\u6050\u9f99\u5316\u77f3\u3002\u5b83\u4eec\u592a\u5e9e\u5927\u592a\u4ee4\u4eba\u9707\u60ca\u4e86\uff01\u6211\u62cd\u4e86\u5f88\u591a\u7167\u7247\u3002\u867d\u7136\u5f88\u7d2f\uff0c\u4f46\u975e\u5e38\u5f00\u5fc3\u3002\u591a\u4e48\u7f8e\u597d\u7684\u5468\u672b\u554a\uff01",
    ["\u6211\u80fd\u7528 What did you do last weekend? \u8be2\u95ee\u5468\u672b\u6d3b\u52a8",
     "\u6211\u80fd\u6b63\u786e\u4f7f\u7528\u4e0d\u89c4\u5219\u52a8\u8bcd\u7684\u8fc7\u53bb\u5f0f",
     "\u6211\u80fd\u7528 Wh- + did \u53e5\u578b\u63d0\u95ee",
     "\u6211\u80fd\u533a\u5206\u89c4\u5219\u548c\u4e0d\u89c4\u5219\u52a8\u8bcd\u8fc7\u53bb\u5f0f",
     "\u6211\u80fd\u7528\u4e00\u822c\u8fc7\u53bb\u65f6\u5199\u4e00\u6bb5\u5468\u672b\u7ecf\u5386"],
    "\u60f3\u8c61\u4f60\u662f\u4e00\u4e2a\u8bb0\u8005\uff0c\u7528\u82f1\u8bed\u91c7\u8bbf\u540c\u5b66\u4e0a\u5468\u672b\u505a\u4e86\u4ec0\u4e48\u3002\u7ec3\u4e60\uff1a\u201cWhat did you do last weekend? What time did you get up? Did you go out? How was your weekend?\u201d \u76f4\u5230\u80fd\u6d41\u5229\u5bf9\u8bdd\u3002",
    ["\U0001f535 1\u5929\u540e\uff1a\u590d\u4e60 Wh- + did \u7591\u95ee\u53e5\u578b",
     "\U0001f7e2 3\u5929\u540e\uff1a\u5199\u51fa go/do/swim/fly/tell \u7684\u8fc7\u53bb\u5f0f",
     "\U0001f7e1 1\u5468\u540e\uff1a\u80cc\u8bf5\u4e0d\u89c4\u5219\u52a8\u8bcd\u8fc7\u53bb\u5f0f\u8868",
     "\U0001f534 1\u6708\u540e\uff1a\u7528\u8fc7\u53bb\u65f6\u53e3\u8ff0\u4e00\u4e2a\u5468\u672b\u7ecf\u5386"],
    "\u4e0b\u4e00\u5355\u5143\uff1aUnit 1 \u4e03\u4e0a \u590d\u4e60",
    "\u8fd9\u662f\u4e03\u5e74\u7ea7\u4e0b\u518c\u6700\u540e\u4e00\u4e2a\u5355\u5143\u3002\u63a5\u4e0b\u6765\u8bf7\u56de\u5230\u4e03\u5e74\u7ea7\u4e0a\u518c Unit 1 \u8fdb\u884c\u5fa9\u4e60\u3002"
)
