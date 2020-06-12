import wx
from wx import xrc

class XrcControl:
    def __init__(self):
        wx.CallAfter(self._DoPostInit)

    def _DoPostInit(self):
        self._init_auto_ids()
        self._PostInit()
    def _init_auto_ids(self):
        if hasattr( self, 'auto_ids'):
            for aid in self.auto_ids: 
                if not aid.startswith('ID_'):
                    raise RuntimeError ( "auto_ids must all be in format ID_XXX: " % aid )
                exec ( 'self._%s=xrc.XRCCTRL(self,"%s")' % ( aid.lower()[3:], aid ) )
    def _PostInit(self):
        raise RuntimeError ( "Extend this method." )
 
class XrcFrame(wx.Frame, XrcControl):
    def __init__(self):
        wx.Frame.__init__(self)
        XrcControl.__init__(self)

class XrcPanel(wx.Panel,XrcControl):
    def __init__(self):
        wx.Panel.__init__(self)
        XrcControl.__init__(self)

class XrcListCtrl(wx.ListCtrl,XrcControl):
    def __init__(self):
        wx.ListCtrl.__init__(self)
        XrcControl.__init__(self)

class XrcListBox(wx.ListBox, XrcControl):
    def __init__(self):
        wx.ListBox.__init__(self)
        XrcControl.__init__(self)

class XrcChoice(wx.Choice, XrcControl):
    def __init__(self):
        wx.Choice.__init__(self)
        XrcControl.__init__(self)

class XrcDialog(wx.Dialog,XrcControl):
    def __init__(self):
        wx.Dialog.__init__(self)
        XrcControl.__init__(self)

