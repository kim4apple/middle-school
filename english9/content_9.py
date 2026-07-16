#!/usr/bin/env python3
"""Grade 9全一册 (14 units) teaching content data."""

UNITS_9 = {}

# ==================== Unit 01 ====================
UNITS_9["u01"] = {
    "num": "U1",
    "title": "How can we become good learners?",
    "topic": "学习方法",
    "en_topic": "Learning Methods",
    "functions": "Talk about how to study and learn effectively",
    "grammar": "Verb + by + V-ing; 动名词作主语",
    "writing": "Write about learning methods and strategies",
    "can_do": [
        "能用英语谈论学习方法",
        "能用 by + V-ing 结构描述学习方式",
        "能写关于学习策略的短文",
        "能制定个人学习计划"
    ],
    "dialogue_scene": "Mei和Peter在教室里讨论英语学习方法。",
    "dialogue": [
        ("Mei", "Hi Peter! You look worried. What's wrong?", "嗨，彼得！你看起来有点担心。怎么了？"),
        ("Peter", "I'm having trouble learning English. I can't remember the new words.", "我学英语有困难。我记不住新单词。"),
        ("Mei", "Don't worry! I can help you. How do you study vocabulary?", "别担心！我可以帮你。你怎么学词汇的？"),
        ("Peter", "I just read the textbook again and again. But it doesn't seem to work.", "我就一遍一遍地读课本。但似乎没什么用。"),
        ("Mei", "You should try making word cards. I study by making flashcards.", "你应该试试做单词卡。我通过制作闪卡来学习。"),
        ("Peter", "That sounds helpful! What about listening and speaking?", "听起来很有帮助！那听力和口语呢？"),
        ("Mei", "I improve my listening by watching English movies. And I practice speaking by talking with friends.", "我通过看英文电影来提高听力。我通过和朋友交谈来练习口语。"),
        ("Peter", "Great ideas! I'll try them. Thanks, Mei!", "好主意！我试试看。谢谢你，梅！")
    ],
    "key_points": [
        "have trouble doing sth 做某事有困难 — Peter said he was having trouble <b>learning</b> English.",
        "by + V-ing 表示「通过……方式」 — I study <b>by making</b> flashcards.",
        "What about...? 用来提建议 — <b>What about</b> listening to English songs?",
        "It doesn't seem to work. 表示「似乎没什么用」 — 用于评价方法的有效性。"
    ],
    "vocab": [
        ("textbook", "ˈtekstbʊk", "n.", "教科书；课本", "Open your textbook to page 10.", "打开课本到第10页。"),
        ("pronunciation", "prəˌnʌnsiˈeɪʃn", "n.", "发音；读音", "Your pronunciation is getting better!", "你的发音越来越好了！"),
        ("sentence", "ˈsentəns", "n.", "句子", "Can you make a sentence with this word?", "你能用这个词造个句子吗？"),
        ("patient", "ˈpeɪʃnt", "adj.", "有耐心的", "Be patient! Learning takes time.", "耐心点！学习需要时间。"),
        ("expression", "ɪkˈspreʃn", "n.", "表达；表情", "This is a useful expression.", "这是一个有用的表达。"),
        ("discover", "dɪˈskʌvər", "v.", "发现；发觉", "I discovered a good way to learn grammar.", "我发现了一个学语法的好方法。"),
        ("secret", "ˈsiːkrət", "n.", "秘密；秘诀", "The secret to learning is practice.", "学习的秘诀是练习。"),
        ("repeat", "rɪˈpiːt", "v.", "重复", "Please repeat the sentence after me.", "请跟着我重复这个句子。"),
        ("note", "noʊt", "n.", "笔记；记录", "I always take notes in class.", "我总是在课堂上做笔记。"),
        ("increase", "ɪnˈkriːs", "v.", "增加；增长", "Reading helps increase your vocabulary.", "阅读有助于增加词汇量。"),
        ("speed", "spiːd", "n.", "速度", "You need to improve your reading speed.", "你需要提高阅读速度。"),
        ("partner", "ˈpɑːrtnər", "n.", "伙伴；搭档", "Practice with a partner.", "和伙伴一起练习。"),
        ("born", "bɔːrn", "v.", "出生；天生", "She was born with a talent for music.", "她天生有音乐天赋。"),
        ("ability", "əˈbɪləti", "n.", "能力；才能", "Everyone has the ability to learn.", "每个人都有学习的能力。"),
        ("create", "kriˈeɪt", "v.", "创造；创建", "Create a study plan for yourself.", "为自己创建一个学习计划。"),
        ("brain", "breɪn", "n.", "大脑", "The brain needs exercise too.", "大脑也需要锻炼。"),
        ("active", "ˈæktɪv", "adj.", "活跃的；积极的", "Stay active in class discussions.", "在课堂讨论中保持积极。"),
        ("attention", "əˈtenʃn", "n.", "注意；关注", "Pay attention to your pronunciation.", "注意你的发音。"),
        ("connect", "kəˈnekt", "v.", "连接；联系", "Connect new words with what you already know.", "把新词和你已知的联系起来。"),
        ("knowledge", "ˈnɒlɪdʒ", "n.", "知识；学问", "Knowledge comes from practice.", "知识来源于实践。"),
        ("review", "rɪˈvjuː", "v./n.", "复习；回顾", "Review your notes after class.", "课后复习你的笔记。"),
        ("wise", "waɪz", "adj.", "明智的；聪明的", "It's wise to learn from mistakes.", "从错误中学习是明智的。")
    ],
    "patterns": [
        ("Verb + by + V-ing",
         "表示「通过做某事来……」，回答 how 引导的问句。",
         "I learn English <b>by listening</b> to English songs. / She improved her speaking <b>by practicing</b> every day."),
        ("What about + V-ing?",
         "用来提出建议或询问看法。",
         "<b>What about</b> joining an English club? / <b>What about</b> reading English newspapers?"),
        ("It + adj + to do sth",
         "描述做某事是怎么样的。",
         "<b>It is important to</b> review after class. / <b>It is helpful to</b> read aloud every morning."),
        ("The + 比较级, the + 比较级",
         "表示「越……就越……」",
         "<b>The more</b> you read, <b>the faster</b> you will become. / <b>The harder</b> you work, <b>the better</b> results you get.")
    ],
    "grammar_title": "Verb + by + V-ing 结构",
    "grammar_sections": [
        ("基本结构", [
            ("结构", "用法", "例句"),
            ("by + 动名词", "表示「通过做某事的方式」", "I learn English by watching movies."),
            ("by + 名词", "表示「通过某种方式」", "Please contact me by email."),
            ("how 问句 + by 结构", "问「如何做某事」", "How do you study for a test? I study by working with a group.")
        ]),
        ("动名词作主语", [
            ("功能", "结构", "例句"),
            ("作主语", "V-ing + is/was + ...", "Reading aloud is very important."),
            ("形式主语", "It is + adj + V-ing", "It's no use crying over spilt milk."),
            ("否定形式", "not + V-ing", "Not reviewing will lead to forgetting.")
        ])
    ],
    "grammar_tips": [
        "by 后面只能跟名词或动名词，不能跟动词原形。",
        "动名词作主语时，谓语动词用第三人称单数。",
        "区分 by 和 with：by 表示「通过某种方式」，with 表示「用某种工具」。",
        "<span class=\"wotd-say\" data-speak=\"Practice makes perfect.\">Practice makes perfect.</span> 熟能生巧。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "How do you study for a test? I study ____ making flashcards.", "by"),
        ("基础", "★☆☆", "____ (read) aloud is a good way to practice pronunciation.", "Reading"),
        ("基础", "★☆☆", "It's important ____ (review) notes after class.", "to review"),
        ("基础", "★☆☆", "She improves her listening ____ watching English TV shows.", "by"),
        ("基础", "★☆☆", "What ____ joining an English club? That sounds great!", "about")
    ],
    "mid_qs": [
        ("提升", "★★☆", "____ carefully you listen, ____ you will understand.<br>A. The more; the better B. More; better C. Most; best D. The most; the best", "A"),
        ("提升", "★★☆", "I have trouble ____ (remember) new words. Can you help me?", "remembering"),
        ("提升", "★★☆", "The secret ____ becoming a good learner is to practice every day.<br>A. to B. of C. for D. in", "A"),
        ("提升", "★★☆", "Rewrite: I study English. I listen to English songs. (Use by) →", "I study English by listening to English songs."),
        ("提升", "★★☆", "____ (watch) English movies is a fun way to learn.", "Watching")
    ],
    "hard_qs": [
        ("挑战", "★★★", "阅读理解：Read the passage and answer: Why is it important to make mistakes when learning a language?", "Mistakes help you learn what is correct and improve your skills."),
        ("挑战", "★★★", "写作：Write a short paragraph about how you learn English, using at least three by + V-ing structures.", "Sample: I learn English by reading English news. I practice speaking by talking with my friends. I also improve my writing by keeping a diary."),
        ("挑战", "★★★", "完成句子：The more you practice your spoken English, ____ (你的英语就会说得越流利).", "the more fluently you will speak English"),
        ("挑战", "★★★", "改错：By practice every day, I improved my grades. (找出错误并改正)", "By practicing every day, I improved my grades.")
    ],
    "reading_title": "How I Learned to Learn English",
    "reading_text": [
        "Last year, I did not like my English class. Every class was like a bad dream. The teacher spoke too quickly. But I was afraid to ask questions because my pronunciation was very bad. So I just hid behind my textbook and never said anything.",
        "Then one day I watched an English movie called Toy Story. I fell in love with this exciting and funny movie! So I began to watch other English movies as well. My pronunciation improved as well by listening to the conversations in English movies.",
        "I discovered that listening to something interesting is the secret to language learning. I also learned useful sentences like «It's a piece of cake» or «It serves you right». I did not understand these sentences at first. But because I wanted to understand the story, I looked them up in a dictionary.",
        "Now I really enjoy my English class. I want to learn new words and more grammar. Then I can have a better understanding of English movies."
    ],
    "reading_gloss": [
        ("as well", "也；同样"),
        ("at first", "起初"),
        ("look up", "查阅"),
        ("a piece of cake", "小菜一碟；很容易"),
        ("It serves you right", "你活该")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "Why did the writer hide behind the textbook?", "Because she was afraid to ask questions and her pronunciation was very bad."),
        ("阅读", "★★☆", "How did the writer's listening improve?", "By listening to the conversations in English movies."),
        ("阅读", "★★☆", "What does «a piece of cake» mean?", "It means something is very easy."),
        ("阅读", "★★★", "What is the secret to language learning according to the passage?", "Listening to something interesting.")
    ],
    "exam_q_type": "阅读理解 — 推理判断",
    "exam_q": "阅读短文，选择最佳答案。",
    "exam_passage": [
        "Many students ask for advice about how to improve their English. There are three common questions. The first question is about real English. Watching English films and TV programs is a great way to learn English. The second question is about speaking. The best way to improve speaking is to speak as much as possible. The third question is about vocabulary. The best way to learn new words is to read English newspapers and magazines."
    ],
    "exam_options": [
        (1, {"A": "Watching films is a bad way to learn.", "B": "Watching English films helps learn English.", "C": "Only TV programs help.", "D": "Films are not real English."}),
        (2, {"A": "Read more books.", "B": "Speak as much as possible.", "C": "Write more sentences.", "D": "Listen to the teacher."}),
        (3, {"A": "By watching films.", "B": "By reading newspapers and magazines.", "C": "By asking teachers.", "D": "By writing diaries."})
    ],
    "exam_answers": ["1. B", "2. B", "3. B"],
    "writing_prompt": "你的朋友李明在学习英语方面遇到了困难。请给他写一封信，提出至少三条学习英语的建议，并说明理由。",
    "writing_framework": [
        "开头：问候 + 表示理解对方的困难",
        "主体1：第一条建议 + 理由和例子",
        "主体2：第二条建议 + 如何实施",
        "主体3：第三条建议 + 预期效果",
        "结尾：鼓励 + 祝福"
    ],
    "writing_model_en": "Dear Li Ming,\n\nI'm sorry to hear that you are having trouble learning English. Don't worry! I'd like to give you some advice.\n\nFirst, you can improve your English by listening to English songs. This will help you learn new words in a fun way. Second, try to speak English every day by talking with your classmates. Don't be afraid of making mistakes! Third, it's helpful to keep a diary in English. Writing every day can improve your writing skills.\n\nI hope these suggestions are helpful. Keep going and you will make progress!\n\nYours,\nMei",
    "writing_model_cn": "亲爱的李明：\n\n听说你在学英语方面遇到了困难，我很难过。别担心！我想给你一些建议。\n\n首先，你可以通过听英文歌来提高英语。这会帮助你以有趣的方式学习新单词。其次，试着每天通过和同学交谈来说英语。别害怕犯错误！第三，用英语写日记是很有帮助的。每天写作可以提高你的写作技能。\n\n希望这些建议有用。坚持下去，你会取得进步的！\n\n你的朋友，\n梅",
    "project_title": "My English Learning Plan",
    "project_desc": "制定一个为期一个月的英语学习计划，包括每日和每周的学习目标。",
    "project_steps": [
        "反思你目前的英语水平和薄弱环节",
        "设定一个具体、可衡量的月目标",
        "制定每日学习计划（10-15分钟可完成的小任务）",
        "设计每周复习计划",
        "和同伴分享并互相评价计划",
        "开始执行并记录进展"
    ],
    "project_rubric": [
        "目标具体且可衡量",
        "计划包含听、说、读、写四个方面",
        "有明确的复习安排",
        "计划切实可行、可持续",
        "与同伴的互评有建设性"
    ],
    "checklist": [
        "我能理解 by + V-ing 的用法",
        "我能用英语描述学习方法",
        "我能掌握本节课的核心词汇",
        "我能理解阅读文章的主旨大意",
        "我能制定并描述学习计划"
    ],
    "feynman": "用英语向同桌解释 how questions + by + V-ing 结构，并举例说明。",
    "review": [
        "🔵 1天后：复习 by + V-ing 结构",
        "🟢 3天后：复习本单元词汇",
        "🟡 1周后：阅读文章复述",
        "🔴 1月后：写作练习 — 给朋友的学习建议"
    ],
    "next_unit_title": "U2: I think that mooncakes are delicious!",
    "next_unit_desc": "学习宾语从句，了解中外节日文化。"
}

# ==================== Unit 02 ====================
UNITS_9["u02"] = {
    "num": "U2",
    "title": "I think that mooncakes are delicious!",
    "topic": "节日与文化",
    "en_topic": "Festivals and Culture",
    "functions": "Express opinions and talk about festivals",
    "grammar": "Object clauses with that/if/whether",
    "writing": "Describe a festival and personal feelings",
    "can_do": [
        "能用宾语从句表达观点",
        "能描述中外重要节日",
        "能谈论节日的传统和习俗",
        "能写一篇介绍节日的短文"
    ],
    "dialogue_scene": "Wu Ming和Harry在谈论中秋节的经历。",
    "dialogue": [
        ("Harry", "Hi Wu Ming! How was your trip to your hometown?", "嗨，吴明！你回老家的旅行怎么样？"),
        ("Wu Ming", "It was great! I went back for the Mid-Autumn Festival.", "太棒了！我回去过中秋节了。"),
        ("Harry", "I think that mooncakes are delicious! What did you do?", "我觉得月饼很好吃！你们都做什么了？"),
        ("Wu Ming", "My family got together and had a big dinner. Then we watched the full moon.", "我们家人聚在一起吃了顿大餐。然后我们赏月了。"),
        ("Harry", "That sounds wonderful. I wonder if they have mooncakes in other countries.", "听起来很棒。我想知道其他国家有没有月饼。"),
        ("Wu Ming", "I'm not sure if they do. But I know that many countries celebrate harvest festivals.", "我不确定。但我知道很多国家都庆祝丰收节。"),
        ("Harry", "I believe that festivals are a time for family and sharing.", "我相信节日是家人团聚和分享的时刻。"),
        ("Wu Ming", "I agree. I think that the best part of a festival is being with family.", "我同意。我觉得节日最棒的部分就是和家人在一起。")
    ],
    "key_points": [
        "I think that... 引导宾语从句，表示「我认为……」 — <b>I think that</b> mooncakes are delicious.",
        "I wonder if/whether... 表示「我想知道是否……」 — <b>I wonder if</b> they have mooncakes in other countries.",
        "宾语从句的语序用陈述语序，不用疑问语序。",
        "that 在口语中常可省略，if/whether 不可省略。"
    ],
    "vocab": [
        ("mooncake", "ˈmuːnkeɪk", "n.", "月饼", "We eat mooncakes on Mid-Autumn Festival.", "我们中秋节吃月饼。"),
        ("lantern", "ˈlæntərn", "n.", "灯笼", "Children carry lanterns on Lantern Festival.", "孩子们在元宵节提灯笼。"),
        ("stranger", "ˈstreɪndʒər", "n.", "陌生人", "Don't talk to strangers.", "不要和陌生人说话。"),
        ("relative", "ˈrelətɪv", "n.", "亲戚；亲属", "We visit relatives during Spring Festival.", "我们春节期间走亲戚。"),
        ("steal", "stiːl", "v.", "偷；窃取", "Someone stole my wallet.", "有人偷了我的钱包。"),
        ("tie", "taɪ", "v.", "捆；绑；系", "Tie the ribbon onto the gift.", "把丝带系在礼物上。"),
        ("admire", "ədˈmaɪər", "v.", "欣赏；仰慕", "We admire the full moon on Mid-Autumn Festival.", "我们中秋节赏月。"),
        ("goddess", "ˈɡɒdəs", "n.", "女神", "Chang'e is the goddess of the moon.", "嫦娥是月亮女神。"),
        ("whoever", "huːˈevər", "pron.", "无论谁；不管什么人", "Whoever steals the magic medicine will fly to the moon.", "无论是谁偷了仙药都会飞到月亮上。"),
        ("folk", "foʊk", "adj.", "民间的", "I love folk stories.", "我喜欢民间故事。"),
        ("dessert", "dɪˈzɜːrt", "n.", "甜点；甜品", "We had ice cream for dessert.", "我们吃了冰淇淋当甜点。"),
        ("garden", "ˈɡɑːrdn", "n.", "花园", "There is a beautiful garden behind the house.", "房子后面有一个漂亮的花园。"),
        ("tradition", "trəˈdɪʃn", "n.", "传统", "It's a tradition to eat dumplings on New Year's Eve.", "除夕吃饺子是一个传统。"),
        ("celebrate", "ˈselɪbreɪt", "v.", "庆祝", "How do you celebrate Christmas?", "你怎样庆祝圣诞节？"),
        ("treat", "triːt", "n./v.", "款待；请客", "The kids got treats on Halloween.", "孩子们在万圣节得到了款待。"),
        ("ghost", "ɡoʊst", "n.", "鬼；幽灵", "Ghost stories are popular on Halloween.", "鬼故事在万圣节很受欢迎。"),
        ("spider", "ˈspaɪdər", "n.", "蜘蛛", "A spider is on the wall.", "墙上有一只蜘蛛。"),
        ("Christmas", "ˈkrɪsməs", "n.", "圣诞节", "We exchange gifts at Christmas.", "我们在圣诞节交换礼物。"),
        ("novel", "ˈnɒvl", "n.", "小说", "Have you read this novel?", "你读过这部小说吗？"),
        ("present", "ˈpreznt", "n.", "礼物", "I got a nice present from my parents.", "我从父母那里收到了一份好礼物。"),
        ("warmth", "wɔːrmθ", "n.", "温暖；温情", "The warmth of family makes me happy.", "家庭的温暖让我开心。"),
        ("spread", "spred", "v.", "传播；展开", "Spread joy and love this holiday season.", "在这个节日季传播快乐和爱。")
    ],
    "patterns": [
        ("I think that...",
         "表达个人观点，后跟宾语从句。",
         "<b>I think that</b> mooncakes are delicious. / <b>I think that</b> festivals are important for families."),
        ("I wonder if/whether...",
         "礼貌地表达疑问或好奇。",
         "<b>I wonder if</b> he likes mooncakes. / <b>I wonder whether</b> they celebrate Christmas in China."),
        ("I believe that...",
         "表达信念或强烈看法。",
         "<b>I believe that</b> festivals bring people together. / <b>I believe that</b> kindness is the best gift."),
        ("主语 + 动词 + that 从句",
         "that 引导的宾语从句作动词的宾语。",
         "She <b>knows that</b> I love dumplings. / They <b>said that</b> the festival was amazing.")
    ],
    "grammar_title": "宾语从句 (Object Clauses)",
    "grammar_sections": [
        ("that 引导的宾语从句", [
            ("引导词", "用法", "例句"),
            ("that", "that 无实义，可省略", "I think (that) mooncakes are delicious."),
            ("that", "用于陈述句作宾语", "She knows (that) I like festivals."),
            ("that", "谓语动词 + that 从句", "He said (that) he enjoyed the dinner.")
        ]),
        ("if / whether 引导的宾语从句", [
            ("引导词", "用法", "例句"),
            ("if", "表示「是否」，用于口语", "I wonder if he likes mooncakes."),
            ("whether", "表示「是否」，正式用法", "I wonder whether they celebrate it too."),
            ("if/whether", "从句用陈述语序", "I'm not sure if she will come.")
        ])
    ],
    "grammar_tips": [
        "宾语从句的语序必须是陈述句语序：主语 + 谓语。",
        "如果主句是一般现在时，从句可以用任何需要的时态。",
        "如果主句是一般过去时，从句要用相应的过去时态。",
        "<span class=\"wotd-say\" data-speak=\"It takes a village to raise a child.\">It takes a village to raise a child.</span> 反映了集体主义文化。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "I think ____ mooncakes are delicious. (填入引导词)", "that"),
        ("基础", "★☆☆", "I wonder ____ he likes mooncakes. (if/whether/that)", "if 或 whether"),
        ("基础", "★☆☆", "变换语序：Where does she live? → I don't know ____.", "I don't know where she lives."),
        ("基础", "★☆☆", "She said (that) ____ (she/be) happy.", "she was"),
        ("基础", "★☆☆", "____ (who) steals the medicine will fly to the moon.", "Whoever")
    ],
    "mid_qs": [
        ("提升", "★★☆", "I'm not sure ____ he will come to the party.<br>A. that B. if C. what D. which", "B"),
        ("提升", "★★☆", "The teacher told us that the earth ____ (go) around the sun.", "goes"),
        ("提升", "★★☆", "Do you know ____?<br>A. where does he live B. where he lives C. he lives where D. does he live where", "B"),
        ("提升", "★★☆", "She wondered ____ the story was true. (if/whether/that)", "if 或 whether"),
        ("提升", "★★☆", "翻译：我认为家庭团聚是节日最重要的部分。", "I think that family reunion is the most important part of festivals.")
    ],
    "hard_qs": [
        ("挑战", "★★★", "改错：I wonder that he will come or not. (找出错误并改正)", "将 that 改为 whether"),
        ("挑战", "★★★", "合并句子：a) He is a teacher. b) I think so. →", "I think that he is a teacher."),
        ("挑战", "★★★", "阅读理解：Why do people celebrate the Mid-Autumn Festival? (根据课文内容回答)", "People celebrate to admire the full moon and enjoy family reunion."),
        ("挑战", "★★★", "写作：介绍一个你最喜欢的节日，使用至少两个宾语从句。", "Sample: I think that Spring Festival is the most important holiday. I believe that family reunion is the best part of it.")
    ],
    "reading_title": "The Story of Chang'e",
    "reading_text": [
        "Chinese people have been celebrating the Mid-Autumn Festival and enjoying mooncakes for centuries. Mooncakes are in the shape of a full moon on the night of the Mid-Autumn Festival.",
        "There are many traditional folk stories about this festival. One of the most famous is the story of Chang'e. Hou Yi, a young man, shot down nine suns and saved the earth. As a reward, he was given a magic medicine. Anyone who took this medicine would live forever.",
        "Hou Yi did not want to take the medicine without his wife, Chang'e. So he asked her to keep it safe. A bad man tried to steal the medicine, but Chang'e refused to give it to him and drank it herself. She flew up to the moon and became the goddess of the moon.",
        "Hou Yi was sad. Every night, he looked at the moon and thought of his wife. The story shows the Chinese people's love for family and peace."
    ],
    "reading_gloss": [
        ("for centuries", "几个世纪以来"),
        ("in the shape of", "以……形状"),
        ("folk story", "民间故事"),
        ("shot down", "射下"),
        ("as a reward", "作为奖赏"),
        ("forever", "永远")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What shape are mooncakes?", "They are in the shape of a full moon."),
        ("阅读", "★★☆", "Why did Hou Yi get the magic medicine?", "Because he shot down nine suns and saved the earth."),
        ("阅读", "★★☆", "Why did Chang'e drink the medicine?", "Because a bad man tried to steal it, and she refused to give it to him."),
        ("阅读", "★★★", "What does the story of Chang'e show about Chinese people?", "It shows Chinese people's love for family and peace.")
    ],
    "exam_q_type": "完形填空 — 节日文化",
    "exam_q": "阅读短文，选择最佳答案填入空白处。",
    "exam_passage": [
        "The Mid-Autumn Festival is one of the most important 1 in China. It falls on the 15th day of the 8th lunar month. On this night, the moon is 2 and bright. People get together with their families and have a big dinner. After dinner, they 3 the full moon and eat mooncakes. The mooncake is a symbol of family reunion. Children love to hear the 4 of Chang'e flying to the moon."
    ],
    "exam_options": [
        (1, {"A": "festivals", "B": "festival", "C": "food", "D": "months"}),
        (2, {"A": "small", "B": "round", "C": "long", "D": "thin"}),
        (3, {"A": "admire", "B": "dislike", "C": "hate", "D": "forget"}),
        (4, {"A": "song", "B": "story", "C": "book", "D": "news"})
    ],
    "exam_answers": ["1. A", "2. B", "3. A", "4. B"],
    "writing_prompt": "假设你是李华，你的美国笔友Tom想了解中国的春节。请给他写一封邮件，介绍春节的时间、习俗和庆祝活动。",
    "writing_framework": [
        "开头：问候 + 表达欣喜",
        "介绍春节的时间和意义",
        "描述春节前的准备工作（大扫除、贴春联等）",
        "描述除夕的活动（年夜饭、守岁等）",
        "描述春节期间的活动（拜年、红包等）",
        "结尾：邀请对方来中国体验春节"
    ],
    "writing_model_en": "Dear Tom,\n\nI'm glad to hear that you are interested in the Spring Festival. Let me tell you something about it.\n\nThe Spring Festival is the most important festival in China. It usually comes in January or February. Before the festival, people clean their houses and put up couplets on the doors.\n\nOn New Year's Eve, families get together for a big dinner. We eat dumplings and stay up late. Children love this festival because they can get red packets with money inside!\n\nDuring the festival, people visit relatives and friends. Everyone says «Happy New Year» to each other. I think that the Spring Festival is a time for joy and family reunion.\n\nI hope you can come to China and experience it yourself!\n\nYours,\nLi Hua",
    "writing_model_cn": "亲爱的汤姆：\n\n很高兴听说你对春节感兴趣。让我给你介绍一下。\n\n春节是中国最重要的节日。它通常在一月或二月到来。节日前，人们打扫房子并在门上贴春联。\n\n在除夕夜，家人聚在一起吃大餐。我们吃饺子，熬夜。孩子们喜欢这个节日，因为他们能得到装着钱的红包！\n\n春节期间，人们走亲访友。大家互相说「新年快乐」。我认为春节是欢乐和家庭团聚的时刻。\n\n希望你能来中国亲自体验一下！\n\n你的朋友，\n李华",
    "project_title": "World Festivals Research Report",
    "project_desc": "选择一个你感兴趣的外国节日，研究它的起源、习俗和意义，制作一份图文并茂的报告。",
    "project_steps": [
        "选择一个外国节日（如圣诞节、万圣节、感恩节等）",
        "查阅资料，了解节日的起源和历史",
        "整理节日的习俗、食物和活动",
        "思考这个节日和哪个中国节日相似",
        "制作报告（海报/PowerPoint/手抄报）",
        "在班级中展示并回答同学的提问"
    ],
    "project_rubric": [
        "信息准确、来源可靠",
        "内容包含节日的起源、习俗和意义",
        "有中外节日的对比",
        "排版美观、图文并茂",
        "口头展示清晰、自信"
    ],
    "checklist": [
        "我能理解 that/if/whether 引导的宾语从句",
        "我能准确使用宾语从句表达观点",
        "我能用英语介绍中秋节的故事",
        "我能写一篇介绍节日的作文",
        "我了解了嫦娥奔月的民间故事"
    ],
    "feynman": "向同桌讲述嫦娥奔月的故事，并说出故事中使用的宾语从句。",
    "review": [
        "🔵 1天后：复习宾语从句的引导词选择",
        "🟢 3天后：复习节日相关词汇",
        "🟡 1周后：复述嫦娥奔月的故事",
        "🔴 1月后：写一篇关于春节的短文"
    ],
    "next_unit_title": "U3: Could you please tell me where the restrooms are?",
    "next_unit_desc": "学习礼貌请求和宾语从句的疑问词用法。"
}

