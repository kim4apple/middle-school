#!/usr/bin/env python3
"""Add 掌握 + 学霸 vocabulary tiers to all english8 and english9 unit pages.
   Run this after gen_vocab.py to regenerate appendix-vocab.html."""
import re, os

W = lambda w, ipa, pos, d, ex, tr: f'''      <div class="vocab-card">
        <span class="headword wotd-say" data-speak="{w}">{w}</span><span class="headword-speak-indicator">🔊</span>
        <span class="ipa">/{ipa}/</span><span class="pos">{pos}</span>
        <div class="definition">{d}</div>
        <div class="example"><span class="wotd-say" data-speak="{ex}">{ex}</span><span class="trans">{tr}</span></div>
      </div>'''

MOD = lambda icon, title, cards: f'<details class="module" open><summary>{icon} {title}</summary><div class="content"><div class="vocab-grid">\n{cards}\n    </div></div></details>'

# DATA: { (grade, unit): [(icon, title, [(w,ipa,pos,defn,ex,trans), ...]), ...] }
D = {}

def add(grade, unit, tier_icon, tier_title, *words):
    key = (str(grade), unit)
    if key not in D: D[key] = []
    D[key].append((tier_icon, tier_title, list(words)))

# ============================================================
# english8 上册
# ============================================================
add(8,'u01','🥈','掌握词汇 · 假期活动',
    ('attend','əˈtend','v.','参加','I will attend the summer camp.','我将参加夏令营。'),
    ('cancel','ˈkænsl','v.','取消','The flight was cancelled.','航班被取消了。'),
    ('arrange','əˈreɪndʒ','v.','安排','She arranged a family trip.','她安排了一次家庭旅行。'),
    ('depart','dɪˈpɑːrt','v.','出发','We departed early in the morning.','我们清晨出发了。'),
    ('transport','ˈtrænspɔːrt','n.','交通','Public transport is cheap.','公共交通很便宜。'),
    ('scenery','ˈsiːnəri','n.','风景','The scenery took my breath away.','风景美得让我屏息。'),
    ('souvenir','ˌsuːvəˈnɪr','n.','纪念品','I bought a souvenir for Mom.','我给妈妈买了纪念品。'),
    ('cultural','ˈkʌltʃərəl','adj.','文化的','We visited cultural sites.','我们参观了文化景点。'),
    ('local','ˈloʊkl','adj.','当地的','We ate at a local restaurant.','我们在当地餐馆吃饭。'),
    ('abroad','əˈbrɔːd','adv.','在国外','She studied abroad last year.','她去年出国学习了。'))
add(8,'u01','🥉','学霸词汇 · 冲刺满分',
    ('memorable','ˈmemərəbl','adj.','难忘的','It was a memorable journey.','这是一次难忘的旅程。'),
    ('magnificent','mæɡˈnɪfɪsnt','adj.','壮丽的','The mountain views were magnificent.','山景非常壮丽。'),
    ('extraordinary','ɪkˈstrɔːrdəneri','adj.','非凡的','We had an extraordinary experience.','我们有一次非凡的经历。'),
    ('unforgettable','ˌʌnfərˈɡetəbl','adj.','难忘的','The trip was unforgettable.','这次旅行令人难忘。'),
    ('delightful','dɪˈlaɪtfl','adj.','令人愉快的','We had a delightful time.','我们度过了愉快的时光。'),
    ('picturesque','ˌpɪktʃərˈesk','adj.','风景如画的','The village was picturesque.','村庄风景如画。'))

add(8,'u02','🥈','掌握词汇 · 生活习惯',
    ('habit','ˈhæbɪt','n.','习惯','Develop good habits early.','尽早养成好习惯。'),
    ('regular','ˈreɡjələr','adj.','有规律的','Regular exercise is important.','规律运动很重要。'),
    ('schedule','ˈskedʒuːl','n.','日程','I have a tight schedule.','我的日程很紧凑。'),
    ('amount','əˈmaʊnt','n.','数量','Limit the amount of sugar.','限制糖的摄入量。'),
    ('screen','skriːn','n.','屏幕','Reduce screen time before bed.','睡前减少看屏幕。'),
    ('average','ˈævərɪdʒ','adj./n.','平均','The average score is 85.','平均分是85。'),
    ('percent','pərˈsent','n.','百分比','80 percent of students exercise.','80%的学生运动。'),
    ('result','rɪˈzʌlt','n.','结果','The result was surprising.','结果令人吃惊。'),
    ('although','ɔːlˈðoʊ','conj.','虽然','Although it\'s hard, I keep trying.','虽然难，我仍坚持。'),
    ('dentist','ˈdentɪst','n.','牙医','I see the dentist twice a year.','我每年看两次牙医。'))
add(8,'u02','🥉','学霸词汇 · 冲刺满分',
    ('discipline','ˈdɪsəplɪn','n.','自律','Self-discipline leads to success.','自律带来成功。'),
    ('moderation','ˌmɒdəˈreɪʃn','n.','适度','Eat and drink in moderation.','饮食要适度。'),
    ('frequency','ˈfriːkwənsi','n.','频率','Frequency of exercise matters.','运动频率很重要。'),
    ('nutrition','njuˈtrɪʃn','n.','营养','Good nutrition boosts health.','好营养促进健康。'),
    ('sufficient','səˈfɪʃnt','adj.','充足的','Get sufficient sleep.','保证充足睡眠。'),
    ('well-being','ˌwel ˈbiːɪŋ','n.','健康；幸福','Exercise improves well-being.','运动提升幸福感。'))

add(8,'u03','🥈','掌握词汇 · 个人特质',
    ('outgoing','ˌaʊtˈɡoʊɪŋ','adj.','外向的','She is outgoing and friendly.','她外向又友好。'),
    ('honest','ˈɒnɪst','adj.','诚实的','An honest person earns trust.','诚实的人赢得信任。'),
    ('brave','breɪv','adj.','勇敢的','Be brave to face challenges.','勇敢面对挑战。'),
    ('modest','ˈmɒdɪst','adj.','谦虚的','Stay modest when you succeed.','成功时保持谦虚。'),
    ('patient','ˈpeɪʃnt','adj.','耐心的','Be patient with others.','对别人要有耐心。'),
    ('clever','ˈklevər','adj.','聪明的','He is clever at math.','他数学很聪明。'),
    ('helpful','ˈhelpfl','adj.','乐于助人的','My classmate is very helpful.','我同学很乐于助人。'),
    ('serious','ˈsɪriəs','adj.','认真的','She is serious about her goals.','她对目标很认真。'),
    ('necessary','ˈnesəseri','adj.','必要的','Friendship is necessary for life.','友谊是生活必需的。'),
    ('though','ðoʊ','conj.','虽然','Though young, he is wise.','虽然年轻，他很有智慧。'))
add(8,'u03','🥉','学霸词汇 · 冲刺满分',
    ('personality','ˌpɜːrsəˈnæləti','n.','个性','Everyone has a unique personality.','每个人都有独特个性。'),
    ('optimistic','ˌɒptɪˈmɪstɪk','adj.','乐观的','Stay optimistic in hard times.','困难时保持乐观。'),
    ('considerate','kənˈsɪdərət','adj.','体贴的','He is considerate of others.','他很体贴别人。'),
    ('diligent','ˈdɪlɪdʒənt','adj.','勤奋的','A diligent student will succeed.','勤奋的学生会成功。'),
    ('reliable','rɪˈlaɪəbl','adj.','可靠的','She is a reliable friend.','她是个可靠的朋友。'),
    ('adaptable','əˈdæptəbl','adj.','适应力强的','Kids are adaptable to change.','孩子适应变化的能力强。'))

add(8,'u04','🥈','掌握词汇 · 偏好比较',
    ('quality','ˈkwɒləti','n.','质量','Quality is more important than price.','质量比价格更重要。'),
    ('service','ˈsɜːrvɪs','n.','服务','The service was excellent.','服务非常好。'),
    ('comfortable','ˈkʌmftəbl','adj.','舒适的','This sofa is very comfortable.','这个沙发很舒适。'),
    ('reasonable','ˈriːznəbl','adj.','合理的；公道的','The price is reasonable.','价格很合理。'),
    ('compare','kəmˈpeər','v.','比较','Don\'t compare yourself to others.','别拿自己和别人比较。'),
    ('popular','ˈpɒpjələr','adj.','流行的','This restaurant is very popular.','这家餐馆很受欢迎。'),
    ('review','rɪˈvjuː','n./v.','评论；复习','Read online reviews before buying.','买之前看看评论。'),
    ('customer','ˈkʌstəmər','n.','顾客','The customer is always right.','顾客永远是对的。'),
    ('perform','pərˈfɔːrm','v.','表演；表现','The singer performed well.','歌手表现很好。'),
    ('choose','tʃuːz','v.','选择','You need to choose wisely.','你需要明智地选择。'))
