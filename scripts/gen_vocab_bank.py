#!/usr/bin/env python3
"""Generate vocab-bank.json — 47 units × 13 words = 611 entries."""
import json

def w(word, ipa, pos, defn, ex, trans):
    return {"w": word, "ipa": ipa, "pos": pos, "defn": defn, "ex": ex, "trans": trans}

U = {}

# ====================== ENGLISH 7 STARTER ======================

U["st01"] = {
    "master": [
        w("how","/haʊ/","adv.","怎样；如何","How are you today?","你今天怎么样？"),
        w("fine","/faɪn/","adj.","好的；健康的","I am fine, thank you.","我很好，谢谢。"),
        w("thanks","/θæŋks/","n.","感谢；谢谢","Thanks for your help.","谢谢你的帮助。"),
        w("teacher","/ˈtiːtʃər/","n.","老师","Our teacher is very kind.","我们的老师很和蔼。"),
        w("classmate","/ˈklæsmeɪt/","n.","同班同学","Tom is my new classmate.","汤姆是我的新同学。"),
        w("letter","/ˈletər/","n.","字母；信","We learned the letter A today.","今天我们学了字母A。"),
        w("friend","/frend/","n.","朋友","Li Ming is my good friend.","李明是我的好朋友。"),
        w("too","/tuː/","adv.","也；太","I like English, too.","我也喜欢英语。"),
    ],
    "expert": [
        w("introduce","/ˌɪntrəˈdjuːs/","v.","介绍","Let me introduce my friend to you.","让我把我的朋友介绍给你。"),
        w("greet","/ɡriːt/","v.","问候","We greet our teachers every morning.","我们每天早上向老师问好。"),
        w("spell","/spel/","v.","拼写","Can you spell your name?","你能拼写你的名字吗？"),
        w("pronounce","/prəˈnaʊns/","v.","发音","Please pronounce this word slowly.","请慢慢读这个单词。"),
        w("conversation","/ˌkɒnvəˈseɪʃən/","n.","对话；交谈","We had a nice conversation in English.","我们用英语进行了愉快的对话。"),
    ],
}

U["st02"] = {
    "master": [
        w("pencil case","/ˈpensl keɪs/","n.","铅笔盒","My pencil case is blue.","我的铅笔盒是蓝色的。"),
        w("notebook","/ˈnəʊtbʊk/","n.","笔记本","Write it in your notebook.","把它写在你的笔记本里。"),
        w("keep","/kiːp/","v.","保持；保留","Please keep your desk tidy.","请保持你的书桌整洁。"),
        w("thing","/θɪŋ/","n.","东西；事物","Put your things away.","把你的东西收好。"),
        w("find","/faɪnd/","v.","找到","I can't find my pen.","我找不到我的钢笔了。"),
        w("lost","/lɒst/","adj.","丢失的","I found a lost pencil.","我找到了一支丢失的铅笔。"),
        w("box","/bɒks/","n.","盒子","The pencils are in the box.","铅笔在盒子里。"),
        w("under","/ˈʌndər/","prep.","在……下面","The cat is under the desk.","猫在书桌下面。"),
    ],
    "expert": [
        w("organize","/ˈɔːrɡənaɪz/","v.","整理；组织","I organize my books every week.","我每周整理我的书。"),
        w("belong","/bɪˈlɒŋ/","v.","属于","This pen belongs to me.","这支钢笔是我的。"),
        w("label","/ˈleɪbl/","n.","标签","Put a label on your bottle.","给你的瓶子上贴个标签。"),
        w("drawer","/drɔːr/","n.","抽屉","Put your toys in the drawer.","把你的玩具放进抽屉里。"),
        w("neat","/niːt/","adj.","整洁的","Her room is always neat.","她的房间总是很整洁。"),
    ],
}

U["st03"] = {
    "master": [
        w("brown","/braʊn/","adj.","棕色的","The dog has brown eyes.","这只狗有棕色的眼睛。"),
        w("purple","/ˈpɜːrpl/","adj.","紫色的","I like the purple flowers.","我喜欢紫色的花朵。"),
        w("pink","/pɪŋk/","adj.","粉色的","Her bag is pink.","她的包是粉色的。"),
        w("grey","/ɡreɪ/","adj.","灰色的","The cat is grey and white.","这只猫是灰白相间的。"),
        w("picture","/ˈpɪktʃər/","n.","图片；图画","Draw a picture of your family.","画一张你家人的图片。"),
        w("paint","/peɪnt/","v.","涂色；绘画","Let's paint the picture together.","我们一起画这幅画吧。"),
        w("show","/ʃəʊ/","v.","展示","Show me your new schoolbag.","给我看看你的新书包。"),
        w("different","/ˈdɪfərənt/","adj.","不同的","They are in different colors.","它们的颜色不同。"),
    ],
    "expert": [
        w("rainbow","/ˈreɪnbəʊ/","n.","彩虹","A rainbow appears after the rain.","雨后出现了彩虹。"),
        w("describe","/dɪˈskraɪb/","v.","描述","Describe your favorite toy.","描述一下你最喜欢的玩具。"),
        w("bright","/braɪt/","adj.","明亮的；鲜艳的","She wore a bright red dress.","她穿了一件鲜红色的连衣裙。"),
        w("colorful","/ˈkʌlərfl/","adj.","色彩丰富的","The garden is colorful in spring.","春天的花园色彩丰富。"),
        w("prefer","/prɪˈfɜːr/","v.","更喜欢","I prefer blue to green.","比起绿色我更喜欢蓝色。"),
    ],
}

# ====================== ENGLISH 7 上册 ======================

U["u01"] = {
    "master": [
        w("hobby","/ˈhɒbi/","n.","爱好","Reading is my hobby.","阅读是我的爱好。"),
        w("age","/eɪdʒ/","n.","年龄","What is your age?","你多大了？"),
        w("country","/ˈkʌntri/","n.","国家","China is a big country.","中国是一个大国。"),
        w("city","/ˈsɪti/","n.","城市","Beijing is a big city.","北京是一座大城市。"),
        w("phone","/fəʊn/","n.","电话","What is your phone number?","你的电话号码是多少？"),
        w("number","/ˈnʌmbər/","n.","号码；数字","My number is 123.","我的号码是123。"),
        w("email","/ˈiːmeɪl/","n.","电子邮件","Send me an email.","给我发一封电子邮件。"),
        w("fun","/fʌn/","adj.","有趣的","The game is fun.","这个游戏很有趣。"),
    ],
    "expert": [
        w("background","/ˈbækɡraʊnd/","n.","背景","Tell me about your family background.","说说你的家庭背景。"),
        w("self-introduction","/ˌself ˌɪntrəˈdʌkʃn/","n.","自我介绍","Please give a self-introduction.","请做自我介绍。"),
        w("hometown","/ˈhəʊmtaʊn/","n.","家乡","My hometown is a small town.","我的家乡是一个小镇。"),
        w("personal","/ˈpɜːrsənl/","adj.","个人的；私人的","Don't share personal information online.","不要在网上分享个人信息。"),
        w("basic","/ˈbeɪsɪk/","adj.","基本的","These are some basic questions.","这些是一些基本问题。"),
    ],
}

U["u02"] = {
    "master": [
        w("parent","/ˈpeərənt/","n.","父/母","My parents are very nice.","我的父母非常好。"),
        w("uncle","/ˈʌŋkl/","n.","叔伯；舅舅","My uncle is a doctor.","我叔叔是一名医生。"),
        w("aunt","/ɑːnt/","n.","姑；姨；婶","My aunt lives in Shanghai.","我姑姑住在上海。"),
        w("cousin","/ˈkʌzn/","n.","堂/表兄弟姐妹","My cousin is ten years old.","我表弟十岁了。"),
        w("pretty","/ˈprɪti/","adj.","漂亮的","She is a pretty girl.","她是一个漂亮的女孩。"),
        w("handsome","/ˈhænsəm/","adj.","英俊的","He is tall and handsome.","他又高又英俊。"),
        w("young","/jʌŋ/","adj.","年轻的","My mother looks very young.","我妈妈看起来很年轻。"),
        w("elder","/ˈeldər/","adj.","年长的","My elder sister is in college.","我姐姐在上大学。"),
    ],
    "expert": [
        w("relative","/ˈrelətɪv/","n.","亲戚","Many relatives came to the party.","很多亲戚来参加了聚会。"),
        w("resemble","/rɪˈzembl/","v.","像；相似","She resembles her mother.","她长得像她妈妈。"),
        w("generous","/ˈdʒenərəs/","adj.","慷慨的；大方的","My grandpa is very generous.","我爷爷非常大方。"),
        w("patient","/ˈpeɪʃnt/","adj.","有耐心的","My father is patient with me.","我爸爸对我很有耐心。"),
        w("family tree","/ˈfæməli triː/","n.","家谱","We made a family tree in class.","我们在课堂上做了一个家谱。"),
    ],
}

U["u03"] = {
    "master": [
        w("office","/ˈɒfɪs/","n.","办公室","The teachers' office is on the second floor.","教师办公室在二楼。"),
        w("gate","/ɡeɪt/","n.","大门","The school gate is very big.","学校大门很大。"),
        w("toilet","/ˈtɔɪlət/","n.","厕所","Where is the toilet?","厕所在哪里？"),
        w("garden","/ˈɡɑːrdn/","n.","花园","There is a beautiful garden at school.","学校有一个美丽的花园。"),
        w("wall","/wɔːl/","n.","墙","There is a map on the wall.","墙上有一张地图。"),
        w("corner","/ˈkɔːrnər/","n.","角落；拐角","The library is at the corner.","图书馆在拐角处。"),
        w("left","/left/","adj./adv.","左边(的)","Turn left at the gate.","在大门口向左转。"),
        w("right","/raɪt/","adj./adv.","右边(的)","The classroom is on the right.","教室在右边。"),
    ],
    "expert": [
        w("facility","/fəˈsɪləti/","n.","设施","Our school has great sports facilities.","我们学校有很棒的运动设施。"),
        w("direction","/dɪˈrekʃn/","n.","方向","Which direction is the library?","图书馆在哪个方向？"),
        w("opposite","/ˈɒpəzɪt/","prep.","在……对面","The garden is opposite the library.","花园在图书馆对面。"),
        w("campus","/ˈkæmpəs/","n.","校园","Our campus is clean and beautiful.","我们校园干净又美丽。"),
        w("location","/ləʊˈkeɪʃn/","n.","位置","The location of the gym is near the playground.","体育馆在操场附近。"),
    ],
}

