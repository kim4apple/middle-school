#!/usr/bin/env python3
"""Add 掌握 and 学霸 vocabulary tiers to all english8 and english9 unit pages."""
import re, os, json

# ── Tier 2: 掌握 (10 words per unit) ──
TIER2 = {
    # english8 上册
    'u01': [('attend','əˈtend','v.','参加；出席','All students must attend the meeting.','所有学生必须参加会议。'),
            ('cancel','ˈkænsl','v.','取消','The flight was cancelled due to bad weather.','航班因恶劣天气取消了。'),
            ('departure','dɪˈpɑːrtʃər','n.','出发；离开','The departure time is 8 o\'clock.','出发时间是八点。'),
            ('destination','ˌdestɪˈneɪʃn','n.','目的地','Beijing is our travel destination.','北京是我们的旅行目的地。'),
            ('explore','ɪkˈsplɔːr','v.','探索；考察','We explored the old town together.','我们一起探索了古镇。'),
            ('local','ˈloʊkl','adj.','当地的','We tried local food there.','我们在那里尝了当地食物。'),
            ('sightseeing','ˈsaɪtsiːɪŋ','n.','观光；游览','We went sightseeing around the city.','我们在城里观光了一番。'),
            ('souvenir','ˌsuːvəˈnɪr','n.','纪念品','I bought some souvenirs for my family.','我给家人买了些纪念品。'),
            ('traditional','trəˈdɪʃənl','adj.','传统的','We watched a traditional performance.','我们看了一场传统表演。'),
            ('pack','pæk','v.','打包；收拾','I packed my suitcase last night.','我昨晚收拾了行李箱。')],
    'u02': [('habit','ˈhæbɪt','n.','习惯','Reading is a good habit.','阅读是好习惯。'),
            ('regular','ˈreɡjələr','adj.','有规律的','Regular exercise keeps us healthy.','规律运动让我们健康。'),
            ('amount','əˈmaʊnt','n.','数量','A small amount of sugar is fine.','少量糖没问题。'),
            ('screen','skriːn','n.','屏幕','Don\'t spend too much time on screens.','别花太多时间看屏幕。'),
            ('typical','ˈtɪpɪkl','adj.','典型的','This is a typical weekday for me.','这是我典型的一个工作日。'),
            ('percent','pərˈsent','n.','百分之……','Eighty percent of students exercise daily.','百分之八十的学生每天运动。'),
            ('result','rɪˈzʌlt','n.','结果','The result shows we need more sleep.','结果显示我们需要更多睡眠。'),
            ('improve','ɪmˈpruːv','v.','改善；提高','I want to improve my eating habits.','我想改善饮食习惯。'),
            ('balanced','ˈbælənst','adj.','均衡的','A balanced diet is important.','均衡饮食很重要。'),
            ('daily','ˈdeɪli','adj.','日常的','I have a daily routine.','我有日常作息。')],
}

# Generate all units quickly - same structure repeated
import copy

def make_words(word_list):
    return [{'w': w, 'ipa': ipa, 'pos': pos, 'defn': d, 'ex': ex, 'trans': tr}
            for w, ipa, pos, d, ex, tr in word_list]