add(8,'u04','🥉','学霸词汇 · 冲刺满分',
    ('preference','ˈprefrəns','n.','偏好；偏爱','Everyone has their own preference.','每个人都有自己的偏好。'),
    ('superior','suːˈpɪriər','adj.','更好的；优越的','This product is superior in quality.','这个产品质量更优。'),
    ('inferior','ɪnˈfɪriər','adj.','较差的','Don\'t buy inferior goods.','别买劣质商品。'),
    ('comparison','kəmˈpærɪsn','n.','比较；对比','In comparison, this one is better.','相比之下，这个更好。'),
    ('distinguish','dɪˈstɪŋɡwɪʃ','v.','区别；辨别','Learn to distinguish good from bad.','学会区分好与坏。'),
    ('advantage','ədˈvæntɪdʒ','n.','优势；优点','Every method has its advantage.','每种方法都有其优势。'))

add(8,'u05','🥈','掌握词汇 · 媒体偏好',
    ('channel','ˈtʃænl','n.','频道','Which channel is your favorite?','你最喜欢哪个频道？'),
    ('educational','ˌedʒuˈkeɪʃənl','adj.','教育的','Watching educational programs helps.','看教育节目有帮助。'),
    ('meaningless','ˈmiːnɪŋləs','adj.','无意义的','Some shows are meaningless.','有些节目毫无意义。'),
    ('entertaining','ˌentərˈteɪnɪŋ','adj.','有趣的；娱乐的','The movie was very entertaining.','电影很有趣。'),
    ('culture','ˈkʌltʃər','n.','文化','Learn about different cultures.','了解不同文化。'),
    ('influence','ˈɪnfluəns','v./n.','影响','Media influences our opinions.','媒体影响我们的观点。'),
    ('audience','ˈɔːdiəns','n.','观众','The show attracted a large audience.','节目吸引了大量观众。'),
    ('valuable','ˈvæljuəbl','adj.','有价值的','This documentary is very valuable.','这部纪录片很有价值。'),
    ('relaxing','rɪˈlæksɪŋ','adj.','令人放松的','Listening to music is relaxing.','听音乐很放松。'),
    ('opinion','əˈpɪnjən','n.','意见；看法','In my opinion, it\'s a great show.','在我看来，这是个好节目。'))
add(8,'u05','🥉','学霸词汇 · 冲刺满分',
    ('addictive','əˈdɪktɪv','adj.','上瘾的','Some games are addictive.','有些游戏会上瘾。'),
    ('critical','ˈkrɪtɪkl','adj.','批判性的','Think critically about what you watch.','对看到的东西要有批判思维。'),
    ('perspective','pərˈspektɪv','n.','视角；观点','Different people have different perspectives.','不同人有不同视角。'),
    ('prejudice','ˈpredʒudɪs','n.','偏见','Media can create prejudice.','媒体可能制造偏见。'),
    ('diverse','daɪˈvɜːrs','adj.','多样化的','We need diverse sources of news.','我们需要多样化的新闻来源。'),
    ('analyze','ˈænəlaɪz','v.','分析','Learn to analyze information.','学会分析信息。'))

add(8,'u06','🥈','掌握词汇 · 职业规划',
    ('career','kəˈrɪr','n.','职业','Choose a career you love.','选择你喜欢的职业。'),
    ('engineer','ˌendʒɪˈnɪr','n.','工程师','My uncle is an engineer.','我叔叔是工程师。'),
    ('scientist','ˈsaɪəntɪst','n.','科学家','She wants to become a scientist.','她想成为科学家。'),
    ('programmer','ˈproʊɡræmər','n.','程序员','He works as a programmer.','他是程序员。'),
    ('education','ˌedʒuˈkeɪʃn','n.','教育','Education is the key to success.','教育是成功的关键。'),
    ('university','ˌjuːnɪˈvɜːrsəti','n.','大学','She was accepted to a top university.','她被一所顶尖大学录取了。'),
    ('medicine','ˈmedɪsn','n.','医学；药','He studies medicine at college.','他在大学学医。'),
    ('resolution','ˌrezəˈluːʃn','n.','决心；决定','I made a resolution to study harder.','我下决心更努力学习。'),
    ('promise','ˈprɒmɪs','v./n.','承诺；保证','Keep your promises.','遵守你的承诺。'),
    ('skill','skɪl','n.','技能；技巧','Practice improves your skills.','练习提升技能。'))
add(8,'u06','🥉','学霸词汇 · 冲刺满分',
    ('ambition','æmˈbɪʃn','n.','雄心；志向','Follow your ambition, not others\' expectations.','追随你的志向，而非他人期望。'),
    ('motivation','ˌmoʊtɪˈveɪʃn','n.','动力；积极性','Find your inner motivation.','找到你内心的动力。'),
    ('vocation','voʊˈkeɪʃn','n.','天职；使命','Teaching is more than a job—it\'s a vocation.','教学不止是工作，更是使命。'),
    ('dedication','ˌdedɪˈkeɪʃn','n.','奉献；专注','Success requires dedication.','成功需要奉献。'),
    ('potential','pəˈtenʃl','n.','潜力；潜能','Everyone has great potential.','每个人都有巨大潜力。'),
    ('profession','prəˈfeʃn','n.','职业；专业','Choose a profession that suits you.','选择适合你的职业。'))

add(8,'u07','🥈','掌握词汇 · 未来预测',
    ('environment','ɪnˈvaɪrənmənt','n.','环境','Protect the environment now.','现在就保护环境。'),
    ('pollution','pəˈluːʃn','n.','污染','Air pollution is a serious problem.','空气污染是个严重问题。'),
    ('technology','tekˈnɒlədʒi','n.','技术','Technology changes fast.','技术变化很快。'),
    ('robot','ˈroʊbɒt','n.','机器人','Robots will do many jobs.','机器人将做很多工作。'),
    ('future','ˈfjuːtʃər','n.','未来','The future is full of possibilities.','未来充满可能。'),
    ('prediction','prɪˈdɪkʃn','n.','预测','Make a prediction about the future.','预测一下未来。'),
    ('dangerous','ˈdeɪndʒərəs','adj.','危险的','This could be dangerous.','这可能很危险。'),
    ('peaceful','ˈpiːsfl','adj.','和平的；平静的','I hope for a peaceful world.','我希望世界和平。'),
    ('believe','bɪˈliːv','v.','相信','I believe in a bright future.','我相信光明的未来。'),
    ('agree','əˈɡriː','v.','同意','Do you agree with this prediction?','你同意这个预测吗？'))
add(8,'u07','🥉','学霸词汇 · 冲刺满分',
    ('artificial','ˌɑːrtɪˈfɪʃl','adj.','人工的；人造的','Artificial intelligence is advancing fast.','人工智能发展很快。'),
    ('sustainable','səˈsteɪnəbl','adj.','可持续的','We need sustainable development.','我们需要可持续发展。'),
    ('inevitable','ɪnˈevɪtəbl','adj.','不可避免的','Change is inevitable.','变化是不可避免的。'),
    ('optimistic','ˌɒptɪˈmɪstɪk','adj.','乐观的','Be optimistic about the future.','对未来保持乐观。'),
    ('pessimistic','ˌpesɪˈmɪstɪk','adj.','悲观的','Don\'t be too pessimistic.','别太悲观。'),
    ('breakthrough','ˈbreɪkθruː','n.','突破','This is a major breakthrough.','这是一项重大突破。'))

