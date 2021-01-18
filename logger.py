"""
@author: Michał Łopaciuch
@date: 16.01.21
"""

from datetime import datetime
from os import path

class Logger:
    """
    A class used for log messages to logfile

    Attributes
    ----------
    handler: file object
        handler used to work with file

    Methods
    -------
    log(message, desc = '')
        Logs the date, description and message by its handler
    """

    handler = open(path.join('logs', 'results.log'), 'w')

    def log(self, message, desc = ''):
        self.handler.write(f'{datetime.now()} [{desc.upper()}] {message}\n')

    def __del__(self):
        self.handler.close()
