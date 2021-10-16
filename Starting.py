# -*- coding:utf-8 -*-
import wx
import Start
import yaml
import util.YAMLLoad
from GlobalControl import Global
# 导入需要的模块

windows_data = util.YAMLLoad.getYAMLDataAll('./config/String.yml')
chara = util.YAMLLoad.getYAMLDataAll('./config/Character.yml')


class Frame1(wx.Frame):
    # 定义主窗口
    def __init__(self, parent, id):
        # 下一行代码设定了主窗口。
        wx.Frame.__init__(self, parent, id=-1, title=windows_data['GameName'], pos=(100, 100), size=(600, 640))

        self.data_1 = 0
        self.data_2 = 0

        panel = wx.Panel(self)
        title = wx.StaticText(panel, label='选择身份', pos=(100, 10))
        font = wx.Font(24, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)

        # 以下代码创建了18个按钮（同一组），用于让玩家选择身份。[rb1 to rb18]
        self.rb1 = wx.RadioButton(panel, -1, label=windows_data['SF']['name1'], pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, -1, label=windows_data['SF']['name2'], pos=(10, 40))
        self.rb3 = wx.RadioButton(panel, -1, label=windows_data['SF']['name3'], pos=(10, 70))
        self.rb4 = wx.RadioButton(panel, -1, label=windows_data['SF']['name4'], pos=(10, 100))
        self.rb5 = wx.RadioButton(panel, -1, label=windows_data['SF']['name5'], pos=(10, 130))
        self.rb6 = wx.RadioButton(panel, -1, label=windows_data['SF']['name6'], pos=(10, 160))
        self.rb7 = wx.RadioButton(panel, -1, label=windows_data['SF']['name7'], pos=(10, 190))
        self.rb8 = wx.RadioButton(panel, -1, label=windows_data['SF']['name8'], pos=(10, 220))
        self.rb9 = wx.RadioButton(panel, -1, label=windows_data['SF']['name9'], pos=(10, 250))
        self.rb10 = wx.RadioButton(panel, -1, label=windows_data['SF']['name10'], pos=(10, 280))
        self.rb11 = wx.RadioButton(panel, -1, label=windows_data['SF']['name11'], pos=(10, 310))
        self.rb12 = wx.RadioButton(panel, -1, label=windows_data['SF']['name12'], pos=(10, 340))
        self.rb13 = wx.RadioButton(panel, -1, label=windows_data['SF']['name13'], pos=(10, 370))
        self.rb14 = wx.RadioButton(panel, -1, label=windows_data['SF']['name14'], pos=(10, 400))
        self.rb15 = wx.RadioButton(panel, -1, label=windows_data['SF']['name15'], pos=(10, 430))
        self.rb16 = wx.RadioButton(panel, -1, label=windows_data['SF']['name16'], pos=(10, 460))
        self.rb17 = wx.RadioButton(panel, -1, label=windows_data['SF']['name17'], pos=(10, 490))
        self.rb18 = wx.RadioButton(panel, -1, label=windows_data['SF']['name18'], pos=(10, 520))

        # 下一行代码创建了一个标签用于存放对于玩家所选择的身份的介绍。
        self.title_2 = wx.StaticText(panel, label=windows_data['jieshao_QuanShi'], pos=(100, 60))

        # 以下代码块使用Bind方法将Click系列函数与上面的选择按钮绑定在一起。
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

        # 第一组通用天赋选择模块。
        self.TongYongShuXing1 = wx.CheckBox(panel, id=-1, label='天赋：量子速读', pos=(100, 150))
        self.TongYongShuXing2 = wx.CheckBox(panel, id=-1, label='天赋：海豹抽卡', pos=(100, 180))
        self.TongYongShuXing3 = wx.CheckBox(panel, id=-1, label='天赋：蓄意轰拳', pos=(100, 210))
        self.TongYongShuXing4 = wx.CheckBox(panel, id=-1, label='天赋：涩图雷达', pos=(100, 240))
        # 第二组通用天赋选择模块。
        self.TongYongShuXing5 = wx.CheckBox(panel, id=-1, label='天赋：百毒不侵', pos=(240, 150))
        self.TongYongShuXing6 = wx.CheckBox(panel, id=-1, label='天赋：键盘钢琴', pos=(240, 180))
        self.TongYongShuXing7 = wx.CheckBox(panel, id=-1, label='天赋：祖安艺术', pos=(240, 210))
        self.TongYongShuXing8 = wx.CheckBox(panel, id=-1, label='天赋：电子越共', pos=(240, 240))
        # 第三组通用天赋选择模块。
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

        # ChuShi = []
        # self.ChuShiZiYuan = wx.ComboBox(panel, id=-1, choices=ChuShi, pos=(100, 360))

        self.ZTLian = wx.StaticText(panel, id=-1,
                                    label='属性总结：\n综合能力值：' + str(chara['Character']['haigui']['Value']['Intelligence']) +
                                          '初始资源点:' + str(chara['Character']['haigui']['Value']['Resources']), pos=(100, 510))

        self.xb1 = wx.RadioButton(panel, -1, label='男', pos=(300, 10), style=wx.RB_GROUP)
        self.xb2 = wx.RadioButton(panel, -1, label='女', pos=(260, 10))

        self.XB = wx.StaticText(panel, id=-1, label='性别:男', pos=(300, 580))
        font3 = wx.Font(8, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.XB.SetFont(font3)

        self.QueDing = wx.Button(panel, -1, label='开始游戏', pos=(480, 560))
        self.Bind(wx.EVT_BUTTON, self.Start, self.QueDing)

        self.BeiJie = wx.StaticText(panel, -1, label=windows_data['JvBen']['JvBen1'], pos=(60, 400))

        self.JB1 = wx.Button(panel, -1, label='新风暴', pos=(100, 380))
        self.JB2 = wx.Button(panel, -1, label='大洪水', pos=(200, 380))
        self.JB3 = wx.Button(panel, -1, label='黑太阳', pos=(300, 380))

        self.Bind(wx.EVT_BUTTON, self.InClick1, self.JB1)
        self.Bind(wx.EVT_BUTTON, self.InClick2, self.JB2)
        self.Bind(wx.EVT_BUTTON, self.InClick3, self.JB3)

        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick1, self.xb1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick2, self.xb2)

        na = [self.rb1.GetValue, self.rb2.GetValue, self.rb3.GetValue]
        # 列表na，用于存放rb系列按钮的布朗值。

        just = ['quanshi', 'tianlongren', 'haigui']
        # 列表just，用于存放字符串作为字典索性。

        globals = Global()
        # 调用跨模块对象
        globals.ceshi = 70
        '''
        # 测试数据，测试完删除。
        self.i = False
        # 创建主方法所属 i 布朗值。
        for j in range(0, 2, 1):
        # 循环，循环内j为0,1,2。
            if self.i:
            # self.i为True退出循环
                break
            if not self.i:
                if na[j]:
                    # 如果按钮被点击返回True—j号按钮的布朗值。
                    self.data_1 = chara['Character'][just[j]]['Value']['Intelligence']
                    self.data_2 = chara['Character'][just[j]]['Value']['Resources']
                    self.i = True
                else:
                    self.i = False
        globals.Intelligence = self.data_1
        '''

    # InClick1-3系列函数的功能是与剧本按钮绑定，点击按钮触发函数修改‘BeiJie’标签内的游戏剧本说明。
    def InClick1(self, event):
        name = windows_data['JvBen']['JvBen1']
        self.BeiJie.SetLabel(name)

    def InClick2(self, event):
        name = windows_data['JvBen']['JvBen2']
        self.BeiJie.SetLabel(name)

    def InClick3(self, event):
        name = windows_data['JvBen']['JvBen3']
        self.BeiJie.SetLabel(name)

    def OnClick1(self, event):
        self.XB.SetLabel('性别:男')

    def OnClick2(self, event):
        self.XB.SetLabel('性别:女')

    def Click1(self, event):
        self.title_2.SetLabel(windows_data['jieshao_HaiGui'])
        self.SFShuXing_1.SetLabel('天赋：大闹公安')
        self.SFShuXing_2.SetLabel('天赋：西式自由')
        self.SFShuXing_3.SetLabel('天赋：高贵特权')

        self.ZTLian.SetLabel('属性总结：\n综合能力值：' + str(chara['Character']['haigui']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['haigui']['Value']['Resources']))

    def Click2(self, event):
        self.title_2.SetLabel(windows_data['jieshao_TianLongRen'])
        self.SFShuXing_1.SetLabel('天赋：高雅贵族')
        self.SFShuXing_2.SetLabel('天赋：拆迁之家')
        self.SFShuXing_3.SetLabel('天赋：无压高考')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['tianlongren']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['tianlongren']['Value']['Resources']))

    def Click3(self, event):
        self.title_2.SetLabel(windows_data['jieshao_QuanShi'])
        self.SFShuXing_1.SetLabel('天赋：战斗公主')
        self.SFShuXing_2.SetLabel('天赋：煽动神言')
        self.SFShuXing_3.SetLabel('天赋：CIA兼职')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['quanshi']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['quanshi']['Value']['Resources']))

    def Click4(self, event):
        self.title_2.SetLabel(windows_data['jieshao_WangYiYun'])
        self.SFShuXing_1.SetLabel('天赋：生不出人')
        self.SFShuXing_2.SetLabel('天赋：口红割腕')
        self.SFShuXing_3.SetLabel('天赋：嘤嘤嘤嘤')
        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(chara['Character']['wangyiyun']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['wangyiyun']['Value']['Resources']))

    def Click5(self, event):
        self.title_2.SetLabel(windows_data['jieshao_ZuoJia'])
        self.SFShuXing_1.SetLabel('天赋：鸽子煲汤')
        self.SFShuXing_2.SetLabel('天赋：鸽子炒肉')
        self.SFShuXing_3.SetLabel('天赋：鸽子油炸')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(chara['Character']['zuojia']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['zuojia']['Value']['Resources']))

    def Click6(self, event):
        self.title_2.SetLabel(windows_data['jieshao_ZuoTiJia'])
        self.SFShuXing_1.SetLabel('天赋：豪车土猪')
        self.SFShuXing_2.SetLabel('天赋：五三模拟')
        self.SFShuXing_3.SetLabel('天赋：铁人意志')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(chara['Character']['zuotijia']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['zuotijia']['Value']['Resources']))

    def Click7(self, event):
        self.title_2.SetLabel(windows_data['jieshao_ZhangXianZhong'])
        self.SFShuXing_1.SetLabel('天赋：高效屠戮')
        self.SFShuXing_2.SetLabel('天赋：魔怔狂热')
        self.SFShuXing_3.SetLabel('天赋：超级加速')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:'+str(chara['Character']['zhangxianzhong']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['zhangxianzhong']['Value']['Resources']))

    def Click8(self, event):
        self.title_2.SetLabel(windows_data['jieshao_HanHuang'])
        self.SFShuXing_1.SetLabel('天赋：伟大国度')
        self.SFShuXing_2.SetLabel('天赋：民族狂热')
        self.SFShuXing_3.SetLabel('天赋：尼哥猎手')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['hanhuang']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['hanhuang']['Value']['Resources']))

    def Click9(self, event):
        self.title_2.SetLabel(windows_data['jieshao_ZuoRen'])
        self.SFShuXing_1.SetLabel('天赋：革你左籍')
        self.SFShuXing_2.SetLabel('天赋：冲击水晶')
        self.SFShuXing_3.SetLabel('天赋：下乡实践')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['zuoren']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['zuoren']['Value']['Resources']))

    def Click10(self, event):
        self.title_2.SetLabel(windows_data['jieshao_ChengXvYuan'])
        self.SFShuXing_1.SetLabel('天赋：删库跑路')
        self.SFShuXing_2.SetLabel('天赋：我即天网')
        self.SFShuXing_3.SetLabel('天赋：电子幽灵')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['manon']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['manon']['Value']['Intelligence']))

    def Click11(self, event):
        self.title_2.SetLabel(windows_data['jieshao_LSP'])
        self.SFShuXing_1.SetLabel('天赋：做个好人')
        self.SFShuXing_2.SetLabel('天赋：见番报号')
        self.SFShuXing_3.SetLabel('天赋：网盘会员')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['LSP']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['LSP']['Value']['Resources']))

    def Click12(self, event):
        self.title_2.SetLabel(windows_data['jieshao_TuMuGou'])
        self.SFShuXing_1.SetLabel('天赋：提桶跑路')
        self.SFShuXing_2.SetLabel('天赋：伟大工程')
        self.SFShuXing_3.SetLabel('天赋：打灰超人')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['tumugou']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['tumugou']['Value']['Resources']))

    def Click13(self, event):
        self.title_2.SetLabel(windows_data['jieshao_GongZhi'])
        self.SFShuXing_1.SetLabel('天赋：刚下飞机')
        self.SFShuXing_2.SetLabel('天赋：四岛补贴')
        self.SFShuXing_3.SetLabel('天赋：精神西人')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['gongzhi']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['gongzhi']['Value']['Resources']))

    def Click14(self, event):
        self.title_2.SetLabel(windows_data['jieshao_TangPing'])
        self.SFShuXing_1.SetLabel('天赋：光合作用')
        self.SFShuXing_2.SetLabel('天赋：自我进化')
        self.SFShuXing_3.SetLabel('天赋：原始居民')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['tangping']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['tangping']['Value']['Resources']))

    def Click15(self, event):
        self.title_2.SetLabel(windows_data['jieshao_SheChu'])
        self.SFShuXing_1.SetLabel('天赋：996007')
        self.SFShuXing_2.SetLabel('天赋：猝死转生')
        self.SFShuXing_3.SetLabel('天赋：半泽直树')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['shechu']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['shechu']['Value']['Resources']))

    def Click16(self, event):
        self.title_2.SetLabel(windows_data['jieshao_2CiYuan'])

        self.SFShuXing_1.SetLabel('天赋：人体声呐')
        self.SFShuXing_2.SetLabel('天赋：穿越之门')
        self.SFShuXing_3.SetLabel('天赋：缝合生物')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['erciyuan']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['erciyuan']['Value']['Resources']))

    def Click17(self, event):
        self.title_2.SetLabel(windows_data['jieshao_XPi'])
        self.SFShuXing_1.SetLabel('天赋：面包芝士')
        self.SFShuXing_2.SetLabel('天赋：农药中毒')
        self.SFShuXing_3.SetLabel('天赋：文化卫兵')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['XPi']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['XPi']['Value']['Resources']))

    def Click18(self, event):
        self.title_2.SetLabel(windows_data['jieshao_DianJingFen'])
        self.SFShuXing_1.SetLabel('天赋：抗吧大佬')
        self.SFShuXing_2.SetLabel('天赋：我行我上')
        self.SFShuXing_3.SetLabel('天赋：一致对外')

        self.ZTLian.SetLabel('属性总结：\n综合能力值:' + str(chara['Character']['LPL']['Value']['Intelligence']) +
                             '初始资源点:' + str(chara['Character']['LPL']['Value']['Resources']))

    def Start(self, event):
        # i为一个计数器，用来统计被激活的SFShuXing系列按钮的个数。
        i = 0
        # 以下代码将被激活的按钮个数统计到i中。
        if self.SFShuXing_1.GetValue() == True:
            i = i+1
        if self.SFShuXing_2.GetValue() == True:
            i = i+1
        if self.SFShuXing_3.GetValue() == True:
            i = i+1
        # 如果没有按钮被激活，则弹出错误提示框。 如果选择按钮超过一个，提示选择过多错误。
        if i > 1:
            errorMessage = wx.MessageDialog(None, '只能拥有一个身份天赋！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage.ShowModal() == wx.ID_YES:
                errorMessage.Destroy()
        if i < 1:
            errorMessage2 = wx.MessageDialog(None, '请选择身份天赋！！！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage2.ShowModal() == wx.ID_YES:
                errorMessage2.Destroy()

        # i2也是一个计数器，用来统计玩家选择的通用天赋的个数。
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