"""
system.py
class System()

A class that holds reference to all useful classes such as logger, version, handlers etc
"""
import os
import sys
from src.Utils import logger
from src.Auth import authHandler


class System:
    def __init__(self):
        self.user = None
        self.logger = logger.Logger("app.log")
        self.authHandler = authHandler.Handler(self)
        self.built = getattr(sys, 'frozen', False) and sys.argv[0] == sys.executable

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller, """
        """ Credits: https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile """
        if not self.built:
            return relative_path
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def login(self, username):
        self.user = username  # todo user class to hold things like permissions, name, easier to use.