# ==================== Unit 03 ====================
UNITS_9["u03"] = {
    "num": "U3",
    "title": "Could you please tell me where the restrooms are?",
    "topic": "问路与请求",
    "en_topic": "Asking for Directions and Requests",
    "functions": "Ask for information politely; give directions",
    "grammar": "Object clauses with wh-questions; polite requests",
    "writing": "Write a polite request or ask for directions",
    "can_do": [
        "能用英语礼貌地问路",
        "能听懂并给出方向指引",
        "能用宾语从句转述疑问句",
        "能在不同场合使用礼貌语言"
    ],
    "dialogue_scene": "一名游客在街上向警察询问如何到达最近的超市。",
    "dialogue": [
        ("Tourist", "Excuse me, could you please tell me where the nearest supermarket is?", "打扰一下，您能告诉我最近的超市在哪里吗？"),
        ("Police", "Sure! Go straight along this street. Then turn left at the second crossing.", "当然！沿着这条街直走，然后在第二个路口左转。"),
        ("Tourist", "Is it far from here? I wonder how long it takes to get there.", "离这里远吗？我想知道到那里要多长时间。"),
        ("Police", "It's about a ten-minute walk. You can also take the bus.", "大约步行10分钟。你也可以坐公交车。"),
        ("Tourist", "Could you tell me which bus I should take?", "你能告诉我应该坐哪路公交车吗？"),
        ("Police", "Bus No. 23 will take you right there. The bus stop is across the street.", "23路公交车会带你去那里。公交车站就在街对面。"),
        ("Tourist", "Thank you very much! You're very helpful.", "非常感谢！你真是太好了。"),
        ("Police", "You're welcome. Enjoy your stay!", "不客气。祝你玩得开心！")
    ],
    "key_points": [
        "Could you please tell me...? 是问路的最礼貌表达，后接疑问词引导的宾语从句。",
        "宾语从句作及物动词的宾语时，wh-疑问词保留，但语序变为陈述语序。",
        "指路常用表达：go straight, turn left/right, at the crossing, on the corner",
        "区分：Could you tell me where the bank is? (礼貌) vs Where is the bank? (直接)"
    ],
    "vocab": [
        ("restroom", "ˈrestrʊm", "n.", "洗手间；厕所", "Could you tell me where the restroom is?", "你能告诉我洗手间在哪里吗？"),
        ("shampoo", "ʃæmˈpuː", "n.", "洗发水", "I need to buy some shampoo.", "我需要买些洗发水。"),
        ("stamp", "stæmp", "n.", "邮票", "I want to buy some stamps.", "我想买一些邮票。"),
        ("department", "dɪˈpɑːrtmənt", "n.", "部门；百货商场", "Let's go to the department store.", "我们去百货商场吧。"),
        ("escalator", "ˈeskəleɪtər", "n.", "自动扶梯", "Take the escalator to the second floor.", "乘自动扶梯到二楼。"),
        ("fascinating", "ˈfæsɪneɪtɪŋ", "adj.", "迷人的；极好的", "What a fascinating city!", "多么迷人的城市啊！"),
        ("uncrowded", "ʌnˈkraʊdɪd", "adj.", "不拥挤的", "Let's find an uncrowded place.", "我们找个不拥挤的地方吧。"),
        ("convenient", "kənˈviːniənt", "adj.", "方便的", "The subway is very convenient.", "地铁非常方便。"),
        ("mall", "mɔːl", "n.", "购物中心", "There's a new mall downtown.", "市中心有一个新的购物中心。"),
        ("clerk", "klɑːrk", "n.", "职员；办事员", "The clerk in the store was very helpful.", "店里的职员非常帮忙。"),
        ("corner", "ˈkɔːrnər", "n.", "拐角；角落", "The bank is on the corner of Main Street.", "银行在主街的拐角处。"),
        ("pass", "pæs", "v.", "经过；传递", "Pass the post office, then turn left.", "经过邮局，然后左转。"),
        ("crossing", "ˈkrɒsɪŋ", "n.", "十字路口", "Turn left at the first crossing.", "在第一个十字路口左转。"),
        ("along", "əˈlɒŋ", "prep.", "沿着", "Walk along this street.", "沿着这条街走。"),
        ("block", "blɒk", "n.", "街区", "It's three blocks away.", "它在三个街区外。"),
        ("address", "əˈdres", "n.", "地址", "Could you write down your address?", "你能写下你的地址吗？"),
        ("direction", "dəˈrekʃn", "n.", "方向", "Excuse me, which direction is the museum?", "打扰一下，博物馆在哪个方向？"),
        ("request", "rɪˈkwest", "n./v.", "请求；要求", "Make a polite request when asking for help.", "请求帮助时要有礼貌。"),
        ("polite", "pəˈlaɪt", "adj.", "有礼貌的", "It's polite to say please and thank you.", "说请和谢谢是有礼貌的。"),
        ("direct", "dəˈrekt", "adj./v.", "直接的；给……指路", "Can you direct me to the nearest hospital?", "你能指给我去最近的医院的路吗？"),
        ("correct", "kəˈrekt", "adj.", "正确的", "Is this the correct bus stop?", "这个公交车站对吗？"),
        ("nearby", "ˌnɪrˈbaɪ", "adj./adv.", "附近的", "Is there a post office nearby?", "附近有邮局吗？")
    ],
    "patterns": [
        ("Could you please tell me + wh- + 陈述语序",
         "礼貌询问信息的句型。",
         "<b>Could you please tell me where</b> the bank is? / <b>Could you please tell me how</b> to get to the station?"),
        ("I wonder + if/wh- + 陈述语序",
         "表达好奇或委婉提问。",
         "<b>I wonder if</b> there is a post office nearby. / <b>I wonder where</b> I can find a restroom."),
        ("Go straight / Turn left / Turn right",
         "指路的核心指令。",
         "<b>Go straight</b> for two blocks, then <b>turn right</b>. / <b>Turn left</b> at the traffic lights."),
        ("It's + 时间 + walk/ride from here",
         "描述距离的句型。",
         "<b>It's about ten minutes' walk from here.</b> / It's a short bus ride from here.")
    ],
    "grammar_title": "疑问词引导的宾语从句",
    "grammar_sections": [
        ("疑问词引导的宾语从句", [
            ("引导词", "功能", "例句"),
            ("where", "询问地点", "Could you tell me where the restroom is?"),
            ("how", "询问方式", "Can you tell me how to get there?"),
            ("when", "询问时间", "I wonder when the store opens."),
            ("which", "询问选择", "Could you tell me which bus to take?")
        ]),
        ("宾语从句语序", [
            ("原句", "错误语序", "正确语序"),
            ("Where is the bank?", "Could you tell me where is the bank?", "Could you tell me where the bank is?"),
            ("How can I get there?", "I wonder how can I get there.", "I wonder how I can get there."),
            ("When does it open?", "Do you know when does it open?", "Do you know when it opens?")
        ])
    ],
    "grammar_tips": [
        "宾语从句必须用陈述句语序：连接词 + 主语 + 谓语。",
        "在 Could you tell me...? 中，could 表示礼貌，不是过去式。",
        "间接疑问句末尾用句号，不用问号。",
        "<span class=\"wotd-say\" data-speak=\"When in Rome, do as the Romans do.\">When in Rome, do as the Romans do.</span> 入乡随俗。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "Could you tell me ____ the restroom is? (填入疑问词)", "where"),
        ("基础", "★☆☆", "I wonder ____ (how) I ____ (can) get to the airport. (改正语序)", "how I can"),
        ("基础", "★☆☆", "____ left at the second crossing, then go straight.", "Turn"),
        ("基础", "★☆☆", "Is it far? → Could you tell me ____?", "Could you tell me if/whether it is far?"),
        ("基础", "★☆☆", "Excuse me, ____ you tell me the way to the museum?", "could")
    ],
    "mid_qs": [
        ("提升", "★★☆", "Can you tell me ____?<br>A. where is the post office B. where the post office is C. the post office is where D. is where the post office", "B"),
        ("提升", "★★☆", "I wonder ____ (whether) he ____ (can) help me. (用括号内词完成句子)", "whether he can"),
        ("提升", "★★☆", "改写为礼貌句：Where is the bank? → Could you tell me ____?", "Could you tell me where the bank is?"),
        ("提升", "★★☆", "It's about five ____ (minute) walk from here.", "minutes'"),
        ("提升", "★★☆", "Would you mind ____ (tell) me the way to the library?", "telling")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：Do you know ____?<br>A. when will the train arrive B. when the train will arrive C. when does the train arrive D. the train will arrive when", "B"),
        ("挑战", "★★★", "将直接引语转为间接引语：He asked, 「Where is the nearest hospital?」→", "He asked where the nearest hospital was."),
        ("挑战", "★★★", "改错：I wonder that he can come to the party. (找出并改正)", "将 that 改为 if/whether"),
        ("挑战", "★★★", "完成对话：A: Excuse me, ____? B: Sure. Go straight and turn right at the traffic lights. You'll see it on your left.", "Could you tell me how to get to the library?")
    ],
    "reading_title": "Asking for Help Politely",
    "reading_text": [
        "When you visit a foreign country, it is important to know how to ask for help politely. Good speakers change the way they speak in different situations. The expressions they use might depend on whom they are speaking to or how well they know each other.",
        "For example, if you need to ask where the restrooms are, you could say «Where are the restrooms?» But this is not very polite. It might be better to say «Excuse me, could you please tell me where the restrooms are?»",
        "Sometimes we need to spend time leading in to a request. For example, we might first say to a stranger, «Excuse me, I wonder if you can help me.» This is a longer, more polite way of making a request. It is much more polite than saying «Give me some help!»",
        "Learning how to make requests politely is an important social skill. It shows respect for others and helps you communicate more effectively."
    ],
    "reading_gloss": [
        ("lead in to", "引入"),
        ("request", "请求"),
        ("stranger", "陌生人"),
        ("social skill", "社交技能"),
        ("effectively", "有效地")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "Why is it important to ask for help politely?", "Because it shows respect and helps you communicate effectively."),
        ("阅读", "★★☆", "What is the difference between «Where are the restrooms?» and «Could you please tell me where the restrooms are?»", "The second one is more polite."),
        ("阅读", "★★☆", "What does «leading in to a request» mean?", "It means saying something first before making the actual request."),
        ("阅读", "★★★", "What does the way we speak depend on according to the passage?", "It depends on whom we are speaking to and how well we know each other.")
    ],
    "exam_q_type": "阅读理解 — 细节理解",
    "exam_q": "阅读短文，判断正误（T/F）。",
    "exam_passage": [
        "In English, asking for information is not just about the right words. It is also about how you say them. When you ask a stranger for help, you should be polite. For example, «Excuse me» is a good way to start. Also, using «could» instead of «can» makes your request sound more polite. Remember to say «thank you» after someone helps you. Being polite helps people feel good and makes them want to help you."
    ],
    "exam_options": [
        (1, {"A": "Asking for information is only about the right words.", "B": "Asking for information is also about how you say the words.", "C": "Words don't matter.", "D": "Only grammar matters."}),
        (2, {"A": "Excuse me is not a polite way to start.", "B": "Excuse me is a good way to start a request.", "C": "You should never say excuse me.", "D": "Excuse me is only for friends."}),
        (3, {"A": "Can is more polite than could.", "B": "Could is more polite than can.", "C": "Both are the same.", "D": "Neither is polite."})
    ],
    "exam_answers": ["1. B", "2. B", "3. B"],
    "writing_prompt": "假设你是一名游客，来到一个陌生的城市。写一段话描述你如何向当地人询问去博物馆的路线。请使用至少三种不同的礼貌表达。",
    "writing_framework": [
        "开头：描述你在哪里，想做什么",
        "主体1：描述第一次问路（向路人询问）",
        "主体2：表示感谢并问第二个问题",
        "主体3：确认路线或询问更多信息",
        "结尾：总结礼貌问路的重要性"
    ],
    "writing_model_en": "I am visiting a new city and want to visit the museum. I ask a local person for help politely. First, I say «Excuse me, could you please tell me how to get to the city museum?» The person tells me to go straight and turn left at the second crossing. Then I say «Thank you. I wonder how long it takes to get there.» He says it's about 15 minutes' walk. Finally, I ask «Could you tell me if there is a bus I can take?» He says Bus No. 5 can take me there. I thank him again. Being polite makes the conversation pleasant and helpful.",
    "writing_model_cn": "我正在参观一个新城市，想去博物馆参观。我礼貌地向一个当地人求助。首先，我说「打扰一下，您能告诉我怎样去市博物馆吗？」那个人告诉我直走，在第二个路口左转。然后我说「谢谢。我想知道到那里要多久。」他说大约步行15分钟。最后我问「您能告诉我有没有公交车可以坐吗？」他说5路公交车可以带我去那里。我再次感谢他。礼貌让对话愉快且有帮助。",
    "project_title": "Design a City Map and Guide",
    "project_desc": "设计一张虚构城市的地图，标注至少8个地点，并用英语写出从A点到B点的路线指南。",
    "project_steps": [
        "设计城市布局草图（街道、十字路口）",
        "标注8个以上地点（银行、超市、医院、学校等）",
        "编写从起点到终点的路线指南（使用本单元句型）",
        "制作最终版本的地图和路线说明",
        "与同伴交换地图，练习问路和指路",
        "收集反馈并修改"
    ],
    "project_rubric": [
        "地图布局清晰、标注准确",
        "包含8个以上的地点",
        "路线指南使用了礼貌请求句型",
        "实践环节能流利对话",
        "设计有创意、美观"
    ],
    "checklist": [
        "我能礼貌地问路和指路",
        "我能正确使用疑问词引导的宾语从句",
        "我能区分直接和礼貌的表达方式",
        "我能用英语描述位置和方向",
        "我掌握了本单元的核心词汇"
    ],
    "feynman": "向同桌解释什么是宾语从句的陈述语序，并用问路句子举例说明。",
    "review": [
        "🔵 1天后：复习宾语从句语序规则",
        "🟢 3天后：复习问路和指路表达",
        "🟡 1周后：角色扮演练习问路对话",
        "🔴 1月后：设计一张英文地图"
    ],
    "next_unit_title": "U4: I used to be afraid of the dark.",
    "next_unit_desc": "学习 used to 结构，描述过去和现在的变化。"
}

# ==================== Unit 04 ====================
UNITS_9["u04"] = {
    "num": "U4",
    "title": "I used to be afraid of the dark.",
    "topic": "变化与成长",
    "en_topic": "Changes and Growth",
    "functions": "Talk about what you used to be like",
    "grammar": "Used to + verb (过去常常)",
    "writing": "Describe how you have changed over time",
    "can_do": [
        "能用 used to 描述过去的习惯和状态",
        "能对比过去和现在的变化",
        "能描述个人的成长经历",
        "能理解并谈论外貌和性格的变化"
    ],
    "dialogue_scene": "Paul和Alfred在旧照片前回忆过去看漫画书的时光。",
    "dialogue": [
        ("Paul", "Look at this old photo! Do you remember those comic books?", "看这张老照片！你还记得那些漫画书吗？"),
        ("Alfred", "Of course! I used to read comic books every day after school.", "当然！我以前每天放学后都看漫画书。"),
        ("Paul", "Me too. I used to spend all my pocket money on them.", "我也是。我以前把所有零花钱都花在漫画书上。"),
        ("Alfred", "You used to have a big collection. What happened to them?", "你以前有好多收藏。它们后来怎么了？"),
        ("Paul", "I gave them away. I don't read comic books anymore. I used to love them, but now I prefer novels.", "我送人了。我现在不看漫画书了。我以前很喜欢它们，但现在我更喜欢小说。"),
        ("Alfred", "People change. I used to be shy, but now I'm more outgoing.", "人是会变的。我以前很害羞，但现在我更外向了。"),
        ("Paul", "Really? I used to be outgoing, but now I enjoy quiet time more.", "真的吗？我以前很外向，但现在我更喜欢安静的时间。"),
        ("Alfred", "It's interesting how we've changed over the years!", "这些年来我们的变化真有趣！")
    ],
    "key_points": [
        "used to + 动词原形 表示「过去常常做某事」，强调过去的状态或习惯现在已经不再存在。",
        "used to 的否定形式：didn't use to / used not to",
        "used to 的疑问形式：Did + 主语 + use to...?",
        "区分：used to do (过去常常), be/get used to doing (习惯于做), be used to do (被用来做)"
    ],
    "vocab": [
        ("humorous", "ˈhjuːmərəs", "adj.", "幽默的；诙谐的", "He is a humorous person.", "他是一个幽默的人。"),
        ("silent", "ˈsaɪlənt", "adj.", "沉默的；安静的", "She used to be silent in class.", "她以前在课堂上很沉默。"),
        ("helpful", "ˈhelpfl", "adj.", "有帮助的；有用的", "My sister is very helpful.", "我姐姐非常乐于助人。"),
        ("score", "skɔːr", "n./v.", "得分；分数", "What's your score on the test?", "你考试得了多少分？"),
        ("background", "ˈbækɡraʊnd", "n.", "背景", "The photo has a beautiful background.", "这张照片的背景很漂亮。"),
        ("interview", "ˈɪntərvjuː", "n./v.", "采访；面试", "I have a job interview tomorrow.", "我明天有个工作面试。"),
        ("Asian", "ˈeɪʒn", "adj./n.", "亚洲的；亚洲人", "She is an Asian student.", "她是一个亚裔学生。"),
        ("deal", "diːl", "v.", "处理；应付", "How do you deal with stress?", "你如何应对压力？"),
        ("shy", "ʃaɪ", "adj.", "害羞的", "She used to be very shy.", "她以前非常害羞。"),
        ("dare", "der", "v.", "敢；敢于", "I dare to speak in public now.", "我现在敢在公共场合说话了。"),
        ("crowd", "kraʊd", "n.", "人群", "I don't like large crowds.", "我不喜欢大群人。"),
        ("ton", "tʌn", "n.", "吨；大量", "I have tons of homework.", "我有大量的作业。"),
        ("private", "ˈpraɪvət", "adj.", "私人的；私密的", "I need some private time.", "我需要一些私人时间。"),
        ("guard", "ɡɑːrd", "n./v.", "警卫；守卫", "The guard stood at the door.", "警卫站在门口。"),
        ("require", "rɪˈkwaɪər", "v.", "需要；要求", "This job requires patience.", "这份工作需要耐心。"),
        ("European", "ˌjʊrəˈpiːən", "adj./n.", "欧洲的；欧洲人", "He is from a European country.", "他来自一个欧洲国家。"),
        ("African", "ˈæfrɪkən", "adj./n.", "非洲的；非洲人", "She has African roots.", "她有非洲血统。"),
        ("British", "ˈbrɪtɪʃ", "adj.", "英国的；英国人的", "He speaks British English.", "他说英式英语。"),
        ("speech", "spiːtʃ", "n.", "演讲；发言", "He gave a wonderful speech.", "他做了一场精彩的演讲。"),
        ("ant", "ænt", "n.", "蚂蚁", "There is an ant on the ground.", "地上有一只蚂蚁。"),
        ("insect", "ˈɪnsekt", "n.", "昆虫", "I used to be afraid of insects.", "我以前害怕昆虫。"),
        ("influence", "ˈɪnfluəns", "n./v.", "影响", "My teacher had a big influence on me.", "我的老师对我有很大影响。")
    ],
    "patterns": [
        ("主语 + used to + 动词原形",
         "表示过去常常做某事（现在不再做）。",
         "I <b>used to</b> be afraid of the dark. / She <b>used to</b> wear glasses."),
        ("主语 + didn't use to + 动词原形",
         "used to 的否定形式。",
         "He <b>didn't use to</b> like vegetables. / I <b>didn't use to</b> exercise."),
        ("Did + 主语 + use to + 动词原形?",
         "used to 的疑问形式。",
         "<b>Did</b> you <b>use to</b> play the piano? / <b>Did</b> she <b>use to</b> live here?"),
        ("主语 + be used to + V-ing / n.",
         "表示习惯于做某事。",
         "I am <b>used to</b> getting up early. / She <b>is used to</b> the noise.")
    ],
    "grammar_title": "Used to 结构",
    "grammar_sections": [
        ("used to 的用法", [
            ("形式", "用法", "例句"),
            ("肯定句", "主语 + used to + V", "I used to be short, but now I am tall."),
            ("否定句", "主语 + didn't use to + V", "He didn't use to like reading."),
            ("一般疑问句", "Did + 主语 + use to + V?", "Did you use to play the guitar?"),
            ("反意疑问句", "主语 + used to + V, didn't + 主语?", "She used to be shy, didn't she?")
        ]),
        ("used to vs be used to", [
            ("结构", "含义", "例句"),
            ("used to do", "过去常常（现在不）", "I used to live in Beijing."),
            ("be used to doing", "习惯于", "I am used to living here."),
            ("be used to do", "被用来", "Wood is used to make paper.")
        ])
    ],
    "grammar_tips": [
        "used to 只用于过去时，不能用于现在时。",
        "注意发音：used to 中的 d 和 t 连读为 /juːstə/。",
        "be used to 中的 to 是介词，后接名词或动名词。",
        "<span class=\"wotd-say\" data-speak=\"Old habits die hard.\">Old habits die hard.</span> 江山易改，本性难移。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "I ____ (use) to be afraid of the dark.", "used"),
        ("基础", "★☆☆", "She ____ (not use) to eat so much.", "didn't use"),
        ("基础", "★☆☆", "____ you ____ (use) to play soccer after school?", "Did ... use"),
        ("基础", "★☆☆", "He used to wear glasses, ____ he?", "didn't"),
        ("基础", "★☆☆", "I am used to ____ (get) up early now.", "getting")
    ],
    "mid_qs": [
        ("提升", "★★☆", "I used to ____ (be) shy, but now I'm outgoing.", "be"),
        ("提升", "★★☆", "My grandfather ____ (used to / is used to) taking a walk after dinner every day.", "is used to"),
        ("提升", "★★☆", "She didn't use to like vegetables, ____?<br>A. did she B. didn't she C. used she D. wasn't she", "A"),
        ("提升", "★★☆", "Wood is ____ (use) to make furniture.", "used"),
        ("提升", "★★☆", "翻译：我过去不习惯在众人面前讲话。", "I didn't use to be used to speaking in front of people.")
    ],
    "hard_qs": [
        ("挑战", "★★★", "改错：I use to play basketball after school when I was young.", "use → used"),
        ("挑战", "★★★", "选择：He ____ get up late, but now he ____ getting up early.<br>A. used to; used to B. is used to; used to C. used to; is used to D. is used to; is used to", "C"),
        ("挑战", "★★★", "完成句子：我过去很胖，但现在瘦了。____", "I used to be fat, but now I am thin."),
        ("挑战", "★★★", "写作：描述你从七年级到现在发生的变化（外貌、性格、习惯等）。", "Sample: I used to be short and shy. I didn't use to speak in class. But now I am taller and more outgoing. I used to hate sports, but now I love playing basketball.")
    ],
    "reading_title": "From Shy to Confident",
    "reading_text": [
        "Wang Mei is a 15-year-old girl. She used to be very shy and quiet. She didn't use to talk much in class. When the teacher asked her questions, she used to look down at her desk and speak very softly. Her classmates thought she was unfriendly, but she was just nervous.",
        "Things began to change when she joined the school's English club. At first, she was too shy to say anything. But her teacher, Ms. Li, encouraged her to try. «Don't be afraid,» Ms. Li said. «Everyone makes mistakes.»",
        "Wang Mei practiced speaking English every day. She used to be afraid of making mistakes, but now she knows that mistakes are part of learning. She made many friends in the club. She even won a prize in the school's English speech competition!",
        "Now Wang Mei is a confident girl. She is not shy anymore. She enjoys talking with people and sharing her ideas. She says, «The most important thing is to believe in yourself. If you try, you can change.»"
    ],
    "reading_gloss": [
        ("softly", "温柔地；轻声地"),
        ("nervous", "紧张的"),
        ("encouraged", "鼓励"),
        ("competition", "比赛"),
        ("confident", "自信的"),
        ("believe in yourself", "相信自己")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What was Wang Mei like before?", "She used to be very shy and quiet."),
        ("阅读", "★★☆", "What helped Wang Mei change?", "Joining the school's English club helped her change."),
        ("阅读", "★★☆", "What did Ms. Li say to encourage her?", "「Don't be afraid. Everyone makes mistakes.」"),
        ("阅读", "★★★", "What does Wang Mei think is the most important thing?", "The most important thing is to believe in yourself.")
    ],
    "exam_q_type": "语法填空 — used to 结构",
    "exam_q": "根据上下文，用所给词的正确形式填空。",
    "exam_passage": [
        "I 1 (use) to be very afraid of speaking in public. Whenever I had to give a speech, my heart 2 (beat) very fast. I 3 (try) to avoid any situation where I had to talk in front of people. But my teacher said, «You need to practice.» So I 4 (join) the speech club. At first, I 5 (be) still nervous, but gradually I got used to 6 (speak) in front of people. Now I enjoy giving speeches!"
    ],
    "exam_options": [
        (1, {"A": "use", "B": "used", "C": "using", "D": "uses"}),
        (2, {"A": "beats", "B": "beat", "C": "beaten", "D": "beating"}),
        (3, {"A": "try", "B": "tried", "C": "trying", "D": "tries"}),
        (4, {"A": "join", "B": "joined", "C": "joining", "D": "joins"}),
        (5, {"A": "am", "B": "was", "C": "were", "D": "been"}),
        (6, {"A": "speak", "B": "speaking", "C": "spoke", "D": "spoken"})
    ],
    "exam_answers": ["1. B", "2. B", "3. B", "4. B", "5. B", "6. B"],
    "writing_prompt": "描述你过去和现在的变化。可以包括外貌、性格、兴趣爱好、学习习惯等方面的变化。写一篇80-100词的短文。",
    "writing_framework": [
        "开头：总述自己的变化",
        "描述过去的自己（外貌、性格、习惯等）",
        "描述现在自己的状态",
        "分析变化的可能原因",
        "结尾：对变化的感受和展望"
    ],
    "writing_model_en": "I have changed a lot over the past few years. I used to be short and thin, but now I am much taller. I used to be shy and didn't use to talk much in class. Now I am more outgoing and I have many friends. I used to hate reading, but now I love it. My English teacher encouraged me to read English stories. Now I read for half an hour every day. I believe change is a good thing. It helps us grow.",
    "writing_model_cn": "在过去的几年里，我变了很多。我以前又矮又瘦，但现在我高多了。我以前很害羞，在课堂上话不多。现在我更外向了，有很多朋友。我以前讨厌阅读，但现在我热爱阅读。我的英语老师鼓励我读英语故事。现在我每天阅读半小时。我相信变化是好事。它帮助我们成长。",
    "project_title": "Then and Now — A Personal Growth Poster",
    "project_desc": "制作一张「过去与现在」对比海报，展示你在外貌、性格、爱好和能力方面的变化。",
    "project_steps": [
        "找一张自己小时候的照片和现在的照片",
        "列出你在外貌、性格、习惯等方面的变化",
        "确定海报的布局：左侧「Then」右侧「Now」",
        "写英文说明，使用 used to 结构",
        "添加图画、贴纸等装饰",
        "在班上展示你的成长故事"
    ],
    "project_rubric": [
        "对比清晰、内容完整",
        "正确使用了 used to 结构",
        "视觉设计有创意、美观",
        "口头展示流利自信",
        "能回答同学的问题"
    ],
    "checklist": [
        "我能正确使用 used to 描述过去",
        "我能区分 used to do 和 be used to doing",
        "我能用英语描述自己和他人的变化",
        "我能理解阅读中关于成长的故事",
        "我能写出自己的成长变化"
    ],
    "feynman": "向同桌解释 used to do 和 be used to doing 的区别，各举两个例子。",
    "review": [
        "🔵 1天后：复习 used to 的三种句式",
        "🟢 3天后：复习变化描述相关词汇",
        "🟡 1周后：复述王梅的变化故事",
        "🔴 1月后：写自己的成长变化"
    ],
    "next_unit_title": "U5: What are the shirts made of?",
    "next_unit_desc": "学习被动语态（一般现在时），描述产品的材料和产地。"
}

