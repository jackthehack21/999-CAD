"""
entry.py
func start()

Entry point from start.py (outer folder), does the data checks, etc here.
"""
import sys
import fasteners
from src import system as systemc
from colorama import initialise
initialise.init(False)  # Thanks, this now allows colour on windows :)


def start():
    sys.stdout.write("\x1b]2;999 - Computer Aided Dispatch Simulator (CONSOLE)\x07")  # Update console title.
    a_lock = fasteners.InterProcessLock('app.lock')
    gotten = a_lock.acquire(blocking=False)
    if not gotten:
        sys.stdout.write("\x1b[1m\030[91m[Error] : Program is already running on this machine.\033[39m\x1b[21m\n")
        sys.exit(1)

    system = systemc.System()
    system.logger.debug("Test debug")
    system.logger.log("Test log")
    system.logger.warning("Test warning")
    system.logger.error("Test error")
    system.logger.critical("Critical error")

    from src import main
    main.start(system)