U["u04"] = {
    "master": [
        w("biology","/baɪˈɒlədʒi/","n.","生物","We learn about plants in biology.","我们在生物课上学习植物。"),
        w("geography","/dʒiˈɒɡrəfi/","n.","地理","Geography is very interesting.","地理课很有趣。"),
        w("physics","/ˈfɪzɪks/","n.","物理","We did an experiment in physics class.","我们在物理课上做了实验。"),
        w("boring","/ˈbɔːrɪŋ/","adj.","无聊的","Some think math is boring.","有些人觉得数学无聊。"),
        w("easy","/ˈiːzi/","adj.","容易的","The test was very easy.","考试很简单。"),
        w("important","/ɪmˈpɔːrtnt/","adj.","重要的","English is very important.","英语非常重要。"),
        w("understand","/ˌʌndərˈstænd/","v.","理解","I understand the question now.","我现在理解这个问题了。"),
        w("explain","/ɪkˈspleɪn/","v.","解释","Please explain the meaning to me.","请给我解释一下意思。"),
    ],
    "expert": [
        w("curriculum","/kəˈrɪkjələm/","n.","课程","Our curriculum includes many subjects.","我们的课程包括很多科目。"),
        w("practical","/ˈpræktɪkl/","adj.","实用的","This subject is very practical.","这门课很实用。"),
        w("timetable","/ˈtaɪmteɪbl/","n.","课程表","Check the timetable for tomorrow.","查看明天的课程表。"),
        w("strength","/streŋθ/","n.","优势；长处","Math is my strength.","数学是我的优势。"),
        w("passion","/ˈpæʃn/","n.","热情；热爱","She has a passion for science.","她对科学充满热情。"),
    ],
}

U["u05"] = {
    "master": [
        w("talent","/ˈtælənt/","n.","才能；天赋","She has a talent for dancing.","她有舞蹈天赋。"),
        w("choose","/tʃuːz/","v.","选择","Which club do you choose?","你选择哪个俱乐部？"),
        w("demonstrate","/ˈdemənstreɪt/","v.","展示；示范","We demonstrate our skills at the show.","我们在表演中展示技能。"),
        w("practice","/ˈpræktɪs/","v.","练习","Practice the piano every day.","每天练习钢琴。"),
        w("member","/ˈmembər/","n.","成员","I am a member of the chess club.","我是象棋俱乐部的成员。"),
        w("activity","/ækˈtɪvəti/","n.","活动","There are many activities after school.","放学后有很多活动。"),
        w("team","/tiːm/","n.","团队","We work as a team.","我们团队合作。"),
        w("competition","/ˌkɒmpəˈtɪʃn/","n.","比赛","We won the singing competition.","我们赢了歌唱比赛。"),
    ],
    "expert": [
        w("audition","/ɔːˈdɪʃn/","n.","试演；面试","I have an audition for the play.","我要参加话剧的试演。"),
        w("volunteer","/ˌvɒlənˈtɪər/","v.","自愿做","I volunteer in the art club.","我在美术俱乐部做志愿者。"),
        w("skill","/skɪl/","n.","技能","Learning a new skill takes time.","学习新技能需要时间。"),
        w("coach","/kəʊtʃ/","n.","教练","The coach teaches us how to play chess.","教练教我们下象棋。"),
        w("tryout","/ˈtraɪaʊt/","n.","选拔；试训","The basketball tryout is next week.","篮球选拔赛在下周。"),
    ],
}

U["u06"] = {
    "master": [
        w("early","/ˈɜːrli/","adv.","早地","I get up early every day.","我每天早起。"),
        w("late","/leɪt/","adv.","晚地；迟地","Don't be late for school.","上学不要迟到。"),
        w("brush","/brʌʃ/","v.","刷","Brush your teeth before bed.","睡觉前刷牙。"),
        w("shower","/ˈʃaʊər/","n.","淋浴","I take a shower every morning.","我每天早上洗澡。"),
        w("always","/ˈɔːlweɪz/","adv.","总是","I always walk to school.","我总是走路去上学。"),
        w("never","/ˈnevər/","adv.","从不","I never eat junk food.","我从不吃垃圾食品。"),
        w("schedule","/ˈʃedjuːl/","n.","时间表","I have a busy schedule today.","我今天的时间表很紧。"),
        w("weekday","/ˈwiːkdeɪ/","n.","工作日","On weekdays, I go to school.","工作日我去上学。"),
    ],
    "expert": [
        w("routine","/ruːˈtiːn/","n.","常规；日常事务","My daily routine is well organized.","我的日常安排很有条理。"),
        w("efficient","/ɪˈfɪʃnt/","adj.","高效的","Plan ahead to be more efficient.","提前计划才能更高效。"),
        w("prepare","/prɪˈpeər/","v.","准备","I prepare my bag the night before.","我头天晚上准备好书包。"),
        w("habit","/ˈhæbɪt/","n.","习惯","Good habits help us learn better.","好习惯帮助我们学得更好。"),
        w("punctual","/ˈpʌŋktʃuəl/","adj.","守时的","She is always punctual for class.","她上课总是很准时。"),
    ],
}

U["u07"] = {
    "master": [
        w("calendar","/ˈkælɪndər/","n.","日历","Check the calendar for the date.","查看日历找日期。"),
        w("celebrate","/ˈselɪbreɪt/","v.","庆祝","We celebrate with a cake.","我们用蛋糕庆祝。"),
        w("present","/ˈpreznt/","n.","礼物","I got a nice present.","我得到了一份好礼物。"),
        w("card","/kɑːrd/","n.","卡片","I made a card for my mom.","我给妈妈做了一张卡片。"),
        w("candle","/ˈkændl/","n.","蜡烛","Blow out the candles on the cake.","吹灭蛋糕上的蜡烛。"),
        w("surprise","/sərˈpraɪz/","n.","惊喜","The party was a big surprise.","这个派对是一个大惊喜。"),
        w("invite","/ɪnˈvaɪt/","v.","邀请","I invite my friends to the party.","我邀请朋友们来派对。"),
        w("balloon","/bəˈluːn/","n.","气球","The room is full of balloons.","房间里满是气球。"),
    ],
    "expert": [
        w("annual","/ˈænjuəl/","adj.","每年的","My birthday is an annual event.","我的生日是一年一度的。"),
        w("tradition","/trəˈdɪʃn/","n.","传统","Eating noodles on birthdays is a tradition.","生日吃面条是一个传统。"),
        w("celebration","/ˌselɪˈbreɪʃn/","n.","庆祝活动","The celebration lasted all day.","庆祝活动持续了一整天。"),
        w("ceremony","/ˈserɪməni/","n.","仪式","The opening ceremony was wonderful.","开幕式非常精彩。"),
        w("memorable","/ˈmemərəbl/","adj.","难忘的","We had a memorable birthday party.","我们举办了一个难忘的生日派对。"),
    ],
}

# ====================== ENGLISH 7 下册 ======================

U["b2u01"] = {
    "master": [
        w("koala","/kəʊˈɑːlə/","n.","考拉","Koalas sleep during the day.","考拉白天睡觉。"),
        w("giraffe","/dʒɪˈræf/","n.","长颈鹿","The giraffe has a very long neck.","长颈鹿有很长的脖子。"),
        w("penguin","/ˈpeŋɡwɪn/","n.","企鹅","Penguins live in cold places.","企鹅生活在寒冷的地方。"),
        w("dolphin","/ˈdɒlfɪn/","n.","海豚","Dolphins are very smart animals.","海豚很聪明。"),
        w("wing","/wɪŋ/","n.","翅膀","Birds use their wings to fly.","鸟用翅膀飞翔。"),
        w("fur","/fɜːr/","n.","皮毛","The cat has soft fur.","猫有柔软的皮毛。"),
        w("tail","/teɪl/","n.","尾巴","The monkey has a long tail.","猴子有长尾巴。"),
        w("claw","/klɔː/","n.","爪子","The eagle has sharp claws.","鹰有锋利的爪子。"),
    ],
    "expert": [
        w("species","/ˈspiːʃiːz/","n.","物种","This species is in danger.","这个物种处于危险中。"),
        w("mammal","/ˈmæml/","n.","哺乳动物","Dolphins are mammals, not fish.","海豚是哺乳动物，不是鱼。"),
        w("endangered","/ɪnˈdeɪndʒərd/","adj.","濒危的","Pandas are an endangered species.","大熊猫是濒危物种。"),
        w("habitat","/ˈhæbɪtæt/","n.","栖息地","The forest is the habitat of many animals.","森林是许多动物的栖息地。"),
        w("conservation","/ˌkɒnsərˈveɪʃn/","n.","保护","Wildlife conservation is very important.","野生动物保护非常重要。"),
    ],
}

U["b2u02"] = {
    "master": [
        w("follow","/ˈfɒləʊ/","v.","遵守；跟随","Follow the school rules.","遵守学校规则。"),
        w("obey","/əˈbeɪ/","v.","服从；遵守","We must obey the traffic rules.","我们必须遵守交通规则。"),
        w("punish","/ˈpʌnɪʃ/","v.","惩罚","Bad behavior will be punished.","不良行为将受到惩罚。"),
        w("behave","/bɪˈheɪv/","v.","表现；举止","Please behave well in class.","请在课堂上表现好。"),
        w("responsible","/rɪˈspɒnsəbl/","adj.","负责的","Be responsible for your actions.","对你的行为负责。"),
        w("discipline","/ˈdɪsəplɪn/","n.","纪律","Discipline is important in school.","纪律在学校很重要。"),
        w("respect","/rɪˈspekt/","v.","尊敬；尊重","Respect your teachers and classmates.","尊敬你的老师和同学。"),
        w("warning","/ˈwɔːrnɪŋ/","n.","警告","He got a warning for being late.","他因为迟到收到了警告。"),
    ],
    "expert": [
        w("regulation","/ˌreɡjuˈleɪʃn/","n.","规章","The school regulations must be followed.","必须遵守学校规章。"),
        w("consequence","/ˈkɒnsɪkwəns/","n.","后果","Every action has a consequence.","每个行为都有后果。"),
        w("permission","/pərˈmɪʃn/","n.","许可","Ask for permission before leaving.","离开前要征得许可。"),
        w("authority","/ɔːˈθɒrəti/","n.","权威；当局","We should respect authority.","我们应该尊重权威。"),
        w("violation","/ˌvaɪəˈleɪʃn/","n.","违反","Running in the hall is a rule violation.","在走廊跑是违规行为。"),
    ],
}

U["b2u03"] = {
    "master": [
        w("jog","/dʒɒɡ/","v.","慢跑","I jog in the park every morning.","我每天早上在公园慢跑。"),
        w("stretch","/stretʃ/","v.","伸展","Stretch your body before exercise.","运动前伸展一下身体。"),
        w("energy","/ˈenərdʒi/","n.","精力；能量","Eating well gives us energy.","吃好给我们能量。"),
        w("active","/ˈæktɪv/","adj.","活跃的","She is very active in PE class.","她在体育课上很活跃。"),
        w("weight","/weɪt/","n.","重量；体重","I want to keep a healthy weight.","我想保持健康的体重。"),
        w("muscle","/ˈmʌsl/","n.","肌肉","Exercise helps build strong muscles.","锻炼帮助建立强壮的肌肉。"),
        w("amount","/əˈmaʊnt/","n.","数量","A proper amount of exercise is good.","适量的运动有好处。"),
        w("daily","/ˈdeɪli/","adj.","每日的","Daily exercise keeps you healthy.","每天锻炼让你保持健康。"),
    ],
    "expert": [
        w("endurance","/ɪnˈdjʊərəns/","n.","耐力","Running improves your endurance.","跑步提高你的耐力。"),
        w("workout","/ˈwɜːrkaʊt/","n.","锻炼","I do a 30-minute workout every day.","我每天做30分钟锻炼。"),
        w("flexibility","/ˌfleksəˈbɪləti/","n.","柔韧性","Yoga helps improve flexibility.","瑜伽有助于提高柔韧性。"),
        w("metabolism","/məˈtæbəlɪzəm/","n.","新陈代谢","Exercise speeds up your metabolism.","运动加速新陈代谢。"),
        w("fitness","/ˈfɪtnəs/","n.","健康","Physical fitness is important for students.","身体健康对学生很重要。"),
    ],
}