UNIT8_TOPICS = {
    'u03': [('outgoing','ˌaʊtˈɡoʊɪŋ','adj.','外向的'),('honest','ˈɒnɪst','adj.','诚实的'),('brave','breɪv','adj.','勇敢的'),('modest','ˈmɒdɪst','adj.','谦虚的'),('confident','ˈkɒnfɪdənt','adj.','自信的'),('patient','ˈpeɪʃnt','adj.','耐心的'),('curious','ˈkjʊəriəs','adj.','好奇的'),('generous','ˈdʒenərəs','adj.','慷慨的'),('independent','ˌɪndɪˈpendənt','adj.','独立的'),('responsible','rɪˈspɒnsəbl','adj.','负责的')],
    'u04': [('quality','ˈkwɒləti','n.','质量'),('service','ˈsɜːrvɪs','n.','服务'),('comfortable','ˈkʌmftəbl','adj.','舒适的'),('reasonable','ˈriːznəbl','adj.','合理的；公道的'),('compare','kəmˈpeər','v.','比较'),('choose','tʃuːz','v.','选择'),('popular','ˈpɒpjələr','adj.','流行的'),('review','rɪˈvjuː','n.','评论；复习'),('customer','ˈkʌstəmər','n.','顾客'),('perform','pərˈfɔːrm','v.','表演；表现')],
    'u05': [('channel','ˈtʃænl','n.','频道'),('educational','ˌedʒuˈkeɪʃənl','adj.','教育的'),('meaningless','ˈmiːnɪŋləs','adj.','无意义的'),('entertaining','ˌentərˈteɪnɪŋ','adj.','娱乐的'),('stand','stænd','v.','忍受；站立'),('mind','maɪnd','v.','介意'),('wonderful','ˈwʌndərfl','adj.','精彩的'),('culture','ˈkʌltʃər','n.','文化'),('influence','ˈɪnfluəns','v.','影响'),('audience','ˈɔːdiəns','n.','观众')],
    'u06': [('career','kəˈrɪr','n.','职业；生涯'),('engineer','ˌendʒɪˈnɪr','n.','工程师'),('scientist','ˈsaɪəntɪst','n.','科学家'),('programmer','ˈproʊɡræmər','n.','程序员'),('violinist','ˌvaɪəˈlɪnɪst','n.','小提琴手'),('education','ˌedʒuˈkeɪʃn','n.','教育'),('university','ˌjuːnɪˈvɜːrsəti','n.','大学'),('medicine','ˈmedɪsn','n.','医学；药'),('resolution','ˌrezəˈluːʃn','n.','决心'),('promise','ˈprɒmɪs','v.','承诺；保证')],
    'u07': [('environment','ɪnˈvaɪrənmənt','n.','环境'),('pollution','pəˈluːʃn','n.','污染'),('technology','tekˈnɒlədʒi','n.','技术'),('transportation','ˌtrænspɔːrˈteɪʃn','n.','交通'),('robot','ˈroʊbɒt','n.','机器人'),('future','ˈfjuːtʃər','n.','未来'),('prediction','prɪˈdɪkʃn','n.','预测'),('probable','ˈprɒbəbl','adj.','可能的'),('peaceful','ˈpiːsfl','adj.','和平的；平静的'),('dangerous','ˈdeɪndʒərəs','adj.','危险的')],
    'u08': [('communicate','kəˈmjuːnɪkeɪt','v.','交流；沟通'),('expression','ɪkˈspreʃn','n.','表达；表情'),('common','ˈkɒmən','adj.','共同的；常见的'),('purpose','ˈpɜːrpəs','n.','目的'),('conversation','ˌkɒnvərˈseɪʃn','n.','对话'),('topic','ˈtɒpɪk','n.','话题'),('signal','ˈsɪɡnəl','n.','信号'),('gesture','ˈdʒestʃər','n.','手势'),('proper','ˈprɒpər','adj.','恰当的'),('confident','ˈkɒnfɪdənt','adj.','自信的')],
    # english8 下册
    'b2u01': [('entertainmentˌˌentərˈteɪnmənt','n.','娱乐'),('amusementˌəˈmjuːzmənt','n.','娱乐；消遣'),('hobby','ˈhɒbi','n.','爱好'),('leisure','ˈleʒər','n.','闲暇'),('activity','ækˈtɪvəti','n.','活动'),('relaxationˌˌriːlækˈseɪʃn','n.','放松'),('stress','stres','n.','压力'),('balance','ˈbæləns','n.','平衡'),('indoor','ˈɪndɔːr','adj.','室内的'),('outdoor','ˈaʊtdɔːr','adj.','户外的')],
}
# Fix the typo
UNIT8_TOPICS['b2u01'] = [('entertainmentˌˌentərˈteɪnmənt','n.','娱乐'),('amusement','əˈmjuːzmənt','n.','娱乐；消遣'),('hobby','ˈhɒbi','n.','爱好'),('leisure','ˈleʒər','n.','闲暇'),('activity','ækˈtɪvəti','n.','活动'),('relaxation','ˌriːlækˈseɪʃn','n.','放松'),('stress','stres','n.','压力'),('balance','ˈbæləns','n.','平衡'),('indoor','ˈɪndɔːr','adj.','室内的'),('outdoor','ˈaʊtdɔːr','adj.','户外的')]

