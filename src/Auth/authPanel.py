"""
authPanel.py
class LoginPanel(wx.Dialog)

GUI for Authentication/Login
"""
import wx


class LoginPanel(wx.Dialog):
    """
    Class to define login dialog
    """

    # ----------------------------------------------------------------------
    def __init__(self, system):
        wx.Dialog.__init__(self, None, title="999 - CADS Authentication", size=(220, 200))
        self.system = system
        self.logged_in = False

        self.system.logger.debug("Building authPanel...", caller="AuthPanel")

        self.SetBackgroundColour("gray")

        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onlogin)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onlogin)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)
    # ----------------------------------------------------------------------

    # noinspection PyUnusedLocal
    def onlogin(self, event):
        """
        Check credentials and login
        """
        username = self.user.GetValue()
        password = self.password.GetValue()
        if self.system.authHandler.verify(username, password):
            self.system.logger.log("Logged in as", username, caller="AuthPanel")
            self.logged_in = True
            self.shownotice(username)
            self.Destroy()
        else:
            self.system.logger.debug("Authentication failed.", caller="AuthPanel")
            self.showwarning()

    @staticmethod
    def shownotice(username):
        dial = wx.MessageDialog(None, 'Welcome back '+username, 'Authentication Success !', wx.OK)
        dial.ShowModal()

    @staticmethod
    def showwarning():
        dial = wx.MessageDialog(None, 'Username/Password incorrect, please try again.', 'Authentication failed !',
                                wx.OK | wx.ICON_EXCLAMATION)
        dial.ShowModal()