U["b2u04"] = {
    "master": [
        w("tomato","/təˈmɑːtəʊ/","n.","西红柿","Tomatoes are red and healthy.","西红柿又红又健康。"),
        w("potato","/pəˈteɪtəʊ/","n.","土豆","Potatoes can be cooked in many ways.","土豆有很多种做法。"),
        w("carrot","/ˈkærət/","n.","胡萝卜","Rabbits like eating carrots.","兔子喜欢吃胡萝卜。"),
        w("sandwich","/ˈsænwɪtʃ/","n.","三明治","I had a sandwich for lunch.","我午餐吃了一个三明治。"),
        w("porridge","/ˈpɒrɪdʒ/","n.","粥；麦片粥","I eat porridge for breakfast.","我早餐喝粥。"),
        w("hungry","/ˈhʌŋɡri/","adj.","饥饿的","I feel hungry before dinner.","晚饭前我感到饿了。"),
        w("thirsty","/ˈθɜːrsti/","adj.","口渴的","Drink water when you are thirsty.","口渴的时候喝水。"),
        w("full","/fʊl/","adj.","饱的；满的","I am full after the meal.","我吃饱了。"),
    ],
    "expert": [
        w("nutrition","/njuˈtrɪʃn/","n.","营养","Fruits provide good nutrition.","水果提供良好的营养。"),
        w("diet","/ˈdaɪət/","n.","饮食","A balanced diet is important.","均衡饮食很重要。"),
        w("ingredient","/ɪnˈɡriːdiənt/","n.","原料","Fresh ingredients make better food.","新鲜食材做出更好的食物。"),
        w("appetite","/ˈæpɪtaɪt/","n.","食欲","Exercise gives me a good appetite.","运动让我胃口好。"),
        w("digest","/daɪˈdʒest/","v.","消化","This food is easy to digest.","这种食物容易消化。"),
    ],
}

U["b2u05"] = {
    "master": [
        w("moment","/ˈməʊmənt/","n.","时刻；瞬间","Wait a moment, please.","请稍等片刻。"),
        w("diary","/ˈdaɪəri/","n.","日记","I write in my diary every night.","我每晚写日记。"),
        w("record","/rɪˈkɔːrd/","v.","记录","I record what I do every day.","我记录每天做的事情。"),
        w("newspaper","/ˈnjuːzpeɪpər/","n.","报纸","My dad reads the newspaper every morning.","我爸爸每天早上看报纸。"),
        w("text message","/tekst ˈmesɪdʒ/","n.","短信","Send me a text message.","给我发条短信。"),
        w("video","/ˈvɪdiəʊ/","n.","视频","I am watching a video now.","我正在看一个视频。"),
        w("phone call","/fəʊn kɔːl/","n.","电话","I am making a phone call.","我正在打电话。"),
        w("right now","/raɪt naʊ/","adv.","现在；立刻","I am doing my homework right now.","我正在做作业。"),
    ],
    "expert": [
        w("currently","/ˈkʌrəntli/","adv.","当前；目前","I am currently reading a book.","我目前正在读一本书。"),
        w("simultaneously","/ˌsɪmlˈteɪniəsli/","adv.","同时地","Don't eat and watch TV simultaneously.","不要同时吃饭和看电视。"),
        w("presently","/ˈprezntli/","adv.","此刻；目前","She is presently in class.","她此刻正在上课。"),
        w("update","/ʌpˈdeɪt/","v.","更新","I update my blog every week.","我每周更新我的博客。"),
        w("progress","/ˈprəʊɡres/","n.","进展；进步","I am making progress in English.","我在英语方面正在进步。"),
    ],
}

U["b2u06"] = {
    "master": [
        w("temperature","/ˈtemprətʃər/","n.","温度","The temperature today is 25 degrees.","今天气温25度。"),
        w("degree","/dɪˈɡriː/","n.","度数","It is 30 degrees outside.","外面30度。"),
        w("raincoat","/ˈreɪnkəʊt/","n.","雨衣","Take your raincoat in case it rains.","带上雨衣以防下雨。"),
        w("umbrella","/ʌmˈbrelə/","n.","雨伞","Don't forget your umbrella today.","今天别忘了你的雨伞。"),
        w("forecast","/ˈfɔːrkɑːst/","n.","预报","Check the weather forecast before going out.","出门前查看天气预报。"),
        w("lightning","/ˈlaɪtnɪŋ/","n.","闪电","Lightning is very dangerous.","闪电非常危险。"),
        w("thunder","/ˈθʌndər/","n.","雷声","The thunder was very loud last night.","昨晚雷声很大。"),
        w("storm","/stɔːrm/","n.","暴风雨","The storm lasted for two hours.","暴风雨持续了两个小时。"),
    ],
    "expert": [
        w("climate","/ˈklaɪmət/","n.","气候","The climate in my city is mild.","我所在的城市气候温和。"),
        w("humid","/ˈhjuːmɪd/","adj.","潮湿的","Summer is hot and humid here.","这里的夏天炎热潮湿。"),
        w("breeze","/briːz/","n.","微风","A cool breeze feels great in summer.","夏天的凉爽微风很舒服。"),
        w("drought","/draʊt/","n.","干旱","The plants died because of the drought.","植物因干旱而枯死。"),
        w("hail","/heɪl/","n.","冰雹","Hail can damage crops.","冰雹会损坏庄稼。"),
    ],
}

U["b2u07"] = {
    "master": [
        w("event","/ɪˈvent/","n.","事件；大事","It was a special event for me.","这对我来说是一件特别的事。"),
        w("experience","/ɪkˈspɪriəns/","n.","经历","I had a wonderful experience.","我有了一次美妙的经历。"),
        w("happen","/ˈhæpən/","v.","发生","What happened yesterday?","昨天发生了什么？"),
        w("suddenly","/ˈsʌdənli/","adv.","突然地","Suddenly, it started to rain.","突然开始下雨了。"),
        w("climb","/klaɪm/","v.","爬；攀登","We climbed the mountain together.","我们一起爬了山。"),
        w("shout","/ʃaʊt/","v.","喊叫","He shouted for help.","他大声呼救。"),
        w("cry","/kraɪ/","v.","哭","Don't cry. Everything will be okay.","别哭，一切都会好起来的。"),
        w("smile","/smaɪl/","v.","微笑","She smiled at me.","她对我微笑。"),
    ],
    "expert": [
        w("adventure","/ədˈventʃər/","n.","冒险","The trip was a great adventure.","这次旅行是一次大冒险。"),
        w("challenge","/ˈtʃælɪndʒ/","n.","挑战","Climbing the mountain was a challenge.","爬山是一个挑战。"),
        w("overcome","/ˌəʊvərˈkʌm/","v.","克服","We overcame many difficulties.","我们克服了很多困难。"),
        w("impression","/ɪmˈpreʃn/","n.","印象","The trip left a deep impression on me.","这次旅行给我留下了深刻的印象。"),
        w("valuable","/ˈvæljuəbl/","adj.","宝贵的","I learned a valuable lesson.","我学到了宝贵的一课。"),
    ],
}

U["b2u08"] = {
    "master": [
        w("prince","/prɪns/","n.","王子","The prince saved the princess.","王子救了公主。"),
        w("princess","/ˌprɪnˈses/","n.","公主","The princess lived in a castle.","公主住在城堡里。"),
        w("castle","/ˈkɑːsl/","n.","城堡","There is a big castle in the story.","故事里有一座大城堡。"),
        w("magic","/ˈmædʒɪk/","adj.","有魔力的","The magic mirror can talk.","魔镜可以说话。"),
        w("beginning","/bɪˈɡɪnɪŋ/","n.","开始","In the beginning, there was a forest.","一开始，有一片森林。"),
        w("middle","/ˈmɪdl/","n.","中间","In the middle of the story, something happens.","故事中间发生了一些事情。"),
        w("ending","/ˈendɪŋ/","n.","结尾","The story has a happy ending.","故事有一个幸福的结尾。"),
        w("brave","/breɪv/","adj.","勇敢的","The brave boy saved his friend.","勇敢的男孩救了他的朋友。"),
    ],
    "expert": [
        w("moral","/ˈmɒrəl/","n.","寓意","The moral of the story is to be kind.","故事的寓意是要善良。"),
        w("fable","/ˈfeɪbl/","n.","寓言","This fable teaches us a lesson.","这个寓言给我们一个教训。"),
        w("character","/ˈkærɪktər/","n.","角色；人物","The main character is a clever fox.","主角是一只聪明的狐狸。"),
        w("plot","/plɒt/","n.","情节","The plot of this story is very interesting.","这个故事的情节非常有趣。"),
        w("imagination","/ɪˌmædʒɪˈneɪʃn/","n.","想象力","Reading stories develops our imagination.","读故事发展我们的想象力。"),
    ],
}

# ====================== ENGLISH 8 上册 ======================

U["u01_8"] = {
    "master": [
        w("destination","/ˌdestɪˈneɪʃn/","n.","目的地","My holiday destination is Hainan.","我的度假目的地是海南。"),
        w("journey","/ˈdʒɜːrni/","n.","旅行；旅程","The journey took five hours.","旅程花了五个小时。"),
        w("tourist","/ˈtʊərɪst/","n.","游客","Many tourists visit the Great Wall.","很多游客游览长城。"),
        w("flight","/flaɪt/","n.","航班","We took an early morning flight.","我们乘坐了早班航班。"),
        w("hotel","/həʊˈtel/","n.","酒店","We stayed at a nice hotel.","我们住在一家不错的酒店。"),
        w("sightseeing","/ˈsaɪtsiːɪŋ/","n.","观光","We went sightseeing in the city.","我们在城市里观光。"),
        w("souvenir","/ˌsuːvəˈnɪər/","n.","纪念品","I bought a souvenir for my friend.","我给朋友买了一个纪念品。"),
        w("pack","/pæk/","v.","打包","I need to pack my suitcase.","我需要收拾行李箱。"),
    ],
    "expert": [
        w("itinerary","/aɪˈtɪnərəri/","n.","行程表","We planned a detailed itinerary.","我们制定了详细的行程表。"),
        w("accommodation","/əˌkɒməˈdeɪʃn/","n.","住宿","We found good accommodation near the beach.","我们在海滩附近找到了不错的住宿。"),
        w("landmark","/ˈlændmɑːrk/","n.","地标","The Eiffel Tower is a famous landmark.","埃菲尔铁塔是著名的地标。"),
        w("reservation","/ˌrezərˈveɪʃn/","n.","预订","I made a hotel reservation online.","我在网上预订了酒店。"),
        w("adventure","/ədˈventʃər/","n.","冒险","Travelling is always an adventure.","旅行总是一次冒险。"),
    ],
}

