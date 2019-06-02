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
        pnl = wx.Panel(self)
        self.system = system
        self.app = app
        self.system.logger.debug("Building MainFrame...", caller="MainFrame")
        self.SetIcon(wx.Icon(self.system.resource_path("data/icon.ico")))

        st = wx.StaticText(pnl, label="Hi There !", pos=(25, 25))  # 25,25 for slight padding.
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

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

        system.logger.log("Displaying MainFrame, call simulator starting in x seconds...", caller="MainFrame")
        self.Show()

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
        self.system.logger.log("Logging out...", caller="MainFrame")
        self.Hide()
        self.system.logger.debug("Constructing authPanel", caller="MainFrame")
        dlg = authPanel.LoginPanel(self.system)
        dlg.ShowModal()
        self.system.logger.debug("authPanel destroyed, checking details...", caller="MainFrame")
        authenticated = dlg.logged_in
        if not authenticated:
            self.system.logger.log("Failed authentication, shutting down.", caller="MainFrame")
            sys.exit(0)
        self.Show()

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
                      "Dependencies - Python@"+platform.python_version()+", wxPython@"+wx.__version__+", "
                      "fasteners@"+fastenersv.version_string(),
                      "999-CAD Simulator Credits", wx.OK | wx.ICON_INFORMATION)

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
