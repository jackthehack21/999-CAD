"""
mainFrame.py
class MainFrame(Frame)
func start()

Starts the main Frame that holds everything for moderating/handling calls
and dispatching and modifying vehicles and calls.
"""
from fasteners import version as fastenersv
import sys
import wx
import platform
from src.Auth import authPanel


class MainFrame(wx.Frame):
    """
    A Frame that will hold main interface in future
    """

    def __init__(self, system, app, *args, **kw, ):
        super(MainFrame, self).__init__(*args, **kw)
        self.panel = wx.Panel(self)
        self.system = system
        self.app = app
        self.system.logger.debug("Building MainFrame...", caller="MainFrame")
        self.SetIcon(wx.Icon(self.system.resource_path("data/icon.ico")))

        st = wx.StaticText(self.panel, label="Hi There !", pos=(25, 25))  # 25,25 for slight padding.
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.panel.Bind(wx.EVT_KEY_UP, self.onkey)

        # create a menu bar
        self.makemenubar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("999 - Computer Aided Dispatch Simulator v0.0.1 Development Build")

        self.Hide()
        # Ask user to login
        system.logger.debug("Constructing authPanel", caller="MainFrame")
        dlg = authPanel.LoginPanel(system)
        dlg.ShowModal()
        system.logger.debug("authPanel destroyed, checking details...", caller="MainFrame")
        authenticated = dlg.logged_in
        if not authenticated:
            system.logger.log("Failed authentication, shutting down.", caller="MainFrame")
            sys.exit(0)

        self.SetTitle("999 - CADS: "+system.user+" - Main Menu")

        system.logger.log("Displaying MainFrame to user.", caller="MainFrame")
        self.Show()
        self.Maximize()
        self.ShowFullScreen(True)

    def onkey(self, event):
        """ Handles shortcuts such as F11 for fullscreen. """
        if event.GetKeyCode() == wx.WXK_F11:
            if self.IsFullScreen():
                self.ShowFullScreen(False)
            else:
                self.ShowFullScreen(True)
        else:
            event.Skip()

    def makemenubar(self):
        filemenu = wx.Menu()
        newitem = filemenu.Append(-1, "&New...\tCtrl-N", "Create/Open new database, refreshes calls/units/history.")
        filemenu.AppendSeparator()
        logoutitem = filemenu.Append(-1, "&Logout\tCtrl-L", "Logout of the interface.")
        exititem = filemenu.Append(wx.ID_EXIT, "&Exit\tCtrl-Q", "Exit the program completely.")

        helpmenu = wx.Menu()
        aboutitem = helpmenu.Append(wx.ID_ABOUT, "&About\tCtrl-A", "About the app/dependencies and their version.")
        creditsitem = helpmenu.Append(-1, "&Credits", "Display the list of people/links "
                                          "that helped make this possible.")

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        menubar.Append(helpmenu, "&Help")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onnew, newitem)
        self.Bind(wx.EVT_MENU, self.onlogout, logoutitem)
        self.Bind(wx.EVT_MENU, self.onexit, exititem)
        self.Bind(wx.EVT_MENU, self.onabout, aboutitem)
        self.Bind(wx.EVT_MENU, self.oncredits, creditsitem)

    # noinspection PyUnusedLocal
    def onexit(self, event):
        """Close the MainFrame, hence terminating program (and MainLoop)"""
        self.system.logger.log("Destroying MainFrame...", caller="MainFrame")
        self.Destroy()

    # noinspection PyUnusedLocal
    def onlogout(self, event):
        """Close the frame, terminating the application."""
        self.system.logger.log("Logging out...", caller="MainFrame")
        self.SetTitle("999 - Computer Aided Dispatch Simulator")
        self.Hide()
        self.system.logger.debug("Constructing authPanel", caller="MainFrame")
        dlg = authPanel.LoginPanel(self.system)
        dlg.ShowModal()
        self.system.logger.debug("authPanel destroyed, checking details...", caller="MainFrame")
        authenticated = dlg.logged_in
        if not authenticated:
            self.system.logger.log("Failed authentication, shutting down.", caller="MainFrame")
            sys.exit(0)
        self.SetTitle("999 - CADS: " + self.system.user + " - Main Menu")
        self.Show()

    # noinspection PyUnusedLocal
    @staticmethod
    def onnew(event):
        """Say hello to the user."""
        wx.MessageBox("Coming soon, (todo dataManager)")

    # noinspection PyUnusedLocal
    @staticmethod
    def oncredits(event):
        """Displays info box about credits."""
        wx.MessageBox("Owner - Jackthehack21\n"
                      "Developers - Jackthehack21\n"
                      "Icon - http://www.ipharmd.net/symbol/star_of_life/emergency_medicine_blue.html\n\n"
                      "Dependencies - Python@"+platform.python_version()+", wxPython@"+wx.__version__+", "
                      "fasteners@"+fastenersv.version_string()+", pyinstaller@3.4.0",
                      "999-CAD Simulator Credits", wx.OK | wx.ICON_INFORMATION)

    # noinspection PyUnusedLocal
    @staticmethod
    def onabout(event):
        """Display an About Dialog"""
        wx.MessageBox("999-CADS - v0.0.1 Development Build\n"
                      "Project written in Python by Jackthehack21, More details to be added.",
                      "About 999-CAD Simulator", wx.OK | wx.ICON_INFORMATION)


def start(system):
    system.logger.debug("Constructing Main Window...")
    app = wx.App(False)
    frm = MainFrame(system, app, None, title='999 - Computer Aided Dispatch Simulator')
    frm.Show()
    app.MainLoop()
