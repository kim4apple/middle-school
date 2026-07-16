#!/usr/bin/env python3
"""Add learning features to all 24 unit HTML files."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = [f for f in os.listdir(BASE) if f.endswith('.html') and f not in ['index.html', 'appendix-grammar.html', 'appendix-vocab.html']]

def add_after(content, marker, new_html):
    """Insert new_html after the first occurrence of marker."""
    pos = content.find(marker)
    if pos == -1:
        return content
    pos += len(marker)
    return content[:pos] + '\n' + new_html + content[pos:]

def add_js_before_end(content, js_block):
    """Insert JS block before the final </script> tag."""
    pos = content.rfind('</script>')
    if pos == -1:
        return content
    return content[:pos] + js_block + '\n' + content[pos:]

def process_file(fpath):
    with open(fpath) as f:
        content = f.read()
    fname = os.path.basename(fpath)
    modified = False

    # ======== 1. Listening Module ========
    if '🎧 听力训练' not in content:
        # Find dialogue English lines to use as audio source
        en_texts = re.findall(r'data-speak="([^"]*)"', content)
        en_texts = [t for t in en_texts if re.search(r'[a-zA-Z]{4,}', t)][:3]
        
        listening_html = '''<!-- ====== 听力训练 ====== -->
<details class="module">
  <summary>🎧 听力训练 · Listen and choose</summary>
  <div class="content">
    <p style="font-size:14px;color:var(--text-secondary);margin-bottom:12px;">听句子，选择正确答案。</p>
'''
        for i, text in enumerate(en_texts):
            qid = f'listening_q_{i+1}'
            listening_html += f'''    <div class="listening-q" style="margin-bottom:16px;padding:12px;border:1px solid var(--border);border-radius:6px;">
      <p><span class="wotd-say" data-speak="{text}">🔊 {i+1}. 点击播放句子</span></p>
      <label style="display:block;margin:4px 0;font-size:14px;"><input type="radio" name="{qid}" value="A"> A. 正确理解</label>
      <label style="display:block;margin:4px 0;font-size:14px;"><input type="radio" name="{qid}" value="B"> B. 部分理解</label>
      <label style="display:block;margin:4px 0;font-size:14px;"><input type="radio" name="{qid}" value="C"> C. 需要重听</label>
      <button class="listening-check" style="margin-top:6px;font-size:11px;padding:2px 10px;border:1px solid var(--border);border-radius:4px;background:var(--bg);cursor:pointer;color:var(--accent);" onclick="this.nextElementSibling.style.display='block';this.disabled=true;">✅ 确认</button>
      <span style="display:none;font-size:12px;color:var(--text-secondary);margin-left:8px;">请核对原文理解。</span>
    </div>
</details>
'''
        # Find insertion point: after 课文精讲 closing </details>
        lesson_end = content.find('<!-- ====== 重点词汇')
        if lesson_end > 0:
            content = content[:lesson_end] + listening_html + '\n' + content[lesson_end:]
            modified = True

    # ======== 2. Grammar Quiz ========
    if 'grammar-quiz' not in content:
        grammar_quiz = '''<div class="grammar-quiz" style="margin-top:12px;padding:12px;background:var(--bg-secondary);border-radius:6px;font-size:14px;">
        <p style="font-weight:600;margin-bottom:8px;">📝 语法小测</p>
        <p style="margin-bottom:6px;">1. 请判断：以下哪个句子语法正确？</p>
        <label style="display:block;margin:2px 0;"><input type="radio" name="gq1" value="A"> A. 选项A</label>
        <label style="display:block;margin:2px 0;"><input type="radio" name="gq1" value="B"> B. 选项B</label>
        <label style="display:block;margin:2px 0;"><input type="radio" name="gq1" value="C"> C. 选项C</label>
        <button class="gq-check" style="margin-top:6px;font-size:11px;padding:2px 10px;border:1px solid var(--border);border-radius:4px;background:var(--bg);cursor:pointer;color:var(--accent);" onclick="var r=this.parentElement.querySelector('input:checked');if(!r){alert('请先选择一个选项');return;}r.value==='B'?this.nextElementSibling.textContent='✅ 正确！':this.nextElementSibling.textContent='❌ 再想想';this.nextElementSibling.style.display='inline';">检查答案</button>
        <span style="display:none;margin-left:8px;font-size:12px;"></span>
      </div>'''
        # Insert after the last grammar table
        # Find the last </table> in the grammar section
        g_start = content.find('语法聚焦')
        if g_start > 0:
            g_end = content.find('三级闯关', g_start)
            if g_end > g_start:
                section = content[g_start:g_end]
                last_table = section.rfind('</table>')
                if last_table > 0:
                    abs_pos = g_start + last_table + len('</table>')
                    content = content[:abs_pos] + '\n' + grammar_quiz + content[abs_pos:]
                    modified = True

    # ======== 3. Oral Output ========
    if '🎙️ 口头输出' not in content:
        # Find unit topic from existing content
        dialogue_texts = re.findall(r'data-speak="([^"]*)"', content)
        dialogue_texts = [t for t in dialogue_texts if len(t) > 10 and len(t) < 80][:3]
        
        oral_html = '''<!-- ====== 口头输出 ====== -->
<details class="module detail-module">
  <summary>🎙️ 口头输出 · Speak aloud</summary>
  <div class="content">
    <p style="font-size:14px;color:var(--text-secondary);margin-bottom:12px;">用英语回答以下问题，练习口语表达。</p>
    <ol style="font-size:14px;line-height:2;">
'''
        for i, t in enumerate(dialogue_texts[:3]):
            oral_html += f'      <li><span class="wotd-say" data-speak="{t}">🔊 {t}</span></li>\n'
        oral_html += '''    </ol>
  </div>
</details>
'''
        # Insert before 微写作
        wx_start = content.find('微写作')
        if wx_start > 0:
            content = content[:wx_start] + oral_html + '\n' + content[wx_start:]
            modified = True

    # ======== 4. Mnemonic Tips ========
    if 'mnemonic' not in content:
        # Add mnemonic JS toggle
        mnemonic_js = '''
  // ===== Mnemonic toggle =====
  document.addEventListener('click', function(e) {
    var t = e.target;
    if (t.classList.contains('mnemonic')) {
      var detail = t.nextElementSibling;
      if (detail && detail.classList.contains('mnemonic-detail')) {
        detail.style.display = detail.style.display === 'block' ? 'none' : 'block';
      }
    }
  });'''
        
        # Use simple mnemonics based on headword
        mnemonics_map = {
            'pencil': 'pen + cil → 钢笔+橡皮擦头',
            'eraser': 'erase(擦除) + r → 橡皮就是用来擦的',
            'ruler': 'rule(规则) + r → 尺子用来画直线(规则)',
            'schoolbag': 'school(学校) + bag(包) → 书包',
            'dictionary': 'dict(说) + ionary → 告诉你词怎么说',
            'notebook': 'note(笔记) + book(本子) → 笔记本',
            'pencil case': '装 pencil 的 case(盒子) → 铅笔盒',
            'watch': 'watch(看) → 用来看时间的手表',
            'ring': 'ring(响) → 戒指/铃声 同形异义词',
            'ID card': 'ID(身份) + card(卡) → 身份证/学生证',
            'pencil box': '装 pencil 的 box(盒子) → 铅笔盒',
            'teacher': 'teach(教) + er(人) → 教书的人',
            'student': 'study(学习) 变 → 学习的人',
            'classroom': 'class(班级) + room(房间) → 教室',
            'bookcase': 'book(书) + case(箱子) → 书柜',
            'backpack': 'back(背) + pack(包) → 背包',
            'baseball': 'base(垒) + ball(球) → 棒球',
            'volleyball': 'volley(截击) + ball(球) → 排球',
            'basketball': 'basket(篮子) + ball(球) → 篮球',
            'soccer': '足球的别称 → 英式足球',
            'tennis': '网球 → 联想 ten(十)个球',
            'banana': 'ba-na-na → 三个音节像香蕉的形状',
            'hamburger': 'ham(火腿) + burger(汉堡) → 汉堡包',
            'sandwich': ' Sandwich(地名) → 三明治的起源',
            'carrot': 'car(车) + rot(腐烂) → 胡萝卜不能放车里',
            'chicken': 'chick(小鸡) + en → 鸡肉/小鸡',
            'breakfast': 'break(打破) + fast(禁食) → 打破禁食→早餐',
            'lunch': '联想 lunch(午餐)和 launch(发射)→补充能量',
            'dinner': 'din(喧闹) + ner → 晚餐时最热闹',
            'socks': 'sock → 短袜，像蛇(s)穿袜子(ock)',
            'shoes': 'shoe → 鞋，sh像两个鞋柜',
            'shirt': 'sh像衬衫领口 + irt → 衬衫',
            'sweater': 'sweat(汗) + er → 穿毛衣会出汗',
            'jacket': 'jack(杰克) + et → 杰克的外套',
            'trousers': 'trouser(裤子) → 复数表示一条裤子',
            'skirt': 'sk(像裙摆) + irt → 短裙',
            'hat': 'h像帽檐 + at在→帽子在头上',
            'birthday': 'birth(出生) + day(日子) → 生日',
            'party': 'part(部分) + y → 大家聚在一起→派对',
            'month': 'mon(月亮) + th → 月亮绕地球一周→月',
            'January': 'Janus(罗马门神) + uary → 一月→辞旧迎新',
            'February': 'Februa(净化) + ruary → 二月→古罗马净化月',
            'March': 'Mars(战神马尔斯) → 三月→出征的月份',
            'April': 'Aphrodite(维纳斯) → 四月→爱神之月',
            'May': 'Maia(迈亚) → 五月→春回大地',
            'June': 'Juno(朱诺) → 六月→天后之月',
            'July': 'Julius Caesar(凯撒) → 七月→凯撒之月',
            'August': 'Augustus(奥古斯都) → 八月→奥古斯都之月',
            'September': 'septem(七) → 原来七月→九月',
            'October': 'octo(八) → 原来八月→十月',
            'November': 'novem(九) → 原来九月→十一月',
            'December': 'decem(十) → 原来十月→十二月',
            'science': 'sci(知道) + ence → 科学让人知道更多',
            'history': 'his(他的) + story(故事) → 历史是他的故事',
            'geography': 'geo(地球) + graphy(写) → 写地球→地理',
            'music': 'Muse(缪斯女神) + ic → 音乐是缪斯的艺术',
            'math': 'math(数学) → 联想 math(计算)',
            'English': 'Eng(英格兰) + lish → 英语来自英格兰',
            'Chinese': 'Chin(China) + ese → 中国人/语文',
            'art': 'art(艺术) → 美术就是艺术',
            'guitar': 'gui(归) + tar(他) → 吉他声引人归',
            'piano': 'pi(皮) + ano → 钢琴有黑白键',
            'violin': 'vi(提琴形状) + olin → 小提琴',
            'drum': 'dr(打) + um(鼓声) → 鼓',
            'swim': 's(像水波) + wim → 游泳划水',
            'sing': 's(声) + ing(正在) → 正在发声→唱歌',
            'dance': 'dan(跳) + ce → 跳舞就是有节奏地跳',
            'draw': 'd(画) + raw(草图) → 画画从草图开始',
            'chess': 'che(车) + ss → 象棋里有車',
            'club': 'cl(一群) + ub → 社团是一群人',
            'story': 'st(讲述) + ory → 讲故事',
            'rain': 'r(像雨点) + ain → 雨点落下来',
            'sunny': 'sun(太阳) + ny → 阳光明媚',
            'cloudy': 'cloud(云) + y → 多云的',
            'windy': 'wind(风) + y → 有风的',
            'snowy': 'snow(雪) + y → 下雪的',
            'warm': 'war(战争)→ 打仗就热了→暖和的',
            'cold': 'cold → 联想 cool(凉爽)更冷→寒冷的',
            'hot': 'hot → 太热了(h在喘气)',
            'weather': 'we(我们) + ather → 我们关心的天气',
            'spring': 'spr(像发芽) + ing → 春天万物生长',
            'summer': 'sum(总和) + mer → 夏天阳光最充足',
            'autumn': 'au(金) + tumn → 金色的秋天',
            'winter': 'win(赢) + ter → 冬天过去就是春',
            'hospital': 'hosp(客人) + ital → 医院里都是"客人"',
            'restaurant': 'rest(休息) + aurant → 餐馆是休息吃饭的地方',
            'supermarket': 'super(超级) + market(市场) → 超市',
            'library': 'libr(书) + ary(场所) → 图书馆是书的场所',
            'museum': 'Muse(缪斯) + um(场所) → 博物馆是艺术之殿',
            'station': 'stat(站立) + ion → 车站是车停的地方',
            'street': 'st(石头)+reet → 街道从前是石头路',
            'bridge': 'b(像桥拱)+ridge(脊) → 桥像脊背',
            'park': 'park(停车) → 公园可以停车休息',
            'bank': 'bank(长凳) → 银行最初是长凳上的兑换处',
            'hotel': 'host(主人)+el → 旅馆是主人招待客人的地方',
            'noodle': 'n(像面条)+oodle → 面条又细又长',
            'dumpling': 'dum(团)+pling → 面团捏成的→饺子',
            'rice': 'r(像米粒)+ice → 米像冰粒',
            'meat': 'm(像肉块)+eat(吃) → 肉是用来吃的',
            'soup': 's(用勺子)+oup → 汤要用勺子喝',
            'salad': 'sal(盐)+ad → 沙拉要加盐',
            'juice': 'ju(juicy多汁)+ice → 果汁像冰爽的汁液',
            'milk': 'mi(蜜)+lk → 牛奶甜甜的像蜜',
            'water': 'wa(哇)+ter → 哇，水！',
            'tea': 't(像茶壶)+ea → 茶壶里泡茶',
            'coffee': 'co(咖啡色)+ffee → 咖啡是棕色的',
            'cabbage': 'cab(出租车)+bage → 卷心菜像出租车?联想记忆',
            'potato': 'po(破)+tato → 土豆煮熟就破皮',
            'tomato': 'to(到)+mato → 番茄(西红柿)',
            'beef': 'b(牛)+eef → 牛肉',
            'chicken': 'chick(小鸡)+en → 鸡肉从小鸡来',
            'fish': 'f(像鱼形)+ish → 鱼',
            'egg': 'e(像鸡蛋形)+gg → 鸡蛋',
            'candy': 'can(能)+dy → 吃糖能开心',
            'cookie': 'cook(烹饪)+ie → 小饼干是烤出来的',
            'cake': 'c(像蛋糕切面)+ake → 蛋糕',
            'ice cream': 'ice(冰)+cream(奶油) → 冰淇淋',
            'trip': 'trip(绊倒) → 旅行中可能会绊倒',
            'museum': '同前→博物馆',
            'farm': 'f(像田地)+arm(手臂) → 用双手种田',
            'yesterday': 'yester(昨)+day(天) → 昨天',
            'weekend': 'week(星期)+end(结束) → 周末',
            'Monday': 'moon(月亮)+day → 周一=月曜日',
            'Tuesday': 'Tyr(战神)+day → 周二=火曜日',
            'Wednesday': 'Odin(主神)+day → 周三=水曜日',
            'Thursday': 'Thor(雷神)+day → 周四=木曜日',
            'Friday': 'Frigg(爱神)+day → 周五=金曜日',
            'Saturday': 'Saturn(土星)+day → 周六=土曜日',
            'Sunday': 'sun(太阳)+day → 周日=日曜日',
        }

        # After each .definition, add mnemonic trigger + detail
        def add_mnemonic(m):
            def_text = m.group(0)
            if 'mnemonic' in def_text:
                return def_text
            # Find the vocab-card this definition belongs to
            # Look back to find the headword
            card_start = content.rfind('<div class="vocab-card"', 0, m.start())
            if card_start == -1:
                return def_text
            card_content = content[card_start:m.end()]
            hw = re.search(r'data-speak="([^"]*)"', card_content)
            if not hw:
                return def_text
            word = hw.group(1).lower()
            mnemonic = mnemonics_map.get(word, f'联想记忆法：{word}')
            return def_text + f'\n        <span class="mnemonic" style="font-size:11px;color:var(--accent);cursor:pointer;margin-top:2px;display:inline-block;">💡 记</span><div class="mnemonic-detail" style="display:none;font-size:12px;color:var(--text-secondary);padding:4px 8px;background:var(--bg-secondary);border-radius:4px;margin-top:2px;">{mnemonic}</div>'
        
        content = re.sub(r'<div class="definition">[^<]*</div>', add_mnemonic, content)
        content = add_js_before_end(content, mnemonic_js)
        modified = True

    if modified:
        with open(fpath, 'w') as f:
            f.write(content)
        print(f'  {fname}: updated')
    else:
        print(f'  {fname}: no changes needed')

if __name__ == '__main__':
    print('Upgrading unit files with learning features...')
    for fname in sorted(FILES):
        process_file(os.path.join(BASE, fname))
    print('Done.')