U["u02_8"] = {
    "master": [
        w("dust","/dʌst/","v.","擦灰","Please dust the shelves.","请擦掉书架上的灰尘。"),
        w("fold","/fəʊld/","v.","折叠","Fold your clothes and put them away.","叠好你的衣服放好。"),
        w("mop","/mɒp/","v.","拖地","I mop the floor every weekend.","我每周末拖地。"),
        w("iron","/ˈaɪərn/","v.","熨烫","My mom irons the clothes.","我妈妈熨衣服。"),
        w("mess","/mes/","n.","杂乱","Clean up the mess in your room.","把你房间的杂乱收拾干净。"),
        w("neighbor","/ˈneɪbər/","n.","邻居","Our neighbor is very friendly.","我们的邻居很友好。"),
        w("invitation","/ˌɪnvɪˈteɪʃn/","n.","邀请","I got an invitation to the party.","我收到了派对的邀请。"),
        w("polite","/pəˈlaɪt/","adj.","有礼貌的","It is polite to say thank you.","说谢谢是有礼貌的。"),
    ],
    "expert": [
        w("household","/ˈhaʊshəʊld/","n.","家庭；家务","Everyone should share household chores.","每个人都应该分担家务。"),
        w("responsibility","/rɪˌspɒnsəˈbɪləti/","n.","责任","Doing chores is our responsibility.","做家务是我们的责任。"),
        w("cooperation","/kəʊˌɒpəˈreɪʃn/","n.","合作","Housework needs family cooperation.","家务需要家庭合作。"),
        w("appreciate","/əˈpriːʃieɪt/","v.","感激","I appreciate your help with the chores.","我感激你帮忙做家务。"),
        w("tidy up","/ˈtaɪdi ʌp/","phr.","整理","Please tidy up your room before dinner.","晚饭前请整理好你的房间。"),
    ],
}

U["u03_8"] = {
    "master": [
        w("gentle","/ˈdʒentl/","adj.","温和的","She is gentler than her sister.","她比她姐姐更温和。"),
        w("clever","/ˈklevər/","adj.","聪明的","He is the cleverest student in class.","他是班上最聪明的学生。"),
        w("lazy","/ˈleɪzi/","adj.","懒惰的","Don't be so lazy. Do your work.","别这么懒，做你的功课。"),
        w("careful","/ˈkeərfl/","adj.","仔细的","Be more careful next time.","下次更仔细些。"),
        w("popular","/ˈpɒpjələr/","adj.","受欢迎的","She is the most popular girl in school.","她是学校里最受欢迎的女孩。"),
        w("confident","/ˈkɒnfɪdənt/","adj.","自信的","He is more confident than before.","他比以前更自信了。"),
        w("similar","/ˈsɪmələr/","adj.","相似的","We have similar interests.","我们有相似的兴趣。"),
        w("compare","/kəmˈpeər/","v.","比较","Compare these two pictures.","比较这两张图片。"),
    ],
    "expert": [
        w("personality","/ˌpɜːrsəˈnæləti/","n.","个性；性格","Everyone has a unique personality.","每个人都有独特的个性。"),
        w("superior","/suːˈpɪriər/","adj.","更优的","This method is superior to that one.","这个方法比那个更好。"),
        w("distinct","/dɪˈstɪŋkt/","adj.","截然不同的","Their styles are quite distinct.","他们的风格截然不同。"),
        w("exception","/ɪkˈsepʃn/","n.","例外","No one is an exception to this rule.","没有人是这条规则的例外。"),
        w("characteristic","/ˌkærɪktəˈrɪstɪk/","n.","特征","Politeness is a good characteristic.","礼貌是一个好特征。"),
    ],
}

U["u04_8"] = {
    "master": [
        w("toucan","/ˈtuːkæn/","n.","巨嘴鸟","The toucan has a colorful beak.","巨嘴鸟有色彩鲜艳的喙。"),
        w("parrot","/ˈpærət/","n.","鹦鹉","The parrot can imitate human speech.","鹦鹉能模仿人说话。"),
        w("jaguar","/ˈdʒæɡjuər/","n.","美洲豹","Jaguars live in the rainforest.","美洲豹生活在雨林里。"),
        w("oxygen","/ˈɒksɪdʒən/","n.","氧气","Trees produce oxygen for us to breathe.","树木产生我们呼吸的氧气。"),
        w("ecosystem","/ˈiːkəʊsɪstəm/","n.","生态系统","The rainforest is a rich ecosystem.","雨林是一个丰富的生态系统。"),
        w("jungle","/ˈdʒʌŋɡl/","n.","丛林","Many wild animals live in the jungle.","很多野生动物生活在丛林里。"),
        w("extinct","/ɪkˈstɪŋkt/","adj.","灭绝的","Some animals are in danger of becoming extinct.","一些动物面临灭绝的危险。"),
        w("tropical","/ˈtrɒpɪkl/","adj.","热带的","Tropical rainforests are near the equator.","热带雨林在赤道附近。"),
    ],
    "expert": [
        w("biodiversity","/ˌbaɪəʊdaɪˈvɜːrsəti/","n.","生物多样性","The Amazon has the richest biodiversity.","亚马孙有着最丰富的生物多样性。"),
        w("camouflage","/ˈkæməflɑːʒ/","n.","伪装","The chameleon uses camouflage to hide.","变色龙用伪装来隐藏。"),
        w("predator","/ˈpredətər/","n.","捕食者","Lions are powerful predators.","狮子是强大的捕食者。"),
        w("adaptation","/ˌædæpˈteɪʃn/","n.","适应","Adaptation helps animals survive.","适应帮助动物生存。"),
        w("conservationist","/ˌkɒnsərˈveɪʃənɪst/","n.","环保人士","Conservationists work to protect nature.","环保人士致力于保护自然。"),
    ],
}

U["u05_8"] = {
    "master": [
        w("stir","/stɜːr/","v.","搅拌","Stir the soup with a spoon.","用勺子搅拌汤。"),
        w("pour","/pɔːr/","v.","倒；灌","Pour the milk into the glass.","把牛奶倒进杯子里。"),
        w("slice","/slaɪs/","v.","切片","Slice the bread into pieces.","把面包切成片。"),
        w("peel","/piːl/","v.","削皮","Peel the apple before eating it.","吃苹果之前削皮。"),
        w("mix","/mɪks/","v.","混合","Mix the flour and water together.","把面粉和水混合在一起。"),
        w("oven","/ˈʌvn/","n.","烤箱","Put the cake in the oven.","把蛋糕放进烤箱。"),
        w("delicious","/dɪˈlɪʃəs/","adj.","美味的","The meal tastes delicious.","这顿饭尝起来很美味。"),
        w("steam","/stiːm/","v.","蒸","We like to steam fish.","我们喜欢蒸鱼。"),
    ],
    "expert": [
        w("cuisine","/kwɪˈziːn/","n.","烹饪；菜肴","Chinese cuisine is famous worldwide.","中国菜世界闻名。"),
        w("gourmet","/ˈɡʊərmeɪ/","n.","美食家","My uncle is a real gourmet.","我叔叔是个真正的美食家。"),
        w("marinate","/ˈmærɪneɪt/","v.","腌制","Marinate the chicken for an hour.","把鸡肉腌制一小时。"),
        w("recipe","/ˈresəpi/","n.","食谱","Follow the recipe carefully.","仔细按照食谱做。"),
        w("appetizing","/ˈæpɪtaɪzɪŋ/","adj.","开胃的","The food looks very appetizing.","这食物看起来很开胃。"),
    ],
}

U["u06_8"] = {
    "master": [
        w("ambition","/æmˈbɪʃn/","n.","志向；抱负","My ambition is to become a doctor.","我的志向是成为一名医生。"),
        w("profession","/prəˈfeʃn/","n.","职业","Teaching is a great profession.","教书是一个伟大的职业。"),
        w("achieve","/əˈtʃiːv/","v.","实现；取得","Work hard to achieve your dream.","努力实现你的梦想。"),
        w("goal","/ɡəʊl/","n.","目标","Set a clear goal for yourself.","为自己设定一个明确的目标。"),
        w("determination","/dɪˌtɜːrmɪˈneɪʃn/","n.","决心","With determination, you can succeed.","有决心就能成功。"),
        w("career","/kəˈrɪər/","n.","事业","She has a successful career as a scientist.","她作为科学家有着成功的事业。"),
        w("opportunity","/ˌɒpəˈtjuːnəti/","n.","机会","Every challenge is an opportunity to learn.","每个挑战都是学习的机会。"),
        w("effort","/ˈefərt/","n.","努力","Put more effort into your studies.","在学习上多努力。"),
    ],
    "expert": [
        w("vocation","/vəʊˈkeɪʃn/","n.","天职；使命感","Teaching is a vocation, not just a job.","教书不只是一种工作，更是一种使命。"),
        w("specialize","/ˈspeʃəlaɪz/","v.","专攻","He wants to specialize in engineering.","他想专攻工程学。"),
        w("perseverance","/ˌpɜːrsɪˈvɪərəns/","n.","坚持不懈","Perseverance is the key to success.","坚持不懈是成功的关键。"),
        w("milestone","/ˈmaɪlstəʊn/","n.","里程碑","Graduation is an important milestone.","毕业是一个重要的里程碑。"),
        w("endeavour","/ɪnˈdevər/","n.","努力；尝试","Learning is a lifelong endeavour.","学习是终身的努力。"),
    ],
}

U["u07_8"] = {
    "master": [
        w("predict","/prɪˈdɪkt/","v.","预测","It is hard to predict the future.","很难预测未来。"),
        w("robot","/ˈrəʊbɒt/","n.","机器人","Robots will help us do housework.","机器人将帮助我们做家务。"),
        w("artificial","/ˌɑːrtɪˈfɪʃl/","adj.","人造的","Artificial intelligence is changing our world.","人工智能正在改变我们的世界。"),
        w("pollute","/pəˈluːt/","v.","污染","Factories should not pollute the rivers.","工厂不应该污染河流。"),
        w("renewable","/rɪˈnjuːəbl/","adj.","可再生的","Solar energy is a renewable resource.","太阳能是可再生的资源。"),
        w("electric","/ɪˈlektrɪk/","adj.","电动的","Electric cars are better for the environment.","电动车对环境更好。"),
        w("smart","/smɑːrt/","adj.","智能的","Smart homes will become more common.","智能家居将变得更常见。"),
        w("solution","/səˈluːʃn/","n.","解决方案","We need to find a solution to pollution.","我们需要找到污染问题的解决方案。"),
    ],
    "expert": [
        w("innovation","/ˌɪnəˈveɪʃn/","n.","创新","Innovation drives progress.","创新推动进步。"),
        w("sustainable","/səˈsteɪnəbl/","adj.","可持续的","We need sustainable development.","我们需要可持续发展。"),
        w("optimistic","/ˌɒptɪˈmɪstɪk/","adj.","乐观的","I am optimistic about the future.","我对未来很乐观。"),
        w("scenario","/sɪˈnɑːriəʊ/","n.","设想；场景","Let's imagine a future scenario.","让我们想象一个未来的场景。"),
        w("breakthrough","/ˈbreɪkθruː/","n.","突破","This is a major breakthrough in science.","这是科学上的重大突破。"),
    ],
}

