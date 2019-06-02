"""
entry.py
func start()

Entry point from start.py (outer folder), does the data checks, etc here.
"""
import sys
import time

import fasteners
from src.Graphics import mainFrame
from src.Boot import system as systemc
from colorama import initialise
import os
initialise.init(False)  # Thanks, this now allows colour and other cool things on windows :)


def start():
    starttime = int(round(time.time() * 1000))
    sys.stdout.write("\x1b]2;999 - Computer Aided Dispatch Simulator (CONSOLE)\x07")  # Update console title.
    a_lock = fasteners.InterProcessLock('app.lock')
    gotten = a_lock.acquire(blocking=False)
    if not gotten:
        sys.stdout.write("\x1b[1m\033[91m[Error] : Program is already running in this directory.\033[39m\x1b[21m\n")
        sys.exit(1)

    if not os.path.exists('data'):
        os.makedirs('data')
        # todo run intial run sequence, displays guide PDF, and default user details to log in. (once user management is complete)

    system = systemc.System()
    # system.logger.debug("Test debug")
    # system.logger.log("Test log")
    # system.logger.warning("Test warning")
    # system.logger.error("Test error")
    # system.logger.critical("Critical error")

    system.logger.debug("Starting Auth Handler...")
    system.authHandler.open()
    system.logger.debug("Starting Auth MainFrame...")
    endtime = int(round(time.time() * 1000))
    system.logger.log("Booted in", str(endtime-starttime)+"ms")
    mainFrame.start(system)