add(8,'u08','🥈','掌握词汇 · 沟通表达',
    ('communicate','kəˈmjuːnɪkeɪt','v.','交流；沟通','Learn to communicate clearly.','学会清晰交流。'),
    ('expression','ɪkˈspreʃn','n.','表达；表情','Facial expressions show feelings.','面部表情表达感受。'),
    ('common','ˈkɒmən','adj.','共同的；常见的','English is a common language.','英语是通用语言。'),
    ('purpose','ˈpɜːrpəs','n.','目的','What is the purpose of this message?','这条信息的目的什么？'),
    ('conversation','ˌkɒnvərˈseɪʃn','n.','对话','Start a conversation with a smile.','用微笑开始对话。'),
    ('topic','ˈtɒpɪk','n.','话题','Change the topic if needed.','必要时换个话题。'),
    ('signal','ˈsɪɡnəl','n.','信号','Body language sends signals.','肢体语言传递信号。'),
    ('gesture','ˈdʒestʃər','n.','手势','Use gestures to help explain.','用手势帮助解释。'),
    ('proper','ˈprɒpər','adj.','恰当的；得体的','Use proper language in formal situations.','正式场合使用得体语言。'),
    ('confident','ˈkɒnfɪdənt','adj.','自信的','Speak with confidence.','自信地说话。'))
add(8,'u08','🥉','学霸词汇 · 冲刺满分',
    ('articulate','ɑːrˈtɪkjuleɪt','v./adj.','清晰地表达；口才好的','She is an articulate speaker.','她是个口才好的演讲者。'),
    ('empathy','ˈempəθi','n.','共情；同理心','Good communication needs empathy.','好的沟通需要同理心。'),
    ('negotiate','nɪˈɡoʊʃieɪt','v.','谈判；协商','Learn to negotiate politely.','学会礼貌地协商。'),
    ('persuade','pərˈsweɪd','v.','说服','She persuaded me to join the club.','她说服我加入了俱乐部。'),
    ('interact','ˌɪntərˈækt','v.','互动；交流','Children interact through play.','孩子通过游戏互动。'),
    ('diplomatic','ˌdɪpləˈmætɪk','adj.','有外交手腕的；委婉的','Be diplomatic when giving feedback.','给反馈时要委婉。'))

# ============================================================
# english8 下册
# ============================================================
add(8,'b2u01','🥈','掌握词汇 · 放松与娱乐',
    ('hobby','ˈhɒbi','n.','爱好','Reading is my favorite hobby.','读书是我最喜欢的爱好。'),
    ('leisure','ˈleʒər','n.','闲暇；空闲','I enjoy my leisure time.','我享受闲暇时光。'),
    ('activity','ækˈtɪvəti','n.','活动','Outdoor activities keep us healthy.','户外活动让我们健康。'),
    ('stress','stres','n.','压力','Take a break to reduce stress.','休息一下减轻压力。'),
    ('balance','ˈbæləns','n./v.','平衡','Keep a balance between work and play.','保持工作与娱乐的平衡。'),
    ('indoor','ˈɪndɔːr','adj.','室内的','We played indoor games.','我们玩了室内游戏。'),
    ('outdoor','ˈaʊtdɔːr','adj.','户外的','Outdoor exercise is good for health.','户外运动有益健康。'),
    ('entertainment','ˌentərˈteɪnmənt','n.','娱乐','Movies are a form of entertainment.','电影是一种娱乐形式。'),
    ('relaxation','ˌriːlækˈseɪʃn','n.','放松','Listen to music for relaxation.','听音乐放松。'),
    ('amusement','əˈmjuːzmənt','n.','消遣；娱乐','The park offers various amusements.','公园提供各种娱乐活动。'))
add(8,'b2u01','🥉','学霸词汇 · 冲刺满分',
    ('recreation','ˌrekriˈeɪʃn','n.','娱乐；消遣','Recreation is important for mental health.','娱乐对心理健康很重要。'),
    ('refresh','rɪˈfreʃ','v.','使恢复精力','A short nap refreshes the mind.','小睡片刻恢复精力。'),
    ('pastime','ˈpæstaɪm','n.','消遣；娱乐','Gardening is a popular pastime.','园艺是一种流行的消遣。'),
    ('recharge','ˌriːˈtʃɑːrdʒ','v.','充电；恢复精力','Take a day off to recharge.','休息一天恢复精力。'),
    ('downtime','ˈdaʊntaɪm','n.','休息时间','Everyone needs some downtime.','每个人都需要休息时间。'),
    ('engage','ɪnˈɡeɪdʒ','v.','参与；从事','Engage in activities you enjoy.','参与你喜欢的活动。'))

add(8,'b2u02','🥈','掌握词汇 · 环保行动',
    ('volunteer','ˌvɒlənˈtɪr','n./v.','志愿者；自愿','I volunteer at the animal shelter.','我在动物收容所做志愿者。'),
    ('recycle','ˌriːˈsaɪkl','v.','回收利用','Please recycle paper and plastic.','请回收纸张和塑料。'),
    ('rubbish','ˈrʌbɪʃ','n.','垃圾','Don\'t throw rubbish on the ground.','别把垃圾扔在地上。'),
    ('waste','weɪst','n./v.','浪费；废物','Don\'t waste water.','别浪费水。'),
    ('protect','prəˈtekt','v.','保护','We should protect the environment.','我们应该保护环境。'),
    ('donate','ˈdoʊneɪt','v.','捐赠','Donate old clothes to charity.','把旧衣服捐给慈善机构。'),
    ('project','ˈprɒdʒekt','n.','项目；计划','Our class started a green project.','我们班启动了一个绿色项目。'),
    ('community','kəˈmjuːnəti','n.','社区','The community worked together.','社区一起努力。'),
    ('organize','ˈɔːrɡənaɪz','v.','组织','We organized a clean-up event.','我们组织了一次清扫活动。'),
    ('affect','əˈfekt','v.','影响','Pollution affects everyone.','污染影响每个人。'))
add(8,'b2u02','🥉','学霸词汇 · 冲刺满分',
    ('conservation','ˌkɒnsərˈveɪʃn','n.','保护；保存','Wildlife conservation is urgent.','野生动物保护刻不容缓。'),
    ('sustainable','səˈsteɪnəbl','adj.','可持续的','We need sustainable energy sources.','我们需要可持续能源。'),
    ('eco-friendly','ˈiːkoʊ ˈfrendli','adj.','环保的','Use eco-friendly products.','使用环保产品。'),
    ('environmentalist','ɪnˌvaɪrənˈmentəlɪst','n.','环保人士','She is an active environmentalist.','她是一位活跃的环保人士。'),
    ('campaign','kæmˈpeɪn','n.','运动；活动','Join the environmental campaign.','加入环保活动。'),
    ('awareness','əˈwernəs','n.','意识','Raise awareness about pollution.','提高对污染的意识。'))

add(8,'b2u03','🥈','掌握词汇 · 家务劳动',
    ('chore','tʃɔːr','n.','家务杂事','Doing chores teaches responsibility.','做家务教会责任感。'),
    ('dish','dɪʃ','n.','餐具；盘子','Wash the dishes after dinner.','晚饭后洗碗。'),
    ('laundry','ˈlɔːndri','n.','要洗的衣物','Do the laundry on weekends.','周末洗衣服。'),
    ('sweep','swiːp','v.','打扫','Sweep the floor every day.','每天扫地。'),
    ('fold','foʊld','v.','折叠','Fold your clothes neatly.','把你的衣服叠整齐。'),
    ('neat','niːt','adj.','整洁的','Keep your room neat.','保持房间整洁。'),
    ('mess','mes','n.','杂乱','Clean up the mess.','把杂乱收拾干净。'),
    ('fairness','ˈfernəs','n.','公正；公平','Fairness means sharing the work.','公平意味着分担工作。'),
    ('neighbor','ˈneɪbər','n.','邻居','Our neighbor is very kind.','我们的邻居很善良。'),
    ('depend','dɪˈpend','v.','依赖；取决于','It depends on the situation.','这取决于情况。'))
add(8,'b2u03','🥉','学霸词汇 · 冲刺满分',
    ('responsible','rɪˈspɒnsəbl','adj.','负责的','Be responsible for your tasks.','对自己的任务负责。'),
    ('obligation','ˌɒblɪˈɡeɪʃn','n.','义务；责任','Doing chores is a family obligation.','做家务是家庭义务。'),
    ('cooperation','koʊˌɒpəˈreɪʃn','n.','合作','Housework needs cooperation.','家务需要合作。'),
    ('appreciation','əˌpriːʃiˈeɪʃn','n.','感激；欣赏','Show appreciation for help.','对帮助表示感激。'),
    ('share','ʃer','v.','分享；分担','Share the housework equally.','平等分担家务。'),
    ('contribute','kənˈtrɪbjuːt','v.','贡献','Everyone should contribute to the family.','每个人都应为家庭做贡献。'))