U["u08_8"] = {
    "master": [
        w("express","/ɪkˈspres/","v.","表达","Learn to express your feelings.","学会表达你的感受。"),
        w("opinion","/əˈpɪnjən/","n.","意见；看法","What is your opinion on this?","你对这个有什么看法？"),
        w("disagree","/ˌdɪsəˈɡriː/","v.","不同意","It's okay to disagree politely.","礼貌地表达不同意是可以的。"),
        w("conversation","/ˌkɒnvəˈseɪʃn/","n.","对话","Practice English conversations with friends.","和朋友练习英语对话。"),
        w("discussion","/dɪˈskʌʃn/","n.","讨论","We had a lively discussion in class.","我们在课堂上进行了热烈的讨论。"),
        w("conflict","/ˈkɒnflɪkt/","n.","冲突","Try to avoid conflicts with others.","尽量避免与他人的冲突。"),
        w("resolve","/rɪˈzɒlv/","v.","解决","We can resolve problems by talking.","我们可以通过对话解决问题。"),
        w("compromise","/ˈkɒmprəmaɪz/","n.","妥协","Sometimes compromise is necessary.","有时妥协是必要的。"),
    ],
    "expert": [
        w("negotiate","/nɪˈɡəʊʃieɪt/","v.","谈判；协商","We need to negotiate a fair solution.","我们需要协商出一个公平的解决方案。"),
        w("empathy","/ˈempəθi/","n.","共情；同理心","Show empathy when others are sad.","当别人难过时表现出同理心。"),
        w("articulate","/ɑːrˈtɪkjuleɪt/","v.","清晰地表达","Learn to articulate your thoughts.","学会清晰地表达你的想法。"),
        w("persuade","/pərˈsweɪd/","v.","说服","Can you persuade him to join us?","你能说服他加入我们吗？"),
        w("diplomatic","/ˌdɪpləˈmætɪk/","adj.","有外交手腕的；委婉的","A diplomatic reply can avoid arguments.","委婉的回复可以避免争论。"),
    ],
}

# ====================== ENGLISH 8 下册 ======================

U["b2u01_8"] = {
    "master": [
        w("hiking","/ˈhaɪkɪŋ/","n.","徒步旅行","We went hiking in the mountains.","我们去山里徒步旅行了。"),
        w("painting","/ˈpeɪntɪŋ/","n.","绘画；画画","I enjoy painting in my free time.","我喜欢在空闲时画画。"),
        w("gardening","/ˈɡɑːrdnɪŋ/","n.","园艺","My grandmother loves gardening.","我奶奶喜欢园艺。"),
        w("photography","/fəˈtɒɡrəfi/","n.","摄影","Photography is an interesting hobby.","摄影是一个有趣的爱好。"),
        w("leisure","/ˈleʒər/","n.","闲暇；休闲","I read books for leisure.","我读书休闲。"),
        w("pastime","/ˈpɑːstaɪm/","n.","消遣；娱乐","Reading is my favorite pastime.","阅读是我最喜欢的消遣。"),
        w("creative","/kriˈeɪtɪv/","adj.","有创造力的","I want to do something creative.","我想做些有创意的事情。"),
        w("relaxation","/ˌriːlækˈseɪʃn/","n.","放松；消遣","Listening to music is a good form of relaxation.","听音乐是一种很好的放松方式。"),
    ],
    "expert": [
        w("recreational","/ˌrekrɪˈeɪʃənl/","adj.","娱乐的；消遣的","We have many recreational activities at school.","我们学校有很多娱乐活动。"),
        w("meditation","/ˌmedɪˈteɪʃn/","n.","冥想","Meditation helps me relax.","冥想帮助我放松。"),
        w("calligraphy","/kəˈlɪɡrəfi/","n.","书法","I practice Chinese calligraphy every weekend.","我每周末练习中国书法。"),
        w("orienteering","/ˌɔːriənˈtɪərɪŋ/","n.","定向越野","Orienteering is fun and challenging.","定向越野有趣又有挑战性。"),
        w("craftsmanship","/ˈkræftsmənʃɪp/","n.","工艺；手艺","I admire the craftsmanship of old buildings.","我欣赏古老建筑的工艺。"),
    ],
}

# ====================== ENGLISH 8 下册 (continued) ======================

U["b2u02_8"] = {
    "master": [
        w("hygiene","/ˈhaɪdʒiːn/","n.","卫生","Good hygiene keeps us healthy.","良好的卫生让我们保持健康。"),
        w("immunity","/ɪˈmjuːnəti/","n.","免疫力","Exercise boosts your immunity.","运动提高你的免疫力。"),
        w("check-up","/ˈtʃek ʌp/","n.","体检","I have a check-up once a year.","我每年做一次体检。"),
        w("moderate","/ˈmɒdərət/","adj.","适度的","Moderate exercise is good for health.","适度的运动对健康有益。"),
        w("nutrition","/njuˈtrɪʃn/","n.","营养","Good nutrition is important for growth.","良好的营养对成长很重要。"),
        w("recovery","/rɪˈkʌvəri/","n.","恢复","Get enough sleep for full recovery.","充足睡眠来完全恢复。"),
        w("treatment","/ˈtriːtmənt/","n.","治疗","He is receiving treatment at the hospital.","他正在医院接受治疗。"),
        w("prevention","/prɪˈvenʃn/","n.","预防","Prevention is better than cure.","预防胜于治疗。"),
    ],
    "expert": [
        w("well-being","/ˌwel ˈbiːɪŋ/","n.","健康；幸福","Mental well-being is just as important.","心理健康同样重要。"),
        w("immune","/ɪˈmjuːn/","adj.","免疫的","A strong immune system fights diseases.","强大的免疫系统抗击疾病。"),
        w("therapy","/ˈθerəpi/","n.","疗法","Rest is the best therapy for illness.","休息是生病最好的疗法。"),
        w("lifestyle","/ˈlaɪfstaɪl/","n.","生活方式","A healthy lifestyle includes exercise and good diet.","健康的生活方式包括运动和良好的饮食。"),
        w("epidemic","/ˌepɪˈdemɪk/","n.","流行病","The government took action to stop the epidemic.","政府采取措施阻止流行病。"),
    ],
}

U["b2u03_8"] = {
    "master": [
        w("adolescent","/ˌædəˈlesnt/","n.","青少年","Adolescents experience many changes.","青少年经历很多变化。"),
        w("mature","/məˈtʃʊər/","adj.","成熟的","She is mature for her age.","她比同龄人成熟。"),
        w("independent","/ˌɪndɪˈpendənt/","adj.","独立的","I want to be more independent.","我想更独立。"),
        w("curious","/ˈkjʊəriəs/","adj.","好奇的","Teenagers are curious about the world.","青少年对世界充满好奇。"),
        w("reflect","/rɪˈflekt/","v.","反思；思考","Take time to reflect on your growth.","花时间反思你的成长。"),
        w("progress","/ˈprəʊɡres/","v.","进步；进展","You have progressed a lot this year.","你今年进步了很多。"),
        w("milestone","/ˈmaɪlstəʊn/","n.","里程碑","Turning 14 is a milestone for me.","满14岁对我来说是一个里程碑。"),
        w("self-esteem","/ˌself ɪˈstiːm/","n.","自尊","Building self-esteem is important.","建立自尊很重要。"),
    ],
    "expert": [
        w("transition","/trænˈzɪʃn/","n.","过渡；转变","The transition to high school can be challenging.","过渡到高中可能很有挑战。"),
        w("identity","/aɪˈdentəti/","n.","身份；认同","Teenagers often search for their identity.","青少年常常寻找自我认同。"),
        w("resilience","/rɪˈzɪliəns/","n.","韧性；适应力","Resilience helps us face difficulties.","韧性帮助我们面对困难。"),
        w("empathy","/ˈempəθi/","n.","共情；同理心","Show empathy towards others.","对别人表现出同理心。"),
        w("adolescence","/ˌædəˈlesns/","n.","青春期","Adolescence is a time of change.","青春期是一个变化的时期。"),
    ],
}

U["b2u04_8"] = {
    "master": [
        w("canyon","/ˈkænjən/","n.","峡谷","The Grand Canyon is very deep.","大峡谷非常深。"),
        w("waterfall","/ˈwɔːtəfɔːl/","n.","瀑布","The waterfall is 50 meters high.","瀑布有50米高。"),
        w("volcano","/vɒlˈkeɪnəʊ/","n.","火山","The volcano erupted last year.","这座火山去年喷发了。"),
        w("reef","/riːf/","n.","礁石","The Great Barrier Reef is amazing.","大堡礁非常壮观。"),
        w("magnificent","/mæɡˈnɪfɪsnt/","adj.","壮丽的","The view from the top was magnificent.","从山顶看到的景色壮丽无比。"),
        w("breathtaking","/ˈbreθteɪkɪŋ/","adj.","令人惊叹的","The sunset was breathtaking.","日落令人惊叹。"),
        w("spectacular","/spekˈtækjələr/","adj.","壮观的","We saw a spectacular view of the mountains.","我们看到了壮观的群山景色。"),
        w("unique","/juˈniːk/","adj.","独特的","Every natural wonder is unique.","每个自然奇观都是独一无二的。"),
    ],
    "expert": [
        w("geological","/ˌdʒiːəˈlɒdʒɪkl/","adj.","地质的","The canyon has a long geological history.","这个峡谷有着悠久的地质历史。"),
        w("erosion","/ɪˈrəʊʒn/","n.","侵蚀","The rocks were shaped by erosion.","这些岩石被侵蚀塑造而成。"),
        w("tectonic","/tekˈtɒnɪk/","adj.","地壳构造的","Tectonic activity created these mountains.","地壳构造活动创造了这些山脉。"),
        w("heritage","/ˈherɪtɪdʒ/","n.","遗产","These sites are part of our natural heritage.","这些地方是我们自然遗产的一部分。"),
        w("expedition","/ˌekspəˈdɪʃn/","n.","探险","They went on an expedition to the Arctic.","他们去北极探险了。"),
    ],
}

U["b2u05_8"] = {
    "master": [
        w("hurricane","/ˈhʌrɪkən/","n.","飓风","The hurricane destroyed many houses.","飓风摧毁了很多房屋。"),
        w("tornado","/tɔːrˈneɪdəʊ/","n.","龙卷风","A tornado can lift cars into the air.","龙卷风能把汽车卷到空中。"),
        w("earthquake","/ˈɜːrθkweɪk/","n.","地震","The ground shook during the earthquake.","地震时地面晃动。"),
        w("flood","/flʌd/","n.","洪水","Heavy rain caused floods in the area.","大雨导致了该地区洪水。"),
        w("disaster","/dɪˈzɑːstər/","n.","灾难","We should help people after a disaster.","灾难后我们应该帮助人们。"),
        w("rescue","/ˈreskjuː/","v.","营救","Firefighters rescued the family from the fire.","消防员从火中救出了这家人。"),
        w("emergency","/iˈmɜːrdʒənsi/","n.","紧急情况","In an emergency, call 110.","紧急情况下打110。"),
        w("shelter","/ˈʃeltər/","n.","避难所","People took shelter from the storm.","人们在暴风雨中避难。"),
    ],
    "expert": [
        w("evacuate","/ɪˈvækjueɪt/","v.","疏散","The village was evacuated before the flood.","洪水前村庄被疏散了。"),
        w("catastrophe","/kəˈtæstrəfi/","n.","大灾难","The earthquake was a terrible catastrophe.","地震是一场可怕的灾难。"),
        w("aftermath","/ˈɑːftərmæθ/","n.","后果；灾后","The aftermath of the storm was devastating.","暴风雨的后果是毁灭性的。"),
        w("relief","/rɪˈliːf/","n.","救援；救济","Relief teams arrived quickly.","救援队迅速到达。"),
        w("devastating","/ˈdevəsteɪtɪŋ/","adj.","毁灭性的","The typhoon had devastating effects.","台风造成了毁灭性的影响。"),
    ],
}

