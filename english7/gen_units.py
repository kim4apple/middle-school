#!/usr/bin/env python3
"""Generate unit HTML files for 人教版七上 English Units 2,4-9."""
import json, os, html as htmlmod

TEMPLATE = open("u03.html", encoding="utf-8").read()

UNITS = {}

# ====== UNIT 2: This is my sister. ======
UNITS["u02"] = {
    "num": "2",
    "title": "This is my sister.",
    "subtitle": "介绍家庭成员 · 指示代词指人 · 名词复数",
    "topic": "The family",
    "func": "Introduce people · Identify people",
    "grammar": "指示代词 this/that/these/those · Who 问句",
    "writing": "描述一张家庭照片",
    "can_do": [
        'I can introduce my family members using "This is..." and "These are..."',
        'I can ask "Who is she?" and answer with family words.',
        "I can use this / that / these / those to talk about people.",
        "I can write a short paragraph about my family photo.",
    ],
    "scene": "Mary 给朋友 Linda 看自己的家庭照片。",
    "dialogue": [
        ("Mary", 'Hi, Linda! Come and look at my family photo!'),
        ("Linda", "Wow! <em>Who's this</em>?"),
        ("Mary", "This is my mother. And this is my father."),
        ("Linda", "Who are they?"),
        ("Mary", "Those are my grandparents, and these are my brothers, Tom and Bob."),
        ("Linda", "Is this your sister?"),
        ("Mary", "No, it isn't. She is my cousin, Jenny."),
        ("Linda", "She's beautiful! You have a big family!"),
    ],
    "translation": [
        "Mary: 嗨 Linda！过来看我的全家福！",
        "Linda: 哇！<em>这位是谁</em>？",
        "Mary: 这是我妈妈。这是我爸爸。",
        "Linda: <em>他们是谁</em>？",
        "Mary: 那些是我的（外）祖父母，这些是我的兄弟 Tom 和 Bob。",
        "Linda: <em>这是你的姐姐吗</em>？",
        "Mary: 不，不是。她是我的表姐 Jenny。",
        "Linda: 她很漂亮！你有一个大家庭！",
    ],
    "key_points": [
        ("Who's this? / Who are they?", "用 <strong>Who</strong> 询问\"谁\"。单数用 is，复数用 are。"),
        ("This is my mother.", "介绍他人用 <strong>This is...</strong>（单数）或 <strong>These are...</strong>（复数）。"),
        ("Those are my grandparents.", "those 指远处的人，these 指近处的人。"),
        ("She is my cousin.", "指代女性用 she，男性用 he。人物介绍中注意人称代词的使用。"),
    ],
    "reading_title": "My Family",
    "reading_paras": [
        "Hello! I'm Mary. This is a photo of my family.",
        "These are my parents. My mother is a teacher. My father is a doctor.",
        "Those are my grandparents. They are very kind.",
        "These two boys are my brothers. Their names are Tom and Bob.",
        'And this little girl is me! I love my family.',
    ],
    "gloss": [
        ("photo", "/ˈfoʊtoʊ/", "n.", "照片"),
        ("parent", "/ˈperənt/", "n.", "父/母"),
        ("grandparent", "/ˈɡrænperənt/", "n.", "(外)祖父/母"),
        ("kind", "/kaɪnd/", "adj.", "慈祥的，友善的"),
    ],
    "vocab": [
        ("sister", "/ˈsɪstər/", "n.", "姐妹", "My sister is a student.", "我姐姐是学生。"),
        ("brother", "/ˈbrʌðər/", "n.", "兄弟", "My brother likes playing soccer.", "我弟弟喜欢踢足球。"),
        ("mother", "/ˈmʌðər/", "n.", "母亲", "My mother cooks dinner every day.", "我妈妈每天做晚饭。"),
        ("father", "/ˈfɑːðər/", "n.", "父亲", "My father reads newspapers after dinner.", "我爸爸晚饭后看报纸。"),
        ("grandmother", "/ˈɡrænmʌðər/", "n.", "（外）祖母", "My grandmother tells me stories.", "我奶奶给我讲故事。"),
        ("grandfather", "/ˈɡrænfɑːðər/", "n.", "（外）祖父", "My grandfather walks in the park every morning.", "我爷爷每天早上在公园散步。"),
        ("parent", "/ˈperənt/", "n.", "父/母（单数）；父母（复数 parents）", "My parents are both doctors.", "我父母都是医生。"),
        ("family", "/ˈfæməli/", "n.", "家，家庭", "My family has four people.", "我家有四口人。"),
        ("who", "/huː/", "pron.", "谁", "Who is she? She is my aunt.", "她是谁？她是我姑姑。"),
        ("aunt", "/ænt/", "n.", "姑姑，阿姨，婶婶", "My aunt lives in Beijing.", "我姑姑住在北京。"),
    ],
    "patterns": [
        ("This is / That is + 人物.", "用来介绍或指认一个人。this 指近处，that 指远处。",
         '✅ <strong>This is</strong> <span class="slot">my mother</span>.<br>\n          ✅ <strong>That is</strong> <span class="slot">my sister</span>.<br>\n          ➡ 复数：<strong>These are</strong> my parents. / <strong>Those are</strong> my grandparents.'),
        ("Who's this / that? & Who are they?", "询问照片中的人是谁。单数用 is，复数用 are。",
         '✅ <strong>Who\'s</strong> <span class="slot">this</span>? — It\'s my cousin.<br>\n          ✅ <strong>Who\'s</strong> <span class="slot">that</span>? — That\'s my uncle.<br>\n          ✅ <strong>Who are</strong> <span class="slot">they</span>? — They are my friends.'),
        ("Is this / that your + 人物?", "确认某人是否是对方的某位家人。",
         '✅ <strong>Is this</strong> <span class="slot">your sister</span>? — Yes, she is.<br>\n          ✅ <strong>Is that</strong> <span class="slot">your brother</span>? — No, he isn\'t. He\'s my friend.<br>\n          ✅ <strong>Are those</strong> <span class="slot">your grandparents</span>? — Yes, they are.'),
        ("He / She is + 描述.", "用 he/she 指代男性/女性，并描述其身份或特征。",
         '✅ <strong>She</strong> is <span class="slot">a teacher</span>.<br>\n          ✅ <strong>He</strong> is <span class="slot">my uncle</span>.<br>\n          ✅ <strong>They</strong> are <span class="slot">very kind</span>.'),
    ],
    "grammar_tables": [
        ("1️⃣ 指示代词指人：this / that / these / those",
         [("", "单数", "复数"),
          ("<strong>近处</strong>（照片中/身边）", '<strong>this</strong> 这位（近处）', '<strong>these</strong> 这些（近处）'),
          ("<strong>远处</strong>（较远/那边）", '<strong>that</strong> 那位（远处）', '<strong>those</strong> 那些（远处）')],
         '📌 <strong>对比：</strong><br>\n      <span class="wotd-say" data-speak="This is my mother.">This is my mother.</span>（近处介绍）<br>\n      <span class="wotd-say" data-speak="That is my aunt.">That is my aunt.</span>（远处指认）<br>\n      <span class="wotd-say" data-speak="These are my cousins.">These are my cousins.</span>（复数近处）<br>\n      <span class="wotd-say" data-speak="Those are my friends.">Those are my friends.</span>（复数远处）'),
        ("2️⃣ Who 问句：询问身份",
         [("问句", "答句"),
          ('Who\'s this?', "It's my sister."),
          ("Who's that?", "That's my grandfather."),
          ("Who are they?", "They are my parents.")],
         '📌 Who 问句的 be 动词根据回答的人称/数来变化——单数用 is，复数用 are。',
         [
             ('He is who?', 'Who is he?'),
             ('This is my sister?', 'Is this your sister?'),
             ('These is my parents.', 'These are my parents.'),
         ]),
        ("3️⃣ 名词复数（复习）",
         [("单数", "复数", "规则"),
          ("brother", "brothers", "一般加 -s"),
          ("parent", "parents", "一般加 -s"),
          ("family", "families", "辅音+y → 变 y 为 i 加 -es")],
         '💡 <strong>对比：</strong><br>\n        <strong>This is</strong> my <strong>brother</strong>.（一个兄弟）<br>\n        <strong>These are</strong> my <strong>brothers</strong>.（两个以上兄弟）'),
    ],
    "exercises": [
        ("基础", "★☆☆", '<span class="slot">my mother</span> (This / These / Those)',
         "This", "介绍一个人用单数指示代词 This。"),
        ("基础", "★☆☆", '____ is that? — That\'s my grandfather.',
         "Who", '问「那是谁?」用 Who。'),
        ("基础", "★☆☆", '____ are my brothers. (That / This / These)',
         "These", "brothers 是复数，谓语用 are，所以指示代词用复数 These。"),
        ("提升", "★★☆", '— ____ is she?<br>— She is my ____ (姑姑).',
         "Who; aunt", '问女性身份用 Who is she? 「姑姑」英文是 aunt。'),
        ("提升", "★★☆", '连词成句：this / your / is / sister / ?',
         "Is this your sister?", "一般疑问句以 be 动词开头。"),
        ("提升", "★★☆", '补全对话：<br>A: Look at the photo! ____ is that girl?<br>B: Oh, ____ is my cousin, Lily.',
         "Who; she/that", '第一空用 Who；第二空回答用 she 或 that。'),
        ("挑战", "★★★", '改错：These is my parent.',
         "These are my parents.", "These 是复数 be 动词用 are；parent 指一人，照片中父母两人用 parents。"),
        ("挑战", "★★★", '根据上下文补全短文：<br>Hi! I ____ Tom. Here is a photo ____ my family.<br> ____ are my parents. This is my ____ (妹妹). She is 7 years old. I love my ____.',
         "am; of; These/Those; sister; family", "I am 固定搭配；a photo of；复数指代用 These/Those；sister；family。"),
    ],
    "micro_task": "写一段话，描述一张你的家庭照片。介绍照片中的每个人（至少3人），用上 This is / These are 和 Who 问句。",
    "model_paras": [
        "<strong>Here is a photo of my family.</strong>",
        "These are my parents. My mother is a nurse. My father is a driver.",
        "This little boy is my brother. He is 8 years old.",
        "Who is that old woman? She is my grandmother. She is very nice.",
    ],
    "model_trans": "这是一张我的全家福。这两位是我的父母。我妈妈是护士，爸爸是司机。这个小男孩是我的弟弟，他8岁了。那位老妇人是谁？她是我的祖母，她非常和蔼。",
    "checklist": [
        "我能用 This is... / These are... 介绍家人",
        '我能用 Who 问句询问「谁」并回答',
        "我能区分 this/that/these/those 在指人时的用法",
        "我能使用 he/she/they 正确指代不同性别和数量的人",
        "我能写一段话介绍家庭合影",
    ],
    "feynman": "指着家庭照片中的每个人，用英语逐一介绍——\"This is my mother. She is a teacher. That is my grandfather. He is very kind.\"",
    "review": [
        "🔵 1天后：默写家庭成员的英文单词",
        "🟢 3天后：口头介绍一张家庭照片",
        "🟡 1周后：写一段关于你家庭的短文",
        "🔴 1月后：复习 Who 问句和指示代词表格",
    ],
    "next_unit": "4",
    "next_title": "Where's my schoolbag?",
    "next_desc": "下一单元你将学习用 <strong>Where</strong> 问物品的位置，使用介词 <strong>in / on / under</strong> 描述方位——这些对话中也会用到家庭房间的场景！",
}