# ==================== Unit 05 ====================
UNITS_9["u05"] = {
    "num": "U5",
    "title": "What are the shirts made of?",
    "topic": "产品与材料",
    "en_topic": "Products and Materials",
    "functions": "Talk about what products are made of and where they are made",
    "grammar": "Passive voice (present tense) — is/are + past participle",
    "writing": "Describe how products are made",
    "can_do": [
        "能用被动语态描述产品的材料和产地",
        "能谈论日常物品的制造过程",
        "能理解并描述中国传统工艺",
        "能写关于产品介绍的文章"
    ],
    "dialogue_scene": "Susan在一家礼品店给朋友挑选礼物，和店员聊天。",
    "dialogue": [
        ("Susan", "Excuse me, I'd like to buy a gift for my friend. What are these shirts made of?", "打扰一下，我想给朋友买个礼物。这些衬衫是什么做的？"),
        ("Clerk", "They are made of cotton. They are very soft and comfortable.", "它们是棉质的。非常柔软舒适。"),
        ("Susan", "I see. Where are they made?", "我明白了。它们是在哪里制造的？"),
        ("Clerk", "They are made in China. The design is quite popular.", "它们是中国制造的。这个设计很受欢迎。"),
        ("Susan", "And what about those beautiful chopsticks?", "那些漂亮的筷子呢？"),
        ("Clerk", "They are made of silver. They are produced in Yunnan.", "它们是银制的。是在云南生产的。"),
        ("Susan", "How about the paper cutting? It's so delicate!", "那剪纸呢？太精致了！"),
        ("Clerk", "The paper cutting is made by hand. It is a traditional art form.", "剪纸是手工制作的。它是一种传统艺术形式。"),
        ("Susan", "Amazing! I'll buy the paper cutting as a gift.", "太棒了！我买剪纸作为礼物吧。")
    ],
    "key_points": [
        "be made of + 材料（看得出原材料）— The shirt is made <b>of</b> cotton.",
        "be made from + 材料（看不出原材料）— Paper is made <b>from</b> wood.",
        "be made in + 地点 — It is made <b>in</b> China.",
        "be made by + 人/方式 — It is made <b>by</b> hand."
    ],
    "vocab": [
        ("chopstick", "ˈtʃɒpstɪk", "n.", "筷子", "We use chopsticks to eat noodles.", "我们用筷子吃面条。"),
        ("coin", "kɔɪn", "n.", "硬币", "I found a coin on the street.", "我在街上发现了一枚硬币。"),
        ("fork", "fɔːrk", "n.", "餐叉", "Please put the fork on the left.", "请把叉子放在左边。"),
        ("blouse", "blaʊz", "n.", "女衬衫", "She is wearing a silk blouse.", "她穿着一件丝绸衬衫。"),
        ("silver", "ˈsɪlvər", "n.", "银；银器", "This ring is made of silver.", "这枚戒指是银制的。"),
        ("glass", "ɡlæs", "n.", "玻璃", "The window is made of glass.", "窗户是玻璃做的。"),
        ("cotton", "ˈkɒtn", "n.", "棉花", "This T-shirt is 100% cotton.", "这件T恤是100%纯棉的。"),
        ("steel", "stiːl", "n.", "钢；钢铁", "The bridge is made of steel.", "这座桥是钢铁建的。"),
        ("grass", "ɡræs", "n.", "草；草地", "Keep off the grass.", "请勿践踏草坪。"),
        ("leaf", "liːf", "n.", "叶子", "The leaves turn yellow in autumn.", "叶子在秋天变黄。"),
        ("produce", "prəˈdjuːs", "v.", "生产；制造", "This factory produces cars.", "这家工厂生产汽车。"),
        ("widely", "ˈwaɪdli", "adv.", "广泛地", "English is widely used around the world.", "英语在全世界被广泛使用。"),
        ("process", "ˈprəʊses", "n./v.", "过程；加工", "The production process is very efficient.", "生产过程非常高效。"),
        ("pack", "pæk", "v.", "包装", "The gifts are packed in beautiful boxes.", "礼物被包装在漂亮的盒子里。"),
        ("product", "ˈprɒdʌkt", "n.", "产品", "This product is made in China.", "这个产品是中国制造的。"),
        ("France", "fræns", "n.", "法国", "This wine is from France.", "这酒来自法国。"),
        ("Germany", "ˈdʒɜːrməni", "n.", "德国", "Cars are made in Germany.", "汽车在德国制造。"),
        ("material", "məˈtɪriəl", "n.", "材料；原料", "What material is this made of?", "这是什么材料做的？"),
        ("traffic", "ˈtræfɪk", "n.", "交通", "There is a lot of traffic in the city.", "城市里交通繁忙。"),
        ("postman", "ˈpoʊstmən", "n.", "邮递员", "The postman brings letters every day.", "邮递员每天送信。"),
        ("cap", "kæp", "n.", "帽子", "He wears a baseball cap.", "他戴着一顶棒球帽。"),
        ("glove", "ɡlʌv", "n.", "手套", "In winter, I wear gloves.", "冬天我戴手套。")
    ],
    "patterns": [
        ("A + be made of + 材料 (看得出原材料)",
         "表示「某物由……制成」。",
         "The shirt <b>is made of</b> cotton. / This ring <b>is made of</b> silver."),
        ("A + be made from + 材料 (看不出原材料)",
         "表示「某物由……制成」。",
         "Paper <b>is made from</b> wood. / Wine <b>is made from</b> grapes."),
        ("A + be made in + 地点",
         "表示「某物在某地制造」。",
         "These cars <b>are made in</b> Japan. / This shirt <b>is made in</b> China."),
        ("A + be made by + 人/方式",
         "表示「某物由某人/用某种方式制造」。",
         "Paper cutting <b>is made by</b> hand. / The model <b>was made by</b> my brother.")
    ],
    "grammar_title": "被动语态 — 一般现在时",
    "grammar_sections": [
        ("被动语态的结构", [
            ("时态", "结构", "例句"),
            ("一般现在时", "am/is/are + V-ed", "The shirts are made of cotton."),
            ("一般过去时", "was/were + V-ed", "The bridge was built in 1990."),
            ("一般将来时", "will be + V-ed", "The meeting will be held next week.")
        ]),
        ("主动变被动", [
            ("主动句", "被动句", "说明"),
            ("The factory produces cars.", "Cars are produced by the factory.", "宾语变为主语"),
            ("People grow tea in Hangzhou.", "Tea is grown in Hangzhou.", "by people 常省略"),
            ("They make this kind of watch in Switzerland.", "This kind of watch is made in Switzerland.", "原主语不明确时省略")
        ])
    ],
    "grammar_tips": [
        "只有及物动词（后接宾语）才能用于被动语态。",
        "be 动词要根据主语的人称和数进行变化。",
        "如果不想提及动作的执行者，可以省略 by 短语。",
        "<span class=\"wotd-say\" data-speak=\"All that glitters is not gold.\">All that glitters is not gold.</span> 闪光的未必都是金子。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "The shirts ____ (make) of cotton.", "are made"),
        ("基础", "★☆☆", "Tea ____ (grow) in many parts of China.", "is grown"),
        ("基础", "★☆☆", "This ring is made ____ silver.", "of"),
        ("基础", "★☆☆", "Paper is made ____ wood.", "from"),
        ("基础", "★☆☆", "These products are made ____ China.", "in")
    ],
    "mid_qs": [
        ("提升", "★★☆", "The cake ____ (make) by my mother every birthday.", "is made"),
        ("提升", "★★☆", "完成被动句：People speak English all over the world. → English ____.", "English is spoken all over the world."),
        ("提升", "★★☆", "选择：This kind of watch ____ in Switzerland.<br>A. made B. is made C. makes D. making", "B"),
        ("提升", "★★☆", "改主动为被动：My grandmother makes the best dumplings. → ____.", "The best dumplings are made by my grandmother."),
        ("提升", "★★☆", "翻译：剪纸是手工制作的。", "Paper cutting is made by hand.")
    ],
    "hard_qs": [
        ("挑战", "★★★", "完成被动句：These flowers ____ (water) every day.", "are watered"),
        ("挑战", "★★★", "改错：The book is wrote by a famous author.", "wrote → written"),
        ("挑战", "★★★", "改写：People use bamboo to make many things. → Bamboo ____.", "Bamboo is used to make many things."),
        ("挑战", "★★★", "写作：用被动语态描述一张纸的制作过程（至少4个步骤）。", "Trees are cut down. Then they are made into wood pulp. The pulp is pressed into sheets. Finally, the paper is cut and packed.")
    ],
    "reading_title": "Chinese Traditional Art Forms",
    "reading_text": [
        "China is famous for its traditional art forms. Many of them are made by hand and have a long history. One example is sky lanterns. They are made of bamboo and paper. Sky lanterns are used at festivals and other celebrations. They are seen as symbols of happiness and good wishes.",
        "Another traditional art form is paper cutting. Paper cutting has been around for over 1,500 years. It is made by cutting paper into different shapes. Red paper is usually used because red is a lucky color in China. Paper cuttings are put on windows, doors, and walls as decorations.",
        "Chinese clay art is also famous. The clay pieces are small and cute. They are about children, animals, or Chinese characters. They are made by hand. First, the clay is shaped. Then it is allowed to air-dry. After drying, it is fired at a very high heat. Finally, it is painted and polished."
    ],
    "reading_gloss": [
        ("sky lantern", "孔明灯；天灯"),
        ("symbol", "象征"),
        ("paper cutting", "剪纸"),
        ("clay", "黏土"),
        ("air-dry", "风干"),
        ("fired", "烧制"),
        ("polished", "抛光")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What are sky lanterns made of?", "They are made of bamboo and paper."),
        ("阅读", "★★☆", "Why is red paper usually used for paper cutting?", "Because red is a lucky color in China."),
        ("阅读", "★★☆", "How many steps are there in making Chinese clay art?", "Five steps: shaped, air-dried, fired, painted, and polished."),
        ("阅读", "★★★", "What do sky lanterns symbolize?", "They are symbols of happiness and good wishes.")
    ],
    "exam_q_type": "阅读理解 — 判断正误",
    "exam_q": "阅读短文，判断下列句子的正（T）误（F）。",
    "exam_passage": [
        "Tea is a popular drink all over the world. It is produced in many countries, but China is the birthplace of tea. In China, tea is grown in many provinces. Fujian, Zhejiang, and Yunnan are famous for tea. Tea is picked by hand and then processed. There are different kinds of tea: green tea, black tea, oolong tea, and white tea. Tea is not only a drink but also a part of Chinese culture. It is often served when guests visit. Tea is also used in traditional Chinese medicine."
    ],
    "exam_options": [
        (1, {"A": "Tea is not produced in China.", "B": "China is the birthplace of tea.", "C": "Tea is only a drink.", "D": "Tea is not used in medicine."}),
        (2, {"A": "Tea is picked by machines.", "B": "Tea is picked by hand.", "C": "Tea is not processed.", "D": "Tea is only from Fujian."}),
        (3, {"A": "Tea is not part of Chinese culture.", "B": "Tea is served when guests visit.", "C": "Only green tea exists.", "D": "Tea has no health benefits."})
    ],
    "exam_answers": ["1. F", "2. T", "3. T"],
    "writing_prompt": "写一篇短文介绍一种你熟悉的中国传统手工艺品。说明它的材料、产地、制作过程和文化意义。",
    "writing_framework": [
        "开头：介绍你要描述的手工艺品",
        "材料：说明它由什么制成",
        "产地：它在什么地方生产",
        "制作过程：简要描述如何制作",
        "文化意义：它象征什么，什么时候使用"
    ],
    "writing_model_en": "Today I want to introduce Chinese paper cutting. It is a traditional art form that has a long history of over 1,500 years. Paper cutting is made of red paper. It is made by hand. The designs are cut into different shapes, such as flowers, animals, and Chinese characters. Paper cuttings are usually put on windows, doors, and walls during the Spring Festival. They are symbols of good luck and happiness. I think paper cutting is a beautiful and meaningful art form.",
    "writing_model_cn": "今天我想介绍中国的剪纸。它是一种有着1500多年历史的传统艺术形式。剪纸是用红纸做的，是手工制作的。图案被剪成不同的形状，如花、动物和汉字。剪纸通常在春节期间贴在窗户、门和墙上。它们是好运和幸福的象征。我认为剪纸是一种美丽而有意义的艺术形式。",
    "project_title": "Product Report — Made in My Hometown",
    "project_desc": "调查你家乡的一种特产或知名产品，了解它的材料、制作工艺和文化意义，做一个报告。",
    "project_steps": [
        "选择你家乡的一种特产或知名产品",
        "了解它的原材料和制作工艺",
        "拍摄或收集产品的照片",
        "用英语写一篇产品报告（含被动语态）",
        "制作PPT或海报展示",
        "向全班介绍你的发现"
    ],
    "project_rubric": [
        "产品选择有意义",
        "信息准确、来源可靠",
        "正确使用了被动语态",
        "展示清晰、有吸引力",
        "能回答同学提问"
    ],
    "checklist": [
        "我能理解被动语态（一般现在时）的结构",
        "我能区分 be made of / from / in / by",
        "我能用被动语态描述产品",
        "我能理解阅读中关于中国传统工艺的介绍",
        "我能写出产品介绍短文"
    ],
    "feynman": "向同桌解释被动语态和主动语态的区别，分别举例说明。",
    "review": [
        "🔵 1天后：复习被动语态结构",
        "🟢 3天后：复习 be made of/from/in/by",
        "🟡 1周后：复述中国传统工艺文章",
        "🔴 1月后：介绍你家乡的一种产品"
    ],
    "next_unit_title": "U6: When was it invented?",
    "next_unit_desc": "学习一般过去时的被动语态，了解重要发明的历史。"
}