U["b2u06_8"] = {
    "master": [
        w("cross-cultural","/krɒs ˈkʌltʃərəl/","adj.","跨文化的","Cross-cultural communication is important.","跨文化交流很重要。"),
        w("custom","/ˈkʌstəm/","n.","风俗习惯","Every country has its own customs.","每个国家都有自己的风俗习惯。"),
        w("etiquette","/ˈetɪket/","n.","礼仪","Table etiquette varies around the world.","餐桌礼仪世界各地不同。"),
        w("value","/ˈvæljuː/","n.","价值观","Family values are important in many cultures.","家庭价值观在许多文化中很重要。"),
        w("belief","/bɪˈliːf/","n.","信仰；信念","We should respect different beliefs.","我们应该尊重不同的信仰。"),
        w("heritage","/ˈherɪtɪdʒ/","n.","遗产","The Great Wall is part of our cultural heritage.","长城是我们文化遗产的一部分。"),
        w("diversity","/daɪˈvɜːrsəti/","n.","多样性","Cultural diversity makes the world interesting.","文化多样性让世界有趣。"),
        w("global","/ˈɡləʊbl/","adj.","全球的","We live in a global village.","我们生活在一个地球村。"),
    ],
    "expert": [
        w("multicultural","/ˌmʌltiˈkʌltʃərəl/","adj.","多元文化的","We live in a multicultural society.","我们生活在一个多元文化的社会。"),
        w("stereotype","/ˈsteriətaɪp/","n.","刻板印象","Try not to judge based on stereotypes.","尽量不要基于刻板印象做判断。"),
        w("tolerance","/ˈtɒlərəns/","n.","宽容","Tolerance is important in a diverse world.","宽容在一个多元的世界很重要。"),
        w("assimilation","/əˌsɪməˈleɪʃn/","n.","同化；融入","Assimilation into a new culture takes time.","融入新文化需要时间。"),
        w("perspective","/pərˈspektɪv/","n.","视角；观点","Learning about other cultures gives us a new perspective.","了解其他文化给我们新的视角。"),
    ],
}

U["b2u07_8"] = {
    "master": [
        w("fiction","/ˈfɪkʃn/","n.","小说","I enjoy reading science fiction.","我喜欢读科幻小说。"),
        w("mystery","/ˈmɪstri/","n.","悬疑；神秘","I love reading mystery novels.","我喜欢读悬疑小说。"),
        w("fantasy","/ˈfæntəsi/","n.","奇幻","Harry Potter is a famous fantasy series.","《哈利·波特》是著名的奇幻系列。"),
        w("biography","/baɪˈɒɡrəfi/","n.","传记","I read a biography of Albert Einstein.","我读了阿尔伯特·爱因斯坦的传记。"),
        w("chapter","/ˈtʃæptər/","n.","章节","This book has twelve chapters.","这本书有十二章。"),
        w("poetry","/ˈpəʊətri/","n.","诗歌","She writes poetry in her free time.","她在空闲时写诗。"),
        w("publish","/ˈpʌblɪʃ/","v.","出版","The writer published his first novel at 25.","这位作家在25岁时出版了他的第一部小说。"),
        w("bestseller","/ˌbestˈselər/","n.","畅销书","This novel became a bestseller.","这本小说成了畅销书。"),
    ],
    "expert": [
        w("genre","/ˈʒɒnrə/","n.","类型；体裁","What genre of books do you prefer?","你更喜欢哪种类型的书？"),
        w("narrative","/ˈnærətɪv/","n.","叙述；故事","The narrative of this novel is very engaging.","这本小说的叙述非常吸引人。"),
        w("literature","/ˈlɪtrətʃər/","n.","文学","We study classic literature in English class.","我们在英语课上学习经典文学。"),
        w("symbolism","/ˈsɪmbəlɪzəm/","n.","象征主义","The author uses symbolism to express ideas.","作者使用象征主义来表达思想。"),
        w("manuscript","/ˈmænjuskrɪpt/","n.","手稿；原稿","The writer's manuscript was found after his death.","作家的手稿在他去世后被发现了。"),
    ],
}

U["b2u08_8"] = {
    "master": [
        w("donate","/dəʊˈneɪt/","v.","捐赠","We donate clothes to people in need.","我们向需要的人捐赠衣物。"),
        w("charity","/ˈtʃærəti/","n.","慈善机构","The charity helps homeless people.","这家慈善机构帮助无家可归的人。"),
        w("volunteer","/ˌvɒlənˈtɪər/","n.","志愿者","I work as a volunteer at the old people's home.","我在养老院做志愿者。"),
        w("campaign","/kæmˈpeɪn/","n.","运动；活动","We started a campaign to clean up the park.","我们发起了清理公园的活动。"),
        w("sponsor","/ˈspɒnsər/","v.","赞助","Local businesses sponsored our event.","当地企业赞助了我们的活动。"),
        w("impact","/ˈɪmpækt/","n.","影响","Small actions can have a big impact.","小行动可以有大影响。"),
        w("community","/kəˈmjuːnəti/","n.","社区","We should help our local community.","我们应该帮助本地社区。"),
        w("awareness","/əˈweərnəs/","n.","意识","We need to raise awareness about environmental issues.","我们需要提高对环境问题的意识。"),
    ],
    "expert": [
        w("philanthropy","/fɪˈlænθrəpi/","n.","慈善事业","Philanthropy can change the world.","慈善事业可以改变世界。"),
        w("advocate","/ˈædvəkeɪt/","v.","提倡；倡导","We advocate for equal rights for everyone.","我们倡导人人平等。"),
        w("grassroots","/ˈɡrɑːsruːts/","adj.","基层的","Grassroots movements can bring real change.","基层运动可以带来真正的改变。"),
        w("sustainable","/səˈsteɪnəbl/","adj.","可持续的","We need sustainable solutions to global problems.","我们需要可持续的全球问题解决方案。"),
        w("initiative","/ɪˈnɪʃətɪv/","n.","倡议；主动行动","She started a community recycling initiative.","她发起了一个社区回收倡议。"),
    ],
}

# ====================== ENGLISH 9 上册 ======================

U["u01_9"] = {
    "master": [
        w("transform","/trænsˈfɔːrm/","v.","转变；改变","Technology has transformed our lives.","技术改变了我们的生活。"),
        w("decade","/ˈdekeɪd/","n.","十年","Great changes happened in the past decade.","过去十年发生了巨大变化。"),
        w("urbanization","/ˌɜːrbənaɪˈzeɪʃn/","n.","城市化","Urbanization has changed many small towns.","城市化改变了许多小镇。"),
        w("globalization","/ˌɡləʊbəlaɪˈzeɪʃn/","n.","全球化","Globalization connects people around the world.","全球化把世界各地的人们联系起来。"),
        w("trend","/trend/","n.","趋势；潮流","This is a growing trend in education.","这是教育发展的一个趋势。"),
        w("welfare","/ˈwelfeər/","n.","福利","The government improved social welfare.","政府改善了社会福利。"),
        w("inequality","/ˌɪnɪˈkwɒləti/","n.","不平等","We should work to reduce inequality.","我们应该努力减少不平等。"),
        w("prosperity","/prɒˈsperəti/","n.","繁荣；兴旺","The country has enjoyed years of prosperity.","这个国家享受了多年的繁荣。"),
    ],
    "expert": [
        w("paradigm","/ˈpærədaɪm/","n.","范式；模式","The internet created a new communication paradigm.","互联网创造了新的沟通范式。"),
        w("demographic","/ˌdeməˈɡræfɪk/","adj.","人口的","Demographic changes affect the economy.","人口变化影响经济。"),
        w("infrastructure","/ˈɪnfrəstrʌktʃər/","n.","基础设施","The city has modern infrastructure.","这座城市拥有现代化的基础设施。"),
        w("metropolitan","/ˌmetrəˈpɒlɪtən/","adj.","大都市的","Metropolitan areas attract many young people.","大都市地区吸引了很多年轻人。"),
        w("innovation","/ˌɪnəˈveɪʃn/","n.","创新","Technological innovation drives economic growth.","技术创新推动经济增长。"),
    ],
}

U["u02_9"] = {
    "master": [
        w("admire","/ədˈmaɪər/","v.","钦佩；赞赏","I admire people who help others.","我钦佩帮助他人的人。"),
        w("achievement","/əˈtʃiːvmənt/","n.","成就","Her achievements inspired many young people.","她的成就激励了很多年轻人。"),
        w("dedicate","/ˈdedɪkeɪt/","v.","奉献","She dedicated her life to science.","她将一生奉献给了科学。"),
        w("pioneer","/ˌpaɪəˈnɪər/","n.","先驱；先锋","Marie Curie was a pioneer in physics.","居里夫人是物理学领域的先驱。"),
        w("courage","/ˈkʌrɪdʒ/","n.","勇气","It takes courage to follow your dreams.","追随梦想需要勇气。"),
        w("perseverance","/ˌpɜːrsɪˈvɪərəns/","n.","毅力","Success requires hard work and perseverance.","成功需要努力和毅力。"),
        w("legacy","/ˈleɡəsi/","n.","遗产；遗赠","Her legacy continues to inspire people.","她的遗产继续激励着人们。"),
        w("contribution","/ˌkɒntrɪˈbjuːʃn/","n.","贡献","He made great contributions to medicine.","他对医学做出了巨大贡献。"),
    ],
    "expert": [
        w("admiration","/ˌædməˈreɪʃn/","n.","钦佩；赞赏","I have great admiration for her work.","我非常钦佩她的工作。"),
        w("selfless","/ˈselfləs/","adj.","无私的","Her selfless dedication touched everyone.","她的无私奉献感动了每个人。"),
        w("humanitarian","/hjuːˌmænɪˈteəriən/","adj.","人道主义的","She received an award for her humanitarian work.","她因人道主义工作获奖。"),
        w("inspirational","/ˌɪnspəˈreɪʃənl/","adj.","鼓舞人心的","His story is truly inspirational.","他的故事真的很鼓舞人心。"),
        w("iconic","/aɪˈkɒnɪk/","adj.","标志性的；偶像级的","She became an iconic figure in history.","她成为历史上的标志性人物。"),
    ],
}