# ====== UNIT 4: Where's my schoolbag? ======
UNITS["u04"] = {
    "num": "4",
    "title": "Where's my schoolbag?",
    "subtitle": "询问物品位置 · 方位介词 · 房间物品",
    "topic": "Things in a room",
    "func": "Ask about location · Describe where things are",
    "grammar": "Where 问句 · 介词 in/on/under · 用 they 指代复数物品",
    "writing": "描述自己的房间布局",
    "can_do": [
        'I can ask "Where is/are...?" to find things.',
        "I can use in / on / under to describe positions.",
        "I can answer with \"It's in/on/under...\" or \"They're in/on/under...\"",
        "I can write about what's in my room.",
    ],
    "scene": "Tom 早上找不到自己的学习用品，妈妈在帮他找。",
    "dialogue": [
        ("Tom", "Mom, where is my schoolbag?"),
        ("Mom", "<em>Is it on your desk</em>?"),
        ("Tom", "No, it isn't. Oh, it's on the chair!"),
        ("Mom", "OK. And <em>where are your books</em>?"),
        ("Tom", "They're in my schoolbag."),
        ("Mom", "Where is your pencil?"),
        ("Tom", "It's under the desk."),
        ("Mom", "Tom, please keep your room tidy!"),
    ],
    "translation": [
        "Tom: 妈妈，我的书包在哪里？",
        "Mom: <em>它在你的桌子上吗</em>？",
        "Tom: 不，不在。哦，它在椅子上！",
        "Mom: 好的。那<em>你的书在哪里</em>？",
        "Tom: 它们在我的书包里。",
        "Mom: 你的铅笔在哪里？",
        "Tom: 它在桌子下面。",
        "Mom: Tom，请保持你的房间整洁！",
    ],
    "key_points": [
        ("Where is my schoolbag?", '用 <strong>Where is / Where are</strong> 提问位置。单数物品用 is，复数物品用 are。'),
        ("Is it on your desk?", 'Yes/No 问句可以把 be 动词提前。<strong>Is it on...?</strong> 确认某物是否在某处。'),
        ("It's on the chair. / They're in my schoolbag.", '回答时单数用 <strong>It is / It\'s</strong>，复数用 <strong>They are / They\'re</strong>。'),
        ("under the desk", '<strong>under</strong> 在……下面；<strong>in</strong> 在……里面；<strong>on</strong> 在……上面。三个最常用的方位介词。'),
    ],
    "reading_title": "My Room",
    "reading_paras": [
        "Welcome to my room! It is small but tidy.",
        "My bed is near the window. My schoolbag is on the chair.",
        "My books are in the bookcase. My pencil box is on the desk.",
        "Under the desk, there is a ball. Where is my clock? It's on the wall.",
        "I like my room very much.",
    ],
    "gloss": [
        ("welcome", "/ˈwelkəm/", "interj.", "欢迎"),
        ("tidy", "/ˈtaɪdi/", "adj.", "整洁的"),
        ("bookcase", "/ˈbʊkkeɪs/", "n.", "书柜"),
        ("wall", "/wɔːl/", "n.", "墙"),
    ],
    "vocab": [
        ("where", "/wer/", "adv.", "在哪里", "Where is my pen?", "我的笔在哪里？"),
        ("schoolbag", "/ˈskuːlbæɡ/", "n.", "书包", "My schoolbag is heavy.", "我的书包很重。"),
        ("desk", "/desk/", "n.", "书桌", "There is a lamp on the desk.", "书桌上有一盏台灯。"),
        ("chair", "/tʃer/", "n.", "椅子", "Sit on the chair, please.", "请坐在椅子上。"),
        ("under", "/ˈʌndər/", "prep.", "在……下面", "The cat is under the table.", "猫在桌子下面。"),
        ("bookcase", "/ˈbʊkkeɪs/", "n.", "书柜", "Put the books in the bookcase.", "把书放进书柜。"),
        ("sofa", "/ˈsoʊfə/", "n.", "沙发", "My father is on the sofa.", "我爸爸在沙发上。"),
        ("drawer", "/drɔːr/", "n.", "抽屉", "The keys are in the drawer.", "钥匙在抽屉里。"),
        ("clock", "/klɒk/", "n.", "时钟", "The clock on the wall is new.", "墙上的钟是新的。"),
        ("tape", "/teɪp/", "n.", "磁带；胶带", "Where is my tape?", "我的磁带在哪里？"),
    ],
    "patterns": [
        ("Where is + 单数物品?", '询问单个物品的位置。',
         '✅ <strong>Where is</strong> <span class="slot">my pen</span>?<br>\n          ➡ <strong>It\'s</strong> <span class="slot">on the desk</span>.<br>\n          ✅ <strong>Where is</strong> <span class="slot">the cat</span>?<br>\n          ➡ <strong>It\'s</strong> <span class="slot">under the table</span>.'),
        ("Where are + 复数物品?", '询问多个物品的位置。',
         '✅ <strong>Where are</strong> <span class="slot">my keys</span>?<br>\n          ➡ <strong>They\'re</strong> <span class="slot">in the drawer</span>.<br>\n          ✅ <strong>Where are</strong> <span class="slot">your books</span>?<br>\n          ➡ <strong>They\'re</strong> <span class="slot">on the desk</span>.'),
        ("Is it / Are they + 位置?", "用 Yes/No 问句确认位置。",
         '✅ <strong>Is it</strong> <span class="slot">on your desk</span>? — Yes, it is.<br>\n          ✅ <strong>Are they</strong> <span class="slot">under the chair</span>? — No, they aren\'t.<br>\n          ➡ 助记：单数用 is it，复数用 are they。'),
        ("物品 + is/are + 位置.", "陈述物品所在位置的基本句型。",
         '✅ My <strong>schoolbag</strong> is <span class="slot">on the chair</span>.<br>\n          ✅ The <strong>books</strong> are <span class="slot">in the bookcase</span>.<br>\n          ✅ The <strong>clock</strong> is <span class="slot">on the wall</span>.'),
    ],
    "grammar_tables": [
        ("1️⃣ Where 问句：询问位置",
         [("问句", "答句", "说明"),
          ('Where <strong>is</strong> my schoolbag?', "It's on the chair.", "单数用 is / It's"),
          ('Where <strong>are</strong> my books?', "They're in the schoolbag.", "复数用 are / They're"),
          ('Where <strong>is</strong> the cat?', "It's under the table.", "单数名词 + is")],
         '📌 <strong>句型结构：</strong><br>\n      Where + is/are + 名词? → 主语 + is/are + 介词短语。'),
        ("2️⃣ 方位介词：in / on / under",
         [("介词", "含义", "示例"),
          ('<span class="wotd-say" data-speak="in"><strong>in</strong></span>', "在……里面", '<span class="wotd-say" data-speak="in the schoolbag">in the schoolbag</span>'),
          ('<span class="wotd-say" data-speak="on"><strong>on</strong></span>', "在……上面", '<span class="wotd-say" data-speak="on the desk">on the desk</span>'),
          ('<span class="wotd-say" data-speak="under"><strong>under</strong></span>', "在……下面", '<span class="wotd-say" data-speak="under the chair">under the chair</span>')],
         '📌 <strong>顺口溜：</strong>in in 在里面，on on 在上面，under under 在下面，位置表达不会乱。',
         [
             ('My book is on the desk?', 'Is my book on the desk?'),
             ('Where is my pen? It in the pencil box.', 'Where is my pen? It\'s in the pencil box.'),
             ('Where are the keys? It\'s on the table.', 'Where are the keys? They\'re on the table.'),
         ]),
        ("3️⃣ 冠词 a / an / the 的基本用法",
         [("冠词", "用法", "示例"),
          ('a', '辅音音素开头的可数名词单数前', 'a desk, a book, a chair'),
          ('an', '元音音素开头的可数名词单数前', 'an eraser, an apple, an hour'),
          ('the', '双方都知道的/上文提到过的', 'the desk, the books, the schoolbag')],
         '📌 <strong>对比：</strong><br>a book（任意一本书）vs the book（双方都知道的那本）'),
    ],
    "exercises": [
        ("基础", "★☆☆", '____ is my pencil? (What / Where / Who)',
         "Where", '问地点用 Where。'),
        ("基础", "★☆☆", 'The cat is ____ the table. (in / on / under)<br>— 猫在桌子下面。',
         "under", "桌子下面用 under。"),
        ("基础", "★☆☆", '____ are your shoes? — ____ are under the bed.',
         "Where; They", "问复数物品用 Where are；回答用 They are。"),
        ("提升", "★★☆", '补全句子：My books ____ (be) in the ____ (书柜).',
         "are; bookcase", "books 是复数用 are；书柜是 bookcase。"),
        ("提升", "★★☆", '连词成句：your / schoolbag / where / is / ?',
         "Where is your schoolbag?", "Where 问句：Where + is + 名词?。"),
        ("提升", "★★☆", '改错：The keys is on the desk.',
         "The keys are on the desk.", "keys 是复数，be 动词用 are。"),
        ("挑战", "★★★", '汉译英：我的铅笔盒在书包里。',
         "My pencil box is in the schoolbag.", "铅笔盒 pencil box；在书包里 in the schoolbag。"),
        ("挑战", "★★★", '补全对话：<br>A: I can\'t find my keys. ____ are they?<br>B: ____ they on the table?<br>A: No, they ____.<br>B: Oh, look! ____ are under the sofa.',
         "Where; Are; aren't; They", "问 Where are they？确认 Are they...？否定 aren't；回答 They are。"),
    ],
    "micro_task": "写一段话，描述你的房间或书房。至少写出5件物品的位置，用上 Where is/are、in/on/under。",
    "model_paras": [
        "This is my room. It is not big but I like it.",
        "Where is my bed? It's near the window.",
        "My desk is next to the bed. My lamp is on the desk.",
        "My books and notebooks are in the bookcase.",
        "Under my desk, there is a basketball. I love my room!",
    ],
    "model_trans": "这是我的房间。它不大，但我很喜欢。我的床在哪里？它在窗户旁边。我的书桌在床边。台灯在书桌上。我的书和笔记本在书柜里。书桌下面有一个篮球。我爱我的房间！",
    "checklist": [
        "我能用 Where is/are 问物品位置并回答",
        "我能正确使用 in/on/under 三个方位介词",
        "我能区分单数回答用 It's，复数回答用 They're",
        "我能理解并运用 a/an/the 的基本区别",
        "我能写一段话介绍我的房间布局",
    ],
    "feynman": "闭上眼睛，用英语说出你房间里5件物品的位置——\"My phone is on the desk. My shoes are under the chair...\"",
    "review": [
        "🔵 1天后：用 Where is/are 向同学提问物品位置",
        "🟢 3天后：画出房间简图并标注英文名称和位置",
        "🟡 1周后：写一篇完整的小短文 My Room",
        "🔴 1月后：复习所有方位介词和 Where 问句",
    ],
    "next_unit": "5",
    "next_title": "Do you have a soccer ball?",
    "next_desc": '下一单元你将学习用 <strong>Do you have...?</strong> 谈论物品所属，运动相关的词汇等你来学！',
}

