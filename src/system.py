"""
system.py
class System()

A class that holds reference to all useful classes such as logger, version, handlers etc
"""
from src import logger


class System:
    def __init__(self):
        self.logger = logger.Logger("app.log")