U["u03_9"] = {
    "master": [
        w("strategy","/ˈstrætədʒi/","n.","策略；方法","Good study strategies help you learn better.","好的学习策略帮助你学得更好。"),
        w("memorize","/ˈmeməraɪz/","v.","记住；背诵","Don't just memorize facts; try to understand them.","不要只背事实，要试着理解。"),
        w("concentrate","/ˈkɒnsntreɪt/","v.","集中注意力","I need to concentrate on my studies.","我需要集中精力学习。"),
        w("distraction","/dɪˈstrækʃn/","n.","分心的事物","Turn off your phone to avoid distractions.","关掉手机避免分心。"),
        w("curiosity","/ˌkjʊəriˈɒsəti/","n.","好奇心","Curiosity drives us to learn new things.","好奇心驱使我们学习新东西。"),
        w("review","/rɪˈvjuː/","v.","复习","Review your notes after class.","课后复习你的笔记。"),
        w("summarize","/ˈsʌməraɪz/","v.","总结","Summarize the main points of the lesson.","总结本课要点。"),
        w("reflect","/rɪˈflekt/","v.","反思","Reflect on what you have learned.","反思你学到了什么。"),
    ],
    "expert": [
        w("metacognition","/ˌmetəkɒɡˈnɪʃn/","n.","元认知","Metacognition helps you think about your own thinking.","元认知帮助你思考自己的思维过程。"),
        w("retention","/rɪˈtenʃn/","n.","记忆；保持","Spaced repetition improves memory retention.","间隔重复提高记忆保持率。"),
        w("cognitive","/ˈkɒɡnətɪv/","adj.","认知的","Regular reading improves cognitive abilities.","定期阅读提高认知能力。"),
        w("critical thinking","/ˈkrɪtɪkl ˈθɪŋkɪŋ/","n.","批判性思维","Critical thinking helps you analyze information.","批判性思维帮助你分析信息。"),
        w("self-discipline","/ˌself ˈdɪsəplɪn/","n.","自律","Self-discipline is the key to effective learning.","自律是高效学习的关键。"),
    ],
}

U["u04_9"] = {
    "master": [
        w("recall","/rɪˈkɔːl/","v.","回忆；回想","I can still recall my first day at school.","我仍然能回忆起第一天上学的情景。"),
        w("remind","/rɪˈmaɪnd/","v.","提醒","This photo reminds me of my childhood.","这张照片让我想起我的童年。"),
        w("childhood","/ˈtʃaɪldhʊd/","n.","童年","I have happy memories of my childhood.","我对童年有快乐的回忆。"),
        w("precious","/ˈpreʃəs/","adj.","珍贵的","These memories are precious to me.","这些记忆对我来说很珍贵。"),
        w("cherish","/ˈtʃerɪʃ/","v.","珍惜","Cherish every moment with your family.","珍惜与家人在一起的每一刻。"),
        w("nostalgic","/nɒˈstældʒɪk/","adj.","怀旧的","Looking at old photos makes me feel nostalgic.","看老照片让我感到怀旧。"),
        w("anniversary","/ˌænɪˈvɜːrsəri/","n.","周年纪念日","Today is my parents' wedding anniversary.","今天是我父母的结婚纪念日。"),
        w("commemorate","/kəˈmeməreɪt/","v.","纪念","We hold a ceremony to commemorate the event.","我们举行仪式来纪念这个事件。"),
    ],
    "expert": [
        w("reminisce","/ˌremɪˈnɪs/","v.","回忆；追忆","Grandparents love to reminisce about the past.","祖父母喜欢回忆过去。"),
        w("sentimental","/ˌsentɪˈmentl/","adj.","情感的；多愁善感的","This song makes me feel sentimental.","这首歌让我感到伤感。"),
        w("permanent","/ˈpɜːrmənənt/","adj.","永久的","Some memories leave a permanent mark.","有些记忆留下永久的印记。"),
        w("evoke","/ɪˈvəʊk/","v.","唤起","The smell of the sea evokes happy memories.","大海的味道唤起快乐的回忆。"),
        w("legacy","/ˈleɡəsi/","n.","遗产；传承","Family stories are a legacy passed down through generations.","家庭故事是代代相传的遗产。"),
    ],
}

U["u05_9"] = {
    "master": [
        w("invent","/ɪnˈvent/","v.","发明","Edison invented the light bulb.","爱迪生发明了电灯泡。"),
        w("design","/dɪˈzaɪn/","v.","设计","Engineers design new machines.","工程师设计新机器。"),
        w("manufacture","/ˌmænjuˈfæktʃər/","v.","制造","This factory manufactures car parts.","这家工厂制造汽车零件。"),
        w("patent","/ˈpeɪtnt/","n.","专利","The inventor applied for a patent.","发明者申请了专利。"),
        w("prototype","/ˈprəʊtətaɪp/","n.","原型","They built a prototype of the new device.","他们制作了新设备的原型。"),
        w("solve","/sɒlv/","v.","解决","We need to solve this problem.","我们需要解决这个问题。"),
        w("problem","/ˈprɒbləm/","n.","问题","Every invention solves a problem.","每一个发明都解决一个问题。"),
        w("creative","/kriˈeɪtɪv/","adj.","有创造力的","Creative thinking leads to new inventions.","创造性思维带来新发明。"),
    ],
    "expert": [
        w("innovation","/ˌɪnəˈveɪʃn/","n.","创新；革新","Innovation drives progress in society.","创新推动社会进步。"),
        w("revolutionize","/ˌrevəˈluːʃənaɪz/","v.","彻底改变","The internet revolutionized communication.","互联网彻底改变了通信。"),
        w("breakthrough","/ˈbreɪkθruː/","n.","突破","This breakthrough will change medicine.","这个突破将改变医学。"),
        w("ingenuity","/ˌɪndʒəˈnjuːəti/","n.","独创性；巧思","Human ingenuity has no limits.","人类的创造力没有极限。"),
        w("cutting-edge","/ˌkʌtɪŋ ˈedʒ/","adj.","前沿的；尖端的","This lab uses cutting-edge technology.","这个实验室使用前沿技术。"),
    ],
}

U["u06_9"] = {
    "master": [
        w("exploration","/ˌekspləˈreɪʃn/","n.","探索","Space exploration requires courage.","太空探索需要勇气。"),
        w("astronaut","/ˈæstrənɔːt/","n.","宇航员","Astronauts train for years before space missions.","宇航员在太空任务前训练多年。"),
        w("telescope","/ˈtelɪskəʊp/","n.","望远镜","We can see stars through a telescope.","我们可以通过望远镜看星星。"),
        w("orbit","/ˈɔːrbɪt/","v.","绕轨道运行","The moon orbits the Earth.","月亮绕地球运行。"),
        w("gravity","/ˈɡrævəti/","n.","重力；引力","Astronauts float in space because of low gravity.","宇航员在太空中漂浮是因为低重力。"),
        w("atmosphere","/ˈætməsfɪər/","n.","大气层","The Earth's atmosphere protects us.","地球的大气层保护着我们。"),
        w("colony","/ˈkɒləni/","n.","殖民地；定居点","Scientists dream of building a colony on Mars.","科学家梦想在火星上建立定居点。"),
        w("frontier","/frʌnˈtɪər/","n.","前沿；边境","Space is the final frontier.","太空是最后的前沿。"),
    ],
    "expert": [
        w("cosmic","/ˈkɒzmɪk/","adj.","宇宙的","Cosmic radiation is a challenge for space travel.","宇宙辐射是太空旅行的挑战。"),
        w("interstellar","/ˌɪntərˈstelər/","adj.","星际的","Interstellar travel is still science fiction.","星际旅行仍然只是科幻。"),
        w("observatory","/əbˈzɜːrvətɔːri/","n.","天文台","The observatory has a powerful telescope.","天文台有一架强大的望远镜。"),
        w("extraterrestrial","/ˌekstrətəˈrestriəl/","adj./n.","外星(的)；地外生物","Scientists search for extraterrestrial life.","科学家寻找地外生命。"),
        w("propulsion","/prəˈpʌlʃn/","n.","推进力；推进系统","New propulsion technology could shorten space travel.","新的推进技术可以缩短太空旅行。"),
    ],
}

U["u07_9"] = {
    "master": [
        w("melody","/ˈmelədi/","n.","旋律","The melody of this song is beautiful.","这首歌的旋律很美。"),
        w("rhythm","/ˈrɪðəm/","n.","节奏","The rhythm of the drums makes me want to dance.","鼓的节奏让我想跳舞。"),
        w("genre","/ˈʒɒnrə/","n.","类型；流派","What genre of music do you like?","你喜欢什么类型的音乐？"),
        w("instrument","/ˈɪnstrəmənt/","n.","乐器","I can play three musical instruments.","我会演奏三种乐器。"),
        w("performance","/pərˈfɔːrməns/","n.","表演；演出","The performance was amazing.","表演非常精彩。"),
        w("audience","/ˈɔːdiəns/","n.","观众","The audience clapped loudly.","观众大声鼓掌。"),
        w("conductor","/kənˈdʌktər/","n.","指挥","The conductor led the orchestra beautifully.","指挥优美地带领着管弦乐队。"),
        w("compose","/kəmˈpəʊz/","v.","作曲","Mozart composed his first piece at age five.","莫扎特五岁时创作了他的第一首曲子。"),
    ],
    "expert": [
        w("symphony","/ˈsɪmfəni/","n.","交响乐","Beethoven's symphonies are world-famous.","贝多芬的交响乐世界闻名。"),
        w("improvisation","/ˌɪmprəvaɪˈzeɪʃn/","n.","即兴创作","Jazz musicians are known for improvisation.","爵士音乐家以即兴创作闻名。"),
        w("harmony","/ˈhɑːrməni/","n.","和声；和谐","The choir sang in perfect harmony.","合唱团唱出了完美的和声。"),
        w("virtuoso","/ˌvɜːrtʃuˈəʊsəʊ/","n.","大师；演奏家","The pianist is a true virtuoso.","这位钢琴家是真正的大师。"),
        w("orchestra","/ˈɔːrkɪstrə/","n.","管弦乐队","The orchestra performed a classic piece.","管弦乐队演奏了一首经典曲目。"),
    ],
}

U["u08_9"] = {
    "master": [
        w("champion","/ˈtʃæmpiən/","n.","冠军","He became the champion after years of training.","经过多年训练他成为了冠军。"),
        w("victory","/ˈvɪktəri/","n.","胜利","The team celebrated their victory.","团队庆祝他们的胜利。"),
        w("defeat","/dɪˈfiːt/","v.","击败","They defeated the opposing team 3-0.","他们以3比0击败了对手。"),
        w("opponent","/əˈpəʊnənt/","n.","对手","Respect your opponent whether you win or lose.","无论输赢都要尊重你的对手。"),
        w("tournament","/ˈtʊərnəmənt/","n.","锦标赛","The school held a basketball tournament.","学校举办了一场篮球锦标赛。"),
        w("referee","/ˌrefəˈriː/","n.","裁判","The referee made a fair decision.","裁判做出了公平的判决。"),
        w("sportsmanship","/ˈspɔːrtsmənʃɪp/","n.","体育精神","Good sportsmanship is more important than winning.","良好的体育精神比赢更重要。"),
        w("medal","/ˈmedl/","n.","奖牌","She won a gold medal in swimming.","她在游泳比赛中获得了金牌。"),
    ],
    "expert": [
        w("perseverance","/ˌpɜːrsɪˈvɪərəns/","n.","毅力；坚持","The athlete's perseverance led to success.","运动员的坚持带来了成功。"),
        w("discipline","/ˈdɪsəplɪn/","n.","纪律；训练","Professional athletes need strict discipline.","职业运动员需要严格的纪律。"),
        w("dedication","/ˌdedɪˈkeɪʃn/","n.","奉献；投入","Her dedication to training was incredible.","她对训练的投入令人难以置信。"),
        w("underdog","/ˈʌndərdɒɡ/","n.","不被看好的一方","The underdog team won the championship.","不被看好的队伍赢得了冠军。"),
        w("mentor","/ˈmentɔːr/","n.","导师；指导者","The coach was a great mentor to the young players.","教练是年轻球员的良师益友。"),
    ],
}

# ====================== ENGLISH 9 下册 ======================