# ====== UNIT 5: Do you have a soccer ball? ======
UNITS["u05"] = {
    "num": "5",
    "title": "Do you have a soccer ball?",
    "subtitle": "谈论物品所属 · 一般现在时 have/has · 运动词汇",
    "topic": "Sports and games",
    "func": "Ownership · Invitations · Suggestions",
    "grammar": "Do/Does 一般疑问句 · have/has 用法 · Let's 祈使句",
    "writing": "描述自己和朋友的体育用品",
    "can_do": [
        'I can ask "Do you have...?" and answer about sports equipment.',
        'I can use "Let\'s play..." to make suggestions.',
        "I can use \"That sounds...\" to give opinions.",
        "I can write about what sports things I have.",
    ],
    "scene": "球场边，Frank 和 Mike 在讨论各自有什么球类用品，商量一起运动。",
    "dialogue": [
        ("Frank", "Mike, <em>do you have a soccer ball</em>?"),
        ("Mike", "No, I don't. But I have a basketball."),
        ("Frank", "Great! Let's play basketball!"),
        ("Mike", "That sounds good. <em>Do you have a basketball</em>?"),
        ("Frank", "Yes, I do. I have a basketball and a baseball, too."),
        ("Mike", "Wow! Do you have a baseball bat?"),
        ("Frank", "No, I don't. <em>Let's ask John</em>. He has one."),
        ("Mike", "OK! Let's go!"),
    ],
    "translation": [
        "Frank: Mike，<em>你有一个足球吗</em>？",
        "Mike: 不，我没有。但我有一个篮球。",
        "Frank: 太好了！我们去打篮球吧！",
        "Mike: 听起来不错。<em>你有一个篮球吗</em>？",
        "Frank: 是的，我有。我有一个篮球，还有一个棒球。",
        "Mike: 哇！你有棒球棒吗？",
        "Frank: 不，我没有。<em>我们去问约翰吧</em>。他有一个。",
        "Mike: 好的！走吧！",
    ],
    "key_points": [
        ("Do you have a soccer ball?", '一般疑问句用 <strong>Do</strong> 开头 + 主语 + have + 物品。回答：<strong>Yes, I do.</strong> / <strong>No, I don\'t.</strong>'),
        ("I don't have one.", '<strong>don\'t</strong> = do not，否定形式。第三人称单数时用 <strong>doesn\'t have</strong>。'),
        ("Let's play basketball!", '<strong>Let\'s</strong> = Let us，表示「让我们……」，后面跟动词原形。用来提出建议。'),
        ("That sounds good.", '<strong>That sounds + 形容词</strong>。"那听起来……"，表达对建议的看法。类似结构：look、feel、taste。'),
    ],
    "reading_title": "Sports in Our Life",
    "reading_paras": [
        "Hi! I'm Frank. I like sports very much.",
        "I have a basketball and a baseball. I play basketball with my friends after school.",
        "My friend Mike doesn't have a soccer ball, but he has a volleyball.",
        "We often play volleyball on weekends. It is fun!",
        "Do you have a favorite sport? Let's play together!",
    ],
    "gloss": [
        ("sport", "/spɔːrt/", "n.", "运动"),
        ("play", "/pleɪ/", "v.", "玩；打（球）"),
        ("weekend", "/ˈwiːkend/", "n.", "周末"),
        ("together", "/təˈɡeðər/", "adv.", "一起"),
    ],
    "vocab": [
        ("have", "/hæv/", "v.", "有", "I have a new basketball.", "我有一个新篮球。"),
        ("soccer", "/ˈsɒkər/", "n.", "英式足球", "Do you play soccer?", "你踢足球吗？"),
        ("ball", "/bɔːl/", "n.", "球", "The ball is under the chair.", "球在椅子下面。"),
        ("tennis", "/ˈtenɪs/", "n.", "网球", "Tennis is an interesting sport.", "网球是一项有趣的运动。"),
        ("basketball", "/ˈbæskɪtbɔːl/", "n.", "篮球", "Let's play basketball.", "我们打篮球吧。"),
        ("volleyball", "/ˈvɑːlibɔːl/", "n.", "排球", "She has a volleyball.", "她有一个排球。"),
        ("baseball", "/ˈbeɪsbɔːl/", "n.", "棒球", "Baseball is popular in the US.", "棒球在美国很流行。"),
        ("bat", "/bæt/", "n.", "球棒；蝙蝠", "Where is the baseball bat?", "棒球棒在哪里？"),
        ("racket", "/ˈrækɪt/", "n.", "球拍", "I need a tennis racket.", "我需要一个网球拍。"),
        ("let's", "/lets/", "abbr.", "让我们（= let us）", "Let's go to the playground.", "我们去操场吧。"),
    ],
    "patterns": [
        ("Do you have + 物品?", "询问对方是否有某物。",
         '✅ <strong>Do you have</strong> <span class="slot">a soccer ball</span>?<br>\n          ➡ Yes, I do. / No, I don\'t.<br>\n          ✅ <strong>Does he have</strong> <span class="slot">a basketball</span>?<br>\n          ➡ Yes, he does. / No, he doesn\'t.'),
        ("Let's + 动词原形 + 其他.", "提出建议。",
         '✅ <strong>Let\'s play</strong> <span class="slot">basketball</span>!<br>\n          ✅ <strong>Let\'s go</strong> <span class="slot">to the park</span>!<br>\n          ✅ <strong>Let\'s ask</strong> <span class="slot">John</span>!'),
        ("That sounds + 形容词.", "表达对建议的看法。",
         '✅ That sounds <span class="slot">good</span>.<br>\n          ✅ That sounds <span class="slot">interesting</span>.<br>\n          ✅ That sounds <span class="slot">boring</span>.'),
        ("主语 + have / has + 物品.", "陈述拥有某物。第三人称单数用 has。",
         '✅ I <strong>have</strong> <span class="slot">a basketball</span>.<br>\n          ✅ She <strong>has</strong> <span class="slot">a volleyball</span>.<br>\n          ✅ He <strong>doesn\'t have</strong> <span class="slot">a soccer ball</span>.'),
    ],
    "grammar_tables": [
        ("1️⃣ 一般现在时 have / has",
         [("主语", "肯定句", "否定句", "疑问句"),
          ("I / You / We / They", "I have a ball.", "I don't have a ball.", "Do you have a ball?"),
          ("He / She / It", "She has a ball.", "She doesn't have a ball.", "Does she have a ball?")],
         '📌 <strong>注意：</strong>第三人称单数用 <strong>has</strong>，否定和疑问用 <strong>doesn\'t/Does</strong> + have（还原）。'),
        ("2️⃣ Do / Does 问答对比",
         [("问句", "肯定回答", "否定回答"),
          ("Do you have a pen?", "Yes, I do.", "No, I don't."),
          ("Does she have a pen?", "Yes, she does.", "No, she doesn't."),
          ("Do they have pens?", "Yes, they do.", "No, they don't.")],
         '📌 <strong>助记：</strong>Does 用于 he/she/it，后面动词变回原形。',
         [
             ('Does he has a basketball?', 'Does he have a basketball?'),
             ('He don\'t have a soccer ball.', 'He doesn\'t have a soccer ball.'),
             ('Do she have a volleyball?', 'Does she have a volleyball?'),
         ]),
        ("3️⃣ Let's 祈使句",
         [("结构", "示例", "回答"),
          ("Let's + 动词原形", "Let's play tennis.", "That sounds good."),
          ("Let's + 动词原形 + 地点", "Let's go to the park.", "OK. Let's go!"),
          ("否定：Let's not + 动词原形", "Let's not be late.", "You're right.")],
         '📌 Let\'s = Let us，表示建议。回答可以用 "That sounds good / interesting / boring."'),
    ],
    "exercises": [
        ("基础", "★☆☆", '____ you have a basketball? (Do / Does / Are)',
         "Do", "you 为第二人称，用 Do 提问。"),
        ("基础", "★☆☆", 'She ____ (have) a volleyball.',
         "has", "第三人称单数用 has。"),
        ("基础", "★☆☆", 'Let\'s ____ (play) soccer!',
         "play", "Let's 后跟动词原形。"),
        ("提升", "★★☆", '— Do you have a tennis racket?<br>— No, I ____. But my brother ____ one.',
         "don't; has", "否定回答 don't；brother 第三人称单数用 has。"),
        ("提升", "★★☆", '连词成句：sounds / that / fun / !',
         "That sounds fun!", "That sounds + 形容词。"),
        ("提升", "★★☆", '改错：He don\'t play soccer.',
         "He doesn't play soccer.", "第三人称单数否定用 doesn't + 动词原形。"),
        ("挑战", "★★★", '补全对话：<br>A: ____ you have a baseball bat?<br>B: No, I ____. But Mike ____ one.<br>A: Let\'s ____ him!',
         "Do; don't; has; ask", "一般疑问句 Do；否定 don't；第三人称 has；Let's + 动词原形。"),
        ("挑战", "★★★", '汉译英：我哥哥有一个篮球。他没有足球，但他有排球。',
         "My brother has a basketball. He doesn't have a soccer ball, but he has a volleyball.", "注意第三人称单数 has 和 doesn't have。"),
    ],
    "micro_task": "写一段话，介绍你和你的朋友有什么体育用品，以及你们喜欢一起做什么运动。",
    "model_paras": [
        "I have a basketball and a tennis racket.",
        "My friend Mike doesn't have a basketball, but he has a volleyball.",
        "We often play volleyball together. It is fun!",
        "Does Mike have a baseball? No, he doesn't. But I have a baseball bat.",
        "Let's play sports every day!",
    ],
    "model_trans": "我有一个篮球和一个网球拍。我的朋友 Mike 没有篮球，但他有一个排球。我们经常一起打排球。它很有趣！Mike 有棒球吗？不，他没有。但我有棒球棒。让我们每天做运动吧！",
    "checklist": [
        "我能用 Do you have...? 提问并回答",
        "我能区分 have 和 has 的不同用法",
        "我能用 Let's... 提出建议",
        "我能用 That sounds... 表达看法",
        "我能简单介绍自己和朋友的体育用品",
    ],
    "feynman": "跟同学来一场英语对话——\"Do you have a soccer ball? Let's play together!\"",
    "review": [
        "🔵 1天后：用 Do you have...? 问5个同学他们有什么球类",
        "🟢 3天后：写一段自己和朋友的运动爱好",
        "🟡 1周后：用 Let's 提出建议，与同学做英语对话练习",
        "🔴 1月后：复习 have/has 的一般现在时表格",
    ],
    "next_unit": "6",
    "next_title": "Do you like bananas?",
    "next_desc": "下一单元你将学习用 <strong>Do you like...?</strong> 谈论喜欢的食物，区分可数和不可数名词！",
}

