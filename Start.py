import wx
import Gamer


class GameWindow(wx.Frame):
    # 定义游戏窗口
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=-1, title="游戏进行时", pos=(800, 100), size=(600, 640))
        panel2 = wx.Panel(self)

        self.time = 1
        self.run = 5
        self.title = wx.StaticText(panel2, label='回合：'+str(self.time), pos=(60, 10))
        font = wx.Font(24, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.title.SetFont(font)

        self.next = wx.Button(panel2, -1, label='下一回合', pos=(490, 540))

        self.Bind(wx.EVT_BUTTON, self.Next_continue, self.next)

        self.Work = wx.Button(panel2, -1, label='劳动', pos=(200, 60))
        self.Learn = wx.Button(panel2, -1, label='学习', pos=(200, 10))

        self.Bind(wx.EVT_BUTTON, self.Action, self.Work)
        self.Bind(wx.EVT_BUTTON, self.Action, self.Learn)

        self.run_title = wx.StaticText(panel2, -1, label='剩余行动力: ' + str(self.run), pos=(320, 10))
        font2 = wx.Font(11, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.run_title.SetFont(font2)

        self.mess = wx.TextCtrl(panel2, -1, value='''
新风暴：自从极东之地的金融波动之后，震坦和四岛社会已经
运转到了极限，人们纷纷追忆起三年前萨布林娜小姐在全国广
播里的讲话，高声唱起图书馆之歌来，似乎是可以念一首《海
燕》了。'''
                                           , pos=(50, 100), size=(360, 300), style=wx.TE_MULTILINE)



    def Next_continue(self, event):
        self.time = self.time + 1
        self.run = 5
        self.title.SetLabel('回合：'+str(self.time))
        self.run_title.SetLabel('剩余行动力: ' + str(self.run))
        self.mess.AppendText('\n测试事件：你早上看见了女人打拳，顿生惊恐（焦虑值+8）')

    def Action(self, event):
        self.run = self.run - 1
        self.run_title.SetLabel('剩余行动力: ' + str(self.run))
        if self.run < 0:
            errorMessage = wx.MessageDialog(None, '你没有行动力了！', '提示：', wx.YES_DEFAULT | wx.ICON_QUESTION)
            if errorMessage.ShowModal() == wx.ID_YES:
                errorMessage.Destroy()


if __name__ == '__main__':
    app2 = wx.App()
    frame2 = GameWindow(parent=None, id=-1)
    frame2.Show()
    app2.MainLoop()