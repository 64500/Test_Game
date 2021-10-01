# -*- coding:utf-8 -*-
import wx
import Gamer
import Start
# 导入需要的模块

JvBen1 = '''
新风暴：自从极东之地的金融波动之后，震坦和四岛社会已经
运转到了极限，人们纷纷追忆起三年前萨布林娜小姐在全国广
播里的讲话，高声唱起图书馆之歌来，似乎是可以念一首《海
燕》了。'''


class Frame1(wx.Frame):
    # 定义主窗口
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=-1, title="文字游戏:资本家模拟器", pos=(100, 100), size=(600, 640))
        panel = wx.Panel(self)
        title = wx.StaticText(panel, label='选择身份', pos=(100, 10))
        font = wx.Font(24, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)

        self.rb1 = wx.RadioButton(panel, -1, label='拳师', pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, -1, label='天龙人', pos=(10, 40))
        self.rb3 = wx.RadioButton(panel, -1, label='海龟贵物', pos=(10, 70))
        self.rb4 = wx.RadioButton(panel, -1, label='网抑云', pos=(10, 100))
        self.rb5 = wx.RadioButton(panel, -1, label='海獭（写手）', pos=(10, 130))
        self.rb6 = wx.RadioButton(panel, -1, label='做题家', pos=(10, 160))
        self.rb7 = wx.RadioButton(panel, -1, label='张献忠', pos=(10, 190))
        self.rb8 = wx.RadioButton(panel, -1, label='汉皇', pos=(10, 220))
        self.rb9 = wx.RadioButton(panel, -1, label='左壬', pos=(10, 250))
        self.rb10 = wx.RadioButton(panel, -1, label='码农', pos=(10, 280))
        self.rb11 = wx.RadioButton(panel, -1, label='老司机', pos=(10, 310))
        self.rb12 = wx.RadioButton(panel, -1, label='土木狗', pos=(10, 340))
        self.rb13 = wx.RadioButton(panel, -1, label='公知', pos=(10, 370))
        self.rb14 = wx.RadioButton(panel, -1, label='下水道', pos=(10, 400))
        self.rb15 = wx.RadioButton(panel, -1, label='社畜', pos=(10, 430))
        self.rb16 = wx.RadioButton(panel, -1, label='萌萌人', pos=(10, 460))
        self.rb17 = wx.RadioButton(panel, -1, label='X批', pos=(10, 490))
        self.rb18 = wx.RadioButton(panel, -1, label='电竞粉', pos=(10, 520))

        jieshao_String = '''
        拳师：分裂社会的恐怖分子，可以使用技能获得“CIA补贴“
        经常刺杀男性网约车司机,但该职业容易入狱，被击杀后会
        给击杀对象25个资源点（联机DLC）
                         '''
        self.title_2 = wx.StaticText(panel, label=jieshao_String, pos=(100, 60))
        self.Bind(wx.EVT_RADIOBUTTON, self.Click1, self.rb3)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click2, self.rb2)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click3, self.rb1)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click4, self.rb4)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click5, self.rb5)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click6, self.rb6)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click7, self.rb7)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click8, self.rb8)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click9, self.rb9)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click10, self.rb10)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click11, self.rb11)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click12, self.rb12)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click13, self.rb13)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click14, self.rb14)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click15, self.rb15)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click16, self.rb16)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click17, self.rb17)
        self.Bind(wx.EVT_RADIOBUTTON, self.Click18, self.rb18)

        self.TongYongShuXing1 = wx.CheckBox(panel, id=-1, label='天赋：量子速读', pos=(100, 150))
        self.TongYongShuXing2 = wx.CheckBox(panel, id=-1, label='天赋：海豹抽卡', pos=(100, 180))
        self.TongYongShuXing3 = wx.CheckBox(panel, id=-1, label='天赋：蓄意轰拳', pos=(100, 210))
        self.TongYongShuXing4 = wx.CheckBox(panel, id=-1, label='天赋：涩图雷达', pos=(100, 240))

        self.TongYongShuXing5 = wx.CheckBox(panel, id=-1, label='天赋：百毒不侵', pos=(240, 150))
        self.TongYongShuXing6 = wx.CheckBox(panel, id=-1, label='天赋：键盘钢琴', pos=(240, 180))
        self.TongYongShuXing7 = wx.CheckBox(panel, id=-1, label='天赋：祖安艺术', pos=(240, 210))
        self.TongYongShuXing8 = wx.CheckBox(panel, id=-1, label='天赋：电子越共', pos=(240, 240))

        self.TongYongShuXing9 = wx.CheckBox(panel, id=-1, label='天赋：打工皇帝', pos=(380, 150))
        self.TongYongShuXing10 = wx.CheckBox(panel, id=-1, label='天赋：手搓高达', pos=(380, 180))
        self.TongYongShuXing11 = wx.CheckBox(panel, id=-1, label='天赋：夜行物种', pos=(380, 210))
        self.TongYongShuXing12 = wx.CheckBox(panel, id=-1, label='天赋：肝脏变异', pos=(380, 240))

        self.title_3 = wx.StaticText(panel, label='身份天赋（不同的身份可选择不同的天赋）', pos=(100, 300))
        font2 = wx.Font(14, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.title_3.SetFont(font2)

        self.SFShuXing_1 = wx.CheckBox(panel, id=-1, label='天赋：战斗公主', pos=(100, 340))
        self.SFShuXing_2 = wx.CheckBox(panel, id=-1, label='天赋：煽动神言', pos=(240, 340))
        self.SFShuXing_3 = wx.CheckBox(panel, id=-1, label='天赋：CIA兼职', pos=(380, 340))

        ChuShi = ['道具卡：五仁月饼,事件卡：三分钟热度 X8', '道具卡：《解析入门》,资源卡：老家地皮',
                  '道具卡：索尼相机,数位画板,廉价吉他,《故事》'
                  , '事件卡：老家拆迁,道具卡：《火星英语四级》', '事件卡：基金大涨 X2,举报间谍 X1,资源卡：技能-成功韭菜的炒股经验']
        self.ChuShiZiYuan = wx.ComboBox(panel, id=-1, choices=ChuShi, pos=(100, 360))

        self.ZTLian = wx.StaticText(panel, id=-1,
                                    label='属性总结：\n综合能力值：' + str(Gamer.QuanShi.intelligence) +
                                          '初始资源点:' + str(Gamer.QuanShi.resources), pos=(100, 510))

        self.xb1 = wx.RadioButton(panel, -1, label='男', pos=(300, 10), style=wx.RB_GROUP)
        self.xb2 = wx.RadioButton(panel, -1, label='女', pos=(260, 10))

        self.XB = wx.StaticText(panel, id=-1, label='性别:男', pos=(300, 580))
        font3 = wx.Font(8, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.XB.SetFont(font3)

        self.QueDing = wx.Button(panel, -1, label='开始游戏', pos=(480, 560))
        self.Bind(wx.EVT_BUTTON, self.Start, self.QueDing)

        JvBen3 = '''
            黑太阳：新大陆的大火山爆发了，联邦国在一周之间分崩离析
            漫天尘埃遮蔽了阳光。阳之力的缺失导致灵异复苏，来自地狱
            的伟人回到了他忠诚的世界——’此去阎台招旧部，十万旌旗斩
            阎罗。’
                 '''

        self.BeiJie = wx.StaticText(panel, -1, label=JvBen1, pos=(60, 400))

        self.JB1 = wx.Button(panel, -1, label='新风暴', pos=(100, 380))
        self.JB2 = wx.Button(panel, -1, label='大洪水', pos=(200, 380))
        self.JB3 = wx.Button(panel, -1, label='黑太阳', pos=(300, 380))

        self.Bind(wx.EVT_BUTTON, self.InClick1, self.JB1)
        self.Bind(wx.EVT_BUTTON, self.InClick2, self.JB2)
        self.Bind(wx.EVT_BUTTON, self.InClick3, self.JB3)

        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick1, self.xb1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick2, self.xb2)

    def InClick1(self, event):
        JvBen1 = '''
            新风暴：自从极东之地的金融波动之后，震坦和四岛社会已经
            运转到了极限，人们纷纷追忆起三年前萨布林娜小姐在全国广
            播里的讲话，高声唱起图书馆之歌来，似乎是可以念一首《海
            燕》了。
                 '''
        self.BeiJie.SetLabel(JvBen1)

    def InClick2(self, event):
        JvBen2 = '''
            大洪水：资本家对自然资源的需求无穷无尽，三罗和震坦首先
            出现了能源危机，矛盾转移掩盖不了两极渐渐融化的冰川，洪
            水的时代要到来了。但东国的废水催生了一只庞大的海洋生物
            无人看见它的容貌，能看见它容貌的人都疯了。
                 '''
        self.BeiJie.SetLabel(JvBen2)

    def InClick3(self, event):
        JvBen3 = '''
            黑太阳：新大陆的大火山爆发了，联邦国在一周之间分崩离析
            漫天尘埃遮蔽了阳光。阳之力的缺失导致灵异复苏，来自地狱
            的导师回到了他奋斗的世界——’此去阎台招旧部，十万旌旗斩
            阎罗。’
                 '''
        self.BeiJie.SetLabel(JvBen3)

    def OnClick1(self, event):
        self.XB.SetLabel('性别:男')

    def OnClick2(self, event):
        self.XB.SetLabel('性别:女')

    def Click1(self, event):
        self.title_2.SetLabel('''
        海龟贵物：海外归来的高等生物，可以使用技能“在阳光下抽大麻”
        可以保持低焦虑值
        ''')
        self.SFShuXing_1.SetLabel('天赋：大闹公安')
        self.SFShuXing_2.SetLabel('天赋：西式自由')
        self.SFShuXing_3.SetLabel('天赋：高贵特权')

        self.ZTLian.SetLabel('属性总结：\n综合能力值：' + str(Gamer.HaiGui.intelligence) +
                             '初始资源点:' + str(Gamer.HaiGui.resources))

    def Click2(self, event):
        self.title_2.SetLabel('''
        天龙人：帝都的高等居民，可以使用技能“正黄旗贵族”
        额外获得大量资源点
        ''')
        self.SFShuXing_1.SetLabel('天赋：高雅贵族')
        self.SFShuXing_2.SetLabel('天赋：拆迁之家')
        self.SFShuXing_3.SetLabel('天赋：无压高考')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.TianLongRen.intelligence) +
                             '初始资源点:' + str(Gamer.TianLongRen.resources))

    def Click3(self, event):
        self.title_2.SetLabel('''
        拳师：分裂社会的恐怖分子，可以使用技能获得“CIA补贴“
        经常狂暴鸿儒冲国男性
        ''')
        self.SFShuXing_1.SetLabel('天赋：战斗公主')
        self.SFShuXing_2.SetLabel('天赋：煽动神言')
        self.SFShuXing_3.SetLabel('天赋：CIA兼职')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.QuanShi.intelligence) +
                             '初始资源点:' + str(Gamer.QuanShi.resources))

    def Click4(self, event):
        self.title_2.SetLabel('''
        网抑云：在网络平台上传播负能量的生物，可以使用技能”口红割腕“
        经常在半夜听歌时狂暴流泪，疑似压力过大导致的压力马斯内
        ''')
        self.SFShuXing_1.SetLabel('天赋：生不出人')
        self.SFShuXing_2.SetLabel('天赋：口红割腕')
        self.SFShuXing_3.SetLabel('天赋：嘤嘤嘤嘤')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(Gamer.WangYiYun.intelligence) +
                             '初始资源点:' + str(Gamer.WangYiYun.resources))

    def Click5(self, event):
        self.title_2.SetLabel('''
        网文作家：除了跨性别繁殖之外，几乎什么都懂一点，可以使用
        技能‘芝加哥打字机’，但部分写手会要求别人删文——“你能删一个小时吗”
        ''')
        self.SFShuXing_1.SetLabel('天赋：鸽子煲汤')
        self.SFShuXing_2.SetLabel('天赋：鸽子炒肉')
        self.SFShuXing_3.SetLabel('天赋：鸽子油炸')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(Gamer.TaTa.intelligence) +
                             '初始资源点:' + str(Gamer.TaTa.resources))

    def Click6(self, event):
        self.title_2.SetLabel('''
        做题家（卷王）：从小卷到大的鬼才，部分人的目标是去拱了城里的白菜
        但由于经常高强度996和偶尔007，卷怪的身体强度一日不如一日。
        ''')
        self.SFShuXing_1.SetLabel('天赋：豪车土猪')
        self.SFShuXing_2.SetLabel('天赋：五三模拟')
        self.SFShuXing_3.SetLabel('天赋：铁人意志')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(Gamer.ZuoTiJia.intelligence) +
                             '初始资源点:' + str(Gamer.ZuoTiJia.resources))

    def Click7(self, event):
        self.title_2.SetLabel('''
        张献忠：我决定那个从今天开始杀人，一天杀一个，直到那个过年。
        杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀杀。
        ''')
        self.SFShuXing_1.SetLabel('天赋：高效屠戮')
        self.SFShuXing_2.SetLabel('天赋：魔怔狂热')
        self.SFShuXing_3.SetLabel('天赋：超级加速')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(Gamer.ZhuanXianZong.intelligence) +
                             '初始资源点:' + str(Gamer.ZhuanXianZong.resources))

    def Click8(self, event):
        self.title_2.SetLabel('''
        大民族主义：我们震坦真是太厉害啦！永恒之城其实是震坦人建造的！西方
        金字塔是波拿巴超人一人抗五万吨石块一个月造起来欺骗国民的！
        天子守国门！君王死社稷！嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷！！！
        ''')
        self.SFShuXing_1.SetLabel('天赋：伟大国度')
        self.SFShuXing_2.SetLabel('天赋：民族狂热')
        self.SFShuXing_3.SetLabel('天赋：尼哥猎手')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.HanHuang.intelligence) +
                             '初始资源点:' + str(Gamer.HanHuang.resources))

    def Click9(self, event):
        self.title_2.SetLabel('''
        左翼：异端最可怕啦！呼啦啦，发动魔法——革你左籍！
        哎，怎么说好呢，好难写哦——苏，马，列，托，猫，甚至
        还有那呼啦呼啦呼啦的安娜其~~~
        ''')
        self.SFShuXing_1.SetLabel('天赋：革你左籍')
        self.SFShuXing_2.SetLabel('天赋：冲击水晶')
        self.SFShuXing_3.SetLabel('天赋：下乡实践')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.GeMingDang.intelligence) +
                             '初始资源点:' + str(Gamer.GeMingDang.resources))

    def Click10(self, event):
        self.title_2.SetLabel('''
        程序员：程序和我，有一个能跑就行。
        整体屎山挖粪，应该去买一瓶护发水来着————
        ''')
        self.SFShuXing_1.SetLabel('天赋：删库跑路')
        self.SFShuXing_2.SetLabel('天赋：我即天网')
        self.SFShuXing_3.SetLabel('天赋：电子幽灵')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.MaNon.intelligence) +
                             '初始资源点:' + str(Gamer.MaNon.resources))

    def Click11(self, event):
        self.title_2.SetLabel('''
        老司机：你只管开车，办法由老爹来想。   
        ''')
        self.SFShuXing_1.SetLabel('天赋：做个好人')
        self.SFShuXing_2.SetLabel('天赋：见番报号')
        self.SFShuXing_3.SetLabel('天赋：网盘会员')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.LSP.intelligence) +
                             '初始资源点:' + str(Gamer.LSP.resources))

    def Click12(self, event):
        self.title_2.SetLabel('''
        土木狗：别水群啦，包工头喊你吃饭了!
        ''')
        self.SFShuXing_1.SetLabel('天赋：提桶跑路')
        self.SFShuXing_2.SetLabel('天赋：伟大工程')
        self.SFShuXing_3.SetLabel('天赋：打灰超人')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.HanHuang.intelligence) +
                             '初始资源点:' + str(Gamer.HanHuang.resources))

    def Click13(self, event):
        self.title_2.SetLabel('''
        公知：灯塔全民免费医保！在微信军事基地部署有1000艘医疗船！高速公路
        不收费，人人买得起帝国大厦，开得起核动力飞车！注重“快乐教育”，孩子
        们课业压力为负五十万！公司关怀员工，给他们每个人500%股份！
        ''')
        self.SFShuXing_1.SetLabel('天赋：刚下飞机')
        self.SFShuXing_2.SetLabel('天赋：四岛补贴')
        self.SFShuXing_3.SetLabel('天赋：精神西人')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.GongZhi.intelligence) +
                             '初始资源点:' + str(Gamer.GongZhi.resources))

    def Click14(self, event):
        self.title_2.SetLabel('''
                躺平人：谢邀，天桥下睡得很舒服，每天可以免费喝水吃小绿藻
                我超！我生活的无忧无虑！
                ''')
        self.SFShuXing_1.SetLabel('天赋：光合作用')
        self.SFShuXing_2.SetLabel('天赋：自我进化')
        self.SFShuXing_3.SetLabel('天赋：原始居民')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.TangPing.intelligence) +
                             '初始资源点:' + str(Gamer.TangPing.resources))

    def Click15(self, event):
        self.title_2.SetLabel('''
        社畜：心口有点疼，现在是几点？我去公司天台晾个衣服——
        哎？老板好！我一定会在今年让您开上迈巴赫的！
        ''')
        self.SFShuXing_1.SetLabel('天赋：996007')
        self.SFShuXing_2.SetLabel('天赋：猝死转生')
        self.SFShuXing_3.SetLabel('天赋：半泽直树')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.SheChu.intelligence) +
                             '初始资源点:' + str(Gamer.SheChu.resources))

    def Click16(self, event):
        self.title_2.SetLabel('''
            二刺螈：（（（（（（（（（呐）））））））））
                   （（（（（（（（（呐）））））））））
                   （（（（（（（（（呐）））））））））                     
                ''')

        self.SFShuXing_1.SetLabel('天赋：人体声呐')
        self.SFShuXing_2.SetLabel('天赋：穿越之门')
        self.SFShuXing_3.SetLabel('天赋：缝合生物')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.TwoWorld.intelligence) +
                             '初始资源点:' + str(Gamer.TwoWorld.resources))

    def Click17(self, event):
        self.title_2.SetLabel('''
                X批：我是充648好呢，还是充648？
                ''')
        self.SFShuXing_1.SetLabel('天赋：面包芝士')
        self.SFShuXing_2.SetLabel('天赋：农药中毒')
        self.SFShuXing_3.SetLabel('天赋：文化卫兵')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.XPi.intelligence) +
                             '初始资源点:' + str(Gamer.XPi.resources))

    def Click18(self, event):
        self.title_2.SetLabel('''
        电竞粉：部分人会打泰拳，部分人会御剑，还有部分人仰卧起坐的能力很强
        喜欢睡在棺材里，时不时出来看一眼。
                ''')
        self.SFShuXing_1.SetLabel('天赋：抗吧大佬')
        self.SFShuXing_2.SetLabel('天赋：我行我上')
        self.SFShuXing_3.SetLabel('天赋：一致对外')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(Gamer.LPL.intelligence) +
                             '初始资源点:' + str(Gamer.LPL.resources))

    def Start(self, event):
        i = 0
        if self.SFShuXing_1.GetValue() == True:
            i = i+1
        if self.SFShuXing_2.GetValue() == True:
            i = i+1
        if self.SFShuXing_3.GetValue() == True:
            i = i+1
        if i > 1:
            errorMessage = wx.MessageDialog(None, '只能拥有一个身份天赋！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage.ShowModal() == wx.ID_YES:
                errorMessage.Destroy()
        if i < 1:
            errorMessage2 = wx.MessageDialog(None, '请选择身份天赋！！！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage2.ShowModal() == wx.ID_YES:
                errorMessage2.Destroy()
        i2 = 0
        if self.TongYongShuXing1.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing2.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing3.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing4.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing5.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing6.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing7.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing8.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing9.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing10.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing11.GetValue() == True:
            i2 = i2 + 1
        if self.TongYongShuXing12.GetValue() == True:
            i2 = i2 + 1
        if i2 > 3:
            errorMessage2 = wx.MessageDialog(None, '只能拥有三个通用天赋！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage2.ShowModal() == wx.ID_YES:
                errorMessage2.Destroy()
        if i2 < 3:
            errorMessage2 = wx.MessageDialog(None, '请选择三个通用天赋！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage2.ShowModal() == wx.ID_YES:
                errorMessage2.Destroy()
        if i == 1 and i2 == 3:
                app2 = wx.App()
                frame2 = GameWindow(parent=None, id=-1)
                frame2.Show()
                app2.MainLoop()


class GameWindow(Start.GameWindow):
    pass


def show():
    app = wx.App()
    frame = Frame1(parent=None, id=-1)
    frame.Show()
    app.MainLoop()