# ==================== Unit 06 ====================
UNITS_9["u06"] = {
    "num": "U6",
    "title": "When was it invented?",
    "topic": "发明历史",
    "en_topic": "Invention History",
    "functions": "Talk about the history of inventions",
    "grammar": "Passive voice (past tense) — was/were + past participle",
    "writing": "Write about an invention and its history",
    "can_do": [
        "能用过去时被动语态谈论发明历史",
        "能描述发明的时间、用途和影响",
        "能比较古代和现代发明",
        "能写一篇关于发明的介绍文章"
    ],
    "dialogue_scene": "Roy和Alice在科技博物馆参观发明展览。",
    "dialogue": [
        ("Roy", "Look at this! When was the telephone invented?", "看这个！电话是什么时候发明的？"),
        ("Alice", "It was invented in 1876 by Alexander Graham Bell.", "它是在1876年由亚历山大·格雷厄姆·贝尔发明的。"),
        ("Roy", "That's amazing! What about the car? When was it invented?", "太神奇了！那汽车呢？它是什么时候发明的？"),
        ("Alice", "The first car was invented in 1885 by Karl Benz.", "第一辆汽车是在1885年由卡尔·本茨发明的。"),
        ("Roy", "I see. And what was the telephone used for at first?", "我明白了。电话最初是用来做什么的？"),
        ("Alice", "It was used for communication, of course! It changed the way people talked to each other.", "当然是用来通讯的！它改变了人们相互交流的方式。"),
        ("Roy", "What invention do you think is the most important?", "你认为最重要的发明是什么？"),
        ("Alice", "I think the Internet is the most important. It was invented in the 1960s and it connects the whole world.", "我认为互联网是最重要的。它是在20世纪60年代发明的，它连接了整个世界。")
    ],
    "key_points": [
        "一般过去时被动语态：was/were + V-ed — The telephone <b>was invented</b> in 1876.",
        "by + 发明者 — The telephone was invented <b>by Alexander Graham Bell</b>.",
        "be used for + V-ing — 表示「被用来做……」 — It <b>was used for</b> communication.",
        "be used to do — 也可以表示「被用来做」 — It was used <b>to communicate</b>."
    ],
    "vocab": [
        ("invent", "ɪnˈvent", "v.", "发明；创造", "Who invented the light bulb?", "谁发明了电灯泡？"),
        ("invention", "ɪnˈvenʃn", "n.", "发明", "The telephone is a great invention.", "电话是一项伟大的发明。"),
        ("inventor", "ɪnˈventər", "n.", "发明家", "Edison was a famous inventor.", "爱迪生是一位著名的发明家。"),
        ("mention", "ˈmenʃn", "v.", "提到；说起", "He mentioned the new project.", "他提到了新项目。"),
        ("project", "ˈprɒdʒekt", "n.", "项目；课题", "We are working on a science project.", "我们正在做一个科学项目。"),
        ("sour", "ˈsaʊər", "adj.", "酸的", "These lemons are sour.", "这些柠檬很酸。"),
        ("mistake", "mɪˈsteɪk", "n.", "错误；失误", "Don't be afraid to make mistakes.", "不要害怕犯错。"),
        ("accidental", "ˌæksɪˈdentl", "adj.", "意外的；偶然的", "The discovery was accidental.", "这个发现是偶然的。"),
        ("ruler", "ˈruːlər", "n.", "尺子；统治者", "Use a ruler to draw a straight line.", "用尺子画一条直线。"),
        ("boil", "bɔɪl", "v.", "煮沸；烧开", "Boil some water, please.", "请烧一些水。"),
        ("remain", "rɪˈmeɪn", "v.", "保持；剩余", "The door remained closed.", "门一直关着。"),
        ("smell", "smel", "n./v.", "气味；闻起来", "The soup smells delicious.", "汤闻起来很香。"),
        ("national", "ˈnæʃnəl", "adj.", "国家的；全国的", "This is a national holiday.", "这是一个全国性节日。"),
        ("trade", "treɪd", "n./v.", "贸易；交易", "China trades with many countries.", "中国与许多国家进行贸易。"),
        ("doubt", "daʊt", "n./v.", "怀疑；疑问", "No doubt, it's a great invention.", "毫无疑问，这是一项伟大的发明。"),
        ("refrigerator", "rɪˈfrɪdʒəreɪtər", "n.", "冰箱", "Keep the milk in the refrigerator.", "把牛奶放在冰箱里。"),
        ("sweet", "swiːt", "adj./n.", "甜的；糖果", "The cake is very sweet.", "蛋糕很甜。"),
        ("crispy", "ˈkrɪspi", "adj.", "脆的；酥脆的", "The fried chicken is crispy.", "炸鸡很脆。"),
        ("salty", "ˈsɔːlti", "adj.", "咸的", "The soup is a bit salty.", "汤有点咸。"),
        ("customer", "ˈkʌstəmər", "n.", "顾客；客户", "The customer is always right.", "顾客永远是对的。"),
        ("divide", "dɪˈvaɪd", "v.", "分开；划分", "Divide the cake into four pieces.", "把蛋糕分成四块。"),
        ("popularity", "ˌpɒpjuˈlærəti", "n.", "普及；流行", "The popularity of smartphones is growing.", "智能手机的普及率在增长。")
    ],
    "patterns": [
        ("主语 + was/were + V-ed + (by + 施动者)",
         "一般过去时被动语态，描述过去的动作。",
         "The telephone <b>was invented</b> in 1876. / The car <b>was invented</b> by Karl Benz."),
        ("When was + 主语 + V-ed?",
         "询问发明的时间。",
         "<b>When was</b> the light bulb <b>invented</b>? / <b>When was</b> paper <b>invented</b>?"),
        ("What was + 主语 + used for?",
         "询问用途。",
         "<b>What was</b> the telephone <b>used for</b>? / <b>What was</b> it <b>used for</b> at first?"),
        ("主语 + was/were + used for + V-ing / used to V",
         "描述用途的两种方式。",
         "It <b>was used for</b> communication. / It <b>was used to</b> send messages.")
    ],
    "grammar_title": "一般过去时的被动语态",
    "grammar_sections": [
        ("结构对比", [
            ("时态", "主动语态", "被动语态"),
            ("一般现在时", "People grow tea in China.", "Tea is grown in China."),
            ("一般过去时", "Bell invented the telephone.", "The telephone was invented by Bell."),
            ("一般将来时", "They will build a new school.", "A new school will be built.")
        ]),
        ("被动语态变化规则", [
            ("动词形式", "过去式", "过去分词"),
            ("regular: work", "worked", "worked"),
            ("regular: invent", "invented", "invented"),
            ("irregular: build", "built", "built"),
            ("irregular: write", "wrote", "written"),
            ("irregular: make", "made", "made"),
            ("irregular: grow", "grew", "grown")
        ])
    ],
    "grammar_tips": [
        "一般过去时被动语态由 was/were + 过去分词构成。",
        "was 用于单数主语，were 用于复数主语。",
        "注意不规则动词的过去分词形式。",
        "<span class=\"wotd-say\" data-speak=\"Necessity is the mother of invention.\">Necessity is the mother of invention.</span> 需要是发明之母。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "The telephone ____ (invent) by Alexander Graham Bell.", "was invented"),
        ("基础", "★☆☆", "When ____ the car ____ (invent)?", "was ... invented"),
        ("基础", "★☆☆", "The light bulb ____ (invent) by Thomas Edison.", "was invented"),
        ("基础", "★☆☆", "Paper ____ (invent) in China.", "was invented"),
        ("基础", "★☆☆", "These computers ____ (make) in China last year.", "were made")
    ],
    "mid_qs": [
        ("提升", "★★☆", "Tea ____ (discover) by accident about 5,000 years ago.", "was discovered"),
        ("提升", "★★☆", "选择：The first Olympic Games ____ in 776 BC.<br>A. held B. were held C. hold D. was held", "B"),
        ("提升", "★★☆", "改主动为被动：Edison invented the light bulb. → ____.", "The light bulb was invented by Edison."),
        ("提升", "★★☆", "What was the abacus used ____? (for / to / in / by)", "for"),
        ("提升", "★★☆", "翻译：风筝最初是用于军事目的的。", "Kites were first used for military purposes.")
    ],
    "hard_qs": [
        ("挑战", "★★★", "改错：The museum was build in 1980.", "build → built"),
        ("挑战", "★★★", "合并：The students designed the robot. It was for cleaning windows. → The robot ____.", "The robot was designed for cleaning windows by the students."),
        ("挑战", "★★★", "被动转主动：The window was broken by Tom. → ____.", "Tom broke the window."),
        ("挑战", "★★★", "写作：用一般过去时被动语态写一段关于茶的历史（至少5句话）。", "Tea was first discovered about 5,000 years ago. It was discovered by accident. The leaves fell into boiling water. A nice smell was produced. Since then, tea has been enjoyed by people all over the world.")
    ],
    "reading_title": "The Accidental Invention of Tea",
    "reading_text": [
        "Did you know that tea, the most popular drink in the world, was invented by accident? According to an old Chinese legend, the emperor Shen Nong discovered tea when he was boiling water over an open fire. Some leaves from a tea plant fell into the water and remained there for some time. The emperor noticed that the water had a pleasant smell. He decided to taste the water, and it was quite delicious. And in this way, one of the world's favorite drinks was invented.",
        "Tea was brought to Korea and Japan during the 6th and 7th centuries. In England, tea didn't appear until 1660. The tea trade from China to Western countries took place in the 19th century. Now tea is widely consumed all over the world. It is more than just a drink — it is a part of many cultures.",
        "In China, tea is often served when guests visit. It is also a symbol of respect and friendship. The Chinese tea ceremony is a traditional way of preparing and serving tea."
    ],
    "reading_gloss": [
        ("by accident", "偶然地；意外地"),
        ("legend", "传说"),
        ("emperor", "皇帝"),
        ("shen nong", "神农"),
        ("pleasant", "令人愉快的"),
        ("consumed", "消费；饮用"),
        ("ceremony", "仪式")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "How was tea discovered according to the legend?", "Some leaves from a tea plant fell into boiling water by accident."),
        ("阅读", "★★☆", "When did tea appear in England?", "In 1660."),
        ("阅读", "★★☆", "What does tea symbolize in Chinese culture?", "It is a symbol of respect and friendship."),
        ("阅读", "★★★", "Why is tea called an accidental invention?", "Because it was discovered by accident when leaves fell into boiling water.")
    ],
    "exam_q_type": "补全对话 — 发明历史",
    "exam_q": "根据上下文，补全对话。",
    "exam_passage": [
        "A: Look at this old thing. What is it?\nB: It's an abacus. It was used for calculating.\nA: When was it invented?\nB: It 1 (invent) in China about 2,000 years ago.\nA: That's so old! What 2 it made of?\nB: It was made 3 wood and beads.\nA: What was it used 4?\nB: It was used to add, subtract, multiply, and divide.\nA: It's amazing that such a simple tool 5 so useful!"
    ],
    "exam_options": [
        (1, {"A": "invented", "B": "was invented", "C": "is invented", "D": "was invent"}),
        (2, {"A": "was", "B": "is", "C": "were", "D": "are"}),
        (3, {"A": "of", "B": "from", "C": "in", "D": "by"}),
        (4, {"A": "to", "B": "for", "C": "in", "D": "by"}),
        (5, {"A": "is", "B": "was", "C": "were", "D": "be"})
    ],
    "exam_answers": ["1. B", "2. A", "3. A", "4. B", "5. B"],
    "writing_prompt": "选择一项你感兴趣的发明（如电话、电灯、互联网、纸等），写一篇短文介绍它的发明时间、发明者、用途和影响。",
    "writing_framework": [
        "开头：引出你要介绍的发明",
        "发明时间：说明它是什么时候发明的",
        "发明者：介绍发明者",
        "用途：描述它的用途和最初的功能",
        "影响：说明它对世界的影响",
        "结尾：你的感想"
    ],
    "writing_model_en": "The light bulb is one of the most important inventions in history. It was invented by Thomas Edison in 1879. Before the light bulb was invented, people had to use candles or oil lamps to see in the dark. The light bulb was used for lighting homes and streets. It changed the way people live and work. Now people can work and study at night. I think the light bulb is a great invention because it made the world brighter and safer.",
    "writing_model_cn": "电灯泡是历史上最重要的发明之一。它是由托马斯·爱迪生在1879年发明的。在电灯泡发明之前，人们不得不在黑暗中用蜡烛或油灯照明。电灯泡被用来照亮家和街道。它改变了人们生活和工作的方式。现在人们可以在晚上工作和学习了。我认为电灯泡是一项伟大的发明，因为它让世界更明亮、更安全。",
    "project_title": "Great Inventions Timeline",
    "project_desc": "制作一张「伟大发明时间线」海报，展示至少10项重要发明及其发明时间、发明者和影响。",
    "project_steps": [
        "列出10项你认为最重要的发明",
        "查找每项发明的发明时间、发明者和国家",
        "按时间顺序排列在时间线上",
        "每项发明配图并写英文介绍",
        "标注哪些发明是中国的",
        "在班级展示并投票选出最伟大的发明"
    ],
    "project_rubric": [
        "选择10项以上重要发明",
        "信息准确、时间正确",
        "使用了过去时被动语态",
        "设计美观、时间线清晰",
        "展示时发音清晰、表达流畅"
    ],
    "checklist": [
        "我能正确使用一般过去时被动语态",
        "我能谈论重要发明的历史",
        "我能区分主动语态和被动语态",
        "我能理解阅读中关于茶的故事",
        "我能写一篇关于发明的短文"
    ],
    "feynman": "向同桌讲述茶叶是如何被偶然发现的，注意使用被动语态。",
    "review": [
        "🔵 1天后：复习过去时被动语态结构",
        "🟢 3天后：复习发明相关词汇和动词过去分词",
        "🟡 1周后：复述茶的发现故事",
        "🔴 1月后：介绍一项你最喜欢的发明"
    ],
    "next_unit_title": "U7: Teenagers should be allowed to choose their own clothes.",
    "next_unit_desc": "学习情态动词的被动语态，讨论规则和许可。"
}

# ==================== Unit 07 ====================
UNITS_9["u07"] = {
    "num": "U7",
    "title": "Teenagers should be allowed to choose their own clothes.",
    "topic": "规则与许可",
    "en_topic": "Rules and Permission",
    "functions": "Talk about what you are allowed to do; agree and disagree",
    "grammar": "Modal verbs + passive voice: should be + V-ed",
    "writing": "Write about rules and express opinions",
    "can_do": [
        "能用 should be allowed to 表达允许",
        "能讨论青少年应被允许做什么",
        "能表达同意和不同意的观点",
        "能写关于规则的文章并表达看法"
    ],
    "dialogue_scene": "Anna和妈妈在讨论学校的着装规定和课外活动。",
    "dialogue": [
        ("Anna", "Mom, can I buy a new dress for the party?", "妈妈，我能买一件新裙子参加派对吗？"),
        ("Mom", "Sure, but I think teenagers should be allowed to choose their own clothes.", "当然，但我认为青少年应该被允许自己选择衣服。"),
        ("Anna", "I agree! Some of the school rules are too strict. We should be allowed to wear our own clothes at school.", "我同意！有些校规太严格了。我们应该被允许在学校穿自己的衣服。"),
        ("Mom", "Well, I think students should be required to wear uniforms. It saves time and money.", "嗯，我认为学生应该被要求穿校服。这样省时省钱。"),
        ("Anna", "Maybe you're right. But I think we should be allowed to choose our hairstyles.", "也许你是对的。但我认为我们应该被允许选择自己的发型。"),
        ("Mom", "I can agree with that. Also, teenagers should be allowed to make their own decisions sometimes.", "这个我同意。而且，青少年有时候应该被允许自己做决定。"),
        ("Anna", "Thanks Mom. Oh, and I think I should be allowed to study with my friends this weekend.", "谢谢妈妈。哦，还有，我认为我这个周末应该被允许和朋友一起学习。"),
        ("Mom", "Fine, as long as you finish your homework first.", "行，只要你先完成作业。")
    ],
    "key_points": [
        "should be allowed to do 表示「应该被允许做某事」— Teenagers <b>should be allowed to</b> choose their own clothes.",
        "should not be allowed to do 表示「不应该被允许做某事」— Students <b>should not be allowed to</b> use phones in class.",
        "情态动词 + be + V-ed 构成情态动词被动语态。",
        "agree/disagree 表达同意或不同意的常用句型。"
    ],
    "vocab": [
        ("allow", "əˈlaʊ", "v.", "允许；准许", "Smoking is not allowed here.", "这里不允许吸烟。"),
        ("choose", "tʃuːz", "v.", "选择", "You can choose any book you like.", "你可以选择任何你喜欢的书。"),
        ("choice", "tʃɔɪs", "n.", "选择；抉择", "It's your choice.", "这是你的选择。"),
        ("drive", "draɪv", "v.", "驾驶", "You are not allowed to drive until you are 18.", "你18岁之前不允许开车。"),
        ("license", "ˈlaɪsns", "n.", "执照；许可证", "He got his driving license last week.", "他上周拿到了驾照。"),
        ("teenager", "ˈtiːneɪdʒər", "n.", "青少年", "Teenagers should have more free time.", "青少年应该有更多自由时间。"),
        ("pierce", "pɪrs", "v.", "刺穿；刺破", "She wants to get her ears pierced.", "她想打耳洞。"),
        ("earring", "ˈɪrɪŋ", "n.", "耳环", "She is wearing beautiful earrings.", "她戴着漂亮的耳环。"),
        ("silly", "ˈsɪli", "adj.", "愚蠢的；傻的", "That's a silly rule.", "那是一条愚蠢的规定。"),
        ("cry", "kraɪ", "v.", "哭；哭泣", "Don't cry. Everything will be fine.", "别哭了。一切都会好的。"),
        ("field", "fiːld", "n.", "田野；领域", "The kids are playing in the field.", "孩子们在田野里玩。"),
        ("hug", "hʌɡ", "v./n.", "拥抱", "Give me a hug!", "给我一个拥抱！"),
        ("lift", "lɪft", "v.", "举起；提升", "Can you lift this box?", "你能举起这个箱子吗？"),
        ("achieve", "əˈtʃiːv", "v.", "实现；达到", "Work hard to achieve your dreams.", "努力去实现你的梦想。"),
        ("support", "səˈpɔːrt", "v./n.", "支持", "My family supports me.", "我的家人支持我。"),
        ("manage", "ˈmænɪdʒ", "v.", "管理；应付", "I can manage my time well.", "我能很好地管理时间。"),
        ("opportunity", "ˌɒpərˈtjuːnəti", "n.", "机会", "This is a great opportunity.", "这是一个很好的机会。"),
        ("safety", "ˈseɪfti", "n.", "安全", "Safety comes first.", "安全第一。"),
        ("educate", "ˈedʒukeɪt", "v.", "教育；培养", "Parents should educate their children.", "家长应该教育孩子。"),
        ("volunteer", "ˌvɒlənˈtɪr", "v./n.", "自愿；志愿者", "I want to volunteer at the hospital.", "我想在医院做志愿者。"),
        ("experience", "ɪkˈspɪriəns", "n./v.", "经验；体验", "This is a valuable experience.", "这是一次宝贵的经历。"),
        ("decision", "dɪˈsɪʒn", "n.", "决定", "Think before you make a decision.", "做决定之前要三思。")
    ],
    "patterns": [
        ("主语 + should (not) be allowed to + V",
         "情态动词被动语态，表示应该（不应该）被允许做某事。",
         "Teenagers <b>should be allowed to</b> choose their own clothes. / Students <b>should not be allowed to</b> use phones."),
        ("主语 + can/may/must be + V-ed",
         "其他情态动词的被动语态。",
         "This work <b>must be finished</b> today. / The problem <b>can be solved</b> easily."),
        ("I agree / disagree with...",
         "表达同意或不同意。",
         "<b>I agree with</b> you. / <b>I disagree with</b> that rule. / <b>I don't think</b> it's a good idea."),
        ("主语 + should (not) be required to V",
         "表示「应该/不应该被要求做某事」。",
         "Students <b>should be required to</b> wear uniforms. / We <b>should not be required to</b> attend extra classes.")
    ],
    "grammar_title": "情态动词的被动语态",
    "grammar_sections": [
        ("情态动词被动语态结构", [
            ("情态动词", "主动语态", "被动语态"),
            ("can", "We can solve this problem.", "This problem can be solved."),
            ("must", "We must finish the work.", "The work must be finished."),
            ("should", "We should allow students to choose.", "Students should be allowed to choose."),
            ("may", "We may hold the meeting.", "The meeting may be held.")
        ]),
        ("常见表达", [
            ("结构", "含义", "例句"),
            ("should be allowed to", "应该被允许", "Kids should be allowed to play."),
            ("should not be allowed to", "不应该被允许", "Teens shouldn't be allowed to drive."),
            ("must be + V-ed", "必须被", "Homework must be done."),
            ("can be + V-ed", "可以被", "The problem can be solved.")
        ])
    ],
    "grammar_tips": [
        "情态动词 + be + 过去分词，注意 be 不能变为 am/is/are。",
        "否定形式在情态动词后加 not：should not be allowed",
        "疑问形式把情态动词提到主语前：Should teenagers be allowed to...?",
        "<span class=\"wotd-say\" data-speak=\"Rules are made to be broken.\">Rules are made to be broken.</span> 规矩是用来打破的。（谚语，常用于娱乐场景）"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "Teenagers should ____ (allow) to choose their own clothes.", "be allowed"),
        ("基础", "★☆☆", "Students ____ not ____ (allow) to run in the hallways.", "should ... be allowed"),
        ("基础", "★☆☆", "This work must ____ (finish) by Friday.", "be finished"),
        ("基础", "★☆☆", "____ teenagers ____ (allow) to have part-time jobs? (疑问句)", "Should ... be allowed"),
        ("基础", "★☆☆", "I agree ____ you. (填入介词)", "with")
    ],
    "mid_qs": [
        ("提升", "★★☆", "选择：Homework should ____ on time.<br>A. be done B. is done C. was done D. done", "A"),
        ("提升", "★★☆", "The problem can ____ (solve) easily.", "be solved"),
        ("提升", "★★☆", "改主动为被动：Parents should encourage their children. → ____.", "Children should be encouraged by their parents."),
        ("提升", "★★☆", "翻译：青少年不应该被允许每天看电视超过两小时。", "Teenagers should not be allowed to watch TV for more than two hours a day."),
        ("提升", "★★☆", "完成：I think sixteen-year-olds should ____ (allow) to drive.", "be allowed")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：____ we be allowed to bring phones to school?<br>A. Do B. Are C. Should D. Have", "C"),
        ("挑战", "★★★", "改错：Teenagers should allowed to make their own decisions.", "should allowed → should be allowed"),
        ("挑战", "★★★", "改写：We should not allow smoking in public places. → Smoking ____.", "Smoking should not be allowed in public places."),
        ("挑战", "★★★", "写作：用情态动词被动语态写一段关于学校规则的话（你是否同意？为什么？）。", "I think students should be allowed to bring phones to school, but phones must be turned off during class. Also, we should be allowed to choose our own after-school activities. However, homework must be finished before we can play.")
    ],
    "reading_title": "Should Teenagers Be Allowed to Make Their Own Decisions?",
    "reading_text": [
        "Many teenagers have hobbies. Sometimes these hobbies can get in the way of schoolwork. Some parents might worry about their children's success at school. They think that teenagers should not be allowed to spend too much time on hobbies.",
        "But teenagers believe that they should be allowed to practice their hobbies as much as they want. For example, Liu Yu, a fifteen-year-old boy from Shandong, wants to be a professional runner. He is a running star at his school. He wants to practice running every day.",
        "However, his parents won't allow him to train as much as he would like. They think he should spend more time on his schoolwork. They say, «He needs to think about what will happen if he doesn't become a professional runner.»",
        "Liu Yu disagrees. He says, «I think I should be allowed to make decisions for myself. My dream is to be a professional runner. I understand that my parents care about me, but I believe I can manage both running and schoolwork.»"
    ],
    "reading_gloss": [
        ("get in the way of", "妨碍"),
        ("professional", "职业的；专业的"),
        ("train", "训练"),
        ("care about", "关心"),
        ("make decisions", "做决定")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What is Liu Yu's dream?", "To be a professional runner."),
        ("阅读", "★★☆", "Why won't Liu Yu's parents allow him to train as much as he wants?", "Because they think he should spend more time on schoolwork."),
        ("阅读", "★★☆", "What does Liu Yu think about his parents' worry?", "He understands but believes he can manage both running and schoolwork."),
        ("阅读", "★★★", "What is the main argument in this passage?", "Whether teenagers should be allowed to make their own decisions about their hobbies and dreams.")
    ],
    "exam_q_type": "任务型阅读",
    "exam_q": "阅读短文，回答问题。",
    "exam_passage": [
        "In many countries, teenagers are not allowed to do certain things until they reach a certain age. For example, in the United States, you must be 16 to get a driver's license. You must be 18 to vote. And you must be 21 to buy alcohol. These laws are made to protect young people. Some people think the ages should be lower. Others think they should be higher. What do you think?"
    ],
    "exam_options": [
        (1, {"A": "At what age can you get a driver's license in the US?", "B": "What is the voting age in the US?", "C": "Why are these laws made?", "D": "How old must you be to buy alcohol in the US?"}),
        (2, {"A": "16", "B": "18", "C": "21", "D": "15"})
    ],
    "exam_answers": ["1. To protect young people.", "2. B - 18"],
    "writing_prompt": "写一篇短文讨论「青少年是否应该被允许自己选择衣服」。给出你的观点和理由。",
    "writing_framework": [
        "开头：引出话题，提出不同看法",
        "正方观点：支持自己选衣服的理由",
        "反方观点：穿校服的好处",
        "你的立场：你认为应该如何",
        "结尾：总结你的观点"
    ],
    "writing_model_en": "Should teenagers be allowed to choose their own clothes? Different people have different opinions. Some people think teenagers should be allowed to choose their own clothes. They say it helps teens express themselves and build confidence. However, others think students should wear uniforms. They say uniforms save time and reduce comparison among students. In my opinion, teenagers should be allowed to choose their own clothes on weekends, but they should wear uniforms to school. This way, they can express themselves while keeping discipline at school.",
    "writing_model_cn": "青少年是否应该被允许自己选择衣服？不同的人有不同的看法。有些人认为青少年应该被允许自己选择衣服。他们说这有助于青少年表达自己和建立自信。然而，其他人认为学生应该穿校服。他们说校服节省时间，减少学生之间的比较。在我看来，青少年在周末应该被允许选择自己的衣服，但上学应该穿校服。这样，他们既可以表达自己，又能保持学校纪律。",
    "project_title": "Class Rules Debate",
    "project_desc": "组织一场班级辩论赛，讨论「我们应该被允许做什么」——讨论并制定你们自己的班级规则。",
    "project_steps": [
        "小组讨论：你们认为学校/班级中哪些规则需要改变",
        "列出3-5条你认为应该改变的规定",
        "用 should (not) be allowed to 写出你的观点",
        "分组辩论（正方 vs 反方）",
        "全班投票，制定最终版班级公约",
        "将班级公约用英文展示在教室"
    ],
    "project_rubric": [
        "观点明确、论据充分",
        "正确使用了 should be allowed to 结构",
        "辩论中尊重对方观点",
        "最终的班级公约合理可行",
        "英文表达基本准确"
    ],
    "checklist": [
        "我能理解情态动词被动语态的结构",
        "我能用 should be allowed to 表达允许和禁止",
        "我能表达同意和不同意",
        "我能理解阅读中关于决定权的讨论",
        "我能写关于规则的文章"
    ],
    "feynman": "向同桌解释情态动词被动语态的结构：情态动词 + be + 过去分词，并举例说明。",
    "review": [
        "🔵 1天后：复习情态动词被动语态",
        "🟢 3天后：复习规则和许可相关词汇",
        "🟡 1周后：复述刘宇的故事",
        "🔴 1月后：写一篇关于学校规则的短文"
    ],
    "next_unit_title": "U8: It must belong to Carla.",
    "next_unit_desc": "学习情态动词表推测，学会推理和判断。"
}

