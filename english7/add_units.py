#!/usr/bin/env python3
"""Add remaining unit data to english7_units.json"""
import json

with open("english7_units.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# U05
data["u05"] = {
    "num": 5,
    "title": "Do you have a soccer ball?",
    "subtitle": "谈论物品所属 \u00b7 一般现在时 have/has \u00b7 运动词汇",
    "topic": "Sports and games",
    "func": "Ownership \u00b7 Invitations \u00b7 Suggestions",
    "grammar": "Do/Does 一般疑问句 \u00b7 have/has 用法 \u00b7 Let's 祈使句",
    "writing": "描述自己和朋友的体育用品",
    "can_do": [
        "I can ask \u201cDo you have...?\u201d and answer about sports equipment.",
        "I can use \u201cLet's play...\u201d to make suggestions.",
        "I can use \u201cThat sounds...\u201d to give opinions.",
        "I can write about what sports things I have."
    ],
    "scene": "Frank \u548c Mike \u5728\u8ba8\u8bba\u5404\u81ea\u6709\u4ec0\u4e48\u7403\u7c7b\u7528\u54c1\uff0c\u5546\u91cf\u4e00\u8d77\u8fd0\u52a8\u3002",
    "dialogue": [
        ["Frank", "Mike, <em>do you have a soccer ball</em>?"],
        ["Mike", "No, I don't. But I have a basketball."],
        ["Frank", "Great! Let's play basketball!"],
        ["Mike", "That sounds good. <em>Do you have a basketball</em>?"],
        ["Frank", "Yes, I do. I have a basketball and a baseball, too."],
        ["Mike", "Wow! Do you have a baseball bat?"],
        ["Frank", "No, I don't. <em>Let's ask John</em>. He has one."],
        ["Mike", "OK! Let's go!"]
    ],
    "translation": [
        "Frank: Mike\uff0c<em>\u4f60\u6709\u4e00\u4e2a\u8db3\u7403\u5417</em>\uff1f",
        "Mike: \u4e0d\uff0c\u6211\u6ca1\u6709\u3002\u4f46\u6211\u6709\u4e00\u4e2a\u7bee\u7403\u3002",
        "Frank: \u592a\u597d\u4e86\uff01\u6211\u4eec\u53bb\u6253\u7bee\u7403\u5427\uff01",
        "Mike: \u542c\u8d77\u6765\u4e0d\u9519\u3002<em>\u4f60\u6709\u4e00\u4e2a\u7bee\u7403\u5417</em>\uff1f",
        "Frank: \u662f\u7684\uff0c\u6211\u6709\u3002\u6211\u6709\u4e00\u4e2a\u7bee\u7403\uff0c\u8fd8\u6709\u4e00\u4e2a\u68d2\u7403\u3002",
        "Mike: \u54c7\uff01\u4f60\u6709\u68d2\u7403\u68d2\u5417\uff1f",
        "Frank: \u4e0d\uff0c\u6211\u6ca1\u6709\u3002<em>\u6211\u4eec\u53bb\u95ee\u7ea6\u7ff0\u5427</em>\u3002\u4ed6\u6709\u4e00\u4e2a\u3002",
        "Mike: \u597d\u7684\uff01\u8d70\u5427\uff01"
    ],
    "key_points": [
        ["Do you have a soccer ball?", "\u4e00\u822c\u7591\u95ee\u53e5\u7528 <strong>Do</strong> \u5f00\u5934 + \u4e3b\u8bed + have + \u7269\u54c1\u3002\u56de\u7b54<strong>Yes, I do.</strong> / <strong>No, I don't.</strong>"],
        ["I don't have one.", "<strong>don't</strong> = do not\uff0c\u5426\u5b9a\u5f62\u5f0f\u3002\u7b2c\u4e09\u4eba\u79f0\u5355\u6570\u7528 <strong>doesn't have</strong>\u3002"],
        ["Let's play basketball!", "<strong>Let's</strong> = Let us\uff0c\u540e\u9762\u8ddf\u52a8\u8bcd\u539f\u5f62\u3002\u7528\u6765\u63d0\u51fa\u5efa\u8bae\u3002"],
        ["That sounds good.", "<strong>That sounds + \u5f62\u5bb9\u8bcd</strong>\u3002\u8868\u8fbe\u5bf9\u5efa\u8bae\u7684\u770b\u6cd5\u3002"]
    ],
    "reading_title": "Sports in Our Life",
    "reading_paras": [
        "Hi! I'm Frank. I like sports very much.",
        "I have a basketball and a baseball. I play basketball with my friends after school.",
        "My friend Mike doesn't have a soccer ball, but he has a volleyball.",
        "We often play volleyball on weekends. It is fun!",
        "Do you have a favorite sport? Let's play together!"
    ],
    "gloss": [
        ["sport", "/sp\u0254\u02d0rt/", "n.", "\u8fd0\u52a8"],
        ["play", "/ple\u026a/", "v.", "\u73a9\uff1b\u6253\uff08\u7403\uff09"],
        ["weekend", "/\u02c8wi\u02d0kend/", "n.", "\u5468\u672b"],
        ["together", "/t\u0259\u02c8\u0261e\u00f0\u0259r/", "adv.", "\u4e00\u8d77"]
    ],
    "vocab": [
        ["have", "/h\u00e6v/", "v.", "\u6709", "I have a new basketball.", "\u6211\u6709\u4e00\u4e2a\u65b0\u7bee\u7403\u3002"],
        ["soccer", "/\u02c8s\u0252k\u0259r/", "n.", "\u82f1\u5f0f\u8db3\u7403", "Do you play soccer?", "\u4f60\u8e22\u8db3\u7403\u5417\uff1f"],
        ["ball", "/b\u0254\u02d0l/", "n.", "\u7403", "The ball is under the chair.", "\u7403\u5728\u6905\u5b50\u4e0b\u9762\u3002"],
        ["tennis", "/\u02c8ten\u026as/", "n.", "\u7f51\u7403", "Tennis is an interesting sport.", "\u7f51\u7403\u662f\u6709\u8da3\u7684\u8fd0\u52a8\u3002"],
        ["basketball", "/\u02c8b\u00e6sk\u026atb\u0254\u02d0l/", "n.", "\u7bee\u7403", "Let's play basketball.", "\u6211\u4eec\u6253\u7bee\u7403\u5427\u3002"],
        ["volleyball", "/\u02c8v\u0251\u02d0lib\u0254\u02d0l/", "n.", "\u6392\u7403", "She has a volleyball.", "\u5979\u6709\u4e00\u4e2a\u6392\u7403\u3002"],
        ["baseball", "/\u02c8be\u026asb\u0254\u02d0l/", "n.", "\u68d2\u7403", "Baseball is popular in the US.", "\u68d2\u7403\u5728\u7f8e\u56fd\u5f88\u6d41\u884c\u3002"],
        ["bat", "/b\u00e6t/", "n.", "\u7403\u68d2\uff1b\u8759\u8760", "Where is the baseball bat?", "\u68d2\u7403\u68d2\u5728\u54ea\u91cc\uff1f"],
        ["racket", "/\u02c8r\u00e6k\u026at/", "n.", "\u7403\u62cd", "I need a tennis racket.", "\u6211\u9700\u8981\u7f51\u7403\u62cd\u3002"],
        ["let's", "/lets/", "abbr.", "\u8ba9\u6211\u4eec\uff08= let us\uff09", "Let's go to the playground.", "\u6211\u4eec\u53bb\u64cd\u573a\u5427\u3002"]
    ],
    "patterns": [
        ["Do you have + \u7269\u54c1?", "\u8be2\u95ee\u5bf9\u65b9\u662f\u5426\u6709\u67d0\u7269\u3002",
         "\u2705 <strong>Do you have</strong> <span class=\"slot\">a soccer ball</span>?<br>\n          \u27a1 Yes, I do. / No, I don't.<br>\n          \u2705 <strong>Does he have</strong> <span class=\"slot\">a basketball</span>?<br>\n          \u27a1 Yes, he does. / No, he doesn't."],
        ["Let's + \u52a8\u8bcd\u539f\u5f62 + \u5176\u4ed6.", "\u63d0\u51fa\u5efa\u8bae\u3002",
         "\u2705 <strong>Let's play</strong> <span class=\"slot\">basketball</span>!<br>\n          \u2705 <strong>Let's go</strong> <span class=\"slot\">to the park</span>!<br>\n          \u2705 <strong>Let's ask</strong> <span class=\"slot\">John</span>!"],
        ["That sounds + \u5f62\u5bb9\u8bcd.", "\u8868\u8fbe\u5bf9\u5efa\u8bae\u7684\u770b\u6cd5\u3002",
         "\u2705 That sounds <span class=\"slot\">good</span>.<br>\n          \u2705 That sounds <span class=\"slot\">interesting</span>.<br>\n          \u2705 That sounds <span class=\"slot\">boring</span>."],
        ["\u4e3b\u8bed + have / has + \u7269\u54c1.", "\u9648\u8ff0\u62e5\u6709\u67d0\u7269\u3002\u7b2c\u4e09\u4eba\u79f0\u5355\u6570\u7528 has\u3002",
         "\u2705 I <strong>have</strong> <span class=\"slot\">a basketball</span>.<br>\n          \u2705 She <strong>has</strong> <span class=\"slot\">a volleyball</span>.<br>\n          \u2705 He <strong>doesn't have</strong> <span class=\"slot\">a soccer ball</span>."]
    ],
    "grammar_tables": [
        ["1\u20e3 \u4e00\u822c\u73b0\u5728\u65f6 have / has",
         [["\u4e3b\u8bed", "\u80af\u5b9a\u53e5", "\u5426\u5b9a\u53e5", "\u7591\u95ee\u53e5"],
          ["I / You / We / They", "I have a ball.", "I don't have a ball.", "Do you have a ball?"],
          ["He / She / It", "She has a ball.", "She doesn't have a ball.", "Does she have a ball?"]],
         "\U0001f4cc <strong>\u6ce8\u610f\uff1a</strong>\u7b2c\u4e09\u4eba\u79f0\u5355\u6570\u7528 <strong>has</strong>\uff0c\u5426\u5b9a\u548c\u7591\u95ee\u7528 <strong>doesn't/Does</strong> + have\uff08\u8fd8\u539f\uff09\u3002"],
        ["2\u20e3 Do / Does \u95ee\u7b54\u5bf9\u6bd4",
         [["\u95ee\u53e5", "\u80af\u5b9a\u56de\u7b54", "\u5426\u5b9a\u56de\u7b54"],
          ["Do you have a pen?", "Yes, I do.", "No, I don't."],
          ["Does she have a pen?", "Yes, she does.", "No, she doesn't."],
          ["Do they have pens?", "Yes, they do.", "No, they don't."]],
         "\U0001f4cc <strong>\u52a9\u8bb0\uff1a</strong>Does \u7528\u4e8e he/she/it\uff0c\u540e\u9762\u52a8\u8bcd\u53d8\u56de\u539f\u5f62\u3002",
         [
            ["Does he has a basketball?", "Does he have a basketball?"],
            ["He don't have a soccer ball.", "He doesn't have a soccer ball."],
            ["Do she have a volleyball?", "Does she have a volleyball?"]
         ]],
        ["3\u20e3 Let's \u7948\u4f7f\u53e5",
         [["\u7ed3\u6784", "\u793a\u4f8b", "\u56de\u7b54"],
          ["Let's + \u52a8\u8bcd\u539f\u5f62", "Let's play tennis.", "That sounds good."],
          ["Let's + \u52a8\u8bcd\u539f\u5f62 + \u5730\u70b9", "Let's go to the park.", "OK. Let's go!"],
          ["\u5426\u5b9a\uff1aLet's not + \u52a8\u8bcd\u539f\u5f62", "Let's not be late.", "You're right."]],
         "\U0001f4cc Let's = Let us\uff0c\u8868\u793a\u5efa\u8bae\u3002\u56de\u7b54\u53ef\u4ee5\u7528 That sounds good / interesting / boring."]
    ],
    "exercises": [
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ you have a basketball? (Do / Does / Are)", "Do", "you \u4e3a\u7b2c\u4e8c\u4eba\u79f0\uff0c\u7528 Do \u63d0\u95ee\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "She ____ (have) a volleyball.", "has", "\u7b2c\u4e09\u4eba\u79f0\u5355\u6570\u7528 has\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "Let's ____ (play) soccer!", "play", "Let's \u540e\u8ddf\u52a8\u8bcd\u539f\u5f62\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u2014 Do you have a tennis racket?<br>\u2014 No, I ____. But my brother ____ one.", "don't; has", "\u5426\u5b9a don't\uff1bbrother \u7b2c\u4e09\u4eba\u79f0\u5355\u6570 has\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u8fde\u8bcd\u6210\u53e5\uff1asounds / that / fun / !", "That sounds fun!", "That sounds + \u5f62\u5bb9\u8bcd\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6539\u9519\uff1aHe don't play soccer.", "He doesn't play soccer.", "\u7b2c\u4e09\u4eba\u79f0\u5355\u6570\u5426\u5b9a\u7528 doesn't + \u52a8\u8bcd\u539f\u5f62\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u8865\u5168\u5bf9\u8bdd\uff1a<br>A: ____ you have a baseball bat?<br>B: No, I ____. But Mike ____ one.<br>A: Let's ____ him!", "Do; don't; has; ask", "\u4e00\u822c\u7591\u95ee\u53e5 Do\uff1b\u5426\u5b9a don't\uff1b\u7b2c\u4e09\u4eba\u79f0 has\uff1bLet's + \u52a8\u8bcd\u539f\u5f62\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u6c49\u8bd1\u82f1\uff1a\u6211\u54e5\u54e5\u6709\u4e00\u4e2a\u7bee\u7403\u3002\u4ed6\u6ca1\u6709\u8db3\u7403\uff0c\u4f46\u4ed6\u6709\u6392\u7403\u3002", "My brother has a basketball. He doesn't have a soccer ball, but he has a volleyball.", "\u7b2c\u4e09\u4eba\u79f0 has \u548c doesn't have\u3002"]
    ],
    "micro_task": "\u5199\u4e00\u6bb5\u8bdd\uff0c\u4ecb\u7ecd\u4f60\u548c\u4f60\u7684\u670b\u53cb\u6709\u4ec0\u4e48\u4f53\u80b2\u7528\u54c1\uff0c\u4ee5\u53ca\u4f60\u4eec\u559c\u6b22\u4e00\u8d77\u505a\u4ec0\u4e48\u8fd0\u52a8\u3002",
    "model_paras": [
        "I have a basketball and a tennis racket.",
        "My friend Mike doesn't have a basketball, but he has a volleyball.",
        "We often play volleyball together. It is fun!",
        "Does Mike have a baseball? No, he doesn't. But I have a baseball bat.",
        "Let's play sports every day!"
    ],
    "model_trans": "\u6211\u6709\u4e00\u4e2a\u7bee\u7403\u548c\u4e00\u4e2a\u7f51\u7403\u62cd\u3002\u6211\u7684\u670b\u53cb Mike \u6ca1\u6709\u7bee\u7403\uff0c\u4f46\u4ed6\u6709\u4e00\u4e2a\u6392\u7403\u3002\u6211\u4eec\u7ecf\u5e38\u4e00\u8d77\u6253\u6392\u7403\u3002Mike \u6709\u68d2\u7403\u5417\uff1f\u4e0d\uff0c\u4ed6\u6ca1\u6709\u3002\u4f46\u6211\u6709\u68d2\u7403\u68d2\u3002\u8ba9\u6211\u4eec\u6bcf\u5929\u8fd0\u52a8\u5427\uff01",
    "checklist": [
        "\u6211\u80fd\u7528 Do you have...? \u63d0\u95ee\u5e76\u56de\u7b54",
        "\u6211\u80fd\u533a\u5206 have \u548c has \u7684\u4e0d\u540c\u7528\u6cd5",
        "\u6211\u80fd\u7528 Let's... \u63d0\u51fa\u5efa\u8bae",
        "\u6211\u80fd\u7528 That sounds... \u8868\u8fbe\u770b\u6cd5",
        "\u6211\u80fd\u7b80\u5355\u4ecb\u7ecd\u81ea\u5df1\u548c\u670b\u53cb\u7684\u4f53\u80b2\u7528\u54c1"
    ],
    "feynman": "\u8ddf\u540c\u5b66\u6765\u4e00\u573a\u82f1\u8bed\u5bf9\u8bdd\u2014\u2014\u201cDo you have a soccer ball? Let's play together!\u201d",
    "review": [
        "\U0001f535 1\u5929\u540e\uff1a\u7528 Do you have...? \u95ee5\u4e2a\u540c\u5b66\u6709\u4ec0\u4e48\u7403\u7c7b",
        "\U0001f7e2 3\u5929\u540e\uff1a\u5199\u4e00\u6bb5\u81ea\u5df1\u548c\u670b\u53cb\u7684\u8fd0\u52a8\u7231\u597d",
        "\U0001f7e1 1\u5468\u540e\uff1a\u7528 Let's \u63d0\u51fa\u5efa\u8bae\uff0c\u4e0e\u540c\u5b66\u505a\u82f1\u8bed\u5bf9\u8bdd\u7ec3\u4e60",
        "\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60 have/has \u7684\u4e00\u822c\u73b0\u5728\u65f6\u8868\u683c"
    ],
    "next_unit": 6,
    "next_title": "Do you like bananas?",
    "next_desc": "\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u7528 <strong>Do you like...?</strong> \u8c08\u8bba\u559c\u6b22\u7684\u98df\u7269\uff0c\u533a\u5206\u53ef\u6570\u548c\u4e0d\u53ef\u6570\u540d\u8bcd\uff01"
}

# U06
data["u06"] = {
    "num": 6,
    "title": "Do you like bananas?",
    "subtitle": "\u8c08\u8bba\u98df\u7269\u559c\u597d \u00b7 \u53ef\u6570/\u4e0d\u53ef\u6570\u540d\u8bcd \u00b7 like \u7528\u6cd5",
    "topic": "Food and eating habits",
    "func": "Express likes and dislikes",
    "grammar": "like \u4e00\u822c\u73b0\u5728\u65f6 \u00b7 \u53ef\u6570/\u4e0d\u53ef\u6570\u540d\u8bcd \u00b7 some/any",
    "writing": "\u63cf\u8ff0\u81ea\u5df1\u7684\u4e00\u65e5\u4e09\u9910\u996e\u98df",
    "can_do": [
        "I can ask \u201cDo you like...?\u201d about food.",
        "I can say what I like and don't like.",
        "I can distinguish countable and uncountable nouns.",
        "I can write about what I eat for three meals."
    ],
    "scene": "\u5348\u9910\u65f6\u95f4\uff0cAnna \u548c Ben \u5728\u98df\u5802\u8ba8\u8bba\u5404\u81ea\u559c\u6b22\u548c\u4e0d\u559c\u6b22\u7684\u98df\u7269\u3002",
    "dialogue": [
        ["Anna", "Ben, <em>do you like bananas</em>?"],
        ["Ben", "Yes, I do. I like fruit very much."],
        ["Anna", "Do you like hamburgers?"],
        ["Ben", "No, <em>I don't like hamburgers</em>. They are unhealthy."],
        ["Anna", "What about salad? <em>Do you like salad</em>?"],
        ["Ben", "Yes, I like salad. It's healthy and delicious."],
        ["Anna", "Let's get some salad for lunch!"],
        ["Ben", "Great! I like chicken salad best."]
    ],
    "translation": [
        "Anna: Ben\uff0c<em>\u4f60\u559c\u6b22\u9999\u8549\u5417</em>\uff1f",
        "Ben: \u662f\u7684\uff0c\u6211\u559c\u6b22\u3002\u6211\u975e\u5e38\u559c\u6b22\u6c34\u679c\u3002",
        "Anna: \u4f60\u559c\u6b22\u6c49\u5821\u5305\u5417\uff1f",
        "Ben: \u4e0d\uff0c<em>\u6211\u4e0d\u559c\u6b22\u6c49\u5821\u5305</em>\u3002\u5b83\u4eec\u4e0d\u5065\u5eb7\u3002",
        "Anna: \u6c99\u62c9\u5462\uff1f<em>\u4f60\u559c\u6b22\u6c99\u62c9\u5417</em>\uff1f",
        "Ben: \u662f\u7684\uff0c\u6211\u559c\u6b22\u6c99\u62c9\u3002\u5b83\u53c8\u5065\u5eb7\u53c8\u7f8e\u5473\u3002",
        "Anna: \u6211\u4eec\u5348\u996d\u4e70\u4e9b\u6c99\u62c9\u5427\uff01",
        "Ben: \u592a\u68d2\u4e86\uff01\u6211\u6700\u559c\u6b22\u9e21\u8089\u6c99\u62c9\u3002"
    ],
    "key_points": [
        ["Do you like bananas?", "\u8be2\u95ee\u559c\u597d\u3002<strong>Do + \u4e3b\u8bed + like + \u98df\u7269?</strong> \u56de\u7b54\uff1a<strong>Yes, I do.</strong> / <strong>No, I don't.</strong>"],
        ["I don't like hamburgers.", "<strong>don't like</strong> = do not like\uff0c\u8868\u793a\u201c\u4e0d\u559c\u6b22\u201d\u3002\u7b2c\u4e09\u4eba\u79f0\u7528 <strong>doesn't like</strong>\u3002"],
        ["I like fruit very much.", "<strong>like + \u98df\u7269</strong> \u8868\u793a\u559c\u6b22\u67d0\u7269\u3002\u53ef\u6570\u540d\u8bcd\u590d\u6570\u8868\u793a\u4e00\u7c7b\u4e8b\u7269\uff0c\u4e0d\u53ef\u6570\u540d\u8bcd\u76f4\u63a5\u7528\u539f\u5f62\u3002"],
        ["Let's get some salad.", "<strong>some</strong> \u7528\u4e8e\u80af\u5b9a\u53e5\u4e2d\u8868\u793a\u201c\u4e00\u4e9b\u201d\u3002<strong>any</strong> \u7528\u4e8e\u5426\u5b9a\u548c\u7591\u95ee\u53e5\u4e2d\u3002"]
    ],
    "reading_title": "My Eating Habits",
    "reading_paras": [
        "Hello! I'm Anna. Let me tell you about my eating habits.",
        "For breakfast, I like eggs and milk. I don't like bread for breakfast.",
        "For lunch, I like rice, chicken and vegetables. Salad is my favorite.",
        "For dinner, I usually have noodles or porridge. I like fruit after dinner.",
        "I eat healthy food every day. I don't eat too much junk food."
    ],
    "gloss": [
        ["habit", "/\u02c8h\u00e6b\u026at/", "n.", "\u4e60\u60ef"],
        ["breakfast", "/\u02c8brekf\u0259st/", "n.", "\u65e9\u9910"],
        ["lunch", "/l\u028cnt\u0283/", "n.", "\u5348\u9910"],
        ["dinner", "/\u02c8d\u026an\u0259r/", "n.", "\u665a\u9910"],
        ["healthy", "/\u02c8hel\u03b8i/", "adj.", "\u5065\u5eb7\u7684"]
    ],
    "vocab": [
        ["like", "/la\u026ak/", "v.", "\u559c\u6b22", "I like apples very much.", "\u6211\u975e\u5e38\u559c\u6b22\u82f9\u679c\u3002"],
        ["banana", "/b\u0259\u02c8n\u00e6n\u0259/", "n.", "\u9999\u8549", "Do you like bananas?", "\u4f60\u559c\u6b22\u9999\u8549\u5417\uff1f"],
        ["hamburger", "/\u02c8h\u00e6mb\u025c\u02d0r\u0261\u0259r/", "n.", "\u6c49\u5821\u5305", "Hamburgers are not healthy.", "\u6c49\u5821\u5305\u4e0d\u5065\u5eb7\u3002"],
        ["tomato", "/t\u0259\u02c8me\u026ato\u028a/", "n.", "\u897f\u7ea2\u67ff", "I like tomato and egg soup.", "\u6211\u559c\u6b22\u897f\u7ea2\u67ff\u86cb\u6c64\u3002"],
        ["salad", "/\u02c8s\u00e6l\u0259d/", "n.", "\u6c99\u62c9", "Fruit salad is delicious.", "\u6c34\u679c\u6c99\u62c9\u5f88\u597d\u5403\u3002"],
        ["chicken", "/\u02c8t\u0283\u026ak\u026an/", "n.", "\u9e21\uff1b\u9e21\u8089", "Chicken is my favorite meat.", "\u9e21\u8089\u662f\u6211\u6700\u559c\u6b22\u7684\u8089\u3002"],
        ["rice", "/ra\u026as/", "n.", "\u7c73\u996d", "We eat rice for lunch.", "\u6211\u4eec\u5348\u996d\u5403\u7c73\u996d\u3002"],
        ["fruit", "/fru\u02d0t/", "n.", "\u6c34\u679c", "I like all kinds of fruit.", "\u6211\u559c\u6b22\u5404\u79cd\u6c34\u679c\u3002"],
        ["breakfast", "/\u02c8brekf\u0259st/", "n.", "\u65e9\u9910", "I have eggs for breakfast.", "\u6211\u65e9\u996d\u5403\u9e21\u86cb\u3002"],
        ["bread", "/bred/", "n.", "\u9762\u5305", "Would you like some bread?", "\u4f60\u60f3\u8981\u4e9b\u9762\u5305\u5417\uff1f"]
    ],
    "patterns": [
        ["Do you like + \u98df\u7269?", "\u8be2\u95ee\u5bf9\u65b9\u662f\u5426\u559c\u6b22\u67d0\u79cd\u98df\u7269\u3002",
         "\u2705 <strong>Do you like</strong> <span class=\"slot\">bananas</span>?<br>\n          \u2705 <strong>Does she like</strong> <span class=\"slot\">salad</span>?<br>\n          \u27a1 Yes, I do. / No, she doesn't."],
        ["I like + \u98df\u7269. / I don't like + \u98df\u7269.", "\u8868\u8fbe\u81ea\u5df1\u7684\u559c\u597d\u3002",
         "\u2705 I <strong>like</strong> <span class=\"slot\">fruit</span>.<br>\n          \u2705 I <strong>don't like</strong> <span class=\"slot\">hamburgers</span>.<br>\n          \u27a1 \u7b2c\u4e09\u4eba\u79f0\uff1a<strong>He likes</strong> salad. / <strong>She doesn't like</strong> meat."],
        ["What about + \u540d\u8bcd/\u52a8\u540d\u8bcd?", "\u63d0\u51fa\u5efa\u8bae\u6216\u8be2\u95ee\u5bf9\u65b9\u610f\u89c1\u3002",
         "\u2705 <strong>What about</strong> <span class=\"slot\">salad</span>?<br>\n          \u2705 <strong>What about</strong> <span class=\"slot\">playing tennis</span>?<br>\n          \u27a1 \u7b49\u4e8e How about...?"],
        ["Let's have / get + \u98df\u7269.", "\u63d0\u8bae\u5403\u67d0\u79cd\u98df\u7269\u3002",
         "\u2705 <strong>Let's have</strong> <span class=\"slot\">some rice</span>.<br>\n          \u2705 <strong>Let's get</strong> <span class=\"slot\">some fruit</span>.<br>\n          \u27a1 \u80af\u5b9a\u53e5\u7528 some\uff0c\u5426\u5b9a/\u7591\u95ee\u7528 any\u3002"]
    ],
    "grammar_tables": [
        ["1\u20e3 like \u7684\u4e00\u822c\u73b0\u5728\u65f6",
         [["\u4e3b\u8bed", "\u80af\u5b9a\u53e5", "\u5426\u5b9a\u53e5", "\u7591\u95ee\u53e5"],
          ["I / You / We / They", "I like apples.", "I don't like apples.", "Do you like apples?"],
          ["He / She / It", "She likes apples.", "She doesn't like apples.", "Does she like apples?"]],
         "\U0001f4cc \u7b2c\u4e09\u4eba\u79f0\u5355\u6570 <strong>like \u2192 likes</strong>\uff1b\u5426\u5b9a\u7528 doesn't like\uff1b\u7591\u95ee\u7528 Does...like\u3002"],
        ["2\u20e3 \u53ef\u6570\u540d\u8bcd vs \u4e0d\u53ef\u6570\u540d\u8bcd",
         [["\u7c7b\u578b", "\u7279\u70b9", "\u793a\u4f8b"],
          ["\u53ef\u6570\u540d\u8bcd (C)", "\u6709\u5355\u590d\u6570\u5f62\u5f0f\uff1b\u53ef\u7528 a/an", "a banana, two bananas, an apple"],
          ["\u4e0d\u53ef\u6570\u540d\u8bcd (U)", "\u6ca1\u6709\u590d\u6570\u5f62\u5f0f\uff1b\u4e0d\u7528 a/an", "rice, bread, milk, salad"],
          ["\u4fee\u9970\u8bcd", "\u53ef\u6570\u7528 many / a few", "many bananas, a few eggs"],
          ["\u4fee\u9970\u8bcd", "\u4e0d\u53ef\u6570\u7528 much / a little", "much rice, a little milk"]],
         "\U0001f4cc <strong>\u5bf9\u6bd4\uff1a</strong>I like <strong>bananas</strong>\uff08\u53ef\u6570\u590d\u6570\u8868\u7c7b\u522b\uff09. I like <strong>rice</strong>\uff08\u4e0d\u53ef\u6570\u7528\u539f\u5f62\uff09."]
    ],
    "exercises": [
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ you like salad? (Do / Does / Are)", "Do", "you \u524d\u7528 Do \u63d0\u95ee\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "She ____ (like) bananas.", "likes", "\u7b2c\u4e09\u4eba\u79f0\u5355\u6570 likes\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "I don't like ____ (hamburger).", "hamburgers", "\u53ef\u6570\u540d\u8bcd\u8868\u7c7b\u522b\u7528\u590d\u6570\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u2014 Do you like milk?<br>\u2014 Yes, I ____. I ____ milk every morning.", "do; drink/have", "\u80af\u5b9a\u56de\u7b54 do\uff1b\u6bcf\u5929\u559d milk\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6539\u9519\uff1aHe like chicken very much.", "He likes chicken very much.", "\u7b2c\u4e09\u4eba\u79f0\u5355\u6570\u52a8\u8bcd\u52a0 -s\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6c49\u8bd1\u82f1\uff1a\u6211\u4e0d\u559c\u6b22\u9762\u5305\u3002\u4f46\u6211\u7684\u59b9\u59b9\u559c\u6b22\u3002", "I don't like bread. But my sister likes it.", "don't like\uff1bsister \u7b2c\u4e09\u4eba\u79f0 likes\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u8865\u5168\u5bf9\u8bdd\uff1a<br>A: ____ your brother like ice-cream?<br>B: Yes, he ____. But he ____ (not like) candy.", "Does; does; doesn't like", "brother \u7b2c\u4e09\u4eba\u79f0 Does\uff1b\u80af\u5b9a does\uff1b\u5426\u5b9a doesn't like\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u7528\u6240\u7ed9\u8bcd\u586b\u7a7a\uff08\u53ef\u6570/\u4e0d\u53ef\u6570\uff09\uff1a<br>I eat ____ rice for lunch. My sister eats ____ fruit every day.", "some/much; much", "rice \u4e0d\u53ef\u6570\u7528 much/some\uff1bfruit \u4e0d\u53ef\u6570\u7528 much\u3002"]
    ],
    "micro_task": "\u5199\u4e00\u6bb5\u8bdd\u4ecb\u7ecd\u4f60\u4e00\u65e5\u4e09\u9910\u7684\u996e\u98df\u559c\u597d\uff0c\u8bf4\u660e\u559c\u6b22\u548c\u4e0d\u559c\u6b22\u4ec0\u4e48\u3002",
    "model_paras": [
        "Hi! I'm Tom. Let me tell you about my three meals.",
        "For breakfast, I like milk and eggs. I don't like bread.",
        "For lunch, I like rice, chicken and vegetables. Salad is great!",
        "For dinner, I usually have noodles. I like fruit after dinner.",
        "I try to eat healthy food every day."
    ],
    "model_trans": "\u55e8\uff01\u6211\u662f Tom\u3002\u8ba9\u6211\u6765\u4ecb\u7ecd\u6211\u7684\u4e09\u9910\u3002\u65e9\u9910\u6211\u559c\u6b22\u725b\u5976\u548c\u9e21\u86cb\u3002\u6211\u4e0d\u559c\u6b22\u9762\u5305\u3002\u5348\u9910\u6211\u559c\u6b22\u7c73\u996d\u3001\u9e21\u8089\u548c\u852c\u83dc\u3002\u6c99\u62c9\u5f88\u4e0d\u9519\uff01\u665a\u9910\u6211\u901a\u5e38\u5403\u9762\u6761\u3002\u6211\u559c\u6b22\u996d\u540e\u5403\u6c34\u679c\u3002\u6211\u5c3d\u91cf\u6bcf\u5929\u5403\u5065\u5eb7\u7684\u98df\u7269\u3002",
    "checklist": [
        "\u6211\u80fd\u7528 Do you like...? \u8be2\u95ee\u5bf9\u98df\u7269\u7684\u559c\u597d",
        "\u6211\u80fd\u7528 like / don't like \u8868\u8fbe\u4e2a\u4eba\u559c\u597d",
        "\u6211\u80fd\u533a\u5206\u53ef\u6570\u540d\u8bcd\u548c\u4e0d\u53ef\u6570\u540d\u8bcd",
        "\u6211\u80fd\u7406\u89e3 some \u548c any \u7684\u57fa\u672c\u7528\u6cd5",
        "\u6211\u80fd\u5199\u4e00\u6bb5\u8bdd\u4ecb\u7ecd\u81ea\u5df1\u7684\u996e\u98df\u4e60\u60ef"
    ],
    "feynman": "\u7528\u82f1\u8bed\u8bf4\u51fa\u4f60\u4e00\u65e5\u4e09\u9910\u5403\u4ec0\u4e48\u2014\u2014\u201cFor breakfast, I like eggs and milk...\u201d",
    "review": [
        "\U0001f535 1\u5929\u540e\uff1a\u7528 Do you like...? \u95ee\u5bb6\u4eba\u559c\u6b22\u4ec0\u4e48\u98df\u7269",
        "\U0001f7e2 3\u5929\u540e\uff1a\u9ed8\u519910\u4e2a\u98df\u54c1\u5355\u8bcd\u5e76\u6807\u6ce8\u53ef\u6570/\u4e0d\u53ef\u6570",
        "\U0001f7e1 1\u5468\u540e\uff1a\u5199\u4e00\u7bc7 My Eating Habits \u5c0f\u77ed\u6587",
        "\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60 like \u4e00\u822c\u73b0\u5728\u65f6\u8868\u683c\u548c\u540d\u8bcd\u5206\u7c7b"
    ],
    "next_unit": 7,
    "next_title": "How much are these socks?",
    "next_desc": "\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u8d2d\u7269\u573a\u666f\u7684\u8868\u8fbe\u2014\u2014<strong>How much is/are...?</strong> \u95ee\u4ef7\u683c\uff0c\u8fd8\u4f1a\u5b66\u5230\u8863\u7269\u7684\u82f1\u6587\u540d\u79f0\uff01"
}

# U07
data["u07"] = {
    "num": 7,
    "title": "How much are these socks?",
    "subtitle": "\u8d2d\u7269\u5bf9\u8bdd \u00b7 \u8be2\u95ee\u4ef7\u683c \u00b7 \u8863\u7269\u540d\u8bcd \u00b7 \u6307\u793a\u4ee3\u8bcd",
    "topic": "Shopping and clothes",
    "func": "Ask about prices \u00b7 Buy and sell",
    "grammar": "How much \u95ee\u53e5 \u00b7 \u6307\u793a\u4ee3\u8bcd + \u540d\u8bcd \u00b7 \u5f62\u5bb9\u8bcd\u63cf\u8ff0",
    "writing": "\u5199\u4e00\u5219\u4fc3\u9500\u5e7f\u544a",
    "can_do": [
        "I can ask \u201cHow much is/are...?\u201d about prices.",
        "I can use this/that/these/those with clothes.",
        "I can use color and size adjectives.",
        "I can write a simple store ad."
    ],
    "scene": "Linda \u5728\u4e00\u5bb6\u670d\u88c5\u5e97\u8d2d\u7269\uff0c\u5e97\u5458\u5728\u5e2e\u5979\u3002",
    "dialogue": [
        ["Clerk", "Welcome to our store! <em>Can I help you</em>?"],
        ["Linda", "Yes, please. I need a sweater for school."],
        ["Linda", "<em>How much is this red sweater</em>?"],
        ["Clerk", "It's 68 dollars."],
        ["Linda", "Oh, it's expensive. Do you have a cheaper one?"],
        ["Clerk", "Yes. <em>How about this blue one</em>? It's 45 dollars."],
        ["Linda", "Great! And how much are these socks?"],
        ["Clerk", "They're 5 dollars for three pairs."],
        ["Linda", "OK, I'll take them!"]
    ],
    "translation": [
        "\u5e97\u5458\uff1a\u6b22\u8fce\u5149\u4e34\uff01<em>\u6211\u80fd\u5e2e\u4f60\u5417</em>\uff1f",
        "Linda: \u662f\u7684\u3002\u6211\u9700\u8981\u4e00\u4ef6\u4e0a\u5b66\u7a7f\u7684\u6bdb\u8863\u3002",
        "Linda: <em>\u8fd9\u4ef6\u7ea2\u6bdb\u8863\u591a\u5c11\u94b1</em>\uff1f",
        "\u5e97\u5458\uff1a68\u7f8e\u5143\u3002",
        "Linda: \u54e6\uff0c\u592a\u8d35\u4e86\u3002\u6709\u4fbf\u5b9c\u4e00\u70b9\u7684\u5417\uff1f",
        "\u5e97\u5458\uff1a\u6709\u3002<em>\u8fd9\u4ef6\u84dd\u8272\u7684\u600e\u4e48\u6837</em>\uff1f45\u7f8e\u5143\u3002",
        "Linda: \u592a\u597d\u4e86\uff01\u8fd9\u4e9b\u889c\u5b50\u591a\u5c11\u94b1\uff1f",
        "\u5e97\u5458\uff1a5\u7f8e\u5143\u4e09\u53cc\u3002",
        "Linda: \u597d\u7684\uff0c\u6211\u4e70\u4e86\uff01"
    ],
    "key_points": [
        ["Can I help you?", "\u8d2d\u7269\u65f6\u5e97\u5458\u7684\u5e38\u7528\u8bed\u3002\u4e5f\u53ef\u4ee5\u8bf4 What can I do for you?"],
        ["How much is this red sweater?", "\u95ee\u4ef7\u683c\u7528 <strong>How much is/are...?</strong> \u5355\u6570\u7528 is\uff0c\u590d\u6570\u7528 are\u3002\u56de\u7b54 It's / They're + \u4ef7\u683c\u3002"],
        ["How about this blue one?", "<strong>How about...?</strong> \u63d0\u51fa\u5efa\u8bae\u6216\u63a8\u8350\u3002<strong>one</strong> \u4ee3\u66ff\u524d\u9762\u63d0\u5230\u7684\u5355\u6570\u540d\u8bcd\u3002"],
        ["I'll take it/them.", "<strong>I'll take it/them.</strong> = \u201c\u6211\u4e70\u4e86\u201d \u8d2d\u7269\u51b3\u5b9a\u8d2d\u4e70\u65f6\u7684\u5e38\u7528\u8868\u8fbe\u3002"]
    ],
    "reading_title": "A Big Sale!",
    "reading_paras": [
        "Welcome to Fashion Store! We have a big sale this weekend.",
        "Do you need sweaters? We have red, blue and white sweaters for only 45 dollars.",
        "How much are our T-shirts? They are 20 dollars for one and 35 dollars for two.",
        "Socks are only 3 dollars for two pairs. Shoes are 55 dollars.",
        "Come to our store now! You will find great things at good prices!"
    ],
    "gloss": [
        ["sale", "/se\u026al/", "n.", "\u7279\u5356\uff1b\u9500\u552e"],
        ["need", "/ni\u02d0d/", "v.", "\u9700\u8981"],
        ["only", "/\u02c8o\u028anli/", "adv.", "\u53ea\u8981\uff1b\u4ec5\u4ec5"],
        ["price", "/pra\u026as/", "n.", "\u4ef7\u683c"]
    ],
    "vocab": [
        ["how much", "/ha\u028a m\u028ct\u0283/", "phrase.", "\u591a\u5c11\u94b1", "How much is this shirt?", "\u8fd9\u4ef6\u886c\u886b\u591a\u5c11\u94b1\uff1f"],
        ["socks", "/s\u0252ks/", "n.", "\u889c\u5b50\uff08\u590d\u6570\uff09", "These socks are cheap.", "\u8fd9\u4e9b\u889c\u5b50\u5f88\u4fbf\u5b9c\u3002"],
        ["shoes", "/\u0283u\u02d0z/", "n.", "\u978b\u5b50\uff08\u590d\u6570\uff09", "The shoes are 55 dollars.", "\u8fd9\u53cc\u978b55\u7f8e\u5143\u3002"],
        ["shirt", "/\u0283\u025c\u02d0rt/", "n.", "\u886c\u886b", "I need a white shirt.", "\u6211\u9700\u8981\u4e00\u4ef6\u767d\u886c\u886b\u3002"],
        ["shorts", "/\u0283\u0254\u02d0rts/", "n.", "\u77ed\u88e4\uff08\u590d\u6570\uff09", "The shorts are on sale.", "\u77ed\u88e4\u5728\u6253\u6298\u3002"],
        ["sweater", "/\u02c8swet\u0259r/", "n.", "\u6bdb\u8863", "This sweater is very warm.", "\u8fd9\u4ef6\u6bdb\u8863\u5f88\u6696\u548c\u3002"],
        ["skirt", "/sk\u025c\u02d0rt/", "n.", "\u88d9\u5b50", "How much is that skirt?", "\u90a3\u6761\u88d9\u5b50\u591a\u5c11\u94b1\uff1f"],
        ["dollar", "/\u02c8d\u0252l\u0259r/", "n.", "\u7f8e\u5143", "It is only 10 dollars.", "\u53ea\u898110\u7f8e\u5143\u3002"],
        ["big", "/b\u026a\u0261/", "adj.", "\u5927\u7684", "I need a big bag.", "\u6211\u9700\u8981\u4e00\u4e2a\u5927\u5305\u3002"],
        ["small", "/sm\u0254\u02d0l/", "adj.", "\u5c0f\u7684", "The small size is fine.", "\u5c0f\u53f7\u5c31\u53ef\u4ee5\u4e86\u3002"]
    ],
    "patterns": [
        ["How much is/are + \u7269\u54c1?", "\u8be2\u95ee\u4ef7\u683c\u3002\u5355\u6570\u7528 is\uff0c\u590d\u6570\u7528 are\u3002",
         "\u2705 <strong>How much is</strong> <span class=\"slot\">this sweater</span>?<br>\n          \u27a1 <strong>It's</strong> 45 dollars.<br>\n          \u2705 <strong>How much are</strong> <span class=\"slot\">these socks</span>?<br>\n          \u27a1 <strong>They're</strong> 5 dollars."],
        ["Can I help you?", "\u5e97\u5458\u62db\u547c\u987e\u5ba2\u7684\u7528\u8bed\u3002",
         "\u2705 <strong>Can I help you</strong>?<br>\n          \u27a1 Yes, please. I need a sweater.<br>\n          \u27a1 No, thanks. I'm just looking."],
        ["How about + \u540d\u8bcd/\u4ee3\u8bcd?", "\u63d0\u51fa\u5efa\u8bae\u6216\u63a8\u8350\u3002",
         "\u2705 <strong>How about</strong> <span class=\"slot\">this blue one</span>?<br>\n          \u2705 <strong>How about</strong> <span class=\"slot\">these shoes</span>?<br>\n          \u27a1 one \u4ee3\u66ff\u5355\u6570\u540d\u8bcd\u3002"],
        ["I'll take + \u7269\u54c1.", "\u51b3\u5b9a\u8d2d\u4e70\u3002",
         "\u2705 <strong>I'll take</strong> <span class=\"slot\">it</span>.<br>\n          \u2705 <strong>I'll take</strong> <span class=\"slot\">them</span>.<br>\n          \u27a1 \u5355\u6570\u7528 it\uff0c\u590d\u6570\u7528 them\u3002"]
    ],
    "grammar_tables": [
        ["1\u20e3 How much \u95ee\u4ef7\u683c",
         [["\u53e5\u6cd5", "\u793a\u4f8b"],
          ["How much + is + \u5355\u6570\u540d\u8bcd?", "How much <strong>is this skirt</strong>?"],
          ["How much + are + \u590d\u6570\u540d\u8bcd?", "How much <strong>are these socks</strong>?"],
          ["\u56de\u7b54", "<strong>It's</strong> 45 dollars. / <strong>They're</strong> 5 dollars."]],
         "\U0001f4cc How much \u65e2\u53ef\u4ee5\u95ee\u4e0d\u53ef\u6570\u540d\u8bcd\u7684\u6570\u91cf\uff0c\u4e5f\u53ef\u4ee5\u95ee\u4ef7\u683c\u3002"],
        ["2\u20e3 \u6307\u793a\u4ee3\u8bcd + \u989c\u8272/\u5927\u5c0f + \u540d\u8bcd",
         [["\u7ed3\u6784", "\u793a\u4f8b"],
          ["this/that + \u5355\u6570", "this red sweater, that blue shirt"],
          ["these/those + \u590d\u6570", "these white socks, those black shoes"],
          ["\u5f62\u5bb9\u8bcd\u987a\u5e8f", "this + \u989c\u8272 + \u540d\u8bcd"]],
         "\U0001f4cc <strong>\u5bf9\u6bd4\uff1a</strong><br>this red sweater\uff08\u8fd1\u5904\uff09<br>that blue skirt\uff08\u8fdc\u5904\uff09<br>these cheap socks\uff08\u590d\u6570\u8fd1\u5904\uff09",
         [
            ["I want buy a shirt.", "I want to buy a shirt."],
            ["How much is these shoes?", "How much are these shoes?"],
            ["I'll take it. These sweater is nice.", "I'll take it. This sweater is nice."]
         ]]
    ],
    "exercises": [
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ much is this shirt? (What / How / Where)", "How", "\u95ee\u4ef7\u683c\u7528 How much\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "How much ____ (be) these socks?", "are", "socks \u662f\u590d\u6570\uff0c\u7528 are\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "I'll take ____ (it / them). \u2014 \u6307\u4ee3 the sweater.", "it", "sweater \u662f\u5355\u6570\uff0c\u7528 it\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "How much ____ that red skirt? \u2014 ____ 68 dollars.", "is; It's", "skirt \u5355\u6570\u7528 is\uff1b\u56de\u7b54 It's\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u8865\u5168\u5bf9\u8bdd\uff1a<br>Clerk: ____ I help you?<br>You: Yes, please. I ____ a T-shirt.", "Can; need", "Can I help you? \u56fa\u5b9a\u642d\u914d\uff1bneed \u9700\u8981\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6c49\u8bd1\u82f1\uff1a\u8fd9\u53cc\u978b55\u7f8e\u5143\u3002", "These shoes are 55 dollars.", "\u978b\u5b50\u590d\u6570\u7528 are\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u6539\u9519\uff1aHow much is these short?", "How much are these shorts?", "shorts \u590d\u6570\u7528 are\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u4f60\u60f3\u77e5\u9053\u90a3\u6761\u84dd\u8272\u88d9\u5b50\u591a\u5c11\u94b1\u3002\u4f60\u95ee\u5e97\u5458\uff1a<br>____", "How much is that blue skirt?", "that \u6307\u8fdc\u5904\uff1b\u95ee\u4ef7\u683c How much is\u3002"]
    ],
    "micro_task": "\u5047\u8bbe\u4f60\u662f\u4e00\u5bb6\u670d\u88c5\u5e97\u7684\u8001\u677f\uff0c\u5199\u4e00\u5219\u4fc3\u9500\u5e7f\u544a\uff0c\u4ecb\u7ecd\u4f60\u7684\u5546\u54c1\u548c\u4ef7\u683c\u3002",
    "model_paras": [
        "Come to Happy Clothes Store! We have a big sale!",
        "Do you need sweaters? We have nice sweaters for only 35 dollars.",
        "How much are our T-shirts? They are 20 dollars for one.",
        "Socks are 4 dollars for two pairs. And shorts are only 25 dollars!",
        "Come and see for yourself! You will love the prices!"
    ],
    "model_trans": "\u5feb\u6765\u5feb\u4e50\u670d\u88c5\u5e97\uff01\u6211\u4eec\u6b63\u5728\u5927\u4fc3\u9500\uff01\u4f60\u9700\u8981\u6bdb\u8863\u5417\uff1f\u6211\u4eec\u6709\u6f02\u4eae\u7684\u6bdb\u8863\u53ea\u898135\u7f8e\u5143\u3002\u6211\u4eec\u7684T\u6064\u591a\u5c11\u94b1\uff1f20\u7f8e\u5143\u4e00\u4ef6\u3002\u889c\u5b504\u7f8e\u5143\u4e24\u53cc\u3002\u77ed\u88e4\u53ea\u898125\u7f8e\u5143\uff01\u5feb\u4eb2\u81ea\u6765\u770b\u770b\u5427\uff01",
    "checklist": [
        "\u6211\u80fd\u7528 How much is/are...? \u95ee\u4ef7\u683c",
        "\u6211\u80fd\u7528 Can I help you? / I'll take it. \u8fdb\u884c\u8d2d\u7269\u5bf9\u8bdd",
        "\u6211\u80fd\u7528 this/that/these/those + \u989c\u8272 + \u540d\u8bcd\u63cf\u8ff0\u8863\u7269",
        "\u6211\u80fd\u7406\u89e3 one \u4ee3\u66ff\u540d\u8bcd\u7684\u7528\u6cd5",
        "\u6211\u80fd\u5199\u4e00\u5219\u7b80\u5355\u7684\u4fc3\u9500\u5e7f\u544a"
    ],
    "feynman": "\u548c\u540c\u5b66\u6a21\u62df\u8d2d\u7269\u573a\u666f\u2014\u2014\u201cCan I help you?\u201d \u201cHow much is this sweater?\u201d \u201cI'll take it.\u201d",
    "review": [
        "\U0001f535 1\u5929\u540e\uff1a\u7528 How much \u95ee5\u4ef6\u7269\u54c1\u7684\u4ef7\u683c\u5e76\u56de\u7b54",
        "\U0001f7e2 3\u5929\u540e\uff1a\u6a21\u62df\u4e00\u6b21\u5b8c\u6574\u7684\u8d2d\u7269\u5bf9\u8bdd",
        "\U0001f7e1 1\u5468\u540e\uff1a\u5199\u4e00\u5219\u82f1\u6587\u4fc3\u9500\u5e7f\u544a\uff0850\u8bcd\u5de6\u53f3\uff09",
        "\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60\u4ef7\u683c\u8be2\u95ee\u548c\u8863\u7269\u8bcd\u6c47"
    ],
    "next_unit": 8,
    "next_title": "When is your birthday?",
    "next_desc": "\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u7528 <strong>When is...?</strong> \u95ee\u65e5\u671f\uff0c\u5b66\u4f1a12\u4e2a\u6708\u4efd\u548c\u5e8f\u6570\u8bcd\u7684\u8868\u8fbe\uff01"
}

# U08
data["u08"] = {
    "num": 8,
    "title": "When is your birthday?",
    "subtitle": "\u8be2\u95ee\u65e5\u671f \u00b7 12\u4e2a\u6708\u4efd \u00b7 \u5e8f\u6570\u8bcd \u00b7 \u65e5\u671f\u8868\u8fbe",
    "topic": "Dates and special days",
    "func": "Ask about and give dates",
    "grammar": "When \u95ee\u53e5 \u00b7 \u5e8f\u6570\u8bcd \u00b7 \u6708\u4efd\u548c\u65e5\u671f\u8868\u8fbe \u00b7 \u4ecb\u8bcd in/on",
    "writing": "\u4ecb\u7ecd\u5b66\u6821\u65e5\u5386\u4e2d\u7684\u91cd\u8981\u4e8b\u4ef6",
    "can_do": [
        "I can ask \u201cWhen is your birthday?\u201d and answer.",
        "I can name all 12 months in English.",
        "I can use ordinal numbers (1st, 2nd, 3rd...).",
        "I can write about important dates at school."
    ],
    "scene": "Chen Jie \u5728\u8ddf\u65b0\u540c\u5b66 Lisa \u4e86\u89e3\u5bf9\u65b9\u7684\u751f\u65e5\u548c\u5b66\u6821\u6d3b\u52a8\u3002",
    "dialogue": [
        ["Chen Jie", "Lisa, <em>when is your birthday</em>?"],
        ["Lisa", "My birthday is on September 10th."],
        ["Chen Jie", "Oh, that's Teachers' Day in China, too!"],
        ["Lisa", "Yes! So it's easy to remember. <em>When is your birthday</em>?"],
        ["Chen Jie", "It's on January 15th."],
        ["Lisa", "Cool! Our school has a basketball game in January."],
        ["Chen Jie", "Really? When is it?"],
        ["Lisa", "It's on January 20th. You can come and watch!"]
    ],
    "translation": [
        "Chen Jie: Lisa\uff0c<em>\u4f60\u7684\u751f\u65e5\u662f\u4ec0\u4e48\u65f6\u5019</em>\uff1f",
        "Lisa: \u6211\u7684\u751f\u65e5\u662f9\u670810\u65e5\u3002",
        "Chen Jie: \u54e6\uff0c\u5728\u4e2d\u56fd\u90a3\u4e5f\u662f\u6559\u5e08\u8282\uff01",
        "Lisa: \u662f\u7684\uff01\u6240\u4ee5\u5f88\u597d\u8bb0\u3002<em>\u4f60\u7684\u751f\u65e5\u5462</em>\uff1f",
        "Chen Jie: \u57281\u670815\u65e5\u3002",
        "Lisa: \u9177\uff01\u6211\u4eec\u5b66\u68211\u6708\u6709\u4e00\u573a\u7bee\u7403\u8d5b\u3002",
        "Chen Jie: \u771f\u7684\uff1f\u4ec0\u4e48\u65f6\u5019\uff1f",
        "Lisa: 1\u670820\u65e5\u3002\u4f60\u53ef\u4ee5\u6765\u770b\uff01"
    ],
    "key_points": [
        ["When is your birthday?", "\u7528 <strong>When</strong> \u8be2\u95ee\u65e5\u671f\u3002\u56de\u7b54 <strong>It's on + \u6708\u4efd + \u65e5\u671f\u5e8f\u6570\u8bcd</strong>\u3002"],
        ["on September 10th", "\u5177\u4f53\u7684\u67d0\u4e00\u5929\u7528\u4ecb\u8bcd <strong>on</strong>\u3002\u6708\u4efd\u9996\u5b57\u6bcd\u5927\u5199\u3002\u65e5\u671f\u7528\u5e8f\u6570\u8bcd\uff0810th = tenth\uff09\u3002"],
        ["in January", "\u53ea\u8bf4\u5230\u6708\u4efd\u65f6\u7528\u4ecb\u8bcd <strong>in</strong>\u3002\u6708\u4efd\u524d\u4e0d\u52a0\u51a0\u8bcd\u3002"],
        ["January 15th", "\u65e5\u671f\u8868\u8fbe\uff1a\u6708\u4efd + \u5e8f\u6570\u8bcd\u3002\u53ef\u4ee5\u5199 January 15 \u6216 January 15th\u3002"]
    ],
    "reading_title": "Our School Calendar",
    "reading_paras": [
        "Welcome to our school! Let me tell you about some important days.",
        "Our school trip is in April. It is on April 12th. We go to the zoo.",
        "The basketball game is on May 20th. I will play in the game!",
        "The English test is on June 15th. I need to study hard.",
        "And the school art festival is in October. It is on October 25th.",
        "What about you? What are the important dates in your school?"
    ],
    "gloss": [
        ["calendar", "/\u02c8k\u00e6l\u026and\u0259r/", "n.", "\u65e5\u5386\uff1b\u65e5\u7a0b\u8868"],
        ["important", "/\u026am\u02c8p\u0254\u02d0rt\u0259nt/", "adj.", "\u91cd\u8981\u7684"],
        ["trip", "/tr\u026ap/", "n.", "\u65c5\u884c\uff1b\u51fa\u6e38"],
        ["festival", "/\u02c8fest\u026avl/", "n.", "\u8282\u65e5\uff1b\u8282\u5e86"]
    ],
    "vocab": [
        ["when", "/wen/", "adv.", "\u4ec0\u4e48\u65f6\u5019", "When is the English test?", "\u82f1\u8bed\u8003\u8bd5\u662f\u4ec0\u4e48\u65f6\u5019\uff1f"],
        ["birthday", "/\u02c8b\u025c\u02d0r\u03b8de\u026a/", "n.", "\u751f\u65e5", "Happy birthday to you!", "\u795d\u4f60\u751f\u65e5\u5feb\u4e50\uff01"],
        ["January", "/\u02c8d\u0292\u00e6njueri/", "n.", "\u4e00\u6708", "New Year is in January.", "\u65b0\u5e74\u5728\u4e00\u6708\u3002"],
        ["February", "/\u02c8februeri/", "n.", "\u4e8c\u6708", "February is the second month.", "\u4e8c\u6708\u662f\u7b2c\u4e8c\u4e2a\u6708\u3002"],
        ["March", "/m\u0251\u02d0rt\u0283/", "n.", "\u4e09\u6708", "Spring comes in March.", "\u6625\u5929\u4e09\u6708\u6765\u4e34\u3002"],
        ["April", "/\u02c8e\u026apr\u0259l/", "n.", "\u56db\u6708", "April has 30 days.", "\u56db\u6708\u670930\u5929\u3002"],
        ["May", "/me\u026a/", "n.", "\u4e94\u6708", "May is a nice month.", "\u4e94\u6708\u662f\u4e2a\u597d\u6708\u4efd\u3002"],
        ["June", "/d\u0292u\u02d0n/", "n.", "\u516d\u6708", "School ends in June.", "\u5b66\u6821\u516d\u6708\u653e\u5047\u3002"],
        ["July", "/d\u0292u\u02d0\u02c8la\u026a/", "n.", "\u4e03\u6708", "July is very hot.", "\u4e03\u6708\u5f88\u70ed\u3002"],
        ["August", "/\u0254\u02d0\u02c8\u0261\u028cst/", "n.", "\u516b\u6708", "We have a holiday in August.", "\u516b\u6708\u6211\u4eec\u6709\u5047\u671f\u3002"],
        ["September", "/sep\u02c8temb\u0259r/", "n.", "\u4e5d\u6708", "School starts in September.", "\u5b66\u6821\u4e5d\u6708\u5f00\u5b66\u3002"],
        ["October", "/\u0252k\u02c8to\u028ab\u0259r/", "n.", "\u5341\u6708", "The art festival is in October.", "\u827a\u672f\u8282\u5728\u5341\u6708\u3002"],
        ["November", "/no\u028a\u02c8vemb\u0259r/", "n.", "\u5341\u4e00\u6708", "November is cold.", "\u5341\u4e00\u6708\u5f88\u51b7\u3002"],
        ["December", "/d\u026a\u02c8semb\u0259r/", "n.", "\u5341\u4e8c\u6708", "Christmas is in December.", "\u5723\u8bde\u8282\u5728\u5341\u4e8c\u6708\u3002"],
        ["happy", "/\u02c8h\u00e6pi/", "adj.", "\u5feb\u4e50\u7684", "I am happy today!", "\u6211\u4eca\u5929\u5f88\u5f00\u5fc3\uff01"]
    ],
    "patterns": [
        ["When is + \u4e8b\u4ef6?", "\u8be2\u95ee\u65e5\u671f\u3002",
         "\u2705 <strong>When is</strong> <span class=\"slot\">your birthday</span>?<br>\n          \u27a1 It's <strong>on</strong> September 10th.<br>\n          \u2705 <strong>When is</strong> <span class=\"slot\">the school trip</span>?<br>\n          \u27a1 It's <strong>in</strong> April."],
        ["It's on + \u6708\u4efd + \u65e5\u671f\u5e8f\u6570\u8bcd.", "\u56de\u7b54\u5177\u4f53\u65e5\u671f\u3002",
         "\u2705 It's on <span class=\"slot\">May 20th</span>.<br>\n          \u2705 It's on <span class=\"slot\">January 1st</span>.<br>\n          \u27a1 \u5e8f\u6570\u8bcd\u7f29\u5199\uff1a1st, 2nd, 3rd, 4th, 5th..."],
        ["How old + be + \u4e3b\u8bed?", "\u8be2\u95ee\u5e74\u9f84\u3002",
         "\u2705 <strong>How old</strong> <span class=\"slot\">are you</span>?<br>\n          \u2705 <strong>How old</strong> <span class=\"slot\">is your brother</span>?<br>\n          \u27a1 \u56de\u7b54\uff1aI'm 13 years old."],
        ["Happy + \u8282\u65e5/\u4e8b\u4ef6!", "\u795d\u798f\u7528\u8bed\u3002",
         "\u2705 <strong>Happy birthday</strong>!<br>\n          \u2705 <strong>Happy New Year</strong>!<br>\n          \u27a1 \u8282\u65e5\u795d\u798f\uff1aHappy + \u8282\u65e5\u540d\u3002"]
    ],
    "grammar_tables": [
        ["1\u20e3 \u5e8f\u6570\u8bcd\uff081-31\uff09",
         [["\u8303\u56f4", "\u89c4\u5f8b", "\u793a\u4f8b"],
          ["\u7b2c1-3", "\u4e0d\u89c4\u5219\u53d8\u5316", "first (1st), second (2nd), third (3rd)"],
          ["\u7b2c4-19", "\u57fa\u6570\u8bcd + th", "fourth (4th), fifth (5th)\u2026nineteenth (19th)"],
          ["\u7b2c20-90\u6574\u5341", "y \u2192 ie + th", "twentieth (20th), thirtieth (30th)"],
          ["\u7b2c21-31", "\u5341\u4f4d\u4e0d\u53d8 + \u4e2a\u4f4d\u5e8f\u6570", "twenty-first (21st), thirty-first (31st)"]],
         "\U0001f4cc <strong>\u5bf9\u6bd4\uff1a</strong>five (5) \u2192 fifth (5th)\uff1btwelve (12) \u2192 twelfth (12th)\uff1btwenty (20) \u2192 twentieth (20th)",
         [
            ["My birthday is in May 10th.", "My birthday is on May 10th."],
            ["When is your birthday? It is in June 1st.", "When is your birthday? It is on June 1st."],
            ["I am 12 year old.", "I am 12 years old."]
         ]],
        ["2\u20e3 12\u4e2a\u6708\u4efd",
         [["\u5e8f\u53f7", "\u6708\u4efd", "\u7f29\u5199"],
          ["1\u6708", "January", "Jan."],
          ["2\u6708", "February", "Feb."],
          ["3\u6708", "March", "Mar."],
          ["4\u6708", "April", "Apr."],
          ["5\u6708", "May", "May"],
          ["6\u6708", "June", "Jun."],
          ["7\u6708", "July", "Jul."],
          ["8\u6708", "August", "Aug."],
          ["9\u6708", "September", "Sep."],
          ["10\u6708", "October", "Oct."],
          ["11\u6708", "November", "Nov."],
          ["12\u6708", "December", "Dec."]],
         "\U0001f4cc <strong>\u52a9\u8bb0\uff1a</strong>\u6708\u4efd\u540d\u79f0\u9996\u5b57\u6bcd\u5fc5\u987b\u5927\u5199\u3002\u5177\u4f53\u65e5\u671f\u7528 on\uff0c\u53ea\u8bf4\u6708\u4efd\u7528 in\u3002"]
    ],
    "exercises": [
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ is your birthday? (What / When / Where)", "When", "\u95ee\u65e5\u671f\u7528 When\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "My birthday is ____ May 10th. (in / on / at)", "on", "\u5177\u4f53\u67d0\u4e00\u5929\u7528 on\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ month of the year is March? (First / Third / Second)", "Third", "\u4e09\u6708\u662f\u7b2c\u4e09\u4e2a\u6708\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u8865\u5168\u5bf9\u8bdd\uff1a<br>A: When is the English test?<br>B: It's ____ June 15th.<br>A: ____ old are you?<br>B: I'm 13.", "on; How", "\u5177\u4f53\u65e5\u671f on\uff1b\u95ee\u5e74\u9f84 How old\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6c49\u8bd1\u82f1\uff1a1\u6708\u662f\u4e00\u5e74\u4e2d\u7684\u7b2c\u4e00\u4e2a\u6708\u3002", "January is the first month of the year.", "first \u5e8f\u6570\u8bcd\u201c\u7b2c\u4e00\u201d\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6539\u9519\uff1aMy birthday is in January 15th.", "My birthday is on January 15th.", "\u5177\u4f53\u65e5\u671f\u7528 on\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u6309\u4ece\u5c0f\u5230\u5927\u6392\u5e8f\uff1a<br>September 1st, August 20th, October 5th, July 15th", "July 15th, August 20th, September 1st, October 5th", "\u6309\u6708\u4efd\u5148\u540e\u6392\u5e8f\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u8865\u5168\u77ed\u6587\uff1a<br>My birthday is ____ April. It is ____ April 18th. I am 13 ____ old.", "in; on; years", "\u53ea\u8bf4\u6708\u4efd\u7528 in\uff1b\u5177\u4f53\u65e5\u671f\u7528 on\uff1byears old\u3002"]
    ],
    "micro_task": "\u5199\u4e00\u6bb5\u8bdd\u4ecb\u7ecd\u4f60\u7684\u751f\u65e5\u548c\u4f60\u5b66\u6821\u4e09\u4e2a\u91cd\u8981\u6d3b\u52a8\u7684\u65e5\u671f\u3002",
    "model_paras": [
        "Hi! I'm Zhang Wei. My birthday is on March 12th.",
        "I am 13 years old. I like March because spring is beautiful.",
        "Our school has some important events every year.",
        "The school trip is on April 10th. We go to the museum.",
        "The sports meeting is on October 15th. I like sports day!"
    ],
    "model_trans": "\u55e8\uff01\u6211\u662f\u5f20\u4f1f\u3002\u6211\u7684\u751f\u65e5\u662f3\u670812\u65e5\u3002\u621113\u5c81\u3002\u6211\u559c\u6b22\u4e09\u6708\uff0c\u56e0\u4e3a\u6625\u5929\u5f88\u7f8e\u4e3d\u3002\u6211\u4eec\u5b66\u6821\u6bcf\u5e74\u6709\u4e00\u4e9b\u91cd\u8981\u6d3b\u52a8\u3002\u5b66\u6821\u65c5\u884c\u57284\u670810\u65e5\uff0c\u6211\u4eec\u53bb\u535a\u7269\u9986\u3002\u8fd0\u52a8\u4f1a\u572810\u670815\u65e5\u3002\u6211\u559c\u6b22\u8fd0\u52a8\u4f1a\uff01",
    "checklist": [
        "\u6211\u4f1a\u7528 When \u95ee\u65e5\u671f\u5e76\u6b63\u786e\u56de\u7b54",
        "\u6211\u80fd\u8bb0\u4f4f12\u4e2a\u6708\u4efd\u7684\u82f1\u6587\u540d\u79f0\u548c\u62fc\u5199",
        "\u6211\u4f1a\u7528\u5e8f\u6570\u8bcd\u8868\u8fbe\u65e5\u671f\uff081st, 2nd, 3rd...\uff09",
        "\u6211\u80fd\u533a\u5206 in\uff08\u6708\u4efd/\u5e74\uff09\u548c on\uff08\u5177\u4f53\u65e5\u671f\uff09\u7684\u7528\u6cd5",
        "\u6211\u80fd\u5199\u4e00\u6bb5\u8bdd\u4ecb\u7ecd\u91cd\u8981\u7684\u65e5\u671f"
    ],
    "feynman": "\u4e0d\u7528\u770b\u7b14\u8bb0\uff0c\u6309\u987a\u5e8f\u8bf4\u51fa12\u4e2a\u6708\u4efd\u30011-31\u7684\u5e8f\u6570\u8bcd\u2014\u2014\u7136\u540e\u4e92\u76f8\u95ee\u751f\u65e5\u3002",
    "review": [
        "\U0001f535 1\u5929\u540e\uff1a\u6309\u987a\u5e8f\u9ed8\u519912\u4e2a\u6708\u4efd",
        "\U0001f7e2 3\u5929\u540e\uff1a\u7528 When is...? \u95ee\u5bb6\u4eba\u7684\u751f\u65e5\u5e76\u5199\u4e0b\u6765",
        "\U0001f7e1 1\u5468\u540e\uff1a\u5199\u4e00\u7bc7 Important Dates in My School",
        "\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60\u5e8f\u6570\u8bcd\u53d8\u5316\u89c4\u5f8b\u548c\u65e5\u671f\u4ecb\u8bcd"
    ],
    "next_unit": 9,
    "next_title": "My favorite subject is science.",
    "next_desc": "\u4e0b\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u7528 <strong>What's your favorite...?</strong> \u8c08\u8bba\u559c\u6b22\u7684\u5b66\u79d1\uff0c\u7528 <strong>Why...? Because...</strong> \u8bf4\u660e\u7406\u7531\uff01"
}

