"""
logger.py

handles the output to console and colour+saving to log file.
"""
import sys
from time import gmtime, strftime


def gettime():
    return strftime("%H:%M:%S", gmtime())


class Logger:
    def __init__(self, path):
        self.file = path

    def debug(self, msg, *args, caller="System"):
        for arg in args:
            msg = msg+" "+arg
        time = "["+gettime()+"] "
        msg = "["+caller+"] [Debug] > "+msg+"\n"
        self._save(time+msg)
        sys.stdout.write("\x1b[1m\033[96m"+time+"\x1b[1m\033[90m"+msg+"\033[39m\x1b[21m")

    def log(self, msg, *args, caller="System"):
        for arg in args:
            msg = msg+" "+arg
        time = "[" + gettime() + "] "
        msg = "[" + caller + "] [Log] > " + msg + "\n"
        self._save(time + msg)
        sys.stdout.write("\x1b[1m\033[96m" + time + "\033[39m\x1b[21m"+msg)

    def warning(self, msg, *args, caller="System"):
        for arg in args:
            msg = msg+" "+arg
        time = "[" + gettime() + "] "
        msg = "[" + caller + "] [Warning] > " + msg + "\n"
        self._save(time + msg)
        sys.stdout.write("\x1b[1m\033[96m" + time + "\x1b[1m\033[33m"+msg+"\033[39m\x1b[21m")

    def error(self, msg, *args, caller="System"):
        for arg in args:
            msg = msg+" "+arg
        time = "[" + gettime() + "] "
        msg = "[" + caller + "] [Error] > " + msg + "\n"
        self._save(time + msg)
        sys.stdout.write("\x1b[1m\033[96m" + time + "\x1b[1m\033[91m" + msg + "\033[39m\x1b[21m")

    def critical(self, msg, *args, caller="System"):
        for arg in args:
            msg = msg+" "+arg
        time = "[" + gettime() + "] "
        msg = "[" + caller + "] [Critical] > " + msg + "\n"
        self._save(time + msg)
        sys.stdout.write("\x1b[1m\033[96m" + time + "\x1b[1m\033[31m\x1b[1m\033[2m" + msg + "\033[39m\x1b[21m")

    def _save(self, msg):
        f = open(self.file, "a")
        f.write(msg)
        f.close()
