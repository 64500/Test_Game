import wx
import Gamer
import yaml
import os
import random
import util.YAMLLoad


Events = ['你今天等公交车的时候，发现天桥下跳下来一个赛里斯女超人，可惜她摔死了，你大为震撼。',
          '你刷手机的时候，看见了一条恐婚新闻，你感觉很惊恐，离爱情又远了很多。(焦虑+4)',
          '你发现了一个黑人留居时间过长，于是举报了他，发现是一个偷渡佬，公安局奖励了你。（资源+3）',
          '你差点被泥头车创死，但旁边被撞到的饮料售卖机凭空消失了，你十分后悔。（焦虑+10）',
          '你今天打了一把Moba游戏，打完后发现自己不用吃饭了（本回合不扣除生活资源）',
          '你有那个大病，于是去人民医院看了看，医生给你看了你的大病。(健康+4，焦虑-10,资源-1)',
          '你看见一辆轿车上画着膏药旗，感到大为震撼。'
          ]
class GameWindow(wx.Frame):
    # 定义游戏窗口
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=-1, title="游戏进行时", pos=(800, 100), size=(630, 640))
        panel2 = wx.Panel(self)

        self.time = 1
        self.run = 5
        self.Health_data = -18
        self.anxious = 144
        self.intelligence_data = 4
        self.resources_data = 5

        self.title = wx.StaticText(panel2, label='回合：'+str(self.time), pos=(60, 10))
        self.title2 = wx.StaticText(panel2, label='身份：拳师', pos=(60, 60))
        self.TYTianFu_1 = wx.Button(panel2, label='通用天赋：蓄意轰拳', pos=(60, 400))
        self.TYTianFu_2 = wx.Button(panel2, label='通用天赋：祖安艺术', pos=(60, 430))
        self.TYTianFu_3 = wx.Button(panel2, label='通用天赋：量子速读', pos=(60, 460))
        self.SFTianFu = wx.Button(panel2, label='身份天赋：CIA兼职', pos=(60, 510))
        self.Ues_Card = wx.Button(panel2, label='打出卡牌', pos=(60, 540))
        font = wx.Font(24, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.title.SetFont(font)

        self.Health = wx.StaticText(panel2, label='健康值:' + str(self.Health_data), pos=(320, 40))
        self.Anxious = wx.StaticText(panel2, label='焦虑值:' + str(self.anxious), pos=(320, 70))
        self.intelligence = wx.StaticText(panel2, label='能力值:' + str(self.intelligence_data), pos=(400, 40))
        self.resources = wx.StaticText(panel2, label='资源点:' + str(self.resources_data), pos=(400, 70))

        self.Gender = wx.StaticText(panel2, label='性别：女', pos=(460, 40))
        self.height = wx.StaticText(panel2, label='身高：150 CM', pos=(460, 60))
        self.ZongHe = wx.StaticText(panel2, label='综合：白毛萝莉拳师', pos=(460, 80))

        self.Card1 = wx.StaticText(panel2, label='手牌：马恩牌X1', pos=(200, 410))
        self.Card2 = wx.StaticText(panel2, label='手牌：喷射牌X1', pos=(200, 440))
        self.Card3 = wx.StaticText(panel2, label='手牌：马恩牌X1', pos=(200, 470))
        self.Card4 = wx.StaticText(panel2, label='手牌：马科长X1', pos=(200, 500))
        self.Card5 = wx.StaticText(panel2, label='手牌：锡特勒X1', pos=(200, 530))
        self.Card6 = wx.StaticText(panel2, label='手牌：贵左X1', pos=(200, 560))

        self.rb1 = wx.RadioButton(panel2, -1, label='1', pos=(320, 410), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel2, -1, label='2', pos=(320, 440))
        self.rb3 = wx.RadioButton(panel2, -1, label='3', pos=(320, 470))
        self.rb4 = wx.RadioButton(panel2, -1, label='4', pos=(320, 500))
        self.rb5 = wx.RadioButton(panel2, -1, label='5', pos=(320, 530))
        self.rb6 = wx.RadioButton(panel2, -1, label='6', pos=(320, 560))

        self.next = wx.Button(panel2, -1, label='下一回合', pos=(490, 540))
        self.Get_Card = wx.Button(panel2, -1, label='抽取卡片', pos=(490, 500))
        self.Shop = wx.Button(panel2, -1, label='消费市场', pos=(490, 460))
        self.TouZi = wx.Button(panel2, -1, label='投资市场', pos=(490, 420))

        self.Buff = wx.TextCtrl(panel2, -1, value='buff栏', pos=(470, 100), size=(100, 300), style=wx.TE_MULTILINE)
        self.Money = wx.TextCtrl(panel2, -1, value='资产', pos=(360, 420), size=(100, 160), style=wx.TE_MULTILINE)

        self.Bind(wx.EVT_BUTTON, self.Next_continue, self.next)

        self.Work = wx.Button(panel2, -1, label='劳动', pos=(200, 60))
        self.Learn = wx.Button(panel2, -1, label='学习', pos=(200, 10))
        self.TianFu = wx.Button(panel2, -1, label='打拳', pos=(450, 10))

        self.Bind(wx.EVT_BUTTON, self.Action, self.Work)
        self.Bind(wx.EVT_BUTTON, self.Action2, self.Learn)
        self.Bind(wx.EVT_BUTTON, self.TianFu_Action, self.TianFu)

        self.run_title = wx.StaticText(panel2, -1, label='剩余行动力: ' + str(self.run), pos=(320, 10))
        font2 = wx.Font(11, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.run_title.SetFont(font2)

        self.mess = wx.TextCtrl(panel2, -1, value='''
新风暴：自从极东之地的金融波动之后，震坦和四岛社会已经
运转到了极限，人们纷纷追忆起三年前萨布林娜小姐在全国广
播里的讲话，高声唱起图书馆之歌来，似乎是可以念一首《海
燕》了。'''
                                           , pos=(50, 100), size=(400, 300), style=wx.TE_MULTILINE)

    def Next_continue(self, event):
        self.time = self.time + 1
        self.run = 5
        self.title.SetLabel('回合：'+str(self.time))
        self.run_title.SetLabel('剩余行动力: ' + str(self.run))
        self.mess.AppendText('\n测试事件：你早上看见了女人打拳，顿生惊恐（焦虑值+8）')
        self.mess.AppendText('\n' + Events[int(6*random.random())+1])

    def Action(self, event):
        self.run = self.run - 1
        self.run_title.SetLabel('剩余行动力: ' + str(self.run))
        if self.run < 0:
            errorMessage = wx.MessageDialog(None, '你没有行动力了！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage.ShowModal() == wx.ID_YES:
                errorMessage.Destroy()
        self.mess.AppendText('\n事件：你遭到了剥削，老板开着迈巴赫施舍了你一点钱。（资源点+1）')

    def Action2(self, event):
        self.run = self.run - 1
        self.run_title.SetLabel('剩余行动力: ' + str(self.run))
        if self.run < 0:
            errorMessage = wx.MessageDialog(None, '你没有行动力了！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage.ShowModal() == wx.ID_YES:
                errorMessage.Destroy()
        self.mess.AppendText('\n事件：你认真学习，提高了自己的能力！（能力+1）')

    def TianFu_Action(self, event):
        self.run = self.run - 1
        self.run_title.SetLabel('剩余行动力: ' + str(self.run))
        if self.run < 0:
            errorMessage = wx.MessageDialog(None, '你没有行动力了！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage.ShowModal() == wx.ID_YES:
                errorMessage.Destroy()
        self.mess.AppendText('\n事件：你在网上打拳，收到了中情局的补贴。（资源点+2）')