# ====== UNIT 6: Do you like bananas? ======
UNITS["u06"] = {
    "num": "6",
    "title": "Do you like bananas?",
    "subtitle": "谈论食物喜好 · 可数/不可数名词 · like 用法",
    "topic": "Food and eating habits",
    "func": "Express likes and dislikes",
    "grammar": "like 一般现在时 · 可数/不可数名词 · some/any",
    "writing": "描述自己的一日三餐饮食",
    "can_do": [
        'I can ask "Do you like...?" about food.',
        "I can say what I like and don't like.",
        "I can distinguish countable and uncountable nouns.",
        "I can write about what I eat for three meals.",
    ],
    "scene": "午餐时间，Anna 和 Ben 在食堂讨论各自喜欢和不喜欢的食物。",
    "dialogue": [
        ("Anna", "Ben, <em>do you like bananas</em>?"),
        ("Ben", "Yes, I do. I like fruit very much."),
        ("Anna", "Do you like hamburgers?"),
        ("Ben", "No, <em>I don't like hamburgers</em>. They are unhealthy."),
        ("Anna", "What about salad? <em>Do you like salad</em>?"),
        ("Ben", "Yes, I like salad. It's healthy and delicious."),
        ("Anna", "Let's get some salad for lunch!"),
        ("Ben", "Great! I like chicken salad best."),
    ],
    "translation": [
        "Anna: Ben，<em>你喜欢香蕉吗</em>？",
        "Ben: 是的，我喜欢。我非常喜欢水果。",
        "Anna: 你喜欢汉堡包吗？",
        "Ben: 不，<em>我不喜欢汉堡包</em>。它们不健康。",
        "Anna: 沙拉呢？<em>你喜欢沙拉吗</em>？",
        "Ben: 是的，我喜欢沙拉。它又健康又美味。",
        "Anna: 我们午饭买些沙拉吧！",
        "Ben: 太棒了！我最喜欢鸡肉沙拉。",
    ],
    "key_points": [
        ("Do you like bananas?", '询问喜好。<strong>Do + 主语 + like + 食物?</strong> 回答：<strong>Yes, I do.</strong> / <strong>No, I don\'t.</strong>'),
        ("I don't like hamburgers.", '<strong>don\'t like</strong> = do not like，表示「不喜欢」。第三人称用 <strong>doesn\'t like</strong>。'),
        ("I like fruit very much.", '<strong>like + 食物</strong> 表示喜欢某物。可数名词复数表示一类事物（如 bananas），不可数名词直接用原形（如 salad）。'),
        ("Let's get some salad.", '<strong>some</strong> 用于肯定句中表示「一些」。<strong>any</strong> 用于否定和疑问句中。'),
    ],
    "reading_title": "My Eating Habits",
    "reading_paras": [
        "Hello! I'm Anna. Let me tell you about my eating habits.",
        "For breakfast, I like eggs and milk. I don't like bread for breakfast.",
        "For lunch, I like rice, chicken and vegetables. Salad is my favorite.",
        "For dinner, I usually have noodles or porridge. I like fruit after dinner.",
        "I eat healthy food every day. I don't eat too much junk food.",
    ],
    "gloss": [
        ("habit", "/ˈhæbɪt/", "n.", "习惯"),
        ("breakfast", "/ˈbrekfəst/", "n.", "早餐"),
        ("lunch", "/lʌntʃ/", "n.", "午餐"),
        ("dinner", "/ˈdɪnər/", "n.", "晚餐"),
        ("healthy", "/ˈhelθi/", "adj.", "健康的"),
    ],
    "vocab": [
        ("like", "/laɪk/", "v.", "喜欢", "I like apples very much.", "我非常喜欢苹果。"),
        ("banana", "/bəˈnænə/", "n.", "香蕉", "Do you like bananas?", "你喜欢香蕉吗？"),
        ("hamburger", "/ˈhæmbɜːrɡər/", "n.", "汉堡包", "Hamburgers are not healthy.", "汉堡包不健康。"),
        ("tomato", "/təˈmeɪtoʊ/", "n.", "西红柿", "I like tomato and egg soup.", "我喜欢西红柿蛋汤。"),
        ("salad", "/ˈsæləd/", "n.", "沙拉", "Fruit salad is delicious.", "水果沙拉很好吃。"),
        ("chicken", "/ˈtʃɪkɪn/", "n.", "鸡；鸡肉", "Chicken is my favorite meat.", "鸡肉是我最喜欢的肉。"),
        ("rice", "/raɪs/", "n.", "米饭", "We eat rice for lunch.", "我们午饭吃米饭。"),
        ("fruit", "/fruːt/", "n.", "水果", "I like all kinds of fruit.", "我喜欢各种水果。"),
        ("breakfast", "/ˈbrekfəst/", "n.", "早餐", "I have eggs for breakfast.", "我早饭吃鸡蛋。"),
        ("bread", "/bred/", "n.", "面包", "Would you like some bread?", "你想要些面包吗？"),
    ],
    "patterns": [
        ("Do you like + 食物?", "询问对方是否喜欢某种食物。",
         '✅ <strong>Do you like</strong> <span class="slot">bananas</span>?<br>\n          ✅ <strong>Does she like</strong> <span class="slot">salad</span>?<br>\n          ➡ Yes, I do. / No, she doesn\'t.'),
        ("I like + 食物. / I don't like + 食物.", "表达自己的喜好。",
         '✅ I <strong>like</strong> <span class="slot">fruit</span>.<br>\n          ✅ I <strong>don\'t like</strong> <span class="slot">hamburgers</span>.<br>\n          ➡ 第三人称：<strong>He likes</strong> salad. / <strong>She doesn\'t like</strong> meat.'),
        ("What about + 名词/动名词?", "用于提出建议或询问对方意见。",
         '✅ <strong>What about</strong> <span class="slot">salad</span>?<br>\n          ✅ <strong>What about</strong> <span class="slot">playing tennis</span>?<br>\n          ➡ 相当于 \"How about...?\"'),
        ("Let's have / get + 食物.", "提议吃某种食物。",
         '✅ <strong>Let\'s have</strong> <span class="slot">some rice</span>.<br>\n          ✅ <strong>Let\'s get</strong> <span class="slot">some fruit</span>.<br>\n          ➡ 肯定句用 some，否定/疑问句用 any。'),
    ],
    "grammar_tables": [
        ("1️⃣ like 的一般现在时",
         [("主语", "肯定句", "否定句", "疑问句"),
          ("I / You / We / They", "I like apples.", "I don't like apples.", "Do you like apples?"),
          ("He / She / It", "She likes apples.", "She doesn't like apples.", "Does she like apples?")],
         '📌 第三人称单数 <strong>like → likes</strong>；否定用 doesn\'t like（like 还原）；疑问用 Does...like...（like 还原）。'),
        ("2️⃣ 可数名词 vs 不可数名词",
         [("类型", "特点", "示例"),
          ("可数名词（C）", "有单复数形式；可用 a/an", "a banana, two bananas, an apple"),
          ("不可数名词（U）", "没有复数形式；不用 a/an", "rice, bread, milk, salad, chicken"),
          ("修饰词", "可数用 many / a few", "many bananas, a few eggs"),
          ("修饰词", "不可数用 much / a little", "much rice, a little milk")],
         '📌 <strong>对比：</strong>I like <strong>bananas</strong>（可数复数表类别）. I like <strong>rice</strong>（不可数用原形）.'),
    ],
    "exercises": [
        ("基础", "★☆☆", '____ you like salad? (Do / Does / Are)',
         "Do", "you 前用 Do 提问。"),
        ("基础", "★☆☆", 'She ____ (like) bananas.',
         "likes", "第三人称单数 likes。"),
        ("基础", "★☆☆", 'I don\'t like ____ (hamburger).',
         "hamburgers", "可数名词表类别用复数。"),
        ("提升", "★★☆", '— Do you like milk?<br>— Yes, I ____. I ____ milk every morning.',
         "do; drink/have", "肯定回答用 do；每天喝 milk。"),
        ("提升", "★★☆", '改错：He like chicken very much.',
         "He likes chicken very much.", "第三人称单数动词加 -s。"),
        ("提升", "★★☆", '汉译英：我不喜欢面包。但我的妹妹喜欢。',
         "I don't like bread. But my sister likes it.", "don't like；sister 第三人称单数用 likes。"),
        ("挑战", "★★★", '补全对话：<br>A: ____ your brother like ice-cream?<br>B: Yes, he ____. But he ____ (not like) candy.<br>A: That\'s good. Ice-cream is ____ (不健康).',
         "Does; does; doesn't like; unhealthy", "brother 第三人称用 Does；肯定回答 does；否定 doesn't like；unhealthy。"),
        ("挑战", "★★★", '用所给词填空（可数/不可数）：<br>I eat ____ (a / many) rice for lunch. I also have ____ (a / some) vegetables. My sister eats ____ (many / much) fruit every day.',
         "some/many; some; much", "rice 不可数用 much/some；vegetables 可数用 some；fruit 不可数用 much。"),
    ],
    "micro_task": "写一段话介绍你一日三餐的饮食喜好，说明喜欢和不喜欢什么。",
    "model_paras": [
        "Hi! I'm Tom. Let me tell you about my three meals.",
        "For breakfast, I like milk and eggs. I don't like bread.",
        "For lunch, I like rice, chicken and vegetables. Salad is great!",
        "For dinner, I usually have noodles. I like fruit after dinner.",
        "I try to eat healthy food every day.",
    ],
    "model_trans": "嗨！我是 Tom。让我来介绍我的三餐。早餐我喜欢牛奶和鸡蛋。我不喜欢面包。午餐我喜欢米饭、鸡肉和蔬菜。沙拉很不错！晚餐我通常吃面条。我喜欢饭后吃水果。我尽量每天吃健康的食物。",
    "checklist": [
        "我能用 Do you like...? 询问对食物的喜好",
        "我能用 like / don't like 表达个人喜好",
        "我能区分可数名词和不可数名词",
        "我能理解 some 和 any 的基本用法",
        "我能写一段话介绍自己的饮食习惯",
    ],
    "feynman": "用英语说出你一日三餐吃什么——\"For breakfast, I like eggs and milk...\"",
    "review": [
        "🔵 1天后：用 Do you like...? 问家人喜欢什么食物",
        "🟢 3天后：默写10个食品单词并标注可数/不可数",
        "🟡 1周后：写一篇 My Eating Habits 小短文",
        "🔴 1月后：复习 like 一般现在时表格和名词分类",
    ],
    "next_unit": "7",
    "next_title": "How much are these socks?",
    "next_desc": "下一单元你将学习购物场景的表达——<strong>How much is/are...?</strong> 问价格，还会学到衣物的英文名称！",
}