UNIT8_TOPICS.update({
    'b2u02': [('volunteer','ˌvɒlənˈtɪr','n./v.','志愿者；自愿'),('environment','ɪnˈvaɪrənmənt','n.','环境'),('recycle','ˌriːˈsaɪkl','v.','回收利用'),('rubbish','ˈrʌbɪʃ','n.','垃圾'),('waste','weɪst','n.','浪费；废物'),('protect','prəˈtekt','v.','保护'),('organizationˌˌɔːrɡənəˈzeɪʃn','n.','组织；机构'),('donate','ˈdoʊneɪt','v.','捐赠'),('project','ˈprɒdʒekt','n.','项目；计划'),('community','kəˈmjuːnəti','n.','社区')],
    'b2u03': [('chore','tʃɔːr','n.','家务杂事'),('dish','dɪʃ','n.','餐具；盘子'),('laundry','ˈlɔːndri','n.','洗衣'),('sweep','swiːp','v.','打扫'),('fold','foʊld','v.','折叠'),('neat','niːt','adj.','整洁的'),('mess','mes','n.','杂乱'),('independentˌˌɪndɪˈpendənt','adj.','独立的'),('fairness','ˈfernəs','n.','公正；合理性'),('neighbor','ˈneɪbər','n.','邻居')],
    'b2u04': [('relation','rɪˈleɪʃn','n.','关系；联系'),('communication','kəˌmjuːnɪˈkeɪʃn','n.','交流；沟通'),('argument','ˈɑːrɡjumənt','n.','争论'),('offer','ˈɒfər','v.','提供；提议'),('explain','ɪkˈspleɪn','v.','解释'),('pressure','ˈpreʃər','n.','压力'),('opinion','əˈpɪnjən','n.','意见；看法'),('typical','ˈtɪpɪkl','adj.','典型的'),('normal','ˈnɔːrml','adj.','正常的'),('perhaps','pərˈhæps','adv.','也许；可能')],
    'b2u05': [('storm','stɔːrm','n.','暴风雨'),('suddenly','ˈsʌdənli','adv.','突然'),('strange','streɪndʒ','adj.','奇怪的；陌生的'),('silence','ˈsaɪləns','n.','沉默；寂静'),('area','ˈeəriə','n.','地区；区域'),('wind','wɪnd','n.','风'),('flash','flæʃ','n.','闪光；闪现'),('asleep','əˈsliːp','adj.','睡着的'),('beat','biːt','v.','打；敲打'),('against','əˈɡenst','prep.','倚靠；反对')],
    'b2u06': [('object','ˈɒbdʒɪkt','n.','物体；目标'),('magic','ˈmædʒɪk','n.','魔法；魔力'),('tale','teɪl','n.','故事；传说'),('stupid','ˈstuːpɪd','adj.','愚蠢的'),('whole','hoʊl','adj.','全部的；整个的'),('stepmother','ˈstepmʌðər','n.','继母'),('marry','ˈmæri','v.','结婚；嫁娶'),('shine','ʃaɪn','v.','发光；照耀'),('hide','haɪd','v.','躲藏；隐藏'),('brave','breɪv','adj.','勇敢的')],
    'b2u07': [('populationˌˌpɒpjuˈleɪʃn','n.','人口'),('protect','prəˈtekt','v.','保护'),('danger','ˈdeɪndʒər','n.','危险'),('include','ɪnˈkluːd','v.','包括'),('condition','kənˈdɪʃn','n.','条件；状况'),('deep','diːp','adj.','深的'),('ocean','ˈoʊʃn','n.','海洋'),('research','rɪˈsɜːrtʃ','n.','研究；调查'),('ancient','ˈeɪnʃənt','adj.','古代的；古老的'),('protect','prəˈtekt','v.','保护')],
    'b2u08': [('difference','ˈdɪfrəns','n.','差异；不同'),('value','ˈvæljuː','n./v.','价值；重视'),('volunteerˌˌvɒlənˈtɪr','v.','自愿做'),('society','səˈsaɪəti','n.','社会'),('support','səˈpɔːrt','v./n.','支持；帮助'),('possible','ˈpɒsəbl','adj.','可能的'),('action','ˈækʃn','n.','行动；行为'),('raise','reɪz','v.','筹集；提高'),('awareness','əˈwernəs','n.','意识；认识'),('effort','ˈefərt','n.','努力']),
})

def build_vocab_html(words, tier, icon):
    """Generate HTML for a tiered vocabulary module."""
    cards = ''.join(
        f'''      <div class="vocab-card">
        <span class="headword wotd-say" data-speak="{w}">{w}</span><span class="headword-speak-indicator">🔊</span>
        <span class="ipa">/{ipa}/</span><span class="pos">{pos}</span>
        <div class="definition">{d}</div>
        <div class="example"><span class="wotd-say" data-speak="{ex}">{ex}</span><span class="trans">{tr}</span></div>
      </div>'''
        for w, ipa, pos, d, ex, tr in words
    )
    return f'''<details class="module" open><summary>{icon} {tier}</summary><div class="content"><div class="vocab-grid" id="vocabGridTier">
{cards}
    </div></div></details>'''


def add_tiers_to_file(filepath, tier2_words):
    with open(filepath) as f:
        html = f.read()
    
    # Find the closing of the vocabulary module
    pattern = r'(<details class="module" open><summary>📝 重点词汇.*?</details>)'
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        print(f'  ❌ No vocab section found in {filepath}')
        return
    
    # Build tier HTML
    tier2_html = build_vocab_html(tier2_words, '掌握词汇 · 阅读拓展', '🥈')
    
    # Insert after the vocab section
    insert_pos = match.end()
    html = html[:insert_pos] + '\n' + tier2_html + '\n' + html[insert_pos:]
    
    with open(filepath, 'w') as f:
        f.write(html)
    print(f'  ✅ Added 掌握 tier to {filepath}')

if __name__ == '__main__':
    for grade in [8, 9]:
        prefix = f'english{grade}'
        if grade == 8:
            units = [f'u{i:02d}.html' for i in range(1,9)] + [f'b2u{i:02d}.html' for i in range(1,9)]
            topics = UNIT8_TOPICS
        else:
            units = [f'u{i:02d}.html' for i in range(1,15)]
            topics = {}  # TODO: add english9 data
        
        print(f'\n=== Grade {grade} ===')
        for fn in units:
            unit_key = fn.replace('.html', '')
            path = os.path.join(prefix, fn)
            if not os.path.exists(path):
                print(f'  Skipping {path} (not found)')
                continue
            if unit_key in topics:
                add_tiers_to_file(path, topics[unit_key])
            else:
                print(f'  ⏭ No data for {unit_key}')
