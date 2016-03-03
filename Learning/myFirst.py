import wx


class Frame(wx.Frame):
    def __init__(self, title, size):
        wx.Frame.__init__(self, None, title=title, size=size)

app = wx.App(redirect=True)
top = Frame("Hello World", (300,200))
top.SetSizeWH(1000, 800)
top.SetSize(wx.Size(400, 300))
top.SetBackgroundColour('#F12331')
top.SetPosition(wx.Point(0, 0))
top.Show()


app.MainLoop()