# ====== UNIT 7: How much are these socks? ======
UNITS["u07"] = {
    "num": "7",
    "title": "How much are these socks?",
    "subtitle": "购物对话 · 询问价格 · 衣物名词 · 指示代词",
    "topic": "Shopping and clothes",
    "func": "Ask about prices · Buy and sell",
    "grammar": "How much 问句 · 指示代词 + 名词 · 形容词描述",
    "writing": "写一则促销广告",
    "can_do": [
        'I can ask "How much is/are...?" about prices.',
        "I can use this/that/these/those with clothes.",
        "I can use color and size adjectives.",
        "I can write a simple store ad.",
    ],
    "scene": "Linda 在一家服装店购物，店员在帮她。",
    "dialogue": [
        ("Clerk", "Welcome to our store! <em>Can I help you</em>?"),
        ("Linda", "Yes, please. I need a sweater for school."),
        ("Clerk", "<em>How much is this red sweater</em>?"),
        ("Clerk", "It's 68 dollars."),
        ("Linda", "Oh, it's expensive. Do you have a cheaper one?"),
        ("Clerk", "Yes. <em>How about this blue one</em>? It's 45 dollars."),
        ("Linda", "Great! And how much are these socks?"),
        ("Clerk", "They're 5 dollars for three pairs."),
        ("Linda", "OK, I'll take them!"),
    ],
    "translation": [
        "店员：欢迎光临！<em>我能帮你吗</em>？",
        "Linda: 是的。我需要一件上学穿的毛衣。",
        "店员：<em>这件红毛衣多少钱</em>？",
        "店员：68美元。",
        "Linda: 哦，太贵了。有便宜一点的吗？",
        "店员：有。<em>这件蓝色的怎么样</em>？45美元。",
        "Linda: 太好了！这些袜子多少钱？",
        "店员：5美元三双。",
        "Linda: 好的，我买了！",
    ],
    "key_points": [
        ("Can I help you?", '购物时店员的常用语。也可以说 <strong>What can I do for you?</strong>'),
        ("How much is this red sweater?", '问价格用 <strong>How much is/are...?</strong> 单数物品用 is，复数用 are。回答用 It\'s / They\'re + 价格。'),
        ("How about this blue one?", '<strong>How about...?</strong> 用于提出建议或推荐。这里的 <strong>one</strong> 代替前面提到的名词，避免重复。'),
        ("I'll take it/them.", '<strong>I\'ll take it/them.</strong> = "我买了。" 购物决定购买时的常用表达。'),
    ],
    "reading_title": "A Big Sale!",
    "reading_paras": [
        "Welcome to Fashion Store! We have a big sale this weekend.",
        "Do you need sweaters? We have red, blue and white sweaters for only 45 dollars.",
        "How much are our T-shirts? They are 20 dollars for one and 35 dollars for two.",
        "Socks are only 3 dollars for two pairs. Shoes are 55 dollars.",
        "Come to our store now! You will find great things at good prices!",
    ],
    "gloss": [
        ("sale", "/seɪl/", "n.", "特卖；销售"),
        ("need", "/niːd/", "v.", "需要"),
        ("only", "/ˈoʊnli/", "adv.", "只要；仅仅"),
        ("price", "/praɪs/", "n.", "价格"),
    ],
    "vocab": [
        ("how much", "/haʊ mʌtʃ/", "phrase.", "多少钱", "How much is this shirt?", "这件衬衫多少钱？"),
        ("socks", "/sɒks/", "n.", "袜子（复数）", "These socks are cheap.", "这些袜子很便宜。"),
        ("shoes", "/ʃuːz/", "n.", "鞋子（复数）", "The shoes are 55 dollars.", "这双鞋55美元。"),
        ("shirt", "/ʃɜːrt/", "n.", "衬衫", "I need a white shirt.", "我需要一件白衬衫。"),
        ("shorts", "/ʃɔːrts/", "n.", "短裤（复数）", "The shorts are on sale.", "短裤在打折。"),
        ("sweater", "/ˈswetər/", "n.", "毛衣", "This sweater is very warm.", "这件毛衣很暖和。"),
        ("skirt", "/skɜːrt/", "n.", "裙子", "How much is that skirt?", "那条裙子多少钱？"),
        ("dollar", "/ˈdɒlər/", "n.", "美元", "It is only 10 dollars.", "只要10美元。"),
        ("big", "/bɪɡ/", "adj.", "大的", "I need a big bag.", "我需要一个大包。"),
        ("small", "/smɔːl/", "adj.", "小的", "The small size is fine.", "小号就可以了。"),
    ],
    "patterns": [
        ("How much is/are + 物品?", "询问价格。单数用 is，复数用 are。",
         '✅ <strong>How much is</strong> <span class="slot">this sweater</span>?<br>\n          ➡ <strong>It\'s</strong> 45 dollars.<br>\n          ✅ <strong>How much are</strong> <span class="slot">these socks</span>?<br>\n          ➡ <strong>They\'re</strong> 5 dollars.'),
        ("Can I help you?", "店员招呼顾客的用语。",
         '✅ <strong>Can I help you</strong>?<br>\n          ➡ Yes, please. I need a sweater.<br>\n          ➡ No, thanks. I\'m just looking.'),
        ("How about + 名词/代词?", "提出建议或推荐。",
         '✅ <strong>How about</strong> <span class="slot">this blue one</span>?<br>\n          ✅ <strong>How about</strong> <span class="slot">these shoes</span>?<br>\n          ➡ one 代替前面提到的单数名词。'),
        ("I'll take + 物品.", "决定购买。",
         '✅ <strong>I\'ll take</strong> <span class="slot">it</span>.<br>\n          ✅ <strong>I\'ll take</strong> <span class="slot">them</span>.<br>\n          ➡ 单数用 it，复数用 them。'),
    ],
    "grammar_tables": [
        ("1️⃣ How much 问价格",
         [("句法", "示例"),
          ("How much + is + 单数名词?", "How much <strong>is this skirt</strong>?"),
          ("How much + are + 复数名词?", "How much <strong>are these socks</strong>?"),
          ("回答", "<strong>It's</strong> 45 dollars. / <strong>They're</strong> 5 dollars.")],
         '📌 <strong>注意：</strong>How much 既可以问不可数名词的数量，也可以问价格。问价格时不分可数不可数。'),
        ("2️⃣ 指示代词 + 颜色/大小 + 名词",
         [("结构", "示例"),
          ("this/that + 单数", "this red sweater, that blue shirt"),
          ("these/those + 复数", "these white socks, those black shoes"),
          ("形容词顺序", "this + 颜色 + 名词 (this red skirt)")],
         '📌 <strong>对比：</strong><br>this red sweater（这件红色毛衣——近处）<br>that blue shirt（那件蓝色衬衫——远处）<br>these cheap socks（这些便宜的袜子——复数近处）',
         [
             ('I want buy a shirt.', 'I want to buy a shirt.'),
             ('How much is these shoes?', 'How much are these shoes?'),
             ('I\'ll take it. These sweater is nice.', 'I\'ll take it. This sweater is nice.'),
         ]),
    ],
    "exercises": [
        ("基础", "★☆☆", '____ much is this shirt? (What / How / Where)',
         "How", '问价格用 How much。'),
        ("基础", "★☆☆", 'How much ____ (be) these socks?',
         "are", "socks 是复数，用 are。"),
        ("基础", "★☆☆", 'I\'ll take ____ (it / them). — 指代 the sweater.',
         "it", "sweater 是单数，用 it。"),
        ("提升", "★★☆", 'How much ____ that red skirt? — ____ 68 dollars.',
         "is; It's", "skirt 单数用 is；回答用 It's。"),
        ("提升", "★★☆", '补全对话：<br>Clerk: ____ I help you?<br>You: Yes, please. I ____ a T-shirt.',
         "Can; need", "Can I help you? 固定搭配；need 需要。"),
        ("提升", "★★☆", '汉译英：这双鞋55美元。',
         "These shoes are 55 dollars.", "鞋子 shoes 复数用 are。"),
        ("挑战", "★★★", '改错：How much is these short?',
         "How much are these shorts?", "shorts 是复数用 are；shorts 本身是复数形式。"),
        ("挑战", "★★★", '根据上下文写句子：<br>你想知道那条蓝色裙子多少钱。你问店员：<br>____',
         "How much is that blue skirt?", "that 指远处；问价格用 How much is。"),
    ],
    "micro_task": "假设你是一家服装店的老板，写一则促销广告，介绍你的商品和价格。",
    "model_paras": [
        "Come to Happy Clothes Store! We have a big sale!",
        "Do you need sweaters? We have nice sweaters for only 35 dollars.",
        "How much are our T-shirts? They are 20 dollars for one.",
        "Socks are 4 dollars for two pairs. And shorts are only 25 dollars!",
        "Come and see for yourself! You will love the prices!",
    ],
    "model_trans": "快来快乐服装店！我们正在大促销！你需要毛衣吗？我们有漂亮的毛衣只要35美元。我们的T恤多少钱？20美元一件。袜子4美元两双。短裤只要25美元！快亲自来看看吧！你会爱上这些价格的！",
    "checklist": [
        "我能用 How much is/are...? 问价格",
        "我能用 Can I help you? / I'll take it. 进行购物对话",
        "我能用 this/that/these/those + 颜色 + 名词描述衣物",
        "我能理解 one 代替前面名词的用法",
        "我能写一则简单的促销广告",
    ],
    "feynman": "和同学模拟购物场景——\"Can I help you?\" \"How much is this sweater?\" \"I'll take it.\"",
    "review": [
        "🔵 1天后：用 How much 问5件物品的价格并回答",
        "🟢 3天后：模拟一次完整的购物对话",
        "🟡 1周后：写一则英文促销广告（50词左右）",
        "🔴 1月后：复习价格询问和衣物词汇",
    ],
    "next_unit": "8",
    "next_title": "When is your birthday?",
    "next_desc": "下一单元你将学习用 <strong>When is...?</strong> 问日期，学会12个月份和序数词的表达！",
}

