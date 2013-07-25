import wx
from wx import xrc

class XrcControl:
    def __init__(self):
        self.Bind( wx.EVT_WINDOW_CREATE , self.OnCreate)
    def OnCreate(self,evt):
        self.Unbind ( wx.EVT_WINDOW_CREATE )
        wx.CallAfter(self._PostInit)
        evt.Skip()
        return True
    def _PostInit(self):
        raise RuntimeError ( "Extend this method." )
 
class XrcFrame(wx.Frame, XrcControl):
    def __init__(self):
        f=wx.PreFrame()
        self.PostCreate(f)
        XrcControl.__init__(self)

class XrcPanel(wx.Panel,XrcControl):
    def __init__(self):
        p=wx.PrePanel()
        self.PostCreate(p)
        XrcControl.__init__(self)

class XrcListCtrl(wx.ListCtrl,XrcControl):
    def __init__(self):
        l=wx.PreListCtrl()
        self.PostCreate(l)
        XrcControl.__init__(self)


class XrcDialog(wx.Dialog,XrcControl):
    def __init__(self):
        d=wx.PreDialog()
        self.PostCreate(d)
        XrcControl.__init__(self)