# ==================== Unit 08 ====================
UNITS_9["u08"] = {
    "num": "U8",
    "title": "It must belong to Carla.",
    "topic": "推测与判断",
    "en_topic": "Speculation and Judgment",
    "functions": "Make inferences and guesses about things and people",
    "grammar": "Modal verbs for deduction: must, might, could, can't",
    "writing": "Write a story using reasoning and deduction",
    "can_do": [
        "能用情态动词表推测",
        "能根据证据做出推理判断",
        "能描述物品的所有者",
        "能写推理性的小故事"
    ],
    "dialogue_scene": "Linda和Tom在教室里发现了一个无人认领的书包，在推测书包的主人。",
    "dialogue": [
        ("Linda", "Look! There's a schoolbag on the desk. Whose is it?", "看！桌子上有一个书包。是谁的？"),
        ("Tom", "I'm not sure. It could be Maria's. She has a pink schoolbag.", "我不确定。可能是玛丽亚的。她有一个粉色的书包。"),
        ("Linda", "No, it can't be hers. Her schoolbag is on her desk. I saw it just now.", "不，不可能是她的。她的书包在她桌子上。我刚才看到了。"),
        ("Tom", "Then it must belong to a girl. There's a hair band in it.", "那它一定是一个女生的。里面有一个发带。"),
        ("Linda", "It might be Lucy's. She has long hair and wears hair bands.", "可能是露西的。她留着长发，戴发带。"),
        ("Tom", "But Lucy is absent today. Wait, there's a science magazine in it. It could be Bob's.", "但露西今天缺席。等等，里面有一本科学杂志。可能是鲍勃的。"),
        ("Linda", "It can't be Bob's. He doesn't like science. I think it must be Tony's. He loves science magazines.", "不可能是鲍勃的。他不喜欢科学。我认为一定是托尼的。他喜欢科学杂志。"),
        ("Tom", "You're right! And look, there's a name tag inside. It IS Tony's!", "你说得对！看，里面有一个名字标签。的确是托尼的！")
    ],
    "key_points": [
        "must + 动词原形 表示「一定……」（非常肯定的推测）— It <b>must</b> belong to Carla.",
        "might/could + 动词原形 表示「可能是……」（不太肯定的推测）— It <b>could</b> be Maria's.",
        "can't + 动词原形 表示「不可能是……」（否定推测）— It <b>can't</b> be hers.",
        "belong to + 人 表示「属于某人」— It must belong <b>to</b> Carla."
    ],
    "vocab": [
        ("belong", "bɪˈlɒŋ", "v.", "属于", "This book belongs to me.", "这本书属于我。"),
        ("whose", "huːz", "pron.", "谁的", "Whose jacket is this?", "这是谁的夹克？"),
        ("truck", "trʌk", "n.", "卡车", "A big truck drove past.", "一辆大卡车开过去了。"),
        ("picnic", "ˈpɪknɪk", "n.", "野餐", "We had a picnic in the park.", "我们在公园里野餐了。"),
        ("rabbit", "ˈræbɪt", "n.", "兔子", "The rabbit is eating carrots.", "兔子在吃胡萝卜。"),
        ("attend", "əˈtend", "v.", "参加；出席", "I attended a concert last night.", "我昨晚参加了一场音乐会。"),
        ("valuable", "ˈvæljuəbl", "adj.", "有价值的；宝贵的", "This is a valuable painting.", "这是一幅有价值的画。"),
        ("pink", "pɪŋk", "adj./n.", "粉色的", "She wears a pink dress.", "她穿着一条粉色裙子。"),
        ("anybody", "ˈenibɒdi", "pron.", "任何人", "Is there anybody in the room?", "房间里有人吗？"),
        ("noise", "nɔɪz", "n.", "噪音；声音", "I heard a strange noise.", "我听到了一个奇怪的声音。"),
        ("happening", "ˈhæpənɪŋ", "n.", "事件；发生的事情", "What's happening over there?", "那边发生了什么事？"),
        ("neighbor", "ˈneɪbər", "n.", "邻居", "My neighbor is very kind.", "我的邻居很友好。"),
        ("interview", "ˈɪntərvjuː", "n./v.", "采访；面试", "The reporter interviewed the mayor.", "记者采访了市长。"),
        ("wind", "wɪnd", "n.", "风", "The wind is blowing hard.", "风很大。"),
        ("sleepy", "ˈsliːpi", "adj.", "困倦的；瞌睡的", "I feel sleepy after lunch.", "午饭后我感到困倦。"),
        ("laboratory", "ləˈbɒrətri", "n.", "实验室", "The science lab is on the second floor.", "科学实验室在二楼。"),
        ("receive", "rɪˈsiːv", "v.", "收到；接受", "I received a gift from my friend.", "我收到了朋友的一份礼物。"),
        ("alien", "ˈeɪliən", "n.", "外星人", "Do you believe in aliens?", "你相信有外星人吗？"),
        ("suit", "suːt", "n./v.", "套装；适合", "This dress suits you very well.", "这条裙子很适合你。"),
        ("express", "ɪkˈspres", "v.", "表达", "I can't express how happy I am.", "我无法表达我有多开心。"),
        ("circle", "ˈsɜːrkl", "n./v.", "圆圈；环绕", "Draw a circle on the paper.", "在纸上画一个圈。"),
        ("purple", "ˈpɜːrpl", "adj./n.", "紫色的", "She loves purple flowers.", "她喜欢紫色的花。")
    ],
    "patterns": [
        ("主语 + must + 动词原形",
         "表示非常肯定的推测（≈ 一定是）。",
         "The schoolbag <b>must belong to</b> Carla. / She <b>must be</b> at home. I saw her car."),
        ("主语 + could/might + 动词原形",
         "表示可能性较小的推测（≈ 可能是）。",
         "It <b>could be</b> Maria's bag. / He <b>might be</b> in the library."),
        ("主语 + can't + 动词原形",
         "表示否定的推测（≈ 不可能是）。",
         "It <b>can't be</b> Bob's. He doesn't like science. / She <b>can't be</b> at school. She's sick."),
        ("主语 + must/could/might + be + V-ing",
         "推测正在进行的动作。",
         "They <b>must be</b> studying. The light is on. / He <b>might be</b> sleeping.")
    ],
    "grammar_title": "情态动词表推测",
    "grammar_sections": [
        ("推测的程度", [
            ("情态动词", "可能性", "含义"),
            ("must", "100% (非常肯定)", "一定是……"),
            ("can't", "0% (非常肯定否定)", "不可能是……"),
            ("could", "约30-50%", "可能是……"),
            ("might", "约10-30%", "也许是……")
        ]),
        ("不同时态的推测", [
            ("时态", "结构", "例句"),
            ("对现在的推测", "must/could/might/can't + V", "He must be tired."),
            ("对正在进行的推测", "must/could/might + be V-ing", "They must be sleeping."),
            ("对过去的推测", "must/could/might + have V-ed", "She must have left.")
        ])
    ],
    "grammar_tips": [
        "must 表推测只用于肯定句，否定句只能用 can't。",
        "can't be 和 must not be 的区别：can't be = 不可能是；must not be = 禁止是。",
        "belong to 后接人称代词时要用宾格（me/him/her）。",
        "<span class=\"wotd-say\" data-speak=\"Where there is smoke, there is fire.\">Where there is smoke, there is fire.</span> 无风不起浪。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "It ____ (一定是) be Carla's. She loves pink.", "must"),
        ("基础", "★☆☆", "It ____ (不可能是) be Tom's. He doesn't like science.", "can't"),
        ("基础", "★☆☆", "It ____ (可能是) be Maria's. I'm not sure.", "could / might"),
        ("基础", "★☆☆", "This book belongs ____ my sister.", "to"),
        ("基础", "★☆☆", "____ (谁的) schoolbag is this?", "Whose")
    ],
    "mid_qs": [
        ("提升", "★★☆", "The baby is crying. She ____ (must/can't) be hungry.", "must"),
        ("提升", "★★☆", "The light is off. They ____ (must/can't) be at home.", "can't"),
        ("提升", "★★☆", "选择：Whose gloves are these? They ____ be Lucy's. She likes wearing gloves.<br>A. must B. could C. can't D. might", "A"),
        ("提升", "★★☆", "改写：Probably the book is his. → The book ____.", "The book must be his. / The book must belong to him."),
        ("提升", "★★☆", "翻译：那个声音可能是风。", "That noise could be the wind.")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：He ____ be at school. I saw him go into the building.<br>A. must B. could C. can't D. might", "A"),
        ("挑战", "★★★", "完成句子：Look at that man running. He ____ (must/can't) be late for the train.", "must"),
        ("挑战", "★★★", "改错：This must be Tom's pen, doesn't it?", "doesn't → isn't"),
        ("挑战", "★★★", "写作：你在教室里发现了一个水杯。用推测结构写出3-4句关于它可能是谁的推理过程。", "This water bottle must belong to a girl because it's pink. It could be Anna's, but it can't be Lucy's — she's absent today. I think it must be Anna's. I'll ask her.")
    ],
    "reading_title": "The Mystery of the Strange Noise",
    "reading_text": [
        "Our neighborhood used to be very quiet. But recently, strange things have been happening. People in the neighborhood hear noises in the night. They don't know what is happening.",
        "Some people think it must be teenagers having fun. They say, «Teens must be playing tricks.» But others disagree. They say, «It can't be teenagers. The noises are too loud.»",
        "One woman said she saw something running in the dark. She thought it could be a bear. But another neighbor said, «It can't be a bear. There are no bears near our town.»",
        "A group of neighbors decided to find out what it was. They stayed up one night. They heard the noise again and followed it. Guess what? It was just a big dog! The dog was looking for food. Everyone felt silly, but they were also relieved."
    ],
    "reading_gloss": [
        ("neighborhood", "社区；街区"),
        ("strange", "奇怪的"),
        ("playing tricks", "搞恶作剧"),
        ("bear", "熊"),
        ("relieved", "如释重负的；放心的")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What strange thing has been happening?", "People have been hearing noises at night."),
        ("阅读", "★★☆", "What did some people think the noise was?", "They thought it must be teenagers playing tricks."),
        ("阅读", "★★☆", "What did the noise turn out to be?", "It was just a big dog looking for food."),
        ("阅读", "★★★", "How did the neighbors feel after finding out the truth?", "They felt silly but relieved.")
    ],
    "exam_q_type": "完形填空 — 推理故事",
    "exam_q": "阅读短文，选择最佳答案。",
    "exam_passage": [
        "I found a wallet on the ground. I opened it and saw some money and a photo. It 1 belong to someone in my school. The photo showed a girl with long hair. She 2 be a student. I asked around. 「I think it 3 be Lily's,」 said one friend. But Lily said her wallet was in her bag. Then I saw the initials on the wallet: J.L. It 4 be Julia's! There is a girl named Julia in my class. I found her and asked. 「Yes! It's mine!」 she said happily. The wallet 5 belongs to Julia."
    ],
    "exam_options": [
        (1, {"A": "can't", "B": "must", "C": "might", "D": "should"}),
        (2, {"A": "must", "B": "can't", "C": "won't", "D": "shouldn't"}),
        (3, {"A": "must", "B": "can't", "C": "could", "D": "will"}),
        (4, {"A": "can't", "B": "must", "C": "couldn't", "D": "wouldn't"}),
        (5, {"A": "must", "B": "can't", "C": "could", "D": "should"})
    ],
    "exam_answers": ["1. B", "2. A", "3. C", "4. B", "5. A"],
    "writing_prompt": "想象你在一个旧房间里发现了一个神秘的箱子。用推测结构（must/can't/might/could）描述它的主人可能是什么样的人。",
    "writing_framework": [
        "开头：描述你在哪里发现了什么",
        "对物品的描述（颜色、材质、形状等）",
        "对主人的推测（年龄、性别、职业等）",
        "推理的依据（物品中的线索）",
        "结尾：谜底揭晓或留下悬念"
    ],
    "writing_model_en": "Yesterday, I found an old box in the attic. It was covered in dust. It must have been there for a long time. The box was blue and had a lock. It might belong to a child because there were stickers on it. Inside, I found some old letters and photos. The person in the photos could be my grandmother when she was young. The letters were written in English, so the owner must have studied English. I asked my grandmother, and she said the box was hers! She used it to keep her treasures when she was a girl.",
    "writing_model_cn": "昨天，我在阁楼上发现了一个旧箱子。上面布满了灰尘。它一定在那里很久了。箱子是蓝色的，有一把锁。它可能属于一个孩子，因为上面有贴纸。在里面，我找到了一些旧信和照片。照片中的人可能是我祖母年轻的时候。信是用英文写的，所以箱子的主人一定学过英语。我问了祖母，她说箱子是她的！她小时候用它来保存她的宝贝。",
    "project_title": "Whose Is It? — A Classroom Mystery Game",
    "project_desc": "举办一场「失物招领」推理游戏。每位同学从家里带一件物品放到箱子里，大家轮流推测物品的主人。",
    "project_steps": [
        "每人带一件不常用的个人物品放进神秘箱",
        "随机抽取一件物品，描述它",
        "用 must/could/might/can't 推测它的主人",
        "说出你的推理过程（物品的特征→可能的用途→主人）",
        "猜测三次后揭晓答案",
        "记录猜对的数量，评出最佳侦探"
    ],
    "project_rubric": [
        "描述物品清晰、准确",
        "正确使用情态动词表推测",
        "推理过程合理、有逻辑",
        "积极参与、尊重他人",
        "能分析自己猜对/错的原因"
    ],
    "checklist": [
        "我能用情态动词表推测",
        "我能区分 must/can't/could/might 的推测程度",
        "我能根据线索推理和判断",
        "我能理解阅读中的推理故事",
        "我能写推理性的短文"
    ],
    "feynman": "向同桌解释 must、can't、could、might 在表推测时的区别和用法。",
    "review": [
        "🔵 1天后：复习情态动词表推测的用法",
        "🟢 3天后：复习推测相关词汇",
        "🟡 1周后：复述神秘噪音的故事",
        "🔴 1月后：写一个推理小故事"
    ],
    "next_unit_title": "U9: I like music that I can dance to.",
    "next_unit_desc": "学习定语从句，表达偏好和喜好。"
}

# ==================== Unit 09 ====================
UNITS_9["u09"] = {
    "num": "U9",
    "title": "I like music that I can dance to.",
    "topic": "偏好与定从",
    "en_topic": "Preferences and Attributive Clauses",
    "functions": "Express preferences and talk about music/movies",
    "grammar": "Attributive clauses with that/who/which",
    "writing": "Write about your favorite music, movie, or book",
    "can_do": [
        "能用定语从句描述人和物",
        "能表达个人喜好和偏好",
        "能谈论音乐、电影、书籍等话题",
        "能运用 that/who/which 引导定语从句"
    ],
    "dialogue_scene": "Jenny和Mike在学校音乐节上讨论自己喜欢的音乐类型。",
    "dialogue": [
        ("Jenny", "What kind of music do you like, Mike?", "你喜欢什么类型的音乐，迈克？"),
        ("Mike", "I like music that I can dance to. It makes me feel happy.", "我喜欢能跟着跳舞的音乐。它让我感到快乐。"),
        ("Jenny", "I prefer music that has great lyrics. Songs that tell a story are my favorite.", "我更喜欢有好歌词的音乐。能讲故事的歌是我的最爱。"),
        ("Mike", "Do you like the band playing on stage right now?", "你喜欢现在在台上表演的乐队吗？"),
        ("Jenny", "Yes, I love them! They are a band that plays different styles of music.", "是的，我很喜欢！他们是一个演奏不同风格音乐的乐队。"),
        ("Mike", "Who is the singer that is wearing a red jacket?", "那个穿红色夹克的歌手是谁？"),
        ("Jenny", "That's Amy. She is a singer who writes her own songs.", "那是艾米。她是一个自己写歌的歌手。"),
        ("Mike", "Wow, that's cool! I like musicians who are creative.", "哇，太酷了！我喜欢有创造力的音乐人。")
    ],
    "key_points": [
        "定语从句修饰名词或代词，相当于形容词的作用。",
        "that 可以指人或物 — I like music <b>that</b> I can dance to.",
        "who 只指人 — She is a singer <b>who</b> writes her own songs.",
        "which 只指物 — I prefer movies <b>which</b> are funny."
    ],
    "vocab": [
        ("prefer", "prɪˈfɜːr", "v.", "更喜欢", "I prefer tea to coffee.", "比起咖啡我更喜欢茶。"),
        ("lyric", "ˈlɪrɪk", "n.", "歌词", "I love the lyrics of this song.", "我喜欢这首歌的歌词。"),
        ("electronic", "ɪˌlekˈtrɒnɪk", "adj.", "电子的", "He likes electronic music.", "他喜欢电子音乐。"),
        ("smooth", "smuːð", "adj.", "平滑的；流畅的", "The music has a smooth rhythm.", "这段音乐有流畅的节奏。"),
        ("spare", "sper", "adj.", "空闲的；多余的", "I like to read in my spare time.", "我喜欢在空闲时间阅读。"),
        ("direction", "dəˈrekʃn", "n.", "方向；指导", "I have a good sense of direction.", "我有很好的方向感。"),
        ("suppose", "səˈpoʊz", "v.", "假设；认为", "I suppose you're right.", "我想你是对的。"),
        ("case", "keɪs", "n.", "情况；案例", "In that case, I'll come with you.", "那样的话，我和你一起去。"),
        ("war", "wɔːr", "n.", "战争", "War is terrible.", "战争是可怕的。"),
        ("reflect", "rɪˈflekt", "v.", "反映；反射", "Music reflects our feelings.", "音乐反映我们的情感。"),
        ("master", "ˈmæstər", "n./v.", "大师；掌握", "He is a master of the piano.", "他是钢琴大师。"),
        ("perform", "pərˈfɔːrm", "v.", "表演；演奏", "She performed a beautiful song.", "她演唱了一首美丽的歌。"),
        ("praise", "preɪz", "v./n.", "赞扬；表扬", "The teacher praised her for her hard work.", "老师表扬她学习努力。"),
        ("pain", "peɪn", "n.", "疼痛；痛苦", "The pain in my leg is getting better.", "我腿上的疼痛正在好转。"),
        ("wound", "wuːnd", "n.", "伤口；创伤", "The wound healed quickly.", "伤口愈合得很快。"),
        ("musician", "mjuˈzɪʃn", "n.", "音乐人；音乐家", "He is a talented musician.", "他是一位有天赋的音乐家。"),
        ("sense", "sens", "n./v.", "感觉；意识", "I have a sense of achievement.", "我有一种成就感。"),
        ("sadness", "ˈsædnəs", "n.", "悲伤；忧愁", "The song is full of sadness.", "这首歌充满了悲伤。"),
        ("pity", "ˈpɪti", "n.", "遗憾；怜悯", "What a pity!", "真遗憾！"),
        ("total", "ˈtoʊtl", "adj./n.", "总共的；总数", "The total cost is $50.", "总费用是50美元。"),
        ("drama", "ˈdrɑːmə", "n.", "戏剧", "I like watching TV dramas.", "我喜欢看电视剧。"),
        ("documentary", "ˌdɒkjuˈmentri", "n.", "纪录片", "I enjoy watching nature documentaries.", "我喜欢看自然纪录片。")
    ],
    "patterns": [
        ("主语 + 谓语 + 名词 + that + 从句 (that 指人或物)",
         "用 that 引导定语从句修饰名词。",
         "I like music <b>that</b> I can dance to. / She likes movies <b>that</b> are funny."),
        ("主语 + 谓语 + 名词 + who + 从句 (who 指人)",
         "用 who 引导定语从句修饰人。",
         "I prefer singers <b>who</b> write their own songs. / He is a teacher <b>who</b> loves his job."),
        ("主语 + 谓语 + 名词 + which + 从句 (which 指物)",
         "用 which 引导定语从句修饰物。",
         "The book <b>which</b> I borrowed is interesting. / The song <b>which</b> she sang is beautiful."),
        ("Prefer A to B / Prefer to do A rather than do B",
         "表示偏好。",
         "I <b>prefer</b> pop music <b>to</b> rock. / She <b>prefers</b> to read at home.")
    ],
    "grammar_title": "定语从句（Attributive Clauses）",
    "grammar_sections": [
        ("关系代词的用法", [
            ("关系代词", "指代", "在从句中的作用", "例句"),
            ("that", "人/物", "主语/宾语", "The music that I like is pop."),
            ("who", "人", "主语/宾语", "The girl who sings well is Amy."),
            ("which", "物", "主语/宾语", "The movie which I saw was great.")
        ]),
        ("关系代词的省略", [
            ("情况", "说明", "例句"),
            ("作宾语时可省略", "关系代词在从句中作宾语时可以省略", "The song (that) she sang was beautiful."),
            ("作主语不可省略", "关系代词在从句中作主语时不可省略", "The girl who is singing is my friend.")
        ])
    ],
    "grammar_tips": [
        "that 可以指人也可以指物，更口语化。",
        "which 只能指物，不能指人。",
        "who 只能指人，不能指物。",
        "关系代词在从句中作宾语时可以省略（即从句中已有主语）。",
        "<span class=\"wotd-say\" data-speak=\"Music is the medicine of the mind.\">Music is the medicine of the mind.</span> 音乐是心灵的良药。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "I like music ____ I can dance to. (填入关系代词)", "that"),
        ("基础", "★☆☆", "She is a singer ____ writes her own songs. (填入关系代词)", "who/that"),
        ("基础", "★☆☆", "The book ____ I read is very interesting. (填入关系代词, 可省略)", "that/which（可省略）"),
        ("基础", "★☆☆", "I ____ (更喜欢) tea to coffee.", "prefer"),
        ("基础", "★☆☆", "I like movies ____ are funny. (填入关系代词)", "that/which")
    ],
    "mid_qs": [
        ("提升", "★★☆", "The woman ____ is standing there is my teacher.<br>A. which B. who C. what D. when", "B"),
        ("提升", "★★☆", "This is the best song ____ I have ever heard.", "that"),
        ("提升", "★★☆", "合并句子：I like the music. The music has a good beat. → ____.", "I like the music that has a good beat."),
        ("提升", "★★☆", "翻译：我更喜欢能让我开心的电影。", "I prefer movies that make me happy."),
        ("提升", "★★☆", "The boy ____ (who/which) is playing basketball is my brother.", "who")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：He is the man ____ helped me yesterday.<br>A. which B. who C. what D. whom", "B"),
        ("挑战", "★★★", "改错：The book which I bought it yesterday is interesting.", "去掉 it（which 已经是宾语）"),
        ("挑战", "★★★", "用定语从句改写：I have a friend. He can speak three languages. → ____.", "I have a friend who can speak three languages."),
        ("挑战", "★★★", "写作：用定语从句写一段话（至少3句）介绍你最喜欢的音乐或音乐人。", "My favorite singer is Jay Chou. He is a singer who writes his own songs. I like music that has meaningful lyrics. His songs always make me feel relaxed.")
    ],
    "reading_title": "What Kind of Music Do You Like?",
    "reading_text": [
        "Music is an important part of our lives. Different people like different kinds of music. Some people like music that is loud and energetic. Others prefer music that is quiet and peaceful.",
        "I have a friend named Sarah. She likes music that she can dance to. She says dancing makes her feel free and happy. Her favorite band is one that plays upbeat pop music.",
        "My brother, on the other hand, prefers music that tells a story. He loves folk music and songs that have deep lyrics. He especially likes musicians who sing about life and nature.",
        "As for me, I like all kinds of music. I believe that every song has something special. Music that moves our hearts is always good music, no matter what style it is. After all, music is a language that everyone can understand."
    ],
    "reading_gloss": [
        ("energetic", "充满活力的"),
        ("upbeat", "欢快的；乐观的"),
        ("folk music", "民谣"),
        ("deep lyrics", "深刻的歌词"),
        ("moves our hearts", "打动我们的心"),
        ("no matter", "无论")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What kind of music does Sarah like?", "She likes music that she can dance to."),
        ("阅读", "★★☆", "Why does the writer's brother like folk music?", "Because he prefers music that tells a story."),
        ("阅读", "★★☆", "What does the writer think about music?", "She thinks every song has something special."),
        ("阅读", "★★★", "What does «Music is a language that everyone can understand» mean?", "It means music can communicate with anyone, regardless of language barriers.")
    ],
    "exam_q_type": "短文填空 — 关系代词",
    "exam_q": "用 that, who, which 填空。",
    "exam_passage": [
        "I have a friend 1 loves movies. She only watches movies 2 make her laugh. She says comedies are the best. Her favorite actor is one 3 is very funny. Last week, she recommended a movie 4 I should watch. It was the funniest movie 5 I have ever seen! I now understand why she likes comedies."
    ],
    "exam_options": [
        (1, {"A": "who", "B": "which", "C": "what", "D": "when"}),
        (2, {"A": "who", "B": "that", "C": "what", "D": "whose"}),
        (3, {"A": "which", "B": "who", "C": "whom", "D": "what"}),
        (4, {"A": "who", "B": "whom", "C": "that", "D": "what"}),
        (5, {"A": "that", "B": "what", "C": "who", "D": "whom"})
    ],
    "exam_answers": ["1. A", "2. B", "3. B", "4. C", "5. A"],
    "writing_prompt": "写一篇短文介绍你最喜欢的一部电影或一首歌曲，包括它的类型、内容和你喜欢它的原因。请使用至少三个定语从句。",
    "writing_framework": [
        "开头：引出你最喜欢的电影/歌曲",
        "类型和风格：它是什么样的（使用定语从句）",
        "内容简介：关于什么",
        "喜欢的原因：为什么你喜欢它",
        "结尾：它给你带来什么感受"
    ],
    "writing_model_en": "My favorite movie is Zootopia. It is a cartoon that tells the story of a rabbit who wants to become a police officer. The movie shows a world where animals live together. I like movies that are both funny and meaningful. Zootopia is a film that makes people think about fairness and dreams. The main character, Judy Hopps, is a rabbit who never gives up. She teaches me that we should always follow our dreams.",
    "writing_model_cn": "我最喜欢的电影是《疯狂动物城》。这是一部讲述一只想成为警察的兔子的卡通电影。电影展示了一个动物们共同生活的世界。我喜欢既有趣又有意义的电影。《疯狂动物城》是一部让人们思考公平和梦想的电影。主角朱迪·霍普斯是一只永不放弃的兔子。她教会我们永远要追随自己的梦想。",
    "project_title": "My Music Playlist",
    "project_desc": "创建一份你个人的「最爱歌单」播放列表，包含5首歌曲，每首歌用英语写出你喜欢的理由（使用定语从句）。",
    "project_steps": [
        "选择5首你最喜爱的歌曲",
        "每首歌写出歌手名和歌名",
        "用英语写出你喜欢每首歌的原因（使用定语从句）",
        "列出歌词中你最喜欢的一句",
        "制作一份精美的歌单海报",
        "在班级中分享你的歌单，播放片段"
    ],
    "project_rubric": [
        "选择了5首有意义的歌曲",
        "每个原因都使用了定语从句",
        "关系代词使用正确（that/who/which）",
        "海报设计精美",
        "口头分享流利自信"
    ],
    "checklist": [
        "我能理解定语从句的结构",
        "我能正确使用 that/who/which",
        "我能用定语从句表达喜好",
        "我能理解阅读中关于音乐的讨论",
        "我能写关于喜好的短文"
    ],
    "feynman": "向同桌解释定语从句中 that、who、which 的区别和用法。",
    "review": [
        "🔵 1天后：复习关系代词的用法",
        "🟢 3天后：复习喜好表达和音乐词汇",
        "🟡 1周后：复述关于音乐的文章",
        "🔴 1月后：写你最喜欢的电影评论"
    ],
    "next_unit_title": "U10: You're supposed to shake hands.",
    "next_unit_desc": "学习 be supposed to 结构，了解不同国家的礼仪文化。"
}

