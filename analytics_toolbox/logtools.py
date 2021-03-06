#AUTOGENERATED! DO NOT EDIT! File to edit: dev/03_logtools.ipynb (unless otherwise specified).

__all__ = ['BaseLog', 'LOGNAME', 'FileLog', 'LocalLog', 'StreamLog', 'logfile_to_df']

#Cell

import logging
import sys

import pandas as pd

#Cell

LOGNAME = "analytics_toolbox"

class BaseLog:
    def _init_logobj(self, handler):
        self.logger = logging.getLogger(LOGNAME)
        self.logger.setLevel(logging.DEBUG)
        self.fh = handler
        self.fh.setLevel(logging.DEBUG)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)


#Cell

class FileLog(BaseLog):
    """
    Creates a local logfile where these classes are imported,
    showing database connections and what was run on databases.
    """
    def __init__(self, logfile):
        handler = logging.FileHandler(logfile)
        self._init_logobj(handler)

class LocalLog(FileLog):
    def __init__(self, logfile):
        super().__init__(logfile)


#Cell

class StreamLog(BaseLog):
    """
    Logs to STDOUT, useful for scripts that query DBs.
    Every query will print JSON with information about SQL ran.
    """

    def __init__(self):
        handler = logging.StreamHandler(sys.stdout)
        self._init_logobj(handler)


#Cell

def logfile_to_df(logfile):
    pass