add(8,'b2u04','🥈','掌握词汇 · 人际沟通',
    ('relation','rɪˈleɪʃn','n.','关系；联系','Good family relations matter.','良好的家庭关系很重要。'),
    ('communication','kəˌmjuːnɪˈkeɪʃn','n.','交流；沟通','Open communication solves problems.','开放的沟通解决问题。'),
    ('argument','ˈɑːrɡjumənt','n.','争论','Avoid unnecessary arguments.','避免不必要的争论。'),
    ('offer','ˈɒfər','v.','提供；提议','She offered to help me.','她主动提出帮我。'),
    ('explain','ɪkˈspleɪn','v.','解释','Can you explain this to me?','你能给我解释一下吗？'),
    ('pressure','ˈpreʃər','n.','压力','Don\'t put too much pressure on kids.','别给孩子太多压力。'),
    ('opinion','əˈpɪnjən','n.','意见；看法','Everyone has their own opinion.','每个人都有自己的看法。'),
    ('normal','ˈnɔːrml','adj.','正常的','It\'s normal to have disagreements.','有分歧是正常的。'),
    ('perhaps','pərˈhæps','adv.','也许；可能','Perhaps you should talk to your parents.','也许你该和父母谈谈。'),
    ('cause','kɔːz','v./n.','导致；原因','What caused the problem?','是什么导致了问题？'))
add(8,'b2u04','🥉','学霸词汇 · 冲刺满分',
    ('compromise','ˈkɒmprəmaɪz','v./n.','妥协；折中','Learn to compromise in relationships.','学会在关系中妥协。'),
    ('conflict','ˈkɒnflɪkt','n.','冲突','Avoid conflict with careful words.','用谨慎的言语避免冲突。'),
    ('perspective','pərˈspektɪv','n.','视角','See things from their perspective.','从他们的角度看问题。'),
    ('respectful','rɪˈspektfl','adj.','尊重的','Always be respectful in arguments.','争论时始终尊重对方。'),
    ('emotional','ɪˈmoʊʃənl','adj.','情绪化的','Stay calm and don\'t be emotional.','保持冷静，不要情绪化。'),
    ('mature','məˈtʃʊr','adj.','成熟的','Handle disagreements in a mature way.','用成熟的方式处理分歧。'))

add(8,'b2u05','🥈','掌握词汇 · 过去进行时',
    ('storm','stɔːrm','n.','暴风雨','The storm hit the city last night.','暴风雨昨晚袭击了城市。'),
    ('suddenly','ˈsʌdənli','adv.','突然地','Suddenly, the lights went out.','突然，灯灭了。'),
    ('strange','streɪndʒ','adj.','奇怪的；陌生的','I heard a strange noise.','我听到了奇怪的声音。'),
    ('silence','ˈsaɪləns','n.','沉默；寂静','There was complete silence.','一片寂静。'),
    ('area','ˈeəriə','n.','地区；区域','The area was flooded.','这个地区被淹了。'),
    ('wind','wɪnd','n.','风','The wind blew strongly.','风猛烈地吹着。'),
    ('flash','flæʃ','n./v.','闪电；闪烁','Lightning flashed across the sky.','闪电划过天空。'),
    ('asleep','əˈsliːp','adj.','睡着的','He fell asleep quickly.','他很快睡着了。'),
    ('beat','biːt','v.','击打；敲打','The rain beat against the window.','雨点敲打着窗户。'),
    ('against','əˈɡenst','prep.','倚靠；反对','Lean against the wall.','靠在墙上。'))
add(8,'b2u05','🥉','学霸词汇 · 冲刺满分',
    ('emergency','iˈmɜːrdʒənsi','n.','紧急情况','Stay calm in an emergency.','紧急情况保持冷静。'),
    ('disaster','dɪˈzæstər','n.','灾难','The flood was a natural disaster.','洪水是自然灾害。'),
    ('panic','ˈpænɪk','n./v.','恐慌','Don\'t panic in danger.','危险中不要恐慌。'),
    ('temporary','ˈtempəreri','adj.','暂时的','The damage was temporary.','损坏是暂时的。'),
    ('survive','sərˈvaɪv','v.','幸存；生存','We survived the storm safely.','我们安全度过了暴风雨。'),
    ('witness','ˈwɪtnəs','v./n.','目击；见证人','He witnessed the accident.','他目击了事故。'))

add(8,'b2u06','🥈','掌握词汇 · 故事传说',
    ('object','ˈɒbdʒɪkt','n.','物体；目标','What is that object?','那个物体是什么？'),
    ('magic','ˈmædʒɪk','n./adj.','魔法；神奇的','The magic stick could change things.','魔棒可以改变东西。'),
    ('tale','teɪl','n.','故事；传说','I love reading folk tales.','我喜欢读民间故事。'),
    ('stupid','ˈstuːpɪd','adj.','愚蠢的','That was a stupid mistake.','那是个愚蠢的错误。'),
    ('whole','hoʊl','adj.','全部的；整个的','Tell me the whole story.','把整个故事告诉我。'),
    ('stepmother','ˈstepmʌðər','n.','继母','The stepmother was cruel.','继母很残忍。'),
    ('marry','ˈmæri','v.','结婚','They got married last year.','他们去年结婚了。'),
    ('shine','ʃaɪn','v.','发光；照耀','The sun shone brightly.','阳光灿烂。'),
    ('hide','haɪd','v.','躲藏；隐藏','The child hid behind the door.','孩子躲在门后面。'),
    ('brave','breɪv','adj.','勇敢的','The hero was brave and strong.','英雄勇敢又强壮。'))
add(8,'b2u06','🥉','学霸词汇 · 冲刺满分',
    ('moral','ˈmɔːrəl','n./adj.','寓意；道德的','The moral of the story is clear.','故事的寓意很清楚。'),
    ('legend','ˈledʒənd','n.','传说；传奇','This is an ancient legend.','这是一个古老的传说。'),
    ('heroic','hɪˈroʊɪk','adj.','英雄的','The hero performed heroic deeds.','英雄做出了英雄事迹。'),
    ('wisdom','ˈwɪzdəm','n.','智慧','The old man shared his wisdom.','老人分享了他的智慧。'),
    ('overcome','ˌoʊvərˈkʌm','v.','克服','She overcame many difficulties.','她克服了很多困难。'),
    ('transform','trænsˈfɔːrm','v.','转变；改变','The frog transformed into a prince.','青蛙变成了王子。'))

add(8,'b2u07','🥈','掌握词汇 · 世界之最',
    ('population','ˌpɒpjuˈleɪʃn','n.','人口','China has a large population.','中国人口众多。'),
    ('danger','ˈdeɪndʒər','n.','危险','Some animals are in danger.','有些动物处于危险中。'),
    ('include','ɪnˈkluːd','v.','包括','The tour includes lunch.','这次旅行包括午餐。'),
    ('condition','kənˈdɪʃn','n.','条件；状况','The living conditions are improving.','生活条件在改善。'),
    ('deep','diːp','adj.','深的','The lake is very deep.','湖很深。'),
    ('ocean','ˈoʊʃn','n.','海洋','The Pacific Ocean is vast.','太平洋很广阔。'),
    ('research','rɪˈsɜːrtʃ','n./v.','研究','Scientists do research on climate.','科学家研究气候。'),
    ('ancient','ˈeɪnʃənt','adj.','古代的','The Great Wall is an ancient wonder.','长城是古代奇迹。'),
    ('protect','prəˈtekt','v.','保护','We must protect endangered species.','我们必须保护濒危物种。'),
    ('achievement','əˈtʃiːvmənt','n.','成就','Climbing the mountain was a great achievement.','登山是一项伟大成就。'))
add(8,'b2u07','🥉','学霸词汇 · 冲刺满分',
    ('record','ˈrekɔːrd','n.','纪录','He broke the world record.','他打破了世界纪录。'),
    ('challenge','ˈtʃælɪndʒ','n./v.','挑战','It was a huge challenge.','这是一个巨大的挑战。'),
    ('extreme','ɪkˈstriːm','adj.','极端的；极限的','Mountain climbing is an extreme sport.','登山是极限运动。'),
    ('amazing','əˈmeɪzɪŋ','adj.','令人惊叹的','The view from the top was amazing.','山顶的景色令人惊叹。'),
    ('unique','juˈniːk','adj.','独特的','Every animal is unique.','每种动物都是独特的。'),
    ('endangered','ɪnˈdeɪndʒərd','adj.','濒危的','Pandas are an endangered species.','熊猫是濒危物种。'))

add(8,'b2u08','🥈','掌握词汇 · 社会责任',
    ('difference','ˈdɪfrəns','n.','差异；不同','One person can make a difference.','一个人也能带来改变。'),
    ('society','səˈsaɪəti','n.','社会','We should contribute to society.','我们应该为社会做贡献。'),
    ('support','səˈpɔːrt','v./n.','支持；帮助','Support each other in difficulties.','困难中互相支持。'),
    ('possible','ˈpɒsəbl','adj.','可能的','Make the world a better place if possible.','如果可能，让世界更美好。'),
    ('action','ˈækʃn','n.','行动；行为','Take action to help others.','采取行动帮助他人。'),
    ('raise','reɪz','v.','筹集；提高','We raised money for the poor.','我们为穷人筹集了资金。'),
    ('awareness','əˈwernəs','n.','意识；认识','Raise awareness about social issues.','提高对社会问题的意识。'),
    ('effort','ˈefərt','n.','努力','Every effort counts.','每一份努力都重要。'),
    ('value','ˈvæljuː','n./v.','价值；重视','We value our volunteers.','我们重视志愿者。'),
    ('encourage','ɪnˈkɜːrɪdʒ','v.','鼓励','Encourage others to join.','鼓励他人加入。'))
add(8,'b2u08','🥉','学霸词汇 · 冲刺满分',
    ('responsible','rɪˈspɒnsəbl','adj.','有责任感的','Be a responsible citizen.','做一个有责任感的公民。'),
    ('initiative','ɪˈnɪʃətɪv','n.','主动性；倡议','Take the initiative to help.','主动提供帮助。'),
    ('impact','ˈɪmpækt','n./v.','影响；冲击','Small actions can have a big impact.','小行动也能有大影响。'),
    ('generous','ˈdʒenərəs','adj.','慷慨的','She is generous with her time.','她慷慨地付出时间。'),
    ('compassion','kəmˈpæʃn','n.','同情心；怜悯','Show compassion for those in need.','对有需要的人表示同情。'),
    ('dedicated','ˈdedɪkeɪtɪd','adj.','奉献的；投入的','She is dedicated to helping others.','她致力于帮助他人。'))

# ============================================================
# english9
# ============================================================
add(9,'u01','🥈','掌握词汇 · 学习方法',
    ('textbook','ˈtekstbʊk','n.','教科书','Read the textbook carefully.','认真阅读教科书。'),
    ('pronunciation','prəˌnʌnsiˈeɪʃn','n.','发音','Practice pronunciation daily.','每天练习发音。'),
    ('grammar','ˈɡræmər','n.','语法','Grammar rules are important.','语法规则很重要。'),
    ('vocabulary','vəˈkæbjəleri','n.','词汇','Build your vocabulary step by step.','逐步积累词汇。'),
    ('understand','ˌʌndərˈstænd','v.','理解','Do you understand the lesson?','你理解这节课吗？'),
    ('express','ɪkˈspres','v.','表达','Learn to express your ideas.','学会表达你的想法。'),
    ('meaning','ˈmiːnɪŋ','n.','意义；意思','Look up the meaning in a dictionary.','在词典里查意思。'),
    ('review','rɪˈvjuː','v./n.','复习','Review what you learned.','复习你学过的内容。'),
    ('strategy','ˈstrætədʒi','n.','策略','Use effective learning strategies.','使用有效的学习策略。'),
    ('improve','ɪmˈpruːv','v.','提高；改善','Practice improves your skills.','练习提高你的技能。'))
add(9,'u01','🥉','学霸词汇 · 冲刺满分',
    ('comprehend','ˌkɒmprɪˈhend','v.','理解；领悟','Read widely to comprehend better.','广泛阅读以更好理解。'),
    ('acquire','əˈkwaɪər','v.','获得；学到','Acquire knowledge through reading.','通过阅读获取知识。'),
    ('efficient','ɪˈfɪʃnt','adj.','高效的','Find efficient learning methods.','找到高效的学习方法。'),
    ('retention','rɪˈtenʃn','n.','记忆；保持','Review helps with retention.','复习有助于记忆。'),
    ('accumulate','əˈkjuːmjuleɪt','v.','积累','Accumulate vocabulary every day.','每天积累词汇。'),
    ('master','ˈmæstər','v.','掌握；精通','Master the basics first.','先掌握基础。'))

add(9,'u02','🥈','掌握词汇 · 节日与文化',
    ('celebrate','ˈselɪbreɪt','v.','庆祝','How do you celebrate the festival?','你怎么庆祝这个节日？'),
    ('tradition','trəˈdɪʃn','n.','传统','This is an ancient tradition.','这是一个古老的传统。'),
    ('festival','ˈfestɪvl','n.','节日','Spring Festival is the most important.','春节是最重要的。'),
    ('delicious','dɪˈlɪʃəs','adj.','美味的','The mooncakes were delicious.','月饼很好吃。'),
    ('relative','ˈrelətɪv','n.','亲戚','We visit relatives during the festival.','节日期间我们拜访亲戚。'),
    ('culture','ˈkʌltʃər','n.','文化','Learn about different cultures.','了解不同的文化。'),
    ('custom','ˈkʌstəm','n.','风俗；习惯','Every country has its own customs.','每个国家有自己的风俗。'),
    ('symbol','ˈsɪmbl','n.','象征','The dragon is a symbol of power.','龙是权力的象征。'),
    ('gather','ˈɡæðər','v.','聚集','Families gather for the reunion.','家人聚在一起团圆。'),
    ('admire','ədˈmaɪər','v.','欣赏；钦佩','We admire the full moon.','我们赏月。'))
add(9,'u02','🥉','学霸词汇 · 冲刺满分',
    ('heritage','ˈherɪtɪdʒ','n.','遗产；传统','Protect our cultural heritage.','保护我们的文化遗产。'),
    ('ancestor','ˈænsestər','n.','祖先','Honor our ancestors.','尊敬我们的祖先。'),
    ('significant','sɪɡˈnɪfɪkənt','adj.','有意义的；重要的','This festival is very significant.','这个节日非常重要。'),
    ('ceremony','ˈserəmoʊni','n.','仪式；典礼','The opening ceremony was grand.','开幕式很盛大。'),
    ('folk','foʊk','adj.','民间的','I enjoy folk music.','我喜欢民乐。'),
    ('reunion','ˌriːˈjuːniən','n.','团圆；重聚','Family reunion is the highlight.','家庭团圆是亮点。'))

add(9,'u03','🥈','掌握词汇 · 问路与请求',
    ('restroom','ˈrestruːm','n.','洗手间','Excuse me, where is the restroom?','请问洗手间在哪？'),
    ('direction','dɪˈrekʃn','n.','方向','Walk in this direction.','朝这个方向走。'),
    ('corner','ˈkɔːrnər','n.','拐角','Turn left at the corner.','在拐角左转。'),
    ('suggest','səˈdʒest','v.','建议','I suggest taking the subway.','我建议坐地铁。'),
    ('polite','pəˈlaɪt','adj.','礼貌的','Be polite when asking for help.','求助时要有礼貌。'),
    ('convenient','kənˈviːniənt','adj.','方便的','The location is very convenient.','位置很方便。'),
    ('neighborhood','ˈneɪbərhʊd','n.','街区；社区','It\'s a safe neighborhood.','这是一个安全的社区。'),
    ('cross','krɔːs','v.','穿过','Cross the street carefully.','小心过马路。'),
    ('address','əˈdres','n.','地址','Write down your address.','写下你的地址。'),
    ('central','ˈsentrəl','adj.','中心的','We\'re in the central area.','我们在中心区域。'))