# ==================== Unit 10 ====================
UNITS_9["u10"] = {
    "num": "U10",
    "title": "You're supposed to shake hands.",
    "topic": "礼仪与文化",
    "en_topic": "Customs and Culture",
    "functions": "Talk about customs and what you are supposed to do",
    "grammar": "Be supposed to + V (应该/被期望做某事)",
    "writing": "Describe customs and etiquette in different countries",
    "can_do": [
        "能用 be supposed to 表达应该做什么",
        "能比较不同国家的礼仪习惯",
        "能礼貌地询问和说明文化差异",
        "能写关于礼仪文化的文章"
    ],
    "dialogue_scene": "中国学生李华第一次去美国参加交换项目，向美国朋友Mike询问美国礼仪。",
    "dialogue": [
        ("Li Hua", "Mike, I'm a little nervous. What am I supposed to do when I meet someone for the first time?", "迈克，我有点紧张。我第一次见到别人时应该做什么？"),
        ("Mike", "You're supposed to shake hands. It's the most common greeting in the US.", "你应该握手。这是美国最常见的问候方式。"),
        ("Li Hua", "What about eye contact? In China, it's not always polite to look directly at someone.", "那眼神接触呢？在中国，直视别人不总是礼貌的。"),
        ("Mike", "Oh, in the US, you're supposed to make eye contact. It shows you are confident and honest.", "哦，在美国，你应该有眼神交流。这显示你自信和诚实。"),
        ("Li Hua", "I see. And when I'm invited to dinner, am I supposed to arrive on time?", "我明白了。那当我被邀请吃饭时，我应该准时到吗？"),
        ("Mike", "Yes, you're supposed to arrive on time. Being late is considered impolite.", "是的，你应该准时到。迟到被认为是不礼貌的。"),
        ("Li Hua", "What should I do at the table? I'm not supposed to make noise while eating, am I?", "吃饭时我应该怎么做？我不应该在吃饭时发出声音，对吗？"),
        ("Mike", "That's right. And you're supposed to say «excuse me» if you need to leave the table. Don't worry, you'll do great!", "对。如果你需要离开餐桌，应该说「抱歉」。别担心，你会做得很好的！")
    ],
    "key_points": [
        "be supposed to do 表示「应该做某事；被期望做某事」— You <b>are supposed to</b> shake hands.",
        "be not supposed to do 表示「不应该做某事」— You <b>are not supposed to</b> eat with your hands.",
        "和 should 的区别：should 语气更强，be supposed to 语气较委婉。",
        "不同国家礼仪不同：日本鞠躬、法国贴面、美国握手。"
    ],
    "vocab": [
        ("shake", "ʃeɪk", "v.", "握着；摇动", "We shake hands when we meet.", "我们见面时握手。"),
        ("kiss", "kɪs", "v./n.", "吻；亲吻", "In some countries, people kiss on the cheek.", "在一些国家，人们亲吻脸颊。"),
        ("custom", "ˈkʌstəm", "n.", "习俗；风俗", "Each country has its own customs.", "每个国家都有自己的习俗。"),
        ("greet", "ɡriːt", "v.", "问候；打招呼", "People greet each other in different ways.", "人们用不同的方式互相问候。"),
        ("relaxed", "rɪˈlækst", "adj.", "放松的；随意的", "The atmosphere was very relaxed.", "氛围非常轻松。"),
        ("value", "ˈvæljuː", "n./v.", "价值；重视", "We value punctuality.", "我们重视守时。"),
        ("drop", "drɒp", "v.", "掉下；拜访", "Drop by anytime if you're free.", "有空随时来坐坐。"),
        ("capital", "ˈkæpɪtl", "n.", "首都；资本", "Paris is the capital of France.", "巴黎是法国的首都。"),
        ("noon", "nuːn", "n.", "正午；中午", "Let's meet at noon.", "我们中午见。"),
        ("mad", "mæd", "adj.", "生气的；疯狂的", "Don't get mad at me.", "别对我生气。"),
        ("effort", "ˈefərt", "n.", "努力", "Make an effort to learn the local customs.", "努力了解当地习俗。"),
        ("passport", "ˈpæspɔːrt", "n.", "护照", "Don't forget your passport.", "别忘了你的护照。"),
        ("chalk", "tʃɔːk", "n.", "粉笔", "Write with chalk on the blackboard.", "用粉笔在黑板上写。"),
        ("blackboard", "ˈblækbɔːrd", "n.", "黑板", "The teacher is writing on the blackboard.", "老师在黑板上写字。"),
        ("northern", "ˈnɔːrðərn", "adj.", "北方的", "It's cold in northern China.", "中国北方很冷。"),
        ("coast", "koʊst", "n.", "海岸", "We drove along the coast.", "我们沿着海岸开车。"),
        ("season", "ˈsiːzn", "n.", "季节", "Which season do you like best?", "你最喜欢哪个季节？"),
        ("knock", "nɒk", "v.", "敲", "Knock on the door before entering.", "进入前先敲门。"),
        ("basic", "ˈbeɪsɪk", "adj.", "基本的", "These are the basic rules.", "这些是基本规则。"),
        ("exchange", "ɪksˈtʃeɪndʒ", "n./v.", "交换；交流", "I'm on an exchange program.", "我在参加一个交换项目。"),
        ("gradually", "ˈɡrædʒuəli", "adv.", "逐渐地", "I gradually got used to the culture.", "我逐渐适应了这里的文化。"),
        ("polite", "pəˈlaɪt", "adj.", "礼貌的", "It's polite to say thank you.", "说谢谢是有礼貌的。")
    ],
    "patterns": [
        ("主语 + be supposed to + 动词原形",
         "表示「应该做某事」。",
         "You <b>are supposed to</b> shake hands. / You <b>are supposed to</b> arrive on time."),
        ("主语 + be not supposed to + 动词原形",
         "表示「不应该做某事」。",
         "You <b>are not supposed to</b> eat with your hands. / We <b>are not supposed to</b> be late."),
        ("What + be + 主语 + supposed to do?",
         "询问应该做什么。",
         "<b>What am I supposed to</b> do? / <b>What are we supposed to</b> wear?"),
        ("You're supposed to... / You should...",
         "be supposed to 比 should 语气更委婉。",
         "<b>You're supposed to</b> bow in Japan. / <b>You should</b> try the local food.")
    ],
    "grammar_title": "Be supposed to 结构",
    "grammar_sections": [
        ("be supposed to 的用法", [
            ("形式", "用法", "含义", "例句"),
            ("肯定句", "be supposed to + V", "应该", "You are supposed to shake hands."),
            ("否定句", "be not supposed to + V", "不应该", "You are not supposed to be late."),
            ("疑问句", "Be + 主语 + supposed to + V?", "应该……吗？", "Am I supposed to bring a gift?")
        ]),
        ("be supposed to vs should", [
            ("表达", "语气", "用法", "例句"),
            ("be supposed to", "较委婉", "表示惯例或期望", "You're supposed to bow in Japan."),
            ("should", "较强", "表示义务或建议", "You should study hard.")
        ])
    ],
    "grammar_tips": [
        "be supposed to 中的 be 动词要随主语变化（am/is/are）。",
        "be supposed to 的否定式在 be 后加 not。",
        "be supposed to 的疑问式把 be 动词提前。",
        "<span class=\"wotd-say\" data-speak=\"When in Rome, do as the Romans do.\">When in Rome, do as the Romans do.</span> 入乡随俗。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "You ____ (应该) shake hands when you meet someone in the US.", "are supposed to"),
        ("基础", "★☆☆", "You ____ not ____ (不应该) eat with your hands at a formal dinner.", "are ... supposed"),
        ("基础", "★☆☆", "____ I ____ (应该) bring a gift when I visit someone?", "Am ... supposed to"),
        ("基础", "★☆☆", "In Japan, you're supposed to ____ (鞠躬) when you meet someone.", "bow"),
        ("基础", "★☆☆", "翻译：你应该准时到达。", "You are supposed to arrive on time.")
    ],
    "mid_qs": [
        ("提升", "★★☆", "选择：You ____ make noise while eating in Western countries.<br>A. are supposed to B. are not supposed to C. supposed to D. not supposed to", "B"),
        ("提升", "★★☆", "What ____ I ____ (suppose) to do if I'm invited to dinner?", "am ... supposed"),
        ("提升", "★★☆", "您在法国应该亲吻脸颊而不是握手。→ In France, you ____.", "In France, you are supposed to kiss on the cheek instead of shaking hands."),
        ("提升", "★★☆", "改错：You are suppose to arrive on time.", "suppose → supposed"),
        ("提升", "★★☆", "You ____ (should/are supposed to) try the local food when you travel.", "should / are supposed to")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：You ____ to bring a gift, but it's a nice thing to do.<br>A. are supposed B. aren't supposed C. don't suppose D. didn't suppose", "B"),
        ("挑战", "★★★", "完成句子：In China, you're supposed to ____ (用筷子吃饭) while in Western countries, you're supposed to use a fork.", "eat with chopsticks"),
        ("挑战", "★★★", "用 be supposed to 改写：People expect you to dress formally. → ____.", "You are supposed to dress formally."),
        ("挑战", "★★★", "写作：比较中国和美国在餐桌礼仪上的不同（至少3点）。", "In China, you're supposed to use chopsticks, but in the US, you're supposed to use a fork and knife. In China, you're supposed to share dishes, but in the US, everyone has their own plate. In China, it's okay to make some noise while eating soup, but in the US, you're not supposed to.")
    ],
    "reading_title": "Customs Around the World",
    "reading_text": [
        "Different countries have different customs. What is polite in one country might be impolite in another. It's important to learn about these customs before you travel.",
        "In Japan, you are supposed to bow when you greet someone. Bowing shows respect. You are also supposed to remove your shoes before entering someone's home. In Japan, it's considered impolite to tip at restaurants.",
        "In France, you are supposed to kiss on the cheek when you greet friends. The number of kisses varies by region. In France, it's polite to say «bonjour» when you enter a store. You are supposed to keep your hands on the table during meals.",
        "In Korea, you are supposed to use both hands when giving something to an older person. It shows respect. You are also supposed to look away when drinking with someone older.",
        "Learning these customs can help you avoid misunderstandings and show respect for other cultures. Remember: when in Rome, do as the Romans do."
    ],
    "reading_gloss": [
        ("bow", "鞠躬"),
        ("remove", "脱掉"),
        ("tip", "给小费"),
        ("region", "地区"),
        ("misunderstanding", "误解")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What are you supposed to do when greeting someone in Japan?", "You are supposed to bow."),
        ("阅读", "★★☆", "Is it polite to tip at restaurants in Japan?", "No, it's considered impolite."),
        ("阅读", "★★☆", "What should you say when you enter a store in France?", "You should say «bonjour»."),
        ("阅读", "★★★", "Why is it important to learn about local customs before traveling?", "It can help you avoid misunderstandings and show respect for other cultures.")
    ],
    "exam_q_type": "任务型阅读 — 文化差异",
    "exam_q": "阅读短文，回答问题。",
    "exam_passage": [
        "Table manners are different around the world. In China, you are supposed to wait for the oldest person to start eating. You are not supposed to stick your chopsticks into your food. In Western countries, you are supposed to keep your napkin on your lap. You are supposed to say «excuse me» if you need to leave the table. In some Middle Eastern countries, you are supposed to eat with your right hand. The left hand is considered unclean."
    ],
    "exam_options": [
        (1, {"A": "What are Chinese supposed to do before eating?", "B": "Why should you wait for the oldest person?", "C": "How to use chopsticks correctly?", "D": "What is the Chinese dining etiquette?"}),
        (2, {"A": "Keep your napkin on your lap.", "B": "Keep your napkin on the table.", "C": "Don't use a napkin.", "D": "Fold the napkin."}),
        (3, {"A": "The right hand.", "B": "The left hand.", "C": "Both hands.", "D": "Chopsticks."})
    ],
    "exam_answers": ["1. Wait for the oldest person to start eating.", "2. A", "3. A"],
    "writing_prompt": "写一篇短文介绍中国的两个重要习俗或礼仪（如见面礼仪、餐桌礼仪、拜访礼仪等），使用 be supposed to 结构。",
    "writing_framework": [
        "开头：介绍中国的基本礼仪和你将提到的习俗",
        "习俗1：见面礼仪或称呼方式",
        "习俗2：餐桌礼仪或拜访礼仪",
        "解释这些习俗背后的文化含义",
        "结尾：总结中国礼仪文化的特点"
    ],
    "writing_model_en": "China has many customs that visitors should know. When you meet someone for the first time in China, you are supposed to shake hands. A light handshake is polite. You are supposed to address people by their title and last name. For example, you should say «Teacher Wang» instead of just «Wang». At the dinner table, you are supposed to wait for the oldest person to start eating. You are not supposed to stick your chopsticks upright in your rice bowl, as it is a symbol of death. These customs show that Chinese culture values respect and harmony.",
    "writing_model_cn": "中国有许多游客应该了解的习俗。当你在中国第一次见到某人时，你应该握手。轻轻握手是礼貌的。你应该用头衔和姓氏称呼别人。例如，你应该说「王老师」而不是只叫「王」。在餐桌上，你应该等最年长的人先开始吃。你不应该把筷子直立在饭碗里，因为这象征死亡。这些习俗显示中国文化重视尊重与和谐。",
    "project_title": "Cultural Etiquette Guide",
    "project_desc": "制作一份「国际礼仪指南」手册，介绍3-5个不同国家的礼仪习俗，并比较它们与中国习俗的异同。",
    "project_steps": [
        "选择3-5个国家进行调研",
        "查阅每个国家的见面礼仪、餐桌礼仪和送礼礼仪",
        "用表格或图文对比各国习俗",
        "用 be supposed to 句型写出礼仪指南",
        "加入和中国习俗的对比",
        "制作成精美的口袋手册/海报"
    ],
    "project_rubric": [
        "覆盖3个以上国家",
        "信息准确可靠",
        "正确使用了 be supposed to 结构",
        "有中外礼仪对比",
        "设计精美、适合展示"
    ],
    "checklist": [
        "我能理解 be supposed to 的用法",
        "我能用英语讨论礼仪和习俗",
        "我能比较不同国家的文化差异",
        "我能理解阅读中关于文化习俗的文章",
        "我能写关于礼仪的文章"
    ],
    "feynman": "向同桌解释 be supposed to 的三种句式（肯定、否定、疑问）并各举一例。",
    "review": [
        "🔵 1天后：复习 be supposed to 句型",
        "🟢 3天后：复习礼仪和习俗相关词汇",
        "🟡 1周后：复述世界各国习俗",
        "🔴 1月后：写一篇中国餐桌礼仪介绍"
    ],
    "next_unit_title": "U11: Sad movies make me cry.",
    "next_unit_desc": "学习 make + 宾语 + 宾补结构，描述影响和情感。"
}

# ==================== Unit 11 ====================
UNITS_9["u11"] = {
    "num": "U11",
    "title": "Sad movies make me cry.",
    "topic": "情感与感受",
    "en_topic": "Emotions and Feelings",
    "functions": "Talk about how things affect you",
    "grammar": "Make + object + infinitive / adjective",
    "writing": "Describe how something influences your feelings",
    "can_do": [
        "能用 make + 宾语 + 宾补表达影响",
        "能描述事物对情感的影响",
        "能谈论压力和情绪管理",
        "能写关于情感体验的文章"
    ],
    "dialogue_scene": "Amy和Bill看完一部悲伤的电影后在讨论他们的感受。",
    "dialogue": [
        ("Amy", "That movie was so sad! It made me cry.", "那部电影太悲伤了！它让我哭了。"),
        ("Bill", "Me too. Sad movies always make me feel emotional.", "我也是。悲伤的电影总是让我情绪化。"),
        ("Amy", "But I also liked it. The story was beautiful. It made me think about my family.", "但我也挺喜欢的。故事很美。它让我想到了我的家人。"),
        ("Bill", "Yes, the ending was touching. Loud music sometimes makes me feel nervous, but the soundtrack in this movie made me feel peaceful.", "是的，结局很感人。大声的音乐有时让我紧张，但这部电影的原声让我感到平静。"),
        ("Amy", "Really? Loud music makes me want to dance!", "真的吗？大声的音乐让我想跳舞！"),
        ("Bill", "Haha, different things affect different people. The colors in the movie — the blue and gray — made me feel sad too.", "哈哈，不同的事物影响不同的人。电影中的颜色——蓝色和灰色——也让我感到悲伤。"),
        ("Amy", "That's true. The gloomy weather in the movie also made me feel down.", "没错。电影中阴沉的天气也让我心情低落。"),
        ("Bill", "But the warm ending made me feel happy again. I think that's what makes a good movie — it takes you on an emotional journey.", "但温暖的结局又让我开心起来。我认为这就是好电影的魅力——它带你踏上一段情感之旅。")
    ],
    "key_points": [
        "make + 宾语 + 形容词 表示「使某人感到……」— Sad movies make me <b>cry</b>.",
        "make + 宾语 + 动词原形 表示「使某人做……」— The story made me <b>think</b> about my family.",
        "make + 宾语 + 名词 表示「使某人成为……」— Hard work will make you <b>a success</b>.",
        "其他使役动词还有 let, have, get（用法不同）。"
    ],
    "vocab": [
        ("would rather", "ˈwʊd ˈræðər", "phrase", "宁愿", "I would rather stay at home.", "我宁愿待在家里。"),
        ("drive", "draɪv", "v.", "开车；迫使", "His words drove me crazy.", "他的话把我逼疯了。"),
        ("friendship", "ˈfrendʃɪp", "n.", "友谊；友情", "Friendship is very important.", "友谊非常重要。"),
        ("king", "kɪŋ", "n.", "国王", "The king ruled the country wisely.", "国王英明地统治着国家。"),
        ("prime", "praɪm", "adj.", "主要的；首要的", "The prime minister gave a speech.", "首相发表了演讲。"),
        ("minister", "ˈmɪnɪstər", "n.", "部长；大臣", "He is the minister of education.", "他是教育部长。"),
        ("wealth", "welθ", "n.", "财富", "Health is more important than wealth.", "健康比财富更重要。"),
        ("fame", "feɪm", "n.", "名声；声誉", "He won fame as a writer.", "他作为作家赢得了声誉。"),
        ("queen", "kwiːn", "n.", "王后；女王", "The queen was very kind.", "王后非常善良。"),
        ("pale", "peɪl", "adj.", "苍白的", "You look pale. Are you OK?", "你看起来很苍白。你还好吗？"),
        ("examine", "ɪɡˈzæmɪn", "v.", "检查；审查", "The doctor examined the patient.", "医生检查了病人。"),
        ("nor", "nɔːr", "conj.", "也不", "He can neither read nor write.", "他既不会读也不会写。"),
        ("neither", "ˈnaɪðər", "pron./adv.", "两者都不", "Neither answer is correct.", "两个答案都不对。"),
        ("banker", "ˈbæŋkər", "n.", "银行家", "He works as a banker.", "他是一名银行家。"),
        ("pale", "peɪl", "adj.", "苍白的", "His face turned pale.", "他的脸色变苍白了。"),
        ("guilty", "ˈɡɪlti", "adj.", "有罪的；内疚的", "He felt guilty about lying.", "他为说谎感到内疚。"),
        ("truth", "truːθ", "n.", "真相；事实", "Tell me the truth.", "告诉我真相。"),
        ("general", "ˈdʒenrəl", "n./adj.", "将军；一般的", "The general led the army.", "将军领导军队。"),
        ("weight", "weɪt", "n.", "重量；体重", "My weight is 60 kilograms.", "我的体重是60公斤。"),
        ("goal", "ɡoʊl", "n.", "目标；球门", "Set a goal and work towards it.", "设定一个目标并为之努力。"),
        ("coach", "koʊtʃ", "n.", "教练", "The coach taught us how to play.", "教练教我们怎么玩。"),
        ("agreement", "əˈɡriːmənt", "n.", "协议；同意", "We reached an agreement.", "我们达成了协议。")
    ],
    "patterns": [
        ("主语 + make + 宾语 + 形容词",
         "表示「使某人感到……」。",
         "Sad movies <b>make me cry</b>. / The music <b>makes me happy</b>."),
        ("主语 + make + 宾语 + 动词原形",
         "表示「使某人做某事」。",
         "The story <b>made me think</b>. / Her words <b>made me laugh</b>."),
        ("主语 + make + 宾语 + 名词",
         "表示「使某人成为……」。",
         "Hard work will <b>make you a success</b>. / She <b>made him a better person</b>."),
        ("Would rather + V (than V)",
         "表示「宁愿做某事（而不愿做）」。",
         "I <b>would rather</b> stay at home (than go out). / She <b>would rather</b> read than watch TV.")
    ],
    "grammar_title": "Make + 宾语 + 宾语补足语",
    "grammar_sections": [
        ("make 的使役用法", [
            ("结构", "补足语类型", "例句"),
            ("make + 宾语 + 形容词", "形容词", "The movie made me sad."),
            ("make + 宾语 + 动词原形", "省略 to 的不定式", "Sad movies make me cry."),
            ("make + 宾语 + 名词", "名词", "He made her his assistant."),
            ("make + 宾语 + 过去分词", "过去分词", "Can you make yourself understood?")
        ]),
        ("其他使役动词对比", [
            ("动词", "结构", "含义", "例句"),
            ("make", "make + O + V", "迫使做", "He made me wait."),
            ("let", "let + O + V", "允许做", "She let me go."),
            ("have", "have + O + V", "让某人做", "I had him fix the car."),
            ("get", "get + O + to V", "让某人做", "I got him to help me.")
        ])
    ],
    "grammar_tips": [
        "make 后接省略 to 的不定式（动词原形）。",
        "被动语态中，make 后要加 to — I was made <b>to</b> wait.",
        "区分 make sb do（迫使）和 let sb do（允许）。",
        "<span class=\"wotd-say\" data-speak=\"Laughter is the best medicine.\">Laughter is the best medicine.</span> 笑是最好的药。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "Sad movies always make me ____ (cry).", "cry"),
        ("基础", "★☆☆", "The loud music makes me ____ (feel) nervous.", "feel"),
        ("基础", "★☆☆", "Her story made us ____ (sad).", "sad"),
        ("基础", "★☆☆", "I would rather ____ (stay) at home tonight.", "stay"),
        ("基础", "★☆☆", "The gift made her ____ (happy).", "happy")
    ],
    "mid_qs": [
        ("提升", "★★☆", "选择：The news made him ____.<br>A. worry B. worried C. worrying D. to worry", "B"),
        ("提升", "★★☆", "The teacher made us ____ (clean) the classroom.", "clean"),
        ("提升", "★★☆", "I was made ____ (wait) for an hour.", "to wait"),
        ("提升", "★★☆", "翻译：这个好消息让我很兴奋。", "The good news made me excited."),
        ("提升", "★★☆", "I would rather ____ than ____. (stay home / go out)", "stay home ... go out")
    ],
    "hard_qs": [
        ("挑战", "★★★", "改错：The movie made her to cry.", "去掉 to"),
        ("挑战", "★★★", "选择：Nothing will make me ____ my mind.<br>A. change B. to change C. changing D. changed", "A"),
        ("挑战", "★★★", "完成句子：考试前的焦虑让我晚上睡不着。→ The anxiety before exams ____.", "The anxiety before exams makes me unable to sleep at night."),
        ("挑战", "★★★", "写作：用 make + 宾语 + 宾补结构写一段话，描述什么让你开心/难过/紧张/平静。", "Soft music makes me feel relaxed. Spending time with friends makes me happy. But exams make me nervous. My mom's cooking makes me feel at home.")
    ],
    "reading_title": "The Happy King and the Unhappy Life",
    "reading_text": [
        "Once upon a time, there was a king who had everything: wealth, fame, and power. But he was still unhappy. He often cried for no reason. The king's doctor examined him and said, «Nothing is wrong with your body. But your mind is sick. You need to find the shirt of a happy person and wear it.»",
        "The prime minister was called to help. He went to a rich banker. The banker had a lot of money. But he was worried about losing it. He was not happy. Then the minister went to a famous singer. The singer was worried about becoming less popular. She was not happy either.",
        "Finally, the minister met a poor man who was singing happily while working in his field. The minister asked the man, «Are you happy?» The man said, «Yes, I have everything I need.»",
        "The minister was very excited. «Give me your shirt!» he said. The man laughed. «I'm sorry,» he said, «but I don't own a shirt.»"
    ],
    "reading_gloss": [
        ("once upon a time", "从前"),
        ("power", "权力"),
        ("for no reason", "无缘无故地"),
        ("prime minister", "首相"),
        ("field", "田地；田野"),
        ("own", "拥有")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What did the king have?", "He had wealth, fame, and power."),
        ("阅读", "★★☆", "Why was the banker unhappy?", "He was worried about losing his money."),
        ("阅读", "★★☆", "Why was the poor man happy?", "He had everything he needed."),
        ("阅读", "★★★", "What is the moral of the story?", "Happiness doesn't come from wealth or fame. It comes from being satisfied with what you have.")
    ],
    "exam_q_type": "阅读理解 — 主旨大意",
    "exam_q": "阅读短文，选择最佳答案。",
    "exam_passage": [
        "Colors can affect our feelings. For example, blue can make us feel calm and peaceful. That's why many bedrooms are painted blue. Red, on the other hand, can make us feel excited or even angry. Restaurants often use red because it makes people eat faster. Green makes us feel relaxed because it reminds us of nature. Yellow makes us feel happy and warm. So when you choose colors for your room, think about how you want to feel."
    ],
    "exam_options": [
        (1, {"A": "How colors affect our feelings.", "B": "How to paint a room.", "C": "What is your favorite color?", "D": "Colors are not important."}),
        (2, {"A": "Excited.", "B": "Calm and peaceful.", "C": "Angry.", "D": "Happy."}),
        (3, {"A": "It makes people feel angry.", "B": "It makes people eat faster.", "C": "It makes people feel calm.", "D": "It makes people want to sleep."}),
        (4, {"A": "Blue.", "B": "Red.", "C": "Green.", "D": "Yellow."})
    ],
    "exam_answers": ["1. A", "2. B", "3. B", "4. D"],
    "writing_prompt": "写一篇短文描述颜色、天气或音乐对你的情绪的影响。请使用 make + 宾语 + 宾补结构。",
    "writing_framework": [
        "开头：引出话题（有些事物会影响我们的情绪）",
        "描述一种影响你情绪的因素（如颜色/天气/音乐）",
        "举例说明它如何影响你的感受",
        "对比不同因素的不同影响",
        "结尾：总结情绪管理的意义"
    ],
    "writing_model_en": "Different things affect my feelings in different ways. Sunny weather always makes me happy and energetic. When the sun shines, I feel like going outside and doing fun things. But rainy days make me feel a little sad and sleepy. I would rather stay at home and read a book when it rains. Music also influences my mood. Pop music makes me want to dance, while soft music makes me feel calm. I think it's important to understand what affects our feelings so we can manage our emotions better.",
    "writing_model_cn": "不同的事物以不同的方式影响我的感受。晴朗的天气总是让我开心和有活力。当阳光明媚时，我想出去做有趣的事情。但雨天让我感到有点悲伤和困倦。下雨时我宁愿待在家里看书。音乐也影响我的情绪。流行音乐让我想跳舞，而柔和的音乐让我感到平静。我认为了解什么影响我们的情绪很重要，这样我们才能更好地管理情绪。",
    "project_title": "My Emotional Color Wheel",
    "project_desc": "制作一个情感色轮图，用不同的颜色代表不同的情绪，并用英语写出每种颜色对你情绪的影响。",
    "project_steps": [
        "列出6-8种情绪（开心、悲伤、平静、愤怒等）",
        "为每种情绪选一种代表色",
        "用 make + 宾语 + 宾补写句子描述颜色如何影响情绪",
        "设计色轮图（彩色圆盘分区标注）",
        "为每种情绪配一句名言或歌词",
        "在班级展示你的情感色轮"
    ],
    "project_rubric": [
        "包含6种以上的情绪",
        "颜色和情绪的匹配合理",
        "正确使用了 make + 宾语 + 宾补",
        "设计美观、有创意",
        "口头展示清晰流畅"
    ],
    "checklist": [
        "我能理解 make + 宾语 + 宾补结构",
        "我能用 make 描述事物对情绪的影响",
        "我能区分 make/let/have/get 的用法",
        "我能理解阅读中关于快乐的故事",
        "我能写关于情感影响的短文"
    ],
    "feynman": "向同桌解释 make + 宾语 + 形容词 和 make + 宾语 + 动词原形的区别。",
    "review": [
        "🔵 1天后：复习 make + 宾语 + 宾补",
        "🟢 3天后：复习情感相关词汇",
        "🟡 1周后：复述快乐国王的故事",
        "🔴 1月后：写颜色如何影响你的情绪"
    ],
    "next_unit_title": "U12: Life is full of the unexpected.",
    "next_unit_desc": "学习过去完成时，讲述意外经历。"
}