# U09
data["u09"] = {
    "num": 9,
    "title": "My favorite subject is science.",
    "subtitle": "\u8c08\u8bba\u5b66\u79d1\u559c\u597d \u00b7 \u661f\u671f\u540d\u79f0 \u00b7 \u9648\u8ff0\u7406\u7531",
    "topic": "School subjects and schedules",
    "func": "Talk about preferences \u00b7 Give reasons",
    "grammar": "What/Why \u7279\u6b8a\u7591\u95ee\u53e5 \u00b7 because \u5f15\u5bfc\u539f\u56e0 \u00b7 \u5f62\u5bb9\u8bcd\u63cf\u8ff0",
    "writing": "\u4ecb\u7ecd\u81ea\u5df1\u6700\u559c\u6b22\u7684\u5b66\u79d1\u548c\u8bfe\u8868",
    "can_do": [
        "I can ask \u201cWhat's your favorite subject?\u201d and answer.",
        "I can ask \u201cWhy do you like...?\u201d and answer with \u201cBecause...\u201d",
        "I can name all 7 days of the week.",
        "I can write about my school schedule and favorite subject."
    ],
    "scene": "\u8bfe\u95f4\uff0cLi Hua \u548c Tom \u5728\u804a\u5404\u81ea\u6700\u559c\u6b22\u7684\u79d1\u76ee\u4ee5\u53ca\u539f\u56e0\u3002",
    "dialogue": [
        ["Li Hua", "Tom, <em>what's your favorite subject</em>?"],
        ["Tom", "My favorite subject is science. I love doing experiments!"],
        ["Li Hua", "That's cool! <em>Why do you like science</em>?"],
        ["Tom", "Because it is very interesting and useful."],
        ["Li Hua", "Who is your science teacher?"],
        ["Tom", "Mr. Wang. He is a great teacher."],
        ["Li Hua", "What day is your science class?"],
        ["Tom", "It's on Monday and Friday. <em>What subject do you like</em>?"],
        ["Li Hua", "I like English. It's fun and I like to speak it!"]
    ],
    "translation": [
        "Li Hua: Tom\uff0c<em>\u4f60\u6700\u559c\u6b22\u7684\u79d1\u76ee\u662f\u4ec0\u4e48</em>\uff1f",
        "Tom: \u6211\u6700\u559c\u6b22\u7684\u79d1\u76ee\u662f\u79d1\u5b66\u3002\u6211\u559c\u6b22\u505a\u5b9e\u9a8c\uff01",
        "Li Hua: \u771f\u9177\uff01<em>\u4f60\u4e3a\u4ec0\u4e48\u559c\u6b22\u79d1\u5b66</em>\uff1f",
        "Tom: \u56e0\u4e3a\u5b83\u975e\u5e38\u6709\u8da3\u4e14\u6709\u7528\u3002",
        "Li Hua: \u4f60\u7684\u79d1\u5b66\u8001\u5e08\u662f\u8c01\uff1f",
        "Tom: \u738b\u8001\u5e08\u3002\u4ed6\u662f\u4e00\u4f4d\u5f88\u68d2\u7684\u8001\u5e08\u3002",
        "Li Hua: \u4f60\u7684\u79d1\u5b66\u8bfe\u5728\u661f\u671f\u51e0\uff1f",
        "Tom: \u5728\u5468\u4e00\u548c\u5468\u4e94\u3002<em>\u4f60\u559c\u6b22\u4ec0\u4e48\u79d1\u76ee</em>\uff1f",
        "Li Hua: \u6211\u559c\u6b22\u82f1\u8bed\u3002\u5b83\u5f88\u6709\u8da3\uff0c\u800c\u4e14\u6211\u559c\u6b22\u8bf4\u82f1\u8bed\uff01"
    ],
    "key_points": [
        ["What's your favorite subject?", "\u7528 <strong>What's your favorite + \u7c7b\u522b?</strong> \u8be2\u95ee\u6700\u559c\u6b22\u7684\u4eba/\u7269\u3002\u56de\u7b54 My favorite... is...\u3002"],
        ["Why do you like science?", "<strong>Why...?</strong> \u95ee\u539f\u56e0\u3002<strong>Because...</strong> \u56de\u7b54\u3002\u201c\u56e0\u4e3a\u2026\u2026\u201d\u662f\u82f1\u8bed\u4e2d\u6700\u5e38\u7528\u7684\u56e0\u679c\u8868\u8fbe\u3002"],
        ["Because it is interesting and useful.", "<strong>Because</strong> \u5f15\u5bfc\u539f\u56e0\u72b6\u8bed\u4ece\u53e5\u3002\u540e\u9762\u8ddf\u5b8c\u6574\u7684\u53e5\u5b50\u3002because \u548c so \u4e0d\u80fd\u540c\u65f6\u4f7f\u7528\u3002"],
        ["What day is your science class?", "\u95ee\u201c\u661f\u671f\u51e0\u201d\u7528 <strong>What day</strong>\u3002\u661f\u671f\u540d\u79f0\u9996\u5b57\u6bcd\u5927\u5199\uff0c\u524d\u9762\u7528 <strong>on</strong>\u3002"]
    ],
    "reading_title": "My Favorite Subject",
    "reading_paras": [
        "My name is Tom. I am a middle school student.",
        "I have many subjects at school. They are Chinese, math, English, science, history and P.E.",
        "My favorite subject is science. Why do I like it? Because it is very interesting. I like doing experiments.",
        "I also like P.E. It is fun and I can play sports with my friends.",
        "But I don't like history. I think it is a little difficult. What is your favorite subject?"
    ],
    "gloss": [
        ["subject", "/\u02c8s\u028cbd\u0292\u026akt/", "n.", "\u5b66\u79d1\uff1b\u79d1\u76ee"],
        ["experiment", "/\u026ak\u02c8sper\u026am\u0259nt/", "n.", "\u5b9e\u9a8c"],
        ["also", "/\u02c8\u0254\u02d0lso\u028a/", "adv.", "\u4e5f\uff1b\u8fd8"],
        ["difficult", "/\u02c8d\u026af\u026ak\u0259lt/", "adj.", "\u56f0\u96be\u7684"]
    ],
    "vocab": [
        ["favorite", "/\u02c8fe\u026av\u0259r\u026at/", "adj.", "\u6700\u559c\u6b22\u7684", "What is your favorite color?", "\u4f60\u6700\u559c\u6b22\u4ec0\u4e48\u989c\u8272\uff1f"],
        ["subject", "/\u02c8s\u028cbd\u0292\u026akt/", "n.", "\u5b66\u79d1", "Math is my favorite subject.", "\u6570\u5b66\u662f\u6211\u6700\u559c\u6b22\u7684\u79d1\u76ee\u3002"],
        ["science", "/\u02c8sa\u026a\u0259ns/", "n.", "\u79d1\u5b66", "Science is very interesting.", "\u79d1\u5b66\u5f88\u6709\u8da3\u3002"],
        ["math", "/m\u00e6\u03b8/", "n.", "\u6570\u5b66", "I am good at math.", "\u6211\u64c5\u957f\u6570\u5b66\u3002"],
        ["English", "/\u02c8\u026a\u014b\u0261l\u026a\u0283/", "n.", "\u82f1\u8bed", "I like English class.", "\u6211\u559c\u6b22\u82f1\u8bed\u8bfe\u3002"],
        ["Chinese", "/\u02cct\u0283a\u026a\u02c8ni\u02d0z/", "n.", "\u4e2d\u6587/\u8bed\u6587", "Chinese is useful.", "\u8bed\u6587\u5f88\u6709\u7528\u3002"],
        ["history", "/\u02c8h\u026ast\u0259ri/", "n.", "\u5386\u53f2", "History tells us about the past.", "\u5386\u53f2\u544a\u8bc9\u6211\u4eec\u8fc7\u53bb\u7684\u4e8b\u3002"],
        ["because", "/b\u026a\u02c8k\u0254\u02d0z/", "conj.", "\u56e0\u4e3a", "I like art because it is fun.", "\u6211\u559c\u6b22\u7f8e\u672f\u56e0\u4e3a\u5b83\u597d\u73a9\u3002"],
        ["Monday", "/\u02c8m\u028cnde\u026a/", "n.", "\u661f\u671f\u4e00", "School starts on Monday.", "\u5b66\u6821\u5468\u4e00\u5f00\u5b66\u3002"],
        ["Friday", "/\u02c8fra\u026ade\u026a/", "n.", "\u661f\u671f\u4e94", "We have P.E. on Friday.", "\u6211\u4eec\u5468\u4e94\u6709\u4f53\u80b2\u8bfe\u3002"]
    ],
    "patterns": [
        ["What's your favorite + \u7c7b\u522b?", "\u8be2\u95ee\u6700\u559c\u6b22\u7684\u4eba/\u4e8b\u7269\u3002",
         "\u2705 <strong>What's your favorite</strong> <span class=\"slot\">subject</span>?<br>\n          \u27a1 My favorite subject is <span class=\"slot\">science</span>.<br>\n          \u2705 <strong>What's your favorite</strong> <span class=\"slot\">sport</span>?<br>\n          \u27a1 My favorite sport is <span class=\"slot\">basketball</span>."],
        ["Why do you like + \u4e8b\u7269?", "\u8be2\u95ee\u559c\u6b22\u7684\u539f\u56e0\u3002",
         "\u2705 <strong>Why do you like</strong> <span class=\"slot\">science</span>?<br>\n          \u27a1 <strong>Because</strong> it is <span class=\"slot\">interesting</span>.<br>\n          \u2705 <strong>Why does he like</strong> <span class=\"slot\">math</span>?<br>\n          \u27a1 <strong>Because</strong> it is <span class=\"slot\">useful</span>."],
        ["What day is + \u8bfe\u7a0b?", "\u8be2\u95ee\u67d0\u8282\u8bfe\u5728\u661f\u671f\u51e0\u3002",
         "\u2705 <strong>What day is</strong> <span class=\"slot\">your science class</span>?<br>\n          \u27a1 It's <strong>on</strong> <span class=\"slot\">Monday and Friday</span>.<br>\n          \u27a1 \u661f\u671f\u540d\u79f0\u5927\u5199\uff0c\u7528 on\u3002"],
        ["Who is your + \u6559\u5e08\u7c7b\u540d\u8bcd?", "\u8be2\u95ee\u8001\u5e08\u662f\u8c01\u3002",
         "\u2705 <strong>Who is</strong> <span class=\"slot\">your science teacher</span>?<br>\n          \u27a1 <span class=\"slot\">Mr. Wang</span> is my science teacher.<br>\n          \u27a1 Mr. \u7537\u58eb / Ms. \u5973\u58eb + \u59d3\u6c0f\u3002"]
    ],
    "grammar_tables": [
        ["1\u20e3 \u7279\u6b8a\u7591\u95ee\u8bcd\u6c47\u603b",
         [["\u7591\u95ee\u8bcd", "\u542b\u4e49", "\u793a\u4f8b"],
          ["What", "\u4ec0\u4e48", "What is your favorite subject?"],
          ["When", "\u4ec0\u4e48\u65f6\u5019", "When is your birthday?"],
          ["Where", "\u5728\u54ea\u91cc", "Where is my schoolbag?"],
          ["Who", "\u8c01", "Who is your teacher?"],
          ["Why", "\u4e3a\u4ec0\u4e48", "Why do you like science?"],
          ["How", "\u600e\u4e48\u6837", "How are you? / How much is it?"]],
         "\U0001f4cc \u7279\u6b8a\u7591\u95ee\u8bcd + \u4e00\u822c\u7591\u95ee\u53e5\u8bed\u5e8f\uff08\u7591\u95ee\u8bcd + be/do/does + \u4e3b\u8bed + \u5176\u4ed6\uff1f\uff09"],
        ["2\u20e3 \u661f\u671f\u540d\u79f0",
         [["\u7f29\u5199", "\u5168\u79f0"],
          ["Mon.", "Monday\uff08\u661f\u671f\u4e00\uff09"],
          ["Tue.", "Tuesday\uff08\u661f\u671f\u4e8c\uff09"],
          ["Wed.", "Wednesday\uff08\u661f\u671f\u4e09\uff09"],
          ["Thu.", "Thursday\uff08\u661f\u671f\u56db\uff09"],
          ["Fri.", "Friday\uff08\u661f\u671f\u4e94\uff09"],
          ["Sat.", "Saturday\uff08\u661f\u671f\u516d\uff09"],
          ["Sun.", "Sunday\uff08\u661f\u671f\u5929\uff09"]],
         "\U0001f4cc \u661f\u671f\u540d\u79f0\u9996\u5b57\u6bcd\u5927\u5199\u3002\u7528 on Monday / on Friday\u3002",
         [
            ["Because I like science, so I study hard.", "I like science, so I study hard."],
            ["Why you like English?", "Why do you like English?"],
            ["What's your favorite subject? It's on Monday.", "My favorite subject is science. It's on Monday."]
         ]]
    ],
    "exercises": [
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ is your favorite subject? (What / When / Who)", "What", "\u95ee\u201c\u4ec0\u4e48\u201d\u7528 What\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "She likes art ____ it is fun. (because / so / but)", "because", "\u8bf4\u660e\u539f\u56e0\u7528 because\u3002"],
        ["\u57fa\u7840", "\u2605\u2606\u2606", "____ do you like English? \u2014 Because it is interesting.", "Why", "\u95ee\u539f\u56e0\u7528 Why\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "My favorite ____ (\u79d1\u76ee) is math.", "subject", "\u79d1\u76ee\u662f subject\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u8865\u5168\u5bf9\u8bdd\uff1a<br>A: ____ is your music teacher?<br>B: ____ Li. She is very nice.", "Who; Ms.", "\u95ee\u8c01\u7528 Who\uff1bMs. \u5973\u58eb\u3002"],
        ["\u63d0\u5347", "\u2605\u2605\u2606", "\u6c49\u8bd1\u82f1\uff1a\u6211\u6700\u559c\u6b22\u7684\u79d1\u76ee\u662f\u5386\u53f2\u3002\u6211\u89c9\u5f97\u5b83\u5f88\u6709\u8da3\u3002", "My favorite subject is history. I think it is very interesting.", "favorite \u62fc\u5199\uff1bthink \u8ba4\u4e3a\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u8865\u5168\u77ed\u6587\uff1a<br>I go to school from ____ to Friday. My ____ subject is English. I like it ____ I can speak English. My English teacher is ____ Green. She is fun.", "Monday; favorite; because; Ms.", "from Monday to Friday\uff1bfavorite\uff1bbecause\uff1bMs. Green\u3002"],
        ["\u6311\u6218", "\u2605\u2605\u2605", "\u8fde\u53e5\u6210\u6bb5\uff1a<br>a. I think it is a little difficult but very useful.<br>b. My favorite subject is math.<br>c. Our math teacher is Mr. Chen.<br>d. Why do I like it?", "b \u2192 d \u2192 a \u2192 c", "\u5148\u4ecb\u7ecd\u6700\u559c\u6b22\u7684\u79d1\u76ee \u2192 \u95ee\u539f\u56e0 \u2192 \u8bf4\u660e\u539f\u56e0 \u2192 \u4ecb\u7ecd\u8001\u5e08\u3002"]
    ],
    "micro_task": "\u5199\u4e00\u6bb5\u8bdd\u4ecb\u7ecd\u4f60\u6700\u559c\u6b22\u7684\u5b66\u79d1\u548c\u539f\u56e0\uff0c\u4ee5\u53ca\u8fd9\u4e2a\u5b66\u79d1\u5728\u6bcf\u5468\u7684\u54ea\u51e0\u5929\u4e0a\u8bfe\u3002",
    "model_paras": [
        "My name is Li Hua. I am a middle school student.",
        "I have many subjects. My favorite subject is English.",
        "Why do I like English? Because it is very useful and interesting.",
        "I like to speak English with my friends. It makes me happy.",
        "I have English classes on Monday, Wednesday and Friday.",
        "My English teacher is Ms. Zhang. She is kind and helpful."
    ],
    "model_trans": "\u6211\u53eb\u674e\u534e\uff0c\u662f\u4e00\u540d\u4e2d\u5b66\u751f\u3002\u6211\u6709\u5f88\u591a\u79d1\u76ee\u3002\u6211\u6700\u559c\u6b22\u7684\u79d1\u76ee\u662f\u82f1\u8bed\u3002\u4e3a\u4ec0\u4e48\u559c\u6b22\u82f1\u8bed\uff1f\u56e0\u4e3a\u5b83\u975e\u5e38\u6709\u7528\u4e14\u6709\u8da3\u3002\u6211\u559c\u6b22\u548c\u670b\u53cb\u8bf4\u82f1\u8bed\u3002\u6211\u5728\u5468\u4e00\u3001\u5468\u4e09\u548c\u5468\u4e94\u6709\u82f1\u8bed\u8bfe\u3002\u6211\u7684\u82f1\u8bed\u8001\u5e08\u662f\u5f20\u8001\u5e08\uff0c\u5979\u548c\u8566\u53c8\u4e50\u4e8e\u52a9\u4eba\u3002",
    "checklist": [
        "\u6211\u80fd\u7528 What's your favorite...? \u8be2\u95ee\u5e76\u56de\u7b54",
        "\u6211\u80fd\u7528 Why...? Because... \u8bf4\u660e\u7406\u7531",
        "\u6211\u80fd\u8bf4\u51fa\u5e76\u62fc\u51997\u5929\u7684\u82f1\u6587\u540d\u79f0",
        "\u6211\u80fd\u7406\u89e3\u7279\u6b8a\u7591\u95ee\u8bcd What/When/Where/Who/Why/How \u7684\u533a\u522b",
        "\u6211\u80fd\u5199\u4e00\u6bb5\u8bdd\u4ecb\u7ecd\u81ea\u5df1\u559c\u6b22\u7684\u5b66\u79d1"
    ],
    "feynman": "\u7528\u82f1\u8bed\u56de\u7b54\u2014\u2014\u201cWhat is your favorite subject? Why? What day is it?\u201d",
    "review": [
        "\U0001f535 1\u5929\u540e\uff1a\u9ed8\u5199\u661f\u671f1-7\u548c\u79d1\u76ee\u540d\u79f0",
        "\U0001f7e2 3\u5929\u540e\uff1a\u7528 What/Why/When/Who \u4e92\u76f8\u63d0\u95ee",
        "\U0001f7e1 1\u5468\u540e\uff1a\u5199\u4e00\u7bc7 My Favorite Subject \u5c0f\u77ed\u6587",
        "\U0001f534 1\u6708\u540e\uff1a\u590d\u4e60\u6240\u6709\u7279\u6b8a\u7591\u95ee\u8bcd\u7684\u7528\u6cd5\u548c\u533a\u522b"
    ],
    "next_unit": 13,
    "next_title": "Can you play the guitar?",
    "next_desc": "\u606d\u559c\u4f60\u5b8c\u6210\u4e86\u4e03\u5e74\u7ea7\u4e0a\u518c\u6240\u6709\u5355\u5143\uff01\u63a5\u4e0b\u6765\u8fdb\u5165\u4e03\u4e0b\u2014\u2014\u7b2c\u4e00\u5355\u5143\u4f60\u5c06\u5b66\u4e60\u7528 <strong>Can</strong> \u8c08\u8bba\u80fd\u529b\uff0c\u8fd8\u4f1a\u8ba4\u8bc6\u5404\u79cd\u4e50\u5668\uff01"
}

with open("english7_units.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"All units added. Keys: {list(data.keys())}")