add(9,'u03','🥉','学霸词汇 · 冲刺满分',
    ('navigate','ˈnævɪɡeɪt','v.','导航；导航','Use GPS to navigate the city.','用GPS导航城市。'),
    ('accessible','əkˈsesəbl','adj.','可到达的；便利的','The museum is accessible by bus.','博物馆可以乘公交到达。'),
    ('landmark','ˈlændmɑːrk','n.','地标','The tower is a famous landmark.','这座塔是著名地标。'),
    ('intersection','ˌɪntərˈsekʃn','n.','十字路口','Turn right at the next intersection.','下一个十字路口右转。'),
    ('pedestrian','pəˈdestriən','n.','行人','The street is for pedestrians only.','这条街只限行人。'),
    ('distance','ˈdɪstəns','n.','距离','It\'s within walking distance.','步行即可到达。'))

add(9,'u04','🥈','掌握词汇 · 变化与成长',
    ('used to','juːst tuː','phr.','过去常常','I used to be shy.','我过去很害羞。'),
    ('background','ˈbækɡraʊnd','n.','背景','She comes from a musical background.','她出身音乐背景。'),
    ('influence','ˈɪnfluəns','v./n.','影响','My parents influenced me a lot.','我父母对我影响很大。'),
    ('teenager','ˈtiːneɪdʒər','n.','青少年','Teenagers face many changes.','青少年面临许多变化。'),
    ('shy','ʃaɪ','adj.','害羞的','Don\'t be shy to speak up.','别害羞，大声说出来。'),
    ('confident','ˈkɒnfɪdənt','adj.','自信的','She became more confident.','她变得更自信了。'),
    ('appearance','əˈpɪrəns','n.','外貌；出现','Don\'t judge by appearance.','不要以貌取人。'),
    ('personality','ˌpɜːrsəˈnæləti','n.','个性','Her personality shines.','她的个性很闪亮。'),
    ('private','ˈpraɪvət','adj.','私人的','Everyone needs private space.','每个人都需要私人空间。'),
    ('guard','ɡɑːrd','n./v.','守卫；保护','Let your guard down sometimes.','有时放下防备。'))
add(9,'u04','🥉','学霸词汇 · 冲刺满分',
    ('adolescent','ˌædəˈlesnt','n./adj.','青少年；青春期的','Adolescent years are full of change.','青春期充满变化。'),
    ('mature','məˈtʃʊr','adj.','成熟的','She has matured a lot.','她成熟了很多。'),
    ('identity','aɪˈdentəti','n.','身份；认同','Teens search for their identity.','青少年寻找自我认同。'),
    ('transform','trænsˈfɔːrm','v.','转变；改变','Life experiences transform us.','生活经历改变了我们。'),
    ('self-esteem','ˌself ɪˈstiːm','n.','自尊','Build your self-esteem.','建立你的自尊。'),
    ('independence','ˌɪndɪˈpendəns','n.','独立','Teenagers want independence.','青少年想要独立。'))

add(9,'u05','🥈','掌握词汇 · 产品与材料',
    ('product','ˈprɒdʌkt','n.','产品','This product is made of cotton.','这个产品是棉制的。'),
    ('material','məˈtɪriəl','n.','材料','What material is it made of?','它是什么材料做的？'),
    ('produce','prəˈduːs','v.','生产','This factory produces shoes.','这家工厂生产鞋子。'),
    ('process','ˈprɒses','n./v.','过程；加工','The production process is complex.','生产过程很复杂。'),
    ('widely','ˈwaɪdli','adv.','广泛地','This product is widely used.','这个产品被广泛使用。'),
    ('known','noʊn','adj.','知名的；已知的','It is known for its quality.','它以品质闻名。'),
    ('brand','brænd','n.','品牌','Which brand do you prefer?','你更喜欢哪个品牌？'),
    ('local','ˈloʊkl','adj.','当地的','Buy local products.','购买当地产品。'),
    ('avoid','əˈvɔɪd','v.','避免','Avoid products with too much packaging.','避免过度包装的产品。'),
    ('handmade','ˌhændˈmeɪd','adj.','手工制作的','Handmade gifts are special.','手工制作的礼物很特别。'))
add(9,'u05','🥉','学霸词汇 · 冲刺满分',
    ('manufacture','ˌmænjuˈfæktʃər','v.','制造','This car is manufactured in China.','这辆车在中国制造。'),
    ('raw material','rɔː məˈtɪriəl','n.','原材料','Wood is a raw material.','木材是一种原材料。'),
    ('quality','ˈkwɒləti','n.','质量','Quality is more important than quantity.','质量比数量更重要。'),
    ('export','ˈekspɔːrt','v./n.','出口','China exports many products.','中国出口很多产品。'),
    ('import','ˈɪmpɔːrt','v./n.','进口','We import coffee from Brazil.','我们从巴西进口咖啡。'),
    ('craftsmanship','ˈkræftsmənʃɪp','n.','工艺；手艺','The craftsmanship is excellent.','工艺非常精湛。'))

add(9,'u06','🥈','掌握词汇 · 发明历史',
    ('invent','ɪnˈvent','v.','发明','Who invented the telephone?','谁发明了电话？'),
    ('invention','ɪnˈvenʃn','n.','发明','The internet is a great invention.','互联网是一个伟大的发明。'),
    ('discover','dɪˈskʌvər','v.','发现','Columbus discovered America.','哥伦布发现了美洲。'),
    ('create','kriˈeɪt','v.','创造','Create something new.','创造新的东西。'),
    ('introduce','ˌɪntrəˈduːs','v.','引入；介绍','When was the computer introduced?','计算机是何时引入的？'),
    ('popular','ˈpɒpjələr','adj.','流行的；受欢迎的','Smartphones became popular quickly.','智能手机迅速流行起来。'),
    ('spread','spred','v.','传播；扩散','The news spread quickly.','消息迅速传播。'),
    ('pioneer','ˌpaɪəˈnɪr','n.','先驱；先锋','She was a pioneer in medicine.','她是医学界的先驱。'),
    ('development','dɪˈveləpmənt','n.','发展','Technology development is fast.','技术发展很快。'),
    ('improvement','ɪmˈpruːvmənt','n.','改进；改善','This is a big improvement.','这是一项大改进。'))
add(9,'u06','🥉','学霸词汇 · 冲刺满分',
    ('innovation','ˌɪnəˈveɪʃn','n.','创新','Innovation drives progress.','创新驱动进步。'),
    ('revolution','ˌrevəˈluːʃn','n.','革命','The industrial revolution changed everything.','工业革命改变了一切。'),
    ('patent','ˈpætnt','n.','专利','He filed a patent for his invention.','他为他的发明申请了专利。'),
    ('technology','tekˈnɒlədʒi','n.','技术','Modern technology makes life easier.','现代技术让生活更方便。'),
    ('breakthrough','ˈbreɪkθruː','n.','突破','This is a medical breakthrough.','这是一项医学突破。'),
    ('milestone','ˈmaɪlstoʊn','n.','里程碑','This invention was a milestone.','这项发明是一个里程碑。'))

add(9,'u07','🥈','掌握词汇 · 规则与许可',
    ('allow','əˈlaʊ','v.','允许','Teenagers should be allowed to choose.','青少年应该被允许选择。'),
    ('choose','tʃuːz','v.','选择','Choose what\'s best for you.','选择最适合你的。'),
    ('rule','ruːl','n.','规则','Follow the school rules.','遵守校规。'),
    ('license','ˈlaɪsns','n.','执照；许可证','Get a driver\'s license at 18.','18岁拿驾照。'),
    ('decision','dɪˈsɪʒn','n.','决定','Make your own decisions.','自己做决定。'),
    ('support','səˈpɔːrt','v./n.','支持','Parents should support their kids.','父母应该支持孩子。'),
    ('fair','fer','adj.','公平的','The rules are fair.','规则是公平的。'),
    ('strict','strɪkt','adj.','严格的','My parents are strict but kind.','我父母严格但友善。'),
    ('concentrate','ˈkɒnsəntreɪt','v.','集中注意力','Concentrate on your studies.','集中精力学习。'),
    ('experience','ɪkˈspɪriəns','n./v.','经验；经历','This is a valuable experience.','这是一次宝贵的经历。'))