# ==================== Unit 12 ====================
UNITS_9["u12"] = {
    "num": "U12",
    "title": "Life is full of the unexpected.",
    "topic": "意外与经历",
    "en_topic": "Unexpected Events and Experiences",
    "functions": "Narrate past events and unexpected experiences",
    "grammar": "Past perfect tense: had + past participle",
    "writing": "Write about an unexpected event that happened",
    "can_do": [
        "能用过去完成时描述过去的经历",
        "能讲述意外事件的前后顺序",
        "能理解时间状语从句中的时态搭配",
        "能写叙事的短文"
    ],
    "dialogue_scene": "Kevin和Emma在谈论他们生活中遇到的意外事情。",
    "dialogue": [
        ("Kevin", "I had the craziest morning today! By the time I got to the bus stop, the bus had already left.", "我今天早上遇到了最疯狂的事！等我到公交车站时，公交车已经开走了。"),
        ("Emma", "What did you do?", "那你怎么办了？"),
        ("Kevin", "I decided to walk to school. But when I arrived at school, I realized I had left my backpack at home!", "我决定走路去学校。但当我到学校时，我意识到我把书包落在家里了！"),
        ("Emma", "Oh no! That's terrible! Did you go back?", "哦不！那太糟了！你回去了吗？"),
        ("Kevin", "I couldn't. By the time I got home, my mom had already left for work. I had to borrow things from my classmates.", "我没法回。等我到家时，我妈已经去上班了。我只能向同学借东西。"),
        ("Emma", "Well, something unexpected happened to me too. I had finished my homework, but I forgot to save it. The computer shut down and I lost everything!", "嗯，我也发生了意外的事。我完成了作业，但忘了保存。电脑关机了，我全丢了！"),
        ("Kevin", "That's worse than my story! What did you do?", "那比我的还糟！你怎么办了？"),
        ("Emma", "I had to do it all over again. Life is full of the unexpected, isn't it?", "我只能重做一遍。生活中充满了意外，不是吗？")
    ],
    "key_points": [
        "过去完成时：had + 过去分词，表示「过去的过去」。",
        "常用于 told, said, knew, realized 等动词后的宾语从句中。",
        "常用句式：By the time + 一般过去时, 主语 + had + 过去分词。",
        "When / After / Before / Until 等引导的时间状语从句常和过去完成时连用。"
    ],
    "vocab": [
        ("backpack", "ˈbækpæk", "n.", "背包", "I left my backpack on the bus.", "我把背包落在公交车上了。"),
        ("oversleep", "ˌoʊvərˈsliːp", "v.", "睡过头", "I overslept and missed the bus.", "我睡过头了，错过了公交车。"),
        ("unexpected", "ˌʌnɪkˈspektɪd", "adj.", "意外的；出乎意料的", "Life is full of the unexpected.", "生活中充满了意外。"),
        ("block", "blɒk", "n.", "街区；阻塞", "The street is two blocks away.", "那条街在两个街区外。"),
        ("worker", "ˈwɜːrkər", "n.", "工人", "The workers are building a new road.", "工人们正在修一条新路。"),
        ("above", "əˈbʌv", "prep./adv.", "在……上方", "The plane flew above the clouds.", "飞机在云层上方飞行。"),
        ("empty", "ˈempti", "adj.", "空的", "The room was empty.", "房间是空的。"),
        ("stare", "ster", "v.", "盯着看；凝视", "Don't stare at people.", "不要盯着人看。"),
        ("disbelief", "ˌdɪsbɪˈliːf", "n.", "不信；怀疑", "He stared at me in disbelief.", "他怀疑地盯着我。"),
        ("burn", "bɜːrn", "v.", "燃烧；烧毁", "The building burned down.", "那栋楼被烧毁了。"),
        ("alive", "əˈlaɪv", "adj.", "活着的；在世", "I'm lucky to be alive.", "我很幸运还活着。"),
        ("airport", "ˈerpɔːrt", "n.", "机场", "We arrived at the airport at 6 AM.", "我们早上6点到达机场。"),
        ("till", "tɪl", "prep./conj.", "直到", "Wait till I come back.", "等到我回来。"),
        ("west", "west", "n./adv.", "西方；向西", "The sun sets in the west.", "太阳从西边落下。"),
        ("market", "ˈmɑːrkɪt", "n.", "市场", "Let's go to the farmer's market.", "我们去农贸市场吧。"),
        ("cream", "kriːm", "n.", "奶油；面霜", "Would you like some cream in your coffee?", "你的咖啡要加奶油吗？"),
        ("pie", "paɪ", "n.", "派；馅饼", "I love apple pie.", "我喜欢苹果派。"),
        ("officer", "ˈɒfɪsər", "n.", "军官；警官", "The police officer helped us.", "警察帮了我们。"),
        ("disappear", "ˌdɪsəˈpɪr", "v.", "消失", "The sun disappeared behind the clouds.", "太阳消失在了云层后面。"),
        ("embarrassed", "ɪmˈbærəst", "adj.", "尴尬的；难为情的", "I felt so embarrassed.", "我感到非常尴尬。"),
        ("announce", "əˈnaʊns", "v.", "宣布；通知", "The teacher announced the test results.", "老师宣布了考试结果。"),
        ("shut", "ʃʌt", "v.", "关闭", "Shut the door, please.", "请关门。")
    ],
    "patterns": [
        ("By the time + 从句 (一般过去时), 主语 + had + V-ed",
         "表示「到……时候为止，某事已经完成了」。",
         "<b>By the time</b> I got to the bus stop, the bus <b>had already left</b>."),
        ("主语 + had + V-ed + when/before + 一般过去时",
         "表示过去某个时间点之前已经完成的动作。",
         "I <b>had finished</b> my homework <b>when</b> my mom came home. / She <b>had left</b> before I arrived."),
        ("主语 + realized + that + 主语 + had + V-ed",
         "表示「意识到某事已经发生」。",
         "I <b>realized that</b> I <b>had left</b> my backpack at home."),
        ("主语 + had never + V-ed + until + 一般过去时",
         "表示「直到……才经历某事」。",
         "I <b>had never</b> seen such a beautiful sunset <b>until</b> I visited the beach.")
    ],
    "grammar_title": "过去完成时 (Past Perfect Tense)",
    "grammar_sections": [
        ("过去完成时的结构", [
            ("句式", "结构", "例句"),
            ("肯定句", "主语 + had + V-ed", "I had finished my homework."),
            ("否定句", "主语 + had not + V-ed", "I hadn't finished my homework."),
            ("疑问句", "Had + 主语 + V-ed?", "Had you finished your homework?")
        ]),
        ("过去完成时 vs 一般过去时", [
            ("时态", "用途", "例句"),
            ("过去完成时", "先发生的动作（过去的过去）", "When I arrived, the bus had already left."),
            ("一般过去时", "后发生的动作或状态", "I arrived at school at 8 o'clock.")
        ])
    ],
    "grammar_tips": [
        "过去完成时表示「过去的过去」——两个动作都在过去，但一个更早。",
        "如果没有明确的先后关系，一般用一般过去时即可。",
        "by the time / when / before 常与过去完成时连用。",
        "<span class=\"wotd-say\" data-speak=\"It's no use crying over spilt milk.\">It's no use crying over spilt milk.</span> 覆水难收。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "By the time I got there, the bus ____ (leave).", "had left"),
        ("基础", "★☆☆", "I realized I ____ (forget) my keys at home.", "had forgotten"),
        ("基础", "★☆☆", "She ____ (finish) her homework before dinner.", "had finished"),
        ("基础", "★☆☆", "The movie ____ (already/start) when we arrived.", "had already started"),
        ("基础", "★☆☆", "Had you ever ____ (visit) Beijing before?", "visited")
    ],
    "mid_qs": [
        ("提升", "★★☆", "选择：When I got home, my mom ____ dinner.<br>A. cooked B. had cooked C. was cooking D. has cooked", "C (was cooking 更合理) or B"),
        ("提升", "★★☆", "By the time he was ten, he ____ (learn) to play the piano.", "had learned"),
        ("提升", "★★☆", "She told me she ____ (never/see) such a beautiful view before.", "had never seen"),
        ("提升", "★★☆", "改错：I had went to the store before my mom came home.", "went → gone"),
        ("提升", "★★☆", "翻译：我到了机场才发现忘带护照了。", "I realized that I had left my passport at home when I arrived at the airport.")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：She ____ the homework before her mom came back.<br>A. finished B. had finished C. has finished D. was finishing", "B"),
        ("挑战", "★★★", "完成句子：By the time the teacher came into the classroom, the students ____ (already/clean) it.", "had already cleaned"),
        ("挑战", "★★★", "改错：After I had ate breakfast, I went to school.", "ate → eaten"),
        ("挑战", "★★★", "写作：用过去完成时写一段你或你朋友遇到的意外事件（至少5句话）。", "Yesterday was a terrible day. By the time I woke up, my brother had already used the bathroom. When I finally got to the kitchen, my mom had eaten all the cereal. I realized I had forgotten to set my alarm. By the time I got to school, the first class had already started. What a morning!")
    ],
    "reading_title": "The Unexpected Morning",
    "reading_text": [
        "September 11, 2001 was a day that nobody would forget. But for one man, it was a morning full of unexpected events that saved his life.",
        "The man was supposed to take a flight from Boston to Los Angeles. But he had overslept! When he woke up, it was already 7:30. His flight was at 8:00. By the time he arrived at the airport, the plane had already taken off.",
        "He was very angry at himself. He had never missed a flight before. He went to the ticket counter to see if he could get on the next flight. The worker said, «I'm sorry, sir. All the flights are full.»",
        "The man sat down, feeling frustrated. Then he turned on the TV in the waiting area and saw the news. The plane he had missed had been hijacked. The man couldn't believe his eyes. He had been saved by oversleeping. Sometimes, the unexpected can save you."
    ],
    "reading_gloss": [
        ("flight", "航班"),
        ("take off", "起飞"),
        ("ticket counter", "票务柜台"),
        ("frustrated", "沮丧的"),
        ("hijacked", "被劫持的"),
        ("saved", "拯救")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "Why did the man miss his flight?", "Because he had overslept."),
        ("阅读", "★★☆", "How did the man feel when he missed the flight?", "He was angry at himself."),
        ("阅读", "★★☆", "What happened to the plane he had missed?", "It was hijacked."),
        ("阅读", "★★★", "What is the message of this story?", "Sometimes unexpected events can save us. What seems like bad luck might be good luck in disguise.")
    ],
    "exam_q_type": "时态填空 — 过去完成时",
    "exam_q": "用所给动词的适当形式填空。",
    "exam_passage": [
        "Yesterday I 1 (have) a really bad day. By the time I 2 (wake) up, my sister 3 (already/take) a shower. When I finally got to the kitchen, there was no milk left — my brother 4 (drink) it all. I 5 (realize) that I 6 (leave) my homework on the kitchen table. By the time I ran back, my mom 7 (already/throw) it away!"
    ],
    "exam_options": [
        (1, {"A": "have", "B": "had", "C": "was having", "D": "has"}),
        (2, {"A": "wake", "B": "woke", "C": "woken", "D": "wakes"}),
        (3, {"A": "already took", "B": "had already taken", "C": "has already taken", "D": "already takes"}),
        (4, {"A": "drunk", "B": "had drunk", "C": "has drunk", "D": "drank"}),
        (5, {"A": "realize", "B": "realized", "C": "had realized", "D": "was realizing"}),
        (6, {"A": "leave", "B": "left", "C": "had left", "D": "was leaving"}),
        (7, {"A": "threw", "B": "had already thrown", "C": "has already thrown", "D": "was throwing"})
    ],
    "exam_answers": ["1. B", "2. B", "3. B", "4. B", "5. B", "6. C", "7. B"],
    "writing_prompt": "写一篇短文讲述你或你的朋友曾经遇到的一次意外经历。使用过去完成时来描述事件的先后顺序。",
    "writing_framework": [
        "开头：引出你的意外经历",
        "背景：描述当时的情况（使用过去完成时）",
        "发生：描述意外如何发生",
        "结果：描述你怎么应对和结果如何",
        "结尾：反思这个经历给你带来的启示"
    ],
    "writing_model_en": "Last week, I had an unforgettable experience. I was supposed to give a speech at the school assembly. By the time I stood up on stage, I realized I had left my notes in the classroom! My heart was beating fast. But then I remembered that I had practiced the speech many times before. I took a deep breath and started speaking. To my surprise, I did very well without the notes! After the speech, my teacher told me that I had done a great job. I learned that we are often more capable than we think. Sometimes unexpected situations help us discover our true abilities.",
    "writing_model_cn": "上周，我有一次难忘的经历。我本应在学校集会上做演讲。等我站上舞台时，我意识到我把演讲稿落在教室了！我的心跳得很快。但随后我记起我之前已经练习过很多次了。我深吸一口气，开始演讲。令我惊讶的是，没有演讲稿我也讲得很好！演讲后，老师告诉我我做得很好。我明白了我们往往比自己想象中更有能力。有时意外的状况会帮助我们发现自己真正的能力。",
    "project_title": "My Unexpected Story Book",
    "project_desc": "编写一本「意外故事集」，收集3-4个来自同学或家人的真实意外经历，用英语记录并配上插图。",
    "project_steps": [
        "采访2-3位同学或家人，询问他们的意外经历",
        "记录故事的关键信息（时间、地点、事件）",
        "用过去完成时和一般过去时写故事",
        "为每个故事配插图或照片",
        "装订成小册子",
        "在班级故事会上分享"
    ],
    "project_rubric": [
        "收集了3个以上的真实故事",
        "正确使用了过去完成时",
        "故事有开头、经过和结尾",
        "插图或照片与故事匹配",
        "分享时表达清晰、生动"
    ],
    "checklist": [
        "我能理解过去完成时的结构和用法",
        "我能区分过去完成时和一般过去时",
        "我能用英语讲述意外经历",
        "我能理解阅读中关于911的故事",
        "我能写叙事性的短文"
    ],
    "feynman": "向同桌解释过去完成时和一般过去时的区别，并用时间线图示说明。",
    "review": [
        "🔵 1天后：复习过去完成时结构",
        "🟢 3天后：复习意外经历相关词汇",
        "🟡 1周后：复述911意外故事",
        "🔴 1月后：写一篇自己的意外经历"
    ],
    "next_unit_title": "U13: We're trying to save the earth!",
    "next_unit_desc": "学习多种时态的复习运用，关注环保议题。"
}

