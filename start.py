"""
Hello, small experiment still deciding on GUI library
"""

import wx
import platform
import time


class MainFrame(wx.Frame):
    """
    A Frame that will hold main interface in future
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)

        self.SetIcon(wx.Icon("data/icon.ico"))

        st = wx.StaticText(pnl, label="Hi There !", pos=(25, 25))  # 25,25 for slight padding.
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # create a menu bar
        self.makemenubar()

        # and a status bar
        # self.CreateStatusBar()
        # self.SetStatusText("999 - Computer Aided Dispatch Simulator v0.0.1 Development Build")

    def makemenubar(self):
        filemenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloitem = filemenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item.")
        filemenu.AppendSeparator()
        exititem = filemenu.Append(wx.ID_EXIT, "&Logout\tCtrl-Q", "Logout of the interface.")

        helpmenu = wx.Menu()
        aboutitem = helpmenu.Append(wx.ID_ABOUT, "&About\tCtrl-A", "About the app/dependencies and their version.")
        creditsitem = helpmenu.Append(-1, "&Credits", "Display the list of people/links that helped make this possible.")

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        menubar.Append(helpmenu, "&Help")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onhello, helloitem)
        self.Bind(wx.EVT_MENU, self.onexit,  exititem)
        self.Bind(wx.EVT_MENU, self.onabout, aboutitem)
        self.Bind(wx.EVT_MENU, self.oncredits, creditsitem)

    def onexit(self, event):
        """Close the frame, terminating the application."""
        self.Hide()
        time.sleep(5)
        self.Show()
        # self.Close(True)

    @staticmethod
    def onhello(event):
        """Say hello to the user."""
        wx.MessageBox("Hi there from Jaxk")

    @staticmethod
    def oncredits(event):
        """Displays info box about credits."""
        wx.MessageBox("Owner - Jackthehack21\n"
                      "Developers - Jackthehack21\n"
                      "Icon - http://www.ipharmd.net/symbol/star_of_life/emergency_medicine_blue.html\n\n"
                      "Dependencies - Python@"+platform.python_version()+", wxPython@"+wx.__version__,
                      "999-CAD Simulator Credits", wx.OK | wx.ICON_INFORMATION)

    @staticmethod
    def onabout(event):
        """Display an About Dialog"""
        wx.MessageBox("999-CADS           - v0.0.1 Development Build\n"
                      "Python Build      - v"+platform.python_version()+"\n"
                      "wxPython Build - v4.0.6\n"
                      "Project written in Python by Jackthehack21",
                      "About 999-CAD Simulator", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App(False)
    frm = MainFrame(None, title='999 - Computer Aided Dispatch Simulator')
    frm.Show()
    app.MainLoop()