add(9,'u07','🥉','学霸词汇 · 冲刺满分',
    ('permission','pərˈmɪʃn','n.','允许；许可','Ask for permission first.','先征得许可。'),
    ('responsible','rɪˈspɒnsəbl','adj.','负责的','Responsible teens earn more trust.','负责任的青少年赢得更多信任。'),
    ('discipline','ˈdɪsəplɪn','n.','纪律；自律','Discipline leads to freedom.','自律带来自由。'),
    ('maturity','məˈtʃʊrəti','n.','成熟','Maturity comes with experience.','成熟来自经历。'),
    ('restrict','rɪˈstrɪkt','v.','限制','Don\'t restrict your dreams.','不要限制你的梦想。'),
    ('negotiate','nɪˈɡoʊʃieɪt','v.','协商','Negotiate with your parents.','和你的父母协商。'))

add(9,'u08','🥈','掌握词汇 · 推测与判断',
    ('belong','bɪˈlɔːŋ','v.','属于','This book belongs to me.','这本书属于我。'),
    ('possibly','ˈpɒsəbli','adv.','可能地','It could possibly rain today.','今天可能下雨。'),
    ('certainly','ˈsɜːrtnli','adv.','当然；certainly','She will certainly succeed.','她一定会成功。'),
    ('whose','huːz','pron.','谁的','Whose backpack is this?','这是谁的书包？'),
    ('valuable','ˈvæljuəbl','adj.','贵重的；有价值的','This ring is valuable.','这枚戒指很贵重。'),
    ('lab','læb','n.','实验室','Do the experiment in the lab.','在实验室做实验。'),
    ('attend','əˈtend','v.','参加；出席','Attend the meeting on time.','准时参加会议。'),
    ('attempt','əˈtempt','v./n.','尝试；企图','She attempted to solve the mystery.','她试图解开谜团。'),
    ('prevent','prɪˈvent','v.','阻止；预防','Prevent accidents before they happen.','防患于未然。'),
    ('reason','ˈriːzn','n.','理由；原因','There\'s a reason for everything.','凡事皆有因。'))
add(9,'u08','🥉','学霸词汇 · 冲刺满分',
    ('deduce','dɪˈduːs','v.','推断；推理','Deduce the truth from the clues.','从线索中推断真相。'),
    ('evidence','ˈevɪdəns','n.','证据','The police found new evidence.','警方发现了新证据。'),
    ('mystery','ˈmɪstəri','n.','神秘；谜','The mystery remains unsolved.','谜团仍未解开。'),
    ('logical','ˈlɒdʒɪkl','adj.','合乎逻辑的','Use logical reasoning.','运用逻辑推理。'),
    ('conclusion','kənˈkluːʒn','n.','结论','Draw a conclusion from the facts.','从事实中得出结论。'),
    ('assume','əˈsuːm','v.','假设；假定','Don\'t assume without proof.','没有证据不要假设。'))

add(9,'u09','🥈','掌握词汇 · 偏好与定语从句',
    ('prefer','prɪˈfɜːr','v.','更喜欢','I prefer classical music.','我更喜欢古典音乐。'),
    ('style','staɪl','n.','风格','This song has a pop style.','这首歌是流行风格。'),
    ('especially','ɪˈspeʃəli','adv.','特别；尤其','I love music, especially jazz.','我喜欢音乐，尤其是爵士。'),
    ('suppose','səˈpoʊz','v.','假设；认为','I suppose you\'re right.','我认为你是对的。'),
    ('director','dɪˈrektər','n.','导演','He is a famous movie director.','他是一位著名导演。'),
    ('dialog','ˈdaɪəlɒɡ','n.','对话','The dialog was funny.','对话很有趣。'),
    ('reflect','rɪˈflekt','v.','反映；反射','Movies reflect our society.','电影反映我们的社会。'),
    ('masterpiece','ˈmæstərpiːs','n.','杰作','This film is a masterpiece.','这部电影是杰作。'),
    ('praise','preɪz','v./n.','赞扬；表扬','The movie received high praise.','这部电影获得了高度赞扬。'),
    ('super','ˈsuːpər','adj.','超级的；极好的','It was a super experience.','这是一次超级体验。'))
add(9,'u09','🥉','学霸词汇 · 冲刺满分',
    ('aesthetic','esˈθetɪk','adj.','审美的；美学的','Art has aesthetic value.','艺术有审美价值。'),
    ('genre','ˈʒɒnrə','n.','类型；流派','What\'s your favorite music genre?','你最喜欢的音乐类型是什么？'),
    ('lyrics','ˈlɪrɪks','n.','歌词','The lyrics are very touching.','歌词很感人。'),
    ('orchestra','ˈɔːrkɪstrə','n.','管弦乐队','The orchestra played beautifully.','管弦乐队演奏得很美。'),
    ('rhythm','ˈrɪðəm','n.','节奏；韵律','The rhythm is catchy.','节奏很上口。'),
    ('sentimental','ˌsentɪˈmentl','adj.','感伤的；多愁善感的','This song makes me sentimental.','这首歌让我感伤。'))

add(9,'u10','🥈','掌握词汇 · 礼仪与文化',
    ('suppose','səˈpoʊz','v.','应该；认为','You\'re supposed to shake hands.','你应该握手。'),
    ('greet','ɡriːt','v.','问候；打招呼','How do you greet elders?','你如何问候长辈？'),
    ('custom','ˈkʌstəm','n.','风俗；习惯','Every culture has its customs.','每种文化都有自己的风俗。'),
    ('manner','ˈmænər','n.','礼貌；举止','Table manners vary across cultures.','餐桌礼仪因文化而异。'),
    ('formal','ˈfɔːrml','adj.','正式的','Use formal language in business.','商务场合使用正式语言。'),
    ('exchange','ɪksˈtʃeɪndʒ','v./n.','交换','Exchange greetings with a smile.','微笑问候。'),
    ('behavior','bɪˈheɪvjər','n.','行为；举止','Good behavior is appreciated.','良好的行为受到赞赏。'),
    ('respect','rɪˈspekt','v./n.','尊重','Respect other cultures.','尊重其他文化。'),
    ('modest','ˈmɒdɪst','adj.','谦虚的','Be modest about your achievements.','对自己的成就谦虚。'),
    ('toast','toʊst','n./v.','敬酒；烤面包','Make a toast at the dinner.','在晚宴上敬酒。'))
add(9,'u10','🥉','学霸词汇 · 冲刺满分',
    ('etiquette','ˈetɪket','n.','礼仪；礼节','Learn business etiquette.','学习商务礼仪。'),
    ('appropriate','əˈproʊpriət','adj.','恰当的；合适的','Wear appropriate clothes.','穿合适的衣服。'),
    ('punctual','ˈpʌŋktʃuəl','adj.','守时的','Be punctual for meetings.','准时参加会议。'),
    ('hospitality','ˌhɒspɪˈtæləti','n.','好客；热情款待','Chinese hospitality is famous.','中国人的好客是出了名的。'),
    ('diplomatic','ˌdɪpləˈmætɪk','adj.','外交的；有策略的','Be diplomatic when refusing.','拒绝时要有策略。'),
    ('hierarchy','ˈhaɪərɑːrki','n.','等级制度','Respect the family hierarchy.','尊重家庭等级。'))

add(9,'u11','🥈','掌握词汇 · 情感与感受',
    ('rather','ˈræðər','adv.','相当；宁可','I\'d rather stay at home.','我宁愿待在家里。'),
    ('drive','draɪv','v.','驾驶；驱使','Sad movies drive me to cry.','悲伤的电影让我想哭。'),
    ('friendship','ˈfrendʃɪp','n.','友谊','True friendship is valuable.','真正的友谊很珍贵。'),
    ('king','kɪŋ','n.','国王','The king was unhappy.','国王不开心。'),
    ('power','ˈpaʊər','n.','权力；力量','Money doesn\'t bring power.','金钱不能带来权力。'),
    ('wealth','welθ','n.','财富','Wealth doesn\'t equal happiness.','财富不等于幸福。'),
    ('fame','feɪm','n.','名声；名誉','Fame comes with pressure.','名声伴随着压力。'),
    ('emotion','ɪˈmoʊʃn','n.','情感；情绪','Control your emotions.','控制你的情绪。'),
    ('disappoint','ˌdɪsəˈpɔɪnt','v.','使失望','Don\'t disappoint your parents.','别让你的父母失望。'),
    ('confident','ˈkɒnfɪdənt','adj.','自信的','Stay confident in difficulties.','困难中保持自信。'))