# ====== UNIT 8: When is your birthday? ======
UNITS["u08"] = {
    "num": "8",
    "title": "When is your birthday?",
    "subtitle": "询问日期 · 12个月份 · 序数词 · 日期表达",
    "topic": "Dates and special days",
    "func": "Ask about and give dates",
    "grammar": "When 问句 · 序数词 · 月份和日期表达 · 介词 in/on",
    "writing": "介绍学校日历中的重要事件",
    "can_do": [
        'I can ask "When is your birthday?" and answer.',
        "I can name all 12 months in English.",
        "I can use ordinal numbers (1st, 2nd, 3rd...).",
        "I can write about important dates at school.",
    ],
    "scene": "下课了，Chen Jie 在跟新同学 Lisa 了解对方的生日和学校活动。",
    "dialogue": [
        ("Chen Jie", "Lisa, <em>when is your birthday</em>?"),
        ("Lisa", "My birthday is on September 10th."),
        ("Chen Jie", "Oh, that's Teachers' Day in China, too!"),
        ("Lisa", "Yes! So it's easy to remember. <em>When is your birthday</em>?"),
        ("Chen Jie", "It's on January 15th."),
        ("Lisa", "Cool! Our school has a basketball game in January."),
        ("Chen Jie", "Really? When is it?"),
        ("Lisa", "It's on January 20th. You can come and watch!"),
    ],
    "translation": [
        "Chen Jie: Lisa，<em>你的生日是什么时候</em>？",
        "Lisa: 我的生日是9月10日。",
        "Chen Jie: 哦，在中国那也是教师节！",
        "Lisa: 是的！所以很好记。<em>你的生日呢</em>？",
        "Chen Jie: 在1月15日。",
        "Lisa: 酷！我们学校1月有一场篮球赛。",
        "Chen Jie: 真的？什么时候？",
        "Lisa: 1月20日。你可以来看！",
    ],
    "key_points": [
        ("When is your birthday?", '用 <strong>When</strong> 询问日期。回答用 <strong>It\'s on + 月份 + 日期序数词</strong>。'),
        ("on September 10th", '具体的某一天用介词 <strong>on</strong>。月份首字母要大写。日期用序数词（10th = tenth）。'),
        ("in January", '只说到月份时用介词 <strong>in</strong>（在……月）。月份前不加冠词。'),
        ("January 15th", '日期表达：月份 + 序数词。读作 "January fifteenth"。可以写 January 15 或 January 15th。'),
    ],
    "reading_title": "Our School Calendar",
    "reading_paras": [
        "Welcome to our school! Let me tell you about some important days.",
        "Our school trip is in April. It is on April 12th. We go to the zoo.",
        "The basketball game is on May 20th. I will play in the game!",
        "The English test is on June 15th. I need to study hard.",
        "And the school art festival is in October. It is on October 25th.",
        "What about you? What are the important dates in your school?",
    ],
    "gloss": [
        ("calendar", "/ˈkælɪndər/", "n.", "日历；日程表"),
        ("important", "/ɪmˈpɔːrtənt/", "adj.", "重要的"),
        ("trip", "/trɪp/", "n.", "旅行；出游"),
        ("festival", "/ˈfestɪvl/", "n.", "节日；节庆"),
    ],
    "vocab": [
        ("when", "/wen/", "adv.", "什么时候", "When is the English test?", "英语考试是什么时候？"),
        ("birthday", "/ˈbɜːrθdeɪ/", "n.", "生日", "Happy birthday to you!", "祝你生日快乐！"),
        ("January", "/ˈdʒænjueri/", "n.", "一月", "New Year is in January.", "新年在一月。"),
        ("February", "/ˈfebrueri/", "n.", "二月", "February is the second month.", "二月是第二个月。"),
        ("March", "/mɑːrtʃ/", "n.", "三月", "Spring comes in March.", "春天三月来临。"),
        ("April", "/ˈeɪprəl/", "n.", "四月", "April has 30 days.", "四月有30天。"),
        ("May", "/meɪ/", "n.", "五月", "May is a nice month.", "五月是个好月份。"),
        ("June", "/dʒuːn/", "n.", "六月", "School ends in June.", "学校六月放假。"),
        ("July", "/dʒuːˈlaɪ/", "n.", "七月", "July is very hot.", "七月很热。"),
        ("August", "/ɔːˈɡʌst/", "n.", "八月", "We have a holiday in August.", "八月我们有假期。"),
        ("September", "/sepˈtembər/", "n.", "九月", "School starts in September.", "学校九月开学。"),
        ("October", "/ɒkˈtoʊbər/", "n.", "十月", "The art festival is in October.", "艺术节在十月。"),
        ("November", "/noʊˈvembər/", "n.", "十一月", "November is cold.", "十一月很冷。"),
        ("December", "/dɪˈsembər/", "n.", "十二月", "Christmas is in December.", "圣诞节在十二月。"),
        ("happy", "/ˈhæpi/", "adj.", "快乐的；高兴的", "I am happy today!", "我今天很开心！"),
        ("old", "/oʊld/", "adj.", "……岁的；老的", "How old are you?", "你几岁了？"),
    ],
    "patterns": [
        ("When is + 事件?", "询问日期。",
         '✅ <strong>When is</strong> <span class="slot">your birthday</span>?<br>\n          ➡ It\'s <strong>on</strong> September 10th.<br>\n          ✅ <strong>When is</strong> <span class="slot">the school trip</span>?<br>\n          ➡ It\'s <strong>in</strong> April.'),
        ("It's on + 月份 + 日期序数词.", "回答具体日期。",
         '✅ It\'s on <span class="slot">May 20th</span>.<br>\n          ✅ It\'s on <span class="slot">January 1st</span>.<br>\n          ➡ 序数词缩写：1st, 2nd, 3rd, 4th, 5th...'),
        ("How old + be + 主语?", "询问年龄。",
         '✅ <strong>How old</strong> <span class="slot">are you</span>?<br>\n          ✅ <strong>How old</strong> <span class="slot">is your brother</span>?<br>\n          ➡ 回答：I\'m 13 years old.'),
        ("Happy + 节日/事件 + to you!", "祝福用语。",
         '✅ <strong>Happy birthday</strong> <span class="slot">to you</span>!<br>\n          ✅ <strong>Happy New Year</strong> <span class="slot">to you</span>!<br>\n          ➡ 节日祝福：Happy + 节日名。'),
    ],
    "grammar_tables": [
        ("1️⃣ 12个月份",
         [("序号", "月份", "缩写"),
          ("1月", "January (Jan.)", "31天 | 2月", "February (Feb.)", "28/29天"),
          ("3月", "March (Mar.)", "31天 | 4月", "April (Apr.)", "30天"),
          ("5月", "May (May)", "31天 | 6月", "June (Jun.)", "30天"),
          ("7月", "July (Jul.)", "31天 | 8月", "August (Aug.)", "31天"),
          ("9月", "September (Sep.)", "30天 | 10月", "October (Oct.)", "31天"),
          ("11月", "November (Nov.)", "30天 | 12月", "December (Dec.)", "31天")],
         '📌 <strong>助记：</strong>月份名称首字母必须大写。'),
        ("2️⃣ 序数词（1-31）",
         [("范围", "规律", "示例"),
          ("第1-3", "不规则变化", "first (1st), second (2nd), third (3rd)"),
          ("第4-19", "基数词 + th", "fourth (4th), fifth (5th)...nineteenth (19th)"),
          ("第20-90整十", "y → ie + th", "twentieth (20th), thirtieth (30th)"),
          ("第21-31", "十位不变 + 个位序数", "twenty-first (21st), thirty-first (31st)")],
         '📌 <strong>对比：</strong>five (5) → fifth (5th)；twelve (12) → twelfth (12th)；twenty (20) → twentieth (20th)',
         [
             ('My birthday is in May 10th.', 'My birthday is on May 10th.'),
             ('When is your birthday? It is in June 1st.', 'When is your birthday? It is on June 1st.'),
             ('I am 12 year old.', 'I am 12 years old.'),
         ]),
    ],
    "exercises": [
        ("基础", "★☆☆", '____ is your birthday? (What / When / Where)',
         "When", '问日期用 When。'),
        ("基础", "★☆☆", 'My birthday is ____ May 10th. (in / on / at)',
         "on", "具体某一天用 on。"),
        ("基础", "★☆☆", '____  month of the year is March? (First / Third / Second)',
         "Third", "三月是第三个月。"),
        ("提升", "★★☆", '补全对话：<br>A: When is the English test?<br>B: It\'s ____ June 15th.<br>A: ____ old are you?<br>B: I\'m 13.',
         "on; How", "具体日期用 on；问年龄用 How old。"),
        ("提升", "★★☆", '汉译英：1月是一年中的第一个月。',
         "January is the first month of the year.", 'first 是序数词「第一」。'),
        ("提升", "★★☆", '改错：My birthday is in January 15th.',
         "My birthday is on January 15th.", "具体日期用 on。"),
        ("挑战", "★★★", '按从小到大排序：<br>September 1st, August 20th, October 5th, July 15th',
         "July 15th, August 20th, September 1st, October 5th", "按月份先后排序。"),
        ("挑战", "★★★", '补全短文：<br>My birthday is ____ April. It is ____ April 18th. I am 13 ____ old. My mother\'s birthday is ____ December 3rd. My father\'s birthday is in ____, too.',
         "in; on; years; on; December", "只说到月份用 in；具体日期用 on；years old 年龄。"),
    ],
    "micro_task": "写一段话介绍你的生日和你学校三个重要活动的日期。",
    "model_paras": [
        "Hi! I'm Zhang Wei. My birthday is on March 12th.",
        "I am 13 years old. I like March because spring is beautiful.",
        "Our school has some important events every year.",
        "The school trip is on April 10th. We go to the museum.",
        "The English speech contest is on May 18th. I want to join it.",
        "And the sports meeting is in October. It is on October 15th.",
    ],
    "model_trans": "嗨！我是张伟。我的生日是3月12日。我13岁。我喜欢三月，因为春天很美丽。我们学校每年有一些重要活动。学校旅行在4月10日，我们去博物馆。英语演讲比赛在5月18日，我想参加。运动会在十月，具体是10月15日。",
    "checklist": [
        "我会用 When 问日期并正确回答",
        "我能记住12个月份的英文名称和拼写",
        "我会用序数词表达日期（1st, 2nd, 3rd...）",
        "我能区分 in（月份/年）和 on（具体日期）的用法",
        "我能写一段话介绍重要的日期",
    ],
    "feynman": "不用看笔记，按顺序说出12个月份、1-31的序数词——然后互相问生日。",
    "review": [
        "🔵 1天后：按顺序默写12个月份",
        "🟢 3天后：用 When is...? 问家人的生日并写下来",
        "🟡 1周后：写一篇 Important Dates in My School",
        "🔴 1月后：复习序数词变化规律和日期介词",
    ],
    "next_unit": "9",
    "next_title": "My favorite subject is science.",
    "next_desc": "下一单元你将学习用 <strong>What's your favorite...?</strong> 谈论喜欢的学科，用 <strong>Why...? Because...</strong> 说明理由！",
}