U["b2u01_9"] = {
    "master": [
        w("lunar","/ˈluːnər/","adj.","月球的；阴历的","The Spring Festival follows the lunar calendar.","春节遵循农历。"),
        w("reunion","/riːˈjuːniən/","n.","团圆；重聚","Family reunion is important during the Spring Festival.","春节期间家庭团圆很重要。"),
        w("decorate","/ˈdekəreɪt/","v.","装饰","We decorate the house with red lanterns.","我们用红灯笼装饰房子。"),
        w("feast","/fiːst/","n.","盛宴；宴会","The Spring Festival feast is delicious.","春节盛宴很美味。"),
        w("blessing","/ˈblesɪŋ/","n.","祝福；福气","Elders give blessings to children during the festival.","节日期间长辈给孩子们祝福。"),
        w("ancestor","/ˈænsestər/","n.","祖先","We honor our ancestors during festivals.","我们在节日期间祭祖。"),
        w("symbolize","/ˈsɪmbəlaɪz/","v.","象征","Red symbolizes good luck in Chinese culture.","红色在中国文化中象征好运。"),
        w("gratitude","/ˈɡrætɪtjuːd/","n.","感恩；感激","We express gratitude for what we have.","我们感恩所拥有的一切。"),
    ],
    "expert": [
        w("commemorate","/kəˈmeməreɪt/","v.","纪念","This festival commemorates an important historical event.","这个节日纪念一个重要历史事件。"),
        w("customary","/ˈkʌstəməri/","adj.","习俗的；惯例的","It is customary to give red packets during the Spring Festival.","春节给红包是习俗。"),
        w("festive","/ˈfestɪv/","adj.","节日的；喜庆的","The streets are decorated in a festive atmosphere.","街道装饰着节日气氛。"),
        w("observe","/əbˈzɜːrv/","v.","庆祝；遵守","People observe the festival in different ways.","人们以不同方式庆祝这个节日。"),
        w("cultural heritage","/ˈkʌltʃərəl ˈherɪtɪdʒ/","n.","文化遗产","Festivals are an important part of cultural heritage.","节日是文化遗产的重要组成部分。"),
    ],
}

U["b2u02_9"] = {
    "master": [
        w("ancient","/ˈeɪnʃənt/","adj.","古代的","China has a long ancient history.","中国有悠久的古代历史。"),
        w("civilization","/ˌsɪvəlaɪˈzeɪʃn/","n.","文明","The Yellow River is the birthplace of Chinese civilization.","黄河是中华文明的发源地。"),
        w("archaeologist","/ˌɑːrkiˈɒlədʒɪst/","n.","考古学家","Archaeologists discovered ancient tombs.","考古学家发现了古墓。"),
        w("artifact","/ˈɑːrtɪfækt/","n.","手工艺品；文物","These artifacts are over 2,000 years old.","这些文物已有两千多年历史。"),
        w("dynasty","/ˈdɪnəsti/","n.","王朝；朝代","The Tang Dynasty was a golden age of Chinese poetry.","唐朝是中国诗歌的黄金时代。"),
        w("relic","/ˈrelɪk/","n.","遗迹；遗物","The museum displays many historical relics.","博物馆展示了许多历史遗迹。"),
        w("ruin","/ˈruːɪn/","n.","废墟","We visited the ruins of an ancient city.","我们参观了一座古城的废墟。"),
        w("treasure","/ˈtreʒər/","n.","宝藏","The tomb was full of treasures.","墓穴里满是宝藏。"),
    ],
    "expert": [
        w("excavation","/ˌekskəˈveɪʃn/","n.","挖掘；发掘","The excavation revealed a hidden palace.","挖掘发现了一座隐藏的宫殿。"),
        w("archaeology","/ˌɑːrkiˈɒlədʒi/","n.","考古学","Archaeology helps us understand the past.","考古学帮助我们了解过去。"),
        w("preservation","/ˌprezərˈveɪʃn/","n.","保存；保护","The preservation of historical sites is important.","历史遗迹的保护很重要。"),
        w("remains","/rɪˈmeɪnz/","n.","遗迹；遗骸","Archaeologists found the remains of an ancient temple.","考古学家发现了一座古庙的遗迹。"),
        w("hieroglyph","/ˈhaɪərəɡlɪf/","n.","象形文字","Ancient Egyptians used hieroglyphs to write.","古埃及人使用象形文字书写。"),
    ],
}

U["b2u03_9"] = {
    "master": [
        w("sculpture","/ˈskʌlptʃər/","n.","雕塑","The sculpture in the park is made of marble.","公园里的雕塑是大理石做的。"),
        w("masterpiece","/ˈmɑːstərpiːs/","n.","杰作","Mona Lisa is a masterpiece of art.","《蒙娜丽莎》是一件艺术杰作。"),
        w("gallery","/ˈɡæləri/","n.","画廊；美术馆","We visited an art gallery on Sunday.","我们周日参观了一个美术馆。"),
        w("abstract","/ˈæbstrækt/","adj.","抽象的","Abstract art can be hard to understand.","抽象艺术可能很难理解。"),
        w("realistic","/ˌriːəˈlɪstɪk/","adj.","现实主义的；逼真的","This painting is very realistic.","这幅画非常逼真。"),
        w("landscape","/ˈlændskeɪp/","n.","风景画","She paints beautiful landscapes.","她画美丽的风景画。"),
        w("portrait","/ˈpɔːrtrət/","n.","肖像画","The portrait of the queen is in the museum.","女王的肖像画在博物馆里。"),
        w("exhibition","/ˌeksɪˈbɪʃn/","n.","展览","The art exhibition attracted many visitors.","艺术展吸引了很多参观者。"),
    ],
    "expert": [
        w("aesthetic","/iːsˈθetɪk/","adj.","美学的；审美的","Everyone has their own aesthetic taste.","每个人都有自己的审美品味。"),
        w("perspective","/pərˈspektɪv/","n.","透视法；视角","The artist uses perspective to create depth.","艺术家使用透视法创造深度。"),
        w("impressionism","/ɪmˈpreʃənɪzəm/","n.","印象派","Impressionism focuses on light and color.","印象派注重光和色彩。"),
        w("Renaissance","/rɪˈneɪsns/","n.","文艺复兴","The Renaissance was a golden age of art.","文艺复兴是艺术的黄金时代。"),
        w("composition","/ˌkɒmpəˈzɪʃn/","n.","构图；作品","The composition of this painting is balanced.","这幅画的构图很平衡。"),
    ],
}

U["b2u04_9"] = {
    "master": [
        w("waste","/weɪst/","n.","垃圾；浪费","We should reduce household waste.","我们应该减少家庭垃圾。"),
        w("plastic","/ˈplæstɪk/","n.","塑料","Plastic pollution is a serious problem.","塑料污染是一个严重的问题。"),
        w("recycle","/ˌriːˈsaɪkl/","v.","回收利用","Remember to recycle paper and glass.","记得回收纸张和玻璃。"),
        w("compost","/ˈkɒmpɒst/","v.","堆肥","We compost food scraps in the garden.","我们在花园里把食物残渣做堆肥。"),
        w("landfill","/ˈlændfɪl/","n.","垃圾填埋场","Much of our trash ends up in landfills.","我们的很多垃圾最终进了填埋场。"),
        w("pollution","/pəˈluːʃn/","n.","污染","Air pollution is harmful to our health.","空气污染对我们的健康有害。"),
        w("resource","/rɪˈsɔːrs/","n.","资源","We must use natural resources wisely.","我们必须明智地使用自然资源。"),
        w("sustainable","/səˈsteɪnəbl/","adj.","可持续的","We need a sustainable future for our planet.","我们需要一个可持续的未来。"),
    ],
    "expert": [
        w("carbon footprint","/ˈkɑːrbən ˈfʊtprɪnt/","n.","碳足迹","We should reduce our carbon footprint.","我们应该减少碳足迹。"),
        w("biodegradable","/ˌbaɪəʊdɪˈɡreɪdəbl/","adj.","可生物降解的","Use biodegradable bags instead of plastic ones.","使用可生物降解的袋子代替塑料袋。"),
        w("conservation","/ˌkɒnsərˈveɪʃn/","n.","节约；保护","Energy conservation helps protect the environment.","节约能源有助于保护环境。"),
        w("emission","/ɪˈmɪʃn/","n.","排放","The government is reducing carbon emissions.","政府正在减少碳排放。"),
        w("eco-friendly","/ˌiːkəʊ ˈfrendli/","adj.","环保的","Choose eco-friendly products when possible.","尽量选择环保产品。"),
    ],
}

U["b2u05_9"] = {
    "master": [
        w("graduation","/ˌɡrædʒuˈeɪʃn/","n.","毕业","Graduation is both exciting and sad.","毕业既兴奋又伤感。"),
        w("farewell","/ˌfeərˈwel/","n.","告别","We said a tearful farewell to our teachers.","我们含泪告别了老师们。"),
        w("journey","/ˈdʒɜːrni/","n.","旅程","Life is a long journey of learning.","人生是一场漫长的学习旅程。"),
        w("growth","/ɡrəʊθ/","n.","成长","I have seen great growth in the past three years.","过去三年我看到了巨大的成长。"),
        w("memorable","/ˈmemərəbl/","adj.","难忘的","My middle school years were truly memorable.","我的中学时光真的令人难忘。"),
        w("promising","/ˈprɒmɪsɪŋ/","adj.","有前途的","The future looks promising for our generation.","未来对我们这一代来说充满希望。"),
        w("opportunity","/ˌɒpəˈtjuːnəti/","n.","机会","High school will bring new opportunities.","高中将带来新的机会。"),
        w("determination","/dɪˌtɜːrmɪˈneɪʃn/","n.","决心","Face the future with courage and determination.","带着勇气和决心面对未来。"),
    ],
    "expert": [
        w("commencement","/kəˈmensmənt/","n.","毕业典礼；开始","The commencement ceremony was held in the auditorium.","毕业典礼在大礼堂举行。"),
        w("nostalgia","/nɒˈstældʒə/","n.","怀旧；乡愁","Looking at yearbook photos fills me with nostalgia.","看年鉴照片让我充满怀旧之情。"),
        w("aspiration","/ˌæspəˈreɪʃn/","n.","抱负；志向","She has high aspirations for her future career.","她对未来的职业有很高的抱负。"),
        w("cherish","/ˈtʃerɪʃ/","v.","珍惜；珍视","I will always cherish the memories of my school days.","我会永远珍惜学生时代的记忆。"),
        w("commence","/kəˈmens/","v.","开始","A new chapter of life is about to commence.","人生的新篇章即将开始。"),
    ],
}

# ====================== GENERATE JSON ======================

OUT = "/Users/kim/Documents/workspace/claudecode/middle-school/scripts/vocab-bank.json"
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(U, f, ensure_ascii=False, indent=2)

total_units = len(U)
total_words = sum(len(v["master"]) + len(v["expert"]) for v in U.values())
print(f"✅ Generated {OUT}")
print(f"   Units: {total_units}")
print(f"   Total words: {total_words}")
print(f"   Master tier: {sum(len(v['master']) for v in U.values())}")
print(f"   Expert tier: {sum(len(v['expert']) for v in U.values())}")
print(f"   Per unit: 8 master + 5 expert = 13 words each")
print(f"   Keys: {sorted(U.keys())}")