# ==================== Unit 13 ====================
UNITS_9["u13"] = {
    "num": "U13",
    "title": "We're trying to save the earth!",
    "topic": "环保与行动",
    "en_topic": "Environmental Protection and Action",
    "functions": "Talk about environmental problems and solutions",
    "grammar": "Review of tenses: present progressive, modal verbs, passive voice",
    "writing": "Write a proposal for protecting the environment",
    "can_do": [
        "能用英语讨论环境问题",
        "能提出环保建议和解决方案",
        "能综合运用多种时态",
        "能写环保倡议书或建议信"
    ],
    "dialogue_scene": "Julia和Mark在学校的环保俱乐部讨论如何保护环境。",
    "dialogue": [
        ("Julia", "Have you noticed how dirty the river near our school has become?", "你注意到我们学校旁边的河变得有多脏了吗？"),
        ("Mark", "Yes, it's terrible! The factories are putting waste into the river. The fish are dying.", "是的，太可怕了！工厂在往河里排放废物。鱼在死去。"),
        ("Julia", "We need to do something! We're trying to save the earth, but big changes start with small actions.", "我们需要做点什么！我们在努力拯救地球，但大变化从小事开始。"),
        ("Mark", "You're right. What can we do as students?", "你说得对。作为学生我们能做什么？"),
        ("Julia", "Well, we can start by recycling. Paper, plastic, and glass should be recycled instead of thrown away.", "嗯，我们可以从回收开始。纸、塑料和玻璃应该回收而不是扔掉。"),
        ("Mark", "Good idea. We could also use fewer plastic bags. They are killing sea animals.", "好主意。我们也可以少用塑料袋。它们正在杀死海洋动物。"),
        ("Julia", "Yes, and we should plant more trees. Trees clean the air and make the world beautiful.", "是的，我们应该种更多的树。树木净化空气，让世界美丽。"),
        ("Mark", "Let's make a plan and share it with the rest of the school!", "我们制定一个计划，和全校分享吧！")
    ],
    "key_points": [
        "复习现在进行时：We <b>are trying</b> to save the earth! — 表示正在进行的动作。",
        "复习情态动词：We <b>can</b> start by recycling. / We <b>should</b> plant more trees.",
        "复习被动语态：Paper <b>should be recycled</b> instead of thrown away.",
        "环保相关表达：cut down, throw away, clean up, save energy, protect the environment"
    ],
    "vocab": [
        ("litter", "ˈlɪtər", "n./v.", "垃圾；乱扔", "Please don't litter.", "请不要乱扔垃圾。"),
        ("bottom", "ˈbɒtəm", "n.", "底部；最下部", "The bottle sank to the bottom of the river.", "瓶子沉到了河底。"),
        ("fisherman", "ˈfɪʃərmən", "n.", "渔民；钓鱼者", "The fishermen caught a lot of fish.", "渔民们捕了很多鱼。"),
        ("coal", "koʊl", "n.", "煤；煤炭", "Burning coal causes air pollution.", "烧煤导致空气污染。"),
        ("ugly", "ˈʌɡli", "adj.", "丑陋的；难看的", "The pollution makes the city ugly.", "污染让城市变得丑陋。"),
        ("advantage", "ədˈvæntɪdʒ", "n.", "优势；有利条件", "Reading has many advantages.", "阅读有很多好处。"),
        ("industry", "ˈɪndəstri", "n.", "工业；行业", "The industry is growing fast.", "这个行业正在快速发展。"),
        ("law", "lɔː", "n.", "法律；法规", "There should be laws to protect the environment.", "应该有保护环境的法律。"),
        ("against", "əˈɡenst", "prep.", "反对；违反", "Littering is against the law.", "乱扔垃圾是违法的。"),
        ("reusable", "riːˈjuːzəbl", "adj.", "可重复使用的", "Bring a reusable bag when shopping.", "购物时带一个可重复使用的袋子。"),
        ("plastic", "ˈplæstɪk", "n./adj.", "塑料；塑料的", "Plastic bottles can be recycled.", "塑料瓶可以回收。"),
        ("recycle", "ˌriːˈsaɪkl", "v.", "回收利用", "We should recycle paper and glass.", "我们应该回收纸和玻璃。"),
        ("napkin", "ˈnæpkɪn", "n.", "餐巾", "Use cloth napkins instead of paper ones.", "使用布餐巾代替纸餐巾。"),
        ("energy", "ˈenərdʒi", "n.", "能量；能源", "Save energy by turning off lights.", "关灯来节约能源。"),
        ("transportation", "ˌtrænspɔːrˈteɪʃn", "n.", "交通；运输", "Public transportation is better for the environment.", "公共交通对环境更好。"),
        ("environment", "ɪnˈvaɪrənmənt", "n.", "环境", "We need to protect the environment.", "我们需要保护环境。"),
        ("pollution", "pəˈluːʃn", "n.", "污染", "Air pollution is a serious problem.", "空气污染是一个严重的问题。"),
        ("protect", "prəˈtekt", "v.", "保护", "We should protect endangered animals.", "我们应该保护濒危动物。"),
        ("throw", "θroʊ", "v.", "扔", "Don't throw away recyclable materials.", "不要扔掉可回收的材料。"),
        ("recycle", "ˌriːˈsaɪkl", "v.", "回收", "Glass can be recycled many times.", "玻璃可以多次回收。"),
        ("reduce", "rɪˈdjuːs", "v.", "减少；降低", "Reduce the use of plastic bags.", "减少塑料袋的使用。"),
        ("reuse", "ˌriːˈjuːz", "v.", "重新使用", "Reuse old bottles as vases.", "重新用旧瓶子做花瓶。")
    ],
    "patterns": [
        ("We're + V-ing + to + V (现在进行时表正在进行)",
         "表示我们正在努力做某事。",
         "<b>We're trying</b> to save the earth! / <b>They are working</b> to clean up the river."),
        ("We should / can + V (情态动词表建议)",
         "提出建议。",
         "We <b>should</b> plant more trees. / We <b>can</b> start by recycling."),
        ("主语 + should / can + be + V-ed (情态动词被动语态)",
         "建议某事应该被做。",
         "Paper <b>should be recycled</b>. / Plastic bags <b>should not be used</b>."),
        ("主语 + is / are + V-ed (一般现在时被动语态)",
         "描述事实或状态。",
         "The river <b>is polluted</b>. / Many animals <b>are killed</b> by pollution.")
    ],
    "grammar_title": "时态综合复习",
    "grammar_sections": [
        ("时态复习对比", [
            ("时态", "结构", "用途", "例句"),
            ("现在进行时", "am/is/are + V-ing", "正在进行的动作", "We are trying to save the earth."),
            ("一般现在时", "V / V-s", "经常性动作、事实", "The river is dirty."),
            ("一般过去时", "V-ed", "过去的动作", "The factory dumped waste."),
            ("现在完成时", "have/has + V-ed", "过去的动作对现在影响", "The river has become dirty.")
        ]),
        ("环保话题常用句型", [
            ("句型", "功能", "例句"),
            ("We should + V", "提出建议", "We should plant more trees."),
            ("主语 + should be + V-ed", "建议某事被做", "Plastic should be recycled."),
            ("It's + adj + for sb + to V", "评价某事", "It's important to protect the earth."),
            ("主语 + is/are V-ing", "描述正在发生的", "The earth is getting warmer.")
        ])
    ],
    "grammar_tips": [
        "现在进行时也可以表示「现阶段正在进行的动作」不一定说话时正在做。",
        "情态动词 should 和 can 后接动词原形。",
        "by + V-ing 表示「通过做某事」，常用于提出建议。",
        "<span class=\"wotd-say\" data-speak=\"We do not inherit the earth from our ancestors; we borrow it from our children.\">We do not inherit the earth from our ancestors; we borrow it from our children.</span> 地球不是我们从祖先那里继承的，而是从子孙那里借来的。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "We ____ (try) to save the earth.", "are trying"),
        ("基础", "★☆☆", "Paper should ____ (recycle).", "be recycled"),
        ("基础", "★☆☆", "We ____ (可以节约) energy by turning off lights.", "can save"),
        ("基础", "★☆☆", "The river ____ (pollute) by factory waste.", "is polluted"),
        ("基础", "★☆☆", "Don't ____ (throw) away recyclable materials.", "throw")
    ],
    "mid_qs": [
        ("提升", "★★☆", "选择：Many sea animals are ____ because of plastic pollution.<br>A. die B. dying C. died D. dead", "B"),
        ("提升", "★★☆", "The number of cars ____ (increase) every year, causing more pollution.", "increases / is increasing"),
        ("提升", "★★☆", "改主动为被动：People should not waste water. → ____.", "Water should not be wasted."),
        ("提升", "★★☆", "翻译：我们应该用布袋代替塑料袋。", "We should use cloth bags instead of plastic bags."),
        ("提升", "★★☆", "We ____ (recycle) about 30% of our waste last year.", "recycled")
    ],
    "hard_qs": [
        ("挑战", "★★★", "用多种时态完成句子：The river ____ (be) clean ten years ago, but now it ____ (become) polluted because factories ____ (dump) waste into it.", "was ... has become ... dump / are dumping"),
        ("挑战", "★★★", "改错：We should to plant more trees to reduce pollution.", "去掉 to"),
        ("挑战", "★★★", "完成句子：拯救地球人人有责。____", "It's everyone's duty to save the earth."),
        ("挑战", "★★★", "写作：写一段话（至少5句）讨论我们学校可以做哪些事情来保护环境。", "Our school can do many things to protect the environment. First, we should set up recycling bins for paper, plastic, and cans. Second, students should bring reusable water bottles instead of buying plastic ones. Third, we can plant more trees on campus. Also, we should turn off lights and fans when we leave the classroom. Let's work together to make our school greener!")
    ],
    "reading_title": "Small Actions, Big Impact",
    "reading_text": [
        "Our planet is in trouble. Air pollution is making people sick. Water pollution is killing sea life. The earth is getting warmer. But there is still hope! If everyone makes small changes, together we can make a big difference.",
        "One person who made a difference is Amy, a 14-year-old girl from California. She noticed that her school used hundreds of plastic water bottles every day. So she started a campaign to encourage students to use reusable bottles. Within a year, her school had reduced plastic waste by 80%.",
        "You can also make a difference. Start by reducing what you throw away. Reuse what you can. Recycle what you can't reuse. Turn off lights when you leave a room. Walk or bike instead of taking the car. Every small action counts.",
        "Remember: we don't need a few people doing everything perfectly. We need millions of people doing something imperfectly. The earth needs you. Start today!"
    ],
    "reading_gloss": [
        ("in trouble", "处于困境中"),
        ("making a difference", "起作用；产生影响"),
        ("campaign", "运动；活动"),
        ("reduced by 80%", "减少了80%"),
        ("counts", "起作用；算数"),
        ("imperfectly", "不完美地")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "What problems does the earth face according to the passage?", "Air pollution, water pollution, and global warming."),
        ("阅读", "★★☆", "What did Amy do to help the environment?", "She started a campaign to encourage students to use reusable water bottles."),
        ("阅读", "★★☆", "What was the result of Amy's campaign?", "Her school reduced plastic waste by 80%."),
        ("阅读", "★★★", "What does the sentence «We need millions of people doing something imperfectly» mean?", "It means many people doing small things imperfectly is better than a few people doing everything perfectly. Collective small actions can make a big difference.")
    ],
    "exam_q_type": "任务型阅读 — 环保建议",
    "exam_q": "阅读短文，完成表格（列举四条环保建议）。",
    "exam_passage": [
        "Here are four easy things you can do to help save the earth. First, turn off the lights when you leave a room. This saves electricity. Second, use both sides of paper before recycling it. This reduces waste. Third, bring your own bag when you go shopping. Plastic bags are bad for the environment. Fourth, walk or ride a bike for short trips. This reduces air pollution. Remember: every little bit helps!"
    ],
    "exam_options": [
        (1, {"A": "Save electricity.", "B": "Turn off lights.", "C": "Use more plastic.", "D": "Drive everywhere."}),
        (2, {"A": "Play video games.", "B": "Use both sides of paper.", "C": "Watch more TV.", "D": "Buy more things."}),
        (3, {"A": "Bring your own bag.", "B": "Use plastic bags.", "C": "Throw bags away.", "D": "Burn plastic."}),
        (4, {"A": "Drive a car.", "B": "Take a taxi.", "C": "Walk or ride a bike.", "D": "Take the plane."})
    ],
    "exam_answers": ["1. B - Turn off lights / Save electricity.", "2. B - Use both sides of paper.", "3. A - Bring your own bag.", "4. C - Walk or ride a bike for short trips."],
    "writing_prompt": "假设你是环保俱乐部的负责人，写一封倡议书，呼吁全校师生共同保护环境。请提出至少三条具体可行的建议。",
    "writing_framework": [
        "标题和称呼",
        "开头：说明环境问题的严重性",
        "第一条建议：节约能源（具体做法）",
        "第二条建议：减少浪费（具体做法）",
        "第三条建议：绿色出行（具体做法）",
        "结尾：呼吁行动、表达希望"
    ],
    "writing_model_en": "Dear teachers and students,\n\nOur planet is facing serious environmental problems. The air is polluted, the rivers are dirty, and many animals are in danger. It's time for us to take action!\n\nHere are some things we can do. First, we should save energy. Turn off lights and fans when you leave the classroom. Second, we can reduce waste. Bring reusable water bottles and lunch boxes. Recycle paper and plastic. Third, let's choose green transportation. Walk or bike to school if possible.\n\nSmall actions can make a big difference. Let's work together to protect our beautiful earth!\n\nSincerely,\nThe Environmental Club",
    "writing_model_cn": "亲爱的老师、同学们：\n\n我们的星球正面临严重的环境问题。空气被污染了，河流变脏了，许多动物处于危险之中。是时候采取行动了！\n\n以下是我们能做的事情。首先，我们应该节约能源。离开教室时关掉灯和风扇。其次，我们可以减少浪费。带上可重复使用的水瓶和饭盒。回收纸和塑料。第三，让我们选择绿色出行。可能的话步行或骑自行车上学。\n\n小行动可以带来大改变。让我们一起努力保护我们美丽的地球！\n\n此致\n环保俱乐部",
    "project_title": "Green School Action Plan",
    "project_desc": "调查你学校的环境问题，制定一份「绿色学校」行动计划，包含问题分析、具体措施和目标。",
    "project_steps": [
        "观察并记录学校存在的环境问题（浪费水电、垃圾未分类等）",
        "采访同学和老师对环境问题的看法",
        "列出3-5个需要解决的主要问题",
        "针对每个问题提出可行的解决方案",
        "制定行动时间表和目标",
        "用英语制作行动计划海报在校园展示"
    ],
    "project_rubric": [
        "问题识别准确、具体",
        "解决方案切实可行",
        "使用了本单元的语法和词汇",
        "有明确的时间表和目标",
        "设计美观、有说服力"
    ],
    "checklist": [
        "我能用英语讨论环境问题和解决方案",
        "我能综合运用多种时态",
        "我能提出环保建议",
        "我能理解阅读中关于环保行动的文章",
        "我能写环保倡议书"
    ],
    "feynman": "向同桌解释reduce、reuse、recycle（3R原则）的含义，并用英语举例说明。",
    "review": [
        "🔵 1天后：复习多种时态的用法对比",
        "🟢 3天后：复习环保相关词汇",
        "🟡 1周后：复述Amy的环保故事",
        "🔴 1月后：写一份个人环保计划"
    ],
    "next_unit_title": "U14: I remember meeting all of you in Grade 7.",
    "next_unit_desc": "综合复习，回忆初中生活，展望未来。"
}

# ==================== Unit 14 ====================
UNITS_9["u14"] = {
    "num": "U14",
    "title": "I remember meeting all of you in Grade 7.",
    "topic": "回忆与毕业",
    "en_topic": "Memories and Graduation",
    "functions": "Share memories and express feelings about the past",
    "grammar": "Review: remember + V-ing / to V; 综合复习",
    "writing": "Write a graduation speech or a letter of thanks",
    "can_do": [
        "能用 remember + V-ing / to V 表达回忆",
        "能回顾和总结初中生活的难忘经历",
        "能表达感恩和对未来的展望",
        "能写毕业演讲或感谢信"
    ],
    "dialogue_scene": "Lily和Sam在毕业典礼后翻看毕业纪念册，回忆三年初中时光。",
    "dialogue": [
        ("Lily", "I can't believe we're graduating! It feels like just yesterday we were in Grade 7.", "真不敢相信我们要毕业了！感觉就像昨天我们还在七年级。"),
        ("Sam", "I know! I remember meeting all of you on the first day of school. We were all so shy!", "是啊！我记得第一天上学见到你们的情景。我们当时都好害羞！"),
        ("Lily", "Do you remember our first English class? Ms. Wang asked us to introduce ourselves in English.", "你还记得我们的第一节英语课吗？王老师让我们用英语自我介绍。"),
        ("Sam", "Ha, yes! I was so nervous that I forgot my own name! Everyone laughed.", "哈，记得！我紧张得连自己的名字都忘了！大家都笑了。"),
        ("Lily", "I remember scoring the winning goal in the basketball game. That was the best moment of Grade 8!", "我记得在篮球比赛中投进了制胜球。那是八年级最棒的时刻！"),
        ("Sam", "And I remember the science fair. Our volcano project won first prize! We stayed up all night working on it.", "还有科学展。我们的火山项目赢得了一等奖！我们熬夜做那个。"),
        ("Lily", "We've had so many great memories. I'll never forget these three years.", "我们有太多美好的回忆了。我永远不会忘记这三年。"),
        ("Sam", "Me neither. But I'm also excited about the future! Remember to keep in touch!", "我也是。但我也对未来充满期待！记得保持联系！")
    ],
    "key_points": [
        "remember + V-ing 表示「记得做过某事」— I remember <b>meeting</b> you in Grade 7.",
        "remember + to V 表示「记得要做某事」— Remember <b>to keep</b> in touch!",
        "forget + V-ing / to V 也有类似区别。",
        "初中毕业话题常用表达：look back at, be thankful to, learn from, look forward to"
    ],
    "vocab": [
        ("survey", "ˈsɜːrveɪ", "n./v.", "调查；测量", "We did a survey about reading habits.", "我们做了一个关于阅读习惯的调查。"),
        ("standard", "ˈstændərd", "n./adj.", "标准；标准的", "She set high standards for herself.", "她为自己设定了高标准。"),
        ("row", "roʊ", "n.", "排；行", "We sat in the front row.", "我们坐在第一排。"),
        ("keyboard", "ˈkiːbɔːrd", "n.", "键盘", "I practice the keyboard every day.", "我每天练习键盘。"),
        ("instruction", "ɪnˈstrʌkʃn", "n.", "说明；指导", "Follow the instructions carefully.", "仔细按照说明操作。"),
        ("double", "ˈdʌbl", "adj./v.", "双倍的；加倍", "Double-check your answers.", "再检查一遍你的答案。"),
        ("shall", "ʃæl", "modal v.", "将要；……好吗？", "Shall we go now?", "我们现在走好吗？"),
        ("overcome", "ˌoʊvərˈkʌm", "v.", "克服；战胜", "I overcame my fear of speaking.", "我克服了说话的恐惧。"),
        ("separate", "ˈseprət", "adj./v.", "分开的；分离", "We will go to separate high schools.", "我们将去不同的高中。"),
        ("wing", "wɪŋ", "n.", "翅膀；翼", "Birds fly with their wings.", "鸟用翅膀飞翔。"),
        ("caring", "ˈkerɪŋ", "adj.", "关心的；关爱他人的", "She is a very caring person.", "她是一个非常关心他人的人。"),
        ("senior", "ˈsiːniər", "adj./n.", "高级的；高中", "I will attend senior high school.", "我将上高中。"),
        ("ours", "ˈaʊərz", "pron.", "我们的", "This classroom is ours.", "这间教室是我们的。"),
        ("gentleman", "ˈdʒentlmən", "n.", "绅士；先生", "He is a true gentleman.", "他是一位真正的绅士。"),
        ("graduation", "ˌɡrædʒuˈeɪʃn", "n.", "毕业", "The graduation ceremony is next week.", "毕业典礼在下周。"),
        ("ceremony", "ˈserəmoʊni", "n.", "仪式；典礼", "The opening ceremony was beautiful.", "开幕式很美。"),
        ("congratulate", "kənˈɡrætʃuleɪt", "v.", "祝贺", "I congratulate you on your success.", "我祝贺你成功。"),
        ("thirsty", "ˈθɜːrsti", "adj.", "口渴的；渴望的", "Be thirsty for knowledge.", "渴望知识。"),
        ("none", "nʌn", "pron.", "没有一个", "None of us knew the answer.", "我们没有一个人知道答案。"),
        ("task", "tæsk", "n.", "任务；作业", "Finish the task before Friday.", "周五前完成任务。"),
        ("ahead", "əˈhed", "adv.", "在前面；向前", "There is a bright future ahead.", "前面有光明的未来。"),
        ("responsible", "rɪˈspɒnsəbl", "adj.", "负责任的", "Be responsible for your actions.", "对你的行为负责。")
    ],
    "patterns": [
        ("Remember + V-ing (记得做过某事)",
         "表示记得过去曾经做过的事情。",
         "I <b>remember meeting</b> all of you in Grade 7. / I <b>remember scoring</b> the winning goal."),
        ("Remember + to V (记得要做某事)",
         "表示记住要去做某事。",
         "<b>Remember to keep</b> in touch! / <b>Remember to bring</b> your camera."),
        ("主语 + will never forget + V-ing / n",
         "表示永远不会忘记。",
         "I <b>will never forget</b> these three years. / We <b>will never forget</b> our teachers."),
        ("主语 + be thankful to + sb + for + n/V-ing",
         "表示因某事感谢某人。",
         "I <b>am thankful to</b> my teachers <b>for</b> their help. / We <b>are thankful to</b> our parents <b>for</b> their support.")
    ],
    "grammar_title": "Remember + V-ing vs Remember + to V",
    "grammar_sections": [
        ("remember / forget 的两种用法", [
            ("动词", "+ V-ing (做过)", "+ to V (要做)"),
            ("remember", "记得做过（已发生）", "记得要做（未发生）"),
            ("forget", "忘记做过（已发生）", "忘记要做（未发生）"),
            ("例句", "I remember meeting her before.", "Remember to call me."),
            ("例句", "I forgot locking the door.", "Don't forget to lock the door.")
        ]),
        ("初中三年主要时态复习", [
            ("时态", "结构", "例句"),
            ("一般现在时", "V / V-s", "We are classmates."),
            ("一般过去时", "V-ed", "I was shy in Grade 7."),
            ("现在完成时", "have/has + V-ed", "I have learned a lot."),
            ("一般将来时", "will + V", "I will go to senior high.")
        ])
    ],
    "grammar_tips": [
        "remember doing 和 remember to do 意思完全不同，注意区分。",
        "stop doing (停止做) vs stop to do (停下来去做) 也有类似区别。",
        "try doing (尝试做) vs try to do (努力做) 同理。",
        "<span class=\"wotd-say\" data-speak=\"The future belongs to those who believe in the beauty of their dreams.\">The future belongs to those who believe in the beauty of their dreams.</span> 未来属于那些相信自己梦想之美的人。"
    ],
    "basic_qs": [
        ("基础", "★☆☆", "I remember ____ (meet) you on the first day of school.", "meeting"),
        ("基础", "★☆☆", "Remember ____ (lock) the door when you leave.", "to lock"),
        ("基础", "★☆☆", "I will never ____ (forget) these three years.", "forget"),
        ("基础", "★☆☆", "I am thankful ____ my teachers ____ their help.", "to ... for"),
        ("基础", "★☆☆", "I ____ (remember / forget) bringing my umbrella. It's in my bag.", "remember")
    ],
    "mid_qs": [
        ("提升", "★★☆", "选择：I remember ____ him somewhere before.<br>A. see B. seeing C. to see D. saw", "B"),
        ("提升", "★★☆", "Don't forget ____ (bring) your notebook tomorrow.", "to bring"),
        ("提升", "★★☆", "She stopped ____ (talk) when the teacher came in.", "talking"),
        ("提升", "★★☆", "翻译：我记得已经把钥匙给你了。", "I remember giving you the key. / I remember having given you the key."),
        ("提升", "★★☆", "I ____ (learn) a lot in the past three years.", "have learned")
    ],
    "hard_qs": [
        ("挑战", "★★★", "选择：I remember ____ the door, but it's open now.<br>A. lock B. locking C. to lock D. locked", "B"),
        ("挑战", "★★★", "完成句子：She forgot ____ (tell) me about the meeting, so I missed it.", "to tell"),
        ("挑战", "★★★", "用 remember / forget 的适当形式填空：When I left home this morning, I ____ (remember) to bring my lunch, but I ____ (forget) my keys.", "remembered ... forgot"),
        ("挑战", "★★★", "写作：用 remember doing / forget doing 和一般过去时写一段关于初中三年难忘经历的短文。", "I remember joining the school basketball team in Grade 7. I was so nervous on my first day of practice. I remember scoring my first point — it was an amazing feeling! I will never forget the friendships I made. I also remember our class trip to the science museum. We had so much fun. I'll always treasure these memories.")
    ],
    "reading_title": "A Graduation Speech",
    "reading_text": [
        "Good morning, dear teachers, parents, and fellow students. Today is a special day. We are graduating from junior high school. I still remember the first day I walked into this school. I was so nervous that my hands were shaking. But you, my classmates, welcomed me with warm smiles. Thank you.",
        "I remember our English teacher, Ms. Wang, who always encouraged us to speak bravely. I remember our math teacher, Mr. Li, who taught us that there is always more than one way to solve a problem. I remember our class monitor, who organized so many fun activities. I remember all of you.",
        "These three years have been full of challenges and achievements. We have learned not only knowledge from textbooks, but also how to be better people. We have learned to work together, to help each other, and to never give up.",
        "Now we are going to different senior high schools. Some of us may not see each other for a long time. But the memories we share will always be with us. As we move on to the next chapter of our lives, let's remember to be brave, to be kind, and to always believe in ourselves. Congratulations, everyone! We did it!"
    ],
    "reading_gloss": [
        ("fellow students", "同学们"),
        ("junior high school", "初中"),
        ("monitor", "班长"),
        ("achievements", "成就"),
        ("textbooks", "课本"),
        ("chapter", "篇章；章节")
    ],
    "reading_qs": [
        ("阅读", "★☆☆", "How did the speaker feel on the first day of school?", "She was very nervous — her hands were shaking."),
        ("阅读", "★★☆", "What did the English teacher encourage the students to do?", "To speak bravely."),
        ("阅读", "★★☆", "What did the students learn during the three years?", "They learned knowledge from textbooks and also how to be better people."),
        ("阅读", "★★★", "What is the main message of this graduation speech?", "To be thankful for the past, to cherish memories, and to be brave and kind for the future.")
    ],
    "exam_q_type": "短文填空 — 毕业话题",
    "exam_q": "用所给词的适当形式填空。",
    "exam_passage": [
        "I 1 (remember) my first day in Grade 7 like it was yesterday. I 2 (be) so shy that I didn't talk to anyone. But my deskmate, Lisa, 3 (smile) at me and said, 「Hi!」 From that day on, we became best friends. We 4 (study) together, laughed together, and even cried together. Now we are 5 (graduate). I will never 6 (forget) the time we spent together. I know we 7 (go) to different high schools, but our friendship will last forever."
    ],
    "exam_options": [
        (1, {"A": "remember", "B": "remembered", "C": "will remember", "D": "am remembering"}),
        (2, {"A": "am", "B": "was", "C": "were", "D": "be"}),
        (3, {"A": "smile", "B": "smiled", "C": "smiling", "D": "smiles"}),
        (4, {"A": "study", "B": "studied", "C": "will study", "D": "are studying"}),
        (5, {"A": "graduate", "B": "graduating", "C": "graduated", "D": "graduates"}),
        (6, {"A": "forget", "B": "forgot", "C": "forgetting", "D": "forgotten"}),
        (7, {"A": "go", "B": "will go", "C": "went", "D": "have gone"})
    ],
    "exam_answers": ["1. A", "2. B", "3. B", "4. B", "5. B", "6. A", "7. B"],
    "writing_prompt": "写一篇毕业演讲稿，回顾初中三年的难忘经历，感谢老师和同学，并展望未来的高中生活。",
    "writing_framework": [
        "开场问候：向老师、家长和同学问好",
        "回顾初一：初入校园的感受",
        "回顾初二：最难忘的经历",
        "回顾初三：努力备考的时光",
        "感恩：感谢老师和同学的帮助",
        "展望：对未来的期待和祝福"
    ],
    "writing_model_en": "Good morning, dear teachers and fellow students. It's a great honor to speak here today. I remember walking into this school for the first time three years ago. I was nervous, but the friendly faces of my classmates quickly made me feel at home.\n\nI remember our class trip to the mountain in Grade 8. We helped each other climb to the top. That day, I learned the meaning of teamwork. I remember the late nights we spent studying for exams in Grade 9. We encouraged each other and never gave up.\n\nI want to say thank you to our teachers. You have taught us knowledge and showed us how to be good people. Thank you to my classmates for the laughter and friendship. As we go to different high schools, let's remember to stay in touch. I believe our future will be bright. Congratulations, Class of 2025!",
    "writing_model_cn": "亲爱的老师、同学们，早上好。今天能站在这里发言，我感到无比荣幸。我记得三年前第一次走进这所学校的情景。当时我很紧张，但同学们友好的面孔很快让我感到自在。\n\n我记得八年级的班级登山活动。我们互相帮助，一起爬到了山顶。那一天，我懂得了团队合作的意义。我记得九年级我们一起熬夜备考的夜晚。我们互相鼓励，永不放弃。\n\n我想对我们的老师说声谢谢。你们不仅教给我们知识，还教会我们如何成为好人。谢谢我的同学们的欢声笑语和友谊。当我们走向不同的高中时，让我们记得保持联系。我相信我们的未来会一片光明。2025届的同学们，恭喜大家！",
    "project_title": "Our Memory Book",
    "project_desc": "制作一本班级毕业纪念册，收录每位同学的留言、照片和难忘回忆。",
    "project_steps": [
        "收集每位同学的毕业留言和签名",
        "收集三年来的班级照片",
        "写一段个人感言（初中最难忘的3-5件事）",
        "给老师写一封感谢信",
        "设计纪念册的版面和封面",
        "在毕业班会上展示并分享"
    ],
    "project_rubric": [
        "每位同学都有参与",
        "回忆内容真实、感人",
        "英语表达基本准确",
        "设计用心、有创意",
        "体现了班级的团结和友谊"
    ],
    "checklist": [
        "我能区分 remember doing 和 remember to do",
        "我能回顾和描述初中的难忘经历",
        "我能使用多种时态表达过去和未来",
        "我能理解毕业演讲的内容",
        "我能写毕业演讲稿或感谢信"
    ],
    "feynman": "向同桌解释 remember + V-ing 和 remember + to V 的区别，并各举两个例子。",
    "review": [
        "🔵 1天后：复习 remember/forget + V-ing vs to V",
        "🟢 3天后：复习毕业相关词汇和句型",
        "🟡 1周后：复述毕业演讲稿",
        "🔴 1月后：写一篇给未来自己的信"
    ],
    "next_unit_title": "🎉 初中英语全部学完！",
    "next_unit_desc": "恭喜你完成了全部14个单元的学习！建议回顾语法全景图，进行综合复习和中考模拟训练。"
}