# ====== UNIT 9: My favorite subject is science. ======
UNITS["u09"] = {
    "num": "9",
    "title": "My favorite subject is science.",
    "subtitle": "谈论学科喜好 · 星期名称 · 陈述理由",
    "topic": "School subjects and schedules",
    "func": "Talk about preferences · Give reasons",
    "grammar": "What/Why 特殊疑问句 · because 引导原因 · 形容词描述",
    "writing": "介绍自己最喜欢的学科和课表",
    "can_do": [
        'I can ask "What\'s your favorite subject?" and answer.',
        'I can ask "Why do you like...?" and answer with "Because...".',
        "I can name all 7 days of the week.",
        "I can write about my school schedule and favorite subject.",
    ],
    "scene": "课间，Li Hua 和 Tom 在聊各自最喜欢的科目以及原因。",
    "dialogue": [
        ("Li Hua", "Tom, <em>what's your favorite subject</em>?"),
        ("Tom", "My favorite subject is science. I love doing experiments!"),
        ("Li Hua", "That's cool! <em>Why do you like science</em>?"),
        ("Tom", "Because it is very interesting and useful."),
        ("Li Hua", "Who is your science teacher?"),
        ("Tom", "Mr. Wang. He is a great teacher."),
        ("Li Hua", "What day is your science class?"),
        ("Tom", "It's on Monday and Friday. <em>What subject do you like</em>?"),
        ("Li Hua", "I like English. It's fun and I like to speak it!"),
    ],
    "translation": [
        "Li Hua: Tom，<em>你最喜欢的科目是什么</em>？",
        "Tom: 我最喜欢的科目是科学。我喜欢做实验！",
        "Li Hua: 真酷！<em>你为什么喜欢科学</em>？",
        "Tom: 因为它非常有趣且有用。",
        "Li Hua: 你的科学老师是谁？",
        "Tom: 王老师。他是一位很棒的老师。",
        "Li Hua: 你的科学课在星期几？",
        "Tom: 在周一和周五。<em>你喜欢什么科目</em>？",
        "Li Hua: 我喜欢英语。它很有趣，而且我喜欢说英语！",
    ],
    "key_points": [
        ("What's your favorite subject?", '用 <strong>What\'s your favorite + 类别?</strong> 询问对方最喜欢的人/物。回答用 <strong>My favorite... is...</strong>'),
        ("Why do you like science?", '<strong>Why...?</strong> 问原因。<strong>Because...</strong> 回答。"因为……"是英语中最常用的因果表达。'),
        ("Because it is interesting and useful.", '<strong>Because</strong> 引导原因状语从句。后面跟完整的句子。注意 because 和 so 不能同时使用。'),
        ("What day is your science class?", '问「星期几」用 <strong>What day</strong>。星期名称首字母大写，前面用介词 <strong>on</strong>。'),
    ],
    "reading_title": "My Favorite Subject",
    "reading_paras": [
        "My name is Tom. I am a middle school student.",
        "I have many subjects at school. They are Chinese, math, English, science, history and P.E.",
        "My favorite subject is science. Why do I like it? Because it is very interesting. I like doing experiments.",
        "I also like P.E. It is fun and I can play sports with my friends.",
        "But I don't like history. I think it is a little difficult. What is your favorite subject?",
    ],
    "gloss": [
        ("subject", "/ˈsʌbdʒɪkt/", "n.", "学科；科目"),
        ("experiment", "/ɪkˈsperɪmənt/", "n.", "实验"),
        ("also", "/ˈɔːlsoʊ/", "adv.", "也；还"),
        ("difficult", "/ˈdɪfɪkəlt/", "adj.", "困难的"),
    ],
    "vocab": [
        ("favorite", "/ˈfeɪvərɪt/", "adj.", "最喜欢的", "What is your favorite color?", "你最喜欢的颜色是什么？"),
        ("subject", "/ˈsʌbdʒɪkt/", "n.", "学科", "Math is my favorite subject.", "数学是我最喜欢的科目。"),
        ("science", "/ˈsaɪəns/", "n.", "科学", "Science is very interesting.", "科学很有趣。"),
        ("math", "/mæθ/", "n.", "数学", "I am good at math.", "我擅长数学。"),
        ("English", "/ˈɪŋɡlɪʃ/", "n.", "英语", "I like English class.", "我喜欢英语课。"),
        ("Chinese", "/ˌtʃaɪˈniːz/", "n.", "中文/语文", "Chinese is useful.", "中文很有用。"),
        ("history", "/ˈhɪstəri/", "n.", "历史", "History tells us about the past.", "历史告诉我们过去的事。"),
        ("because", "/bɪˈkɔːz/", "conj.", "因为", "I like art because it is fun.", "我喜欢美术因为它好玩。"),
        ("Monday", "/ˈmʌndeɪ/", "n.", "星期一", "School starts on Monday.", "学校周一开学。"),
        ("Friday", "/ˈfraɪdeɪ/", "n.", "星期五", "We have P.E. on Friday.", "我们周五有体育课。"),
    ],
    "patterns": [
        ("What's your favorite + 类别?", "询问最喜欢的人/事物。",
         '✅ <strong>What\'s your favorite</strong> <span class="slot">subject</span>?<br>\n          ➡ My favorite subject is <span class="slot">science</span>.<br>\n          ✅ <strong>What\'s your favorite</strong> <span class="slot">sport</span>?<br>\n          ➡ My favorite sport is <span class="slot">basketball</span>.'),
        ("Why do you like + 事物?", "询问喜欢的原因。",
         '✅ <strong>Why do you like</strong> <span class="slot">science</span>?<br>\n          ➡ <strong>Because</strong> it is <span class="slot">interesting</span>.<br>\n          ✅ <strong>Why does he like</strong> <span class="slot">math</span>?<br>\n          ➡ <strong>Because</strong> it is <span class="slot">useful</span>.'),
        ("What day is + 课程?", "询问某节课在星期几。",
         '✅ <strong>What day is</strong> <span class="slot">your science class</span>?<br>\n          ➡ It\'s <strong>on</strong> <span class="slot">Monday and Friday</span>.<br>\n          ➡ 星期名称开头大写，用 on。'),
        ("Who is your + 教师类名词?", "询问老师是谁。",
         '✅ <strong>Who is</strong> <span class="slot">your science teacher</span>?<br>\n          ➡ <span class="slot">Mr. Wang</span> is my science teacher.<br>\n          ➡ Mr. 男士/Ms. 女士/Miss 小姐 + 姓氏。'),
    ],
    "grammar_tables": [
        ("1️⃣ 特殊疑问词汇总",
         [("疑问词", "含义", "示例"),
          ("What", "什么", 'What is your favorite subject?'),
          ("When", "什么时候", 'When is your birthday?'),
          ("Where", "在哪里", 'Where is my schoolbag?'),
          ("Who", "谁", 'Who is your teacher?'),
          ("Why", "为什么", 'Why do you like science?'),
          ("How", "怎么样/如何", 'How are you? / How much is it?')],
         '📌 <strong>句型结构：</strong>特殊疑问词 + 一般疑问句语序（疑问词 + be/do/does + 主语 + 其他？）'),
        ("2️⃣ 星期名称",
         [("缩写", "全称"),
          ("Mon.", "Monday（星期一）"),
          ("Tue.", "Tuesday（星期二）"),
          ("Wed.", "Wednesday（星期三）"),
          ("Thu.", "Thursday（星期四）"),
          ("Fri.", "Friday（星期五）"),
          ("Sat.", "Saturday（星期六）"),
          ("Sun.", "Sunday（星期天）")],
         '📌 <strong>注意：</strong>星期名称首字母必须大写。用 on Monday / on Friday。',
         [
             ("Because I like science, so I study hard.", "I like science, so I study hard. / Because I like science, I study hard."),
             ('I like English because it is interesting. Why you like English?', 'I like English because it is interesting. Why do you like English?'),
             ("What's your favorite subject? It's on Monday.", "My favorite subject is science. It's on Monday."),
         ]),
    ],
    "exercises": [
        ("基础", "★☆☆", '____ is your favorite subject? (What / When / Who)',
         "What", "问「什么」用 What。"),
        ("基础", "★☆☆", 'She likes art ____ it is fun. (because / so / but)',
         "because", "说明原因用 because。"),
        ("基础", "★☆☆", '____ do you like English? — Because it is interesting.',
         "Why", "问原因用 Why。"),
        ("提升", "★★☆", 'My favorite ____ (科目) is math.',
         "subject", "科目是 subject。"),
        ("提升", "★★☆", '补全对话：<br>A: ____ is your music teacher?<br>B: ____ Li. She is very nice.',
         "Who; Ms.", "问谁用 Who；Ms. 用于女性。"),
        ("提升", "★★☆", '汉译英：我最喜欢的科目是历史。我觉得它很有趣。',
         "My favorite subject is history. I think it is very interesting.", "注意 favorite 拼写；think 认为。"),
        ("挑战", "★★★", '补全短文：<br>I go to school from ____ to Friday. I have many subjects. My ____ subject is English. I like it ____ I can speak to people from other countries. My English teacher is ____ Green. She is fun.',
         "Monday; favorite; because; Ms.", "周一到周五 from Monday to Friday；favorite；because；Ms. Green。"),
        ("挑战", "★★★", '连句成段：<br>a. I think it is a little difficult but very useful.<br>b. My favorite subject is math.<br>c. Our math teacher is Mr. Chen. He explains everything clearly.<br>d. Why do I like it?',
         "b → d → a → c", "先介绍最喜欢的科目 → 问原因 → 说明原因 → 介绍老师。"),
    ],
    "micro_task": "写一段话介绍你最喜欢的学科和原因，以及这个学科在每周的哪几天上课。",
    "model_paras": [
        "My name is Li Hua. I am a middle school student.",
        "I have many subjects. My favorite subject is English.",
        "Why do I like English? Because it is very useful and interesting.",
        "I like to speak English with my friends. It makes me happy.",
        "I have English classes on Monday, Wednesday and Friday.",
        "My English teacher is Ms. Zhang. She is kind and helpful.",
    ],
    "model_trans": "我叫李华，是一名中学生。我有很多科目。我最喜欢的科目是英语。为什么我喜欢英语？因为它非常有用且有趣。我喜欢和朋友说英语，这让我很开心。我在周一、周三和周五有英语课。我的英语老师是张老师，她和蔼又乐于助人。",
    "checklist": [
        "我能用 What's your favorite...? 询问并回答",
        "我能用 Why...? Because... 说明理由",
        "我能说出并拼写7天的英文名称",
        "我能理解特殊疑问词 What/When/Where/Who/Why/How 的区别",
        "我能写一段话介绍自己喜欢的学科",
    ],
    "feynman": "用英语回答这个问题——\"What is your favorite subject? Why? What day is it?\"",
    "review": [
        "🔵 1天后：默写星期1-7和科目名称",
        "🟢 3天后：用 What/Why/When/Who 互相提问",
        "🟡 1周后：写一篇 My Favorite Subject 小短文",
        "🔴 1月后：复习所有特殊疑问词的用法和区别",
    ],
    "next_unit": "13",
    "next_title": "Can you play the guitar? (七下 U1)",
    "next_desc": "恭喜你完成了七年级上册所有单元！接下来进入七下——第一单元你将学习用 <strong>Can</strong> 谈论能力，还会认识各种乐器！",
}

# ===== GENERATE HTML =====
import re