add(9,'u11','🥉','学霸词汇 · 冲刺满分',
    ('depression','dɪˈpreʃn','n.','抑郁；沮丧','Don\'t let depression take over.','别让抑郁控制你。'),
    ('anxiety','æŋˈzaɪəti','n.','焦虑','Reduce anxiety through relaxation.','通过放松减少焦虑。'),
    ('optimism','ˈɒptɪmɪzəm','n.','乐观','Optimism helps overcome difficulties.','乐观帮助克服困难。'),
    ('gratitude','ˈɡrætɪtuːd','n.','感激；感恩','Express gratitude every day.','每天表达感恩。'),
    ('resilient','rɪˈzɪliənt','adj.','坚韧的；有弹性的','Be resilient in tough times.','困难时期保持坚韧。'),
    ('affection','əˈfekʃn','n.','喜爱；情感','Show affection to your family.','向家人表达关爱。'))

add(9,'u12','🥈','掌握词汇 · 意外与经历',
    ('unexpected','ˌʌnɪkˈspektɪd','adj.','出乎意料的','Life is full of the unexpected.','生活充满意外。'),
    ('oversleep','ˌoʊvərˈsliːp','v.','睡过头','I overslept this morning.','我今天早上睡过头了。'),
    ('cancel','ˈkænsl','v.','取消','The flight was cancelled.','航班被取消了。'),
    ('miss','mɪs','v.','错过；想念','Don\'t miss the bus.','别错过公交车。'),
    ('discover','dɪˈskʌvər','v.','发现','I discovered a new cafe.','我发现了一家新咖啡店。'),
    ('embarrass','ɪmˈbærəs','v.','使尴尬','The mistake embarrassed me.','这个错误让我很尴尬。'),
    ('announce','əˈnaʊns','v.','宣布','The result will be announced tomorrow.','结果明天公布。'),
    ('believe','bɪˈliːv','v.','相信','I couldn\'t believe my eyes.','我无法相信自己的眼睛。'),
    ('survive','sərˈvaɪv','v.','幸存；生存','We survived the traffic jam.','我们在交通堵塞中熬过来了。'),
    ('manage','ˈmænɪdʒ','v.','设法做到','I managed to catch the train.','我设法赶上了火车。'))
add(9,'u12','🥉','学霸词汇 · 冲刺满分',
    ('coincidence','koʊˈɪnsɪdəns','n.','巧合','What a coincidence!','真是巧合！'),
    ('fortunate','ˈfɔːrtʃənət','adj.','幸运的','I was fortunate to escape.','我幸运地逃过了。'),
    ('disaster','dɪˈzæstər','n.','灾难','The storm was a disaster.','暴风雨是一场灾难。'),
    ('unpredictable','ˌʌnprɪˈdɪktəbl','adj.','不可预测的','The future is unpredictable.','未来不可预测。'),
    ('remarkable','rɪˈmɑːrkəbl','adj.','非凡的；显著的','It was a remarkable escape.','这是一次非凡的逃脱。'),
    ('chaos','ˈkeɪɒs','n.','混乱；杂乱','The airport was in chaos.','机场一片混乱。'))

add(9,'u13','🥈','掌握词汇 · 环保与行动',
    ('environment','ɪnˈvaɪrənmənt','n.','环境','Protect the environment now.','现在就保护环境。'),
    ('pollution','pəˈluːʃn','n.','污染','Air pollution is harmful.','空气污染有害。'),
    ('recycle','ˌriːˈsaɪkl','v.','回收','Recycle paper and plastic.','回收纸张和塑料。'),
    ('reduce','rɪˈduːs','v.','减少','Reduce waste every day.','每天减少浪费。'),
    ('reuse','ˌriːˈjuːz','v.','再利用','Reuse shopping bags.','重复使用购物袋。'),
    ('plastic','ˈplæstɪk','n./adj.','塑料','Avoid plastic packaging.','避免塑料包装。'),
    ('solution','səˈluːʃn','n.','解决方案','Find a green solution.','找一个绿色方案。'),
    ('effect','ɪˈfekt','n.','效果；影响','The effect of pollution is serious.','污染的影响很严重。'),
    ('cause','kɔːz','v./n.','引起；原因','What causes air pollution?','什么导致空气污染？'),
    ('action','ˈækʃn','n.','行动','Take action to save the planet.','采取行动拯救地球。'))
add(9,'u13','🥉','学霸词汇 · 冲刺满分',
    ('sustainable','səˈsteɪnəbl','adj.','可持续的','We need sustainable solutions.','我们需要可持续的解决方案。'),
    ('conservation','ˌkɒnsərˈveɪʃn','n.','保护','Energy conservation is important.','节约能源很重要。'),
    ('carbon','ˈkɑːrbən','n.','碳','Reduce your carbon footprint.','减少碳足迹。'),
    ('renewable','rɪˈnuːəbl','adj.','可再生的','Use renewable energy.','使用可再生能源。'),
    ('degrade','dɪˈɡreɪd','v.','降解','Plastic takes long to degrade.','塑料需要很长时间降解。'),
    ('legislation','ˌledʒɪˈsleɪʃn','n.','立法','Stronger legislation is needed.','需要更强有力的立法。'))

add(9,'u14','🥈','掌握词汇 · 回忆与毕业',
    ('remember','rɪˈmembər','v.','记住；回忆起','I remember my first day at school.','我记得上学的第一天。'),
    ('overcome','ˌoʊvərˈkʌm','v.','克服','We overcame all difficulties together.','我们一起克服了所有困难。'),
    ('graduate','ˈɡrædʒueɪt','v.','毕业','We will graduate next month.','我们下个月毕业。'),
    ('separate','ˈseprət','v./adj.','分开；分离','Don\'t be sad about separation.','别为分离而伤心。'),
    ('caring','ˈkerɪŋ','adj.','关心他人的','She is a caring teacher.','她是一位关心学生的老师。'),
    ('encourage','ɪnˈkɜːrɪdʒ','v.','鼓励','Teachers encouraged us a lot.','老师们给了我们很多鼓励。'),
    ('responsible','rɪˈspɒnsəbl','adj.','负责的','Be responsible for your future.','对自己的未来负责。'),
    ('achievement','əˈtʃiːvmənt','n.','成就','Graduation is a big achievement.','毕业是一项大成就。'),
    ('pride','praɪd','n.','骄傲；自豪','We take pride in our school.','我们为学校感到骄傲。'),
    ('memory','ˈmeməri','n.','记忆；回忆','Cherish the good memories.','珍惜美好的回忆。'))
add(9,'u14','🥉','学霸词汇 · 冲刺满分',
    ('cherish','ˈtʃerɪʃ','v.','珍惜；珍视','Cherish every moment.','珍惜每一刻。'),
    ('nostalgic','nɒˈstældʒɪk','adj.','怀旧的','Looking at photos makes me nostalgic.','看照片让我怀旧。'),
    ('farewell','ˌferˈwel','n./interj.','告别；再见','Say farewell to your classmates.','向同学告别。'),
    ('milestone','ˈmaɪlstoʊn','n.','里程碑','Graduation is a milestone.','毕业是人生里程碑。'),
    ('bond','bɒnd','n.','纽带；联系','The bond between classmates is strong.','同学之间的纽带很牢固。'),
    ('legacy','ˈleɡəsi','n.','遗产；传承','Leave a positive legacy.','留下积极的传承。'))

# ============================================================
# Injection
# ============================================================
def inject(filepath, tiers):
    with open(filepath) as f:
        html = f.read()
    pattern = r'(<details class="module" open><summary>📝 重点词汇.*?</details>)'
    m = re.search(pattern, html, re.DOTALL)
    if not m:
        print(f'  ❌ No vocab section in {filepath}')
        return False
    insert_at = m.end()
    new_content = ''
    for icon, title, words in tiers:
        cards = '\n'.join(W(*t) for t in words)
        new_content += '\n' + MOD(icon, title, cards)
    html = html[:insert_at] + new_content + '\n' + html[insert_at:]
    with open(filepath, 'w') as f:
        f.write(html)
    return True

if __name__ == '__main__':
    by_file = {}
    for (grade, unit), tiers in D.items():
        path = f'english{grade}/{unit}.html'
        if not os.path.exists(path):
            print(f'  ⏭ {path} not found')
            continue
        by_file[path] = tiers
    
    count = 0
    for path, tiers in sorted(by_file.items()):
        if inject(path, tiers):
            count += 1
            print(f'  ✅ {os.path.basename(path)}')
    print(f'\nDone: {count} files updated')