def gen_html(unit_key, u):
    h = TEMPLATE

    # title
    h = h.replace("Unit 3 Is this your pencil? | 初中英语七年级",
                  f"Unit {u['num']} {u['title']} | 初中英语七年级")

    # === Cover ===
    h = re.sub(r'<div class="sub-en">Unit 3</div>',
               f'<div class="sub-en">Unit {u["num"]}</div>', h)
    h = re.sub(r'<h1>Is this your pencil\?</h1>',
               f'<h1>{u["title"]}</h1>', h)
    h = re.sub(r'<p>确认物品归属 · 物主代词入门 · 失物招领</p>',
               f'<p>{u["subtitle"]}</p>', h)

    # unit-meta
    h = re.sub(r'<span>📖 话题：School things</span>',
               f'<span>📖 话题：{u["topic"]}</span>', h)
    h = re.sub(r'<span>💬 功能：Identify ownership</span>',
               f'<span>💬 功能：{u["func"]}</span>', h)
    h = re.sub(r'<span>📚 语法：指示代词 · 物主代词</span>',
               f'<span>📚 语法：{u["grammar"]}</span>', h)
    h = re.sub(r'<span>📝 写作：Lost & Found</span>',
               f'<span>📝 写作：{u["writing"]}</span>', h)

    # can-do
    can_do_lines = []
    for item in u["can_do"]:
        can_do_lines.append(f'  <label><input type="checkbox"> {item}</label>')
    can_do_block = '\n'.join(can_do_lines)
    h = re.sub(r"<label><input type=\"checkbox\"> I can ask \"Is this/that\.\.\.\?\" and answer \"Yes, it is\.\" / \"No, it isn't\.\"</label>[\s\S]*?<label><input type=\"checkbox\"> I can write a simple lost / found notice\.</label>",
               can_do_block, h)

    # === Dialogue ===
    # scene
    h = re.sub(r'<span style="font-size:13px;color:var\(--text-secondary\);">场景：Ann 和 Tom 在教室捡到一些文具，正在寻找失主。</span>',
               f'<span style="font-size:13px;color:var(--text-secondary);">场景：{u["scene"]}</span>', h)

    # dialogue lines
    dialogue_lines = []
    for speaker, text in u["dialogue"]:
        dia_text_clean = re.sub(r'<[^>]+>', '', text).replace('<em>', '').replace('</em>', '')
        dialogue_lines.append(f'      <div class="dialogue-line">\n        <span class="speaker">{speaker}:</span>\n        <span class="en-text wotd-say" data-speak="{dia_text_clean}">{text}</span>\n      </div>')
    dialogue_block = '\n'.join(dialogue_lines)
    # Replace the dialogue section
    h = re.sub(r'<div class="dialogue" id="dialogueText">[\s\S]*?</div>\n\n    <details style="margin-top:12px;">',
               f'<div class="dialogue" id="dialogueText">\n{dialogue_block}\n    </div>\n\n    <details style="margin-top:12px;">', h)

    # Translation lines
    trans_lines = []
    for t in u["translation"]:
        trans_lines.append(f'        <p>{t}</p>')
    trans_block = '\n'.join(trans_lines)
    h = re.sub(r'<p>Tom: 嘿 Ann！看！<em>这是你的尺子吗？</em></p>[\s\S]*?<p>Ann: 不，不是。<em>我的是黄色的</em>。那些是红色的。</p>',
               trans_block, h)

    # Key points
    key_lines = []
    for title, desc in u["key_points"]:
        key_lines.append(f'      <p><strong>{title}</strong> → {desc}</p>')
    key_block = '\n'.join(key_lines)
    h = re.sub(r'<p><strong>1\.</strong> <em>Is this your ruler\?</em> → "这是你的尺子吗\?" 一般疑问句，把 <strong>be 动词 \(is/are\)</strong> 提到句首\..*?</p>\n      <p><strong>4\.</strong> <em>You\'re welcome\.</em> → "不客气" 固定搭配，回应 Thank you / Thanks\.</p>',
               key_block, h)

    # Reading title
    h = re.sub(r'<h3 style="font-size:15px;color:var\(--accent\);margin:0;">📖 Reading: Lost &amp; Found Notice</h3>',
               f'<h3 style="font-size:15px;color:var(--accent);margin:0;">📖 Reading: {u["reading_title"]}</h3>', h)

    # Reading paragraphs
    reading_paras = []
    for p in u["reading_paras"]:
        reading_paras.append(f'      <p class="en-text" data-speak="{p}">{p}</p>')
    reading_block = '\n'.join(reading_paras)
    h = re.sub(r'<div id="readingEnglish">\n      <div class="notice">\n        <div class="title en-text" data-speak="Found">Found</div>[\s\S]*?</div>\n      </div>',
               f'<div id="readingEnglish">\n{reading_block}\n      </div>', h)

    # Gloss items
    gloss_items = []
    for word, ipa, pos, defn in u["gloss"]:
        gloss_items.append(f'        <span class="gloss-item wotd-say" data-speak="{word}">📘 {word} {ipa} {pos} {defn}</span>')
    gloss_block = '\n'.join(gloss_items)
    h = re.sub(r'<span class="gloss-item wotd-say" data-speak="schoolbag">📘 schoolbag /ˈskuːlbæɡ/ n\. 书包</span>[\s\S]*?<span class="gloss-item wotd-say" data-speak="a set of">📘 a set of 一串 / 一套</span>',
               gloss_block, h)

    # === Vocabulary ===
    vocab_cards = []
    for word, ipa, pos, defn, example, trans in u["vocab"]:
        card = f'''      <div class="vocab-card">
        <span class="headword wotd-say" data-speak="{word}">{word}</span><span class="headword-speak-indicator">🔊</span>
        <span class="ipa">{ipa}</span>
        <span class="pos">{pos}</span>
        <div class="definition">{defn}</div>
        <div class="example"><span class="wotd-say" data-speak="{example}">{example}</span><span class="trans">{trans}</span></div>
      </div>'''
        vocab_cards.append(card)
    vocab_block = '\n'.join(vocab_cards)
    h = re.sub(r'<div class="vocab-grid" id="vocabGrid">[\s\S]*?</div>\n\n    </div>\n  </div>\n</details>',
               f'<div class="vocab-grid" id="vocabGrid">\n{vocab_block}\n    </div>\n\n    </div>\n  </div>\n</details>', h)

    # === Pattern cards ===
    pattern_cards = []
    for i, (structure, desc, substitution) in enumerate(u["patterns"], 1):
        card = f'''      <div class="pattern-card">
        <div class="structure">{structure}</div> <button class="speak-btn" data-target="sp{i}" title="朗读句型">🔊</button>
        <div>{desc}</div>
        <div class="substitution"><span class="q-speak-wrap" id="sp{i}">{substitution}</span></div>
      </div>'''
        pattern_cards.append(card)
    pattern_block = '\n    \n'.join(pattern_cards)
    # Replace pattern grid - we'll do a simple replacement approach
    h = re.sub(r'<div class="pattern-grid">[\s\S]*?</div>\n\n    </div>\n</details>',
               f'<div class="pattern-grid">\n    \n{pattern_block}\n\n    </div>\n\n    </div>\n</details>', h)

    # === Grammar ===
    # We'll reconstruct the grammar section blocks
    grammar_modules = []
    for gt in u["grammar_tables"]:
        title = gt[0]
        table_rows = gt[1]
        note = gt[2] if len(gt) > 2 else ""
        
        # Build table
        table_html = '      <table class="grammar-table">\n'
        for ri, row in enumerate(table_rows):
            if ri == 0:
                table_html += '        <tr>' + ''.join(f'<th>{c}</th>' for c in row) + '</tr>\n'
            else:
                table_html += '        <tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>\n'
        table_html += '      </table>'
        
        # Errors
        error_html = ""
        if len(gt) > 3 and gt[3]:
            error_html = '\n      <div class="chinese-error">\n        <strong>⚠️ 中式英语纠错：</strong><br>\n'
            for wrong, correct in gt[3]:
                error_html += f'        ❌ <span class="wrong wotd-say" data-speak="{wrong}">{wrong}</span><br>\n'
                error_html += f'        ✅ <span class="correct wotd-say" data-speak="{correct}">{correct}</span><br><br>\n'
            error_html += '      </div>'
        
        module = f'''    <div class="grammar-module">
      <h3>{title}</h3>
{table_html}
      <p style="font-size:14px;margin-top:8px;">{note}</p>
{error_html}
    </div>'''
        grammar_modules.append(module)
    
    grammar_block = '\n\n'.join(grammar_modules)
    h = re.sub(r'<div class="grammar-module">\n      <h3>1️⃣ 指示代词：this / that / these / those</h3>[\s\S]*?</div>\n\n  </div>\n</details>',
               f'{grammar_block}\n\n  </div>\n</details>', h)

    # === Exercises ===
    exercise_blocks = []
    tier_labels = {"基础": '🥉 基础关 · 概念识记', "提升": '🥈 提升关 · 语境运用', "挑战": '🥇 挑战关 · 综合运用'}
    current_tier = None
    ex_data = u["exercises"]
    
    for idx, (tier, diff, q_body, answer, explanation) in enumerate(ex_data, 1):
        if current_tier != tier:
            current_tier = tier
            tier_label = tier_labels[tier]
            exercise_blocks.append(f'\n    <h3 style="color:var(--accent);margin:0 0 10px;">{tier_label}</h3>\n')
        
        # Escape text for data-speak
        q_text_clean = re.sub(r'<[^>]+>', '', q_body).replace('<br>', ' ').replace('<br/>', ' ').strip()
        exercise_blocks.append(f'''    <div class="exam-q">
      <span class="q-tag">{tier}</span>
      <span class="q-diff">{diff}</span>
      <div class="q-body"><span class="q-speak-wrap" id="q{idx}">{q_body}</span> <button class="speak-btn" data-target="q{idx}" title="朗读题目">🔊</button></div>
      <span class="q-toggle">📝 查看答案</span>
      <div class="q-solution"><strong>答案：</strong>{answer}<br><strong>解析：</strong>{explanation}</div>
    </div>''')
    
    exercise_block = '\n'.join(exercise_blocks)
    h = re.sub(r'<h3 style="color:var\(--accent\);margin:0 0 10px;">🥉 基础关 · 概念识记</h3>[\s\S]*?</div>\n\n</details>',
               f'{exercise_block}\n\n  </div>\n\n</details>', h)

    # === Micro-writing ===
    model_paras = []
    for p in u["model_paras"]:
        clean = re.sub(r'<[^>]+>', '', p)
        model_paras.append(f'    <p class="en"><span class="wotd-say" data-speak="{clean}">{p}</span></p>')
    model_block = '\n'.join(model_paras)
    h = re.sub(r'<p>假设你丢失了学生证，请用英文写一则寻物启事。注意格式：标题 Lost，描述物品特征，留下联系方式。</p>',
               f'<p>{u["micro_task"]}</p>', h)
    h = re.sub(r'<p class="en"><span class="wotd-say" data-speak="Lost:"><strong>Lost:</strong></span></p>[\s\S]*?<span class="trans">我丢失了学生证。它是蓝白色的，上面有我的名字"张伟"。我必须找到它。请致电 139-1234-5678。谢谢！</span>',
               f'{model_block}\n    <span class="trans">{u["model_trans"]}</span>', h)

    # === Checklist ===
    checklist_items = []
    for item in u["checklist"]:
        checklist_items.append(f'  <label><span class="self-score">🟡→🟢</span><input type="checkbox"> {item}</label>')
    checklist_block = '\n'.join(checklist_items)
    h = re.sub(r'<label><span class="self-score">🟡→🟢</span><input type="checkbox"> 我能分清 this/that/these/those 的区别，并正确使用</label>[\s\S]*?<label><span class="self-score">🟡→🟢</span><input type="checkbox"> 我能写一则英文失物招领启事</label>',
               checklist_block, h)
    
    # Feynman
    h = re.sub(r"<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>\u7528\u82f1\u8bed\u6307\u7740\u8eab\u8fb9\u7684\u7269\u54c1\uff0c\u81ea\u95ee\u81ea\u7b54\u2014\u2014\u201cIs this my pen\? No, it isn't\. It's Tom's pen\.\u201d",
               f'<strong>\U0001f9d1\u200d\U0001f3eb \u8d39\u66fc\u6311\u6218\uff1a</strong>{u["feynman"]}', h)

    # Review schedule
    review_items = []
    for r in u["review"]:
        review_items.append(f'  <span class="review-dot">{r}</span>')
    review_block = '\n'.join(review_items)
    h = re.sub(r'<span class="review-dot">🔵 1天后：重做错题</span>\n  <span class="review-dot">🟢 3天后：口头自问自答物主代词</span>\n  <span class="review-dot">🟡 1周后：写一则完整的失物招领</span>\n  <span class="review-dot">🔴 1月后：复习所有物主代词表格</span>',
               review_block, h)

    # Next stop
    h = re.sub(r'<strong>➡️ 下一单元：Unit 4 Where\'s my schoolbag\?</strong><br>\n  下一单元你将学习用 <strong>Where</strong> 问物品的位置，使用介词 <strong>in / on / under</strong> 描述方位——这在失物招领场景中也会用到！',
               f'<strong>➡️ 下一单元：Unit {u["next_unit"]} {u["next_title"]}</strong><br>\n  {u["next_desc"]}', h)

    # Sidebar active
    h = re.sub(r'<a href="u03\.html" class="active">U3 Is this your pencil\?</a>',
               f'<a href="u03.html">U3 Is this your pencil?</a>', h)
    h = re.sub(f'<a href="{unit_key}\.html">U{u["num"]}',
               f'<a href="{unit_key}.html" class="active">U{u["num"]}', h)

    return h

for key, data in UNITS.items():
    html = gen_html(key, data)
    fname = f"{key}.html"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {fname} created ({len(html)} bytes)")

print("\n🎉 All files generated!")
