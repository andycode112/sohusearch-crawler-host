'''
@Author: your name
@Date: 2020-05-26 09:23:39
@LastEditTime: 2020-05-26 12:55:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\sohu-crawler\app\server\Logger.py
'''
import logging
import os
import sys

class Logger():
    def __init__(self, level="debug",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=None,
                 log_path=os.path.join(os.getcwd(), "log"),
                 use_console=True):
        '''
            set_level： log level ,default DEBUG
            name： print name of in the log ，default program name
            log_name： log file of the name ，y-m-d.log
            log_path： 
            use_console：
        '''
        self.logger = logging.getLogger(name)
        if level.lower() == "critical":
            self.logger.setLevel(logging.CRITICAL)
        elif level.lower() == "error":
            self.logger.setLevel(logging.ERROR)
        elif level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif level.lower() == "debug":
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.NOTSET)
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        if log_name:
            log_file_path = os.path.join(log_path, log_name)
            log_handler = logging.FileHandler(log_file_path+".log")

            log_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
            self.logger.addHandler(log_handler)

        if use_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
            self.logger.addHandler(console_handler)

    def addHandler(self, hdlr):
        self.logger.addHandler(hdlr)

    def removeHandler(self, hdlr):
        self.logger.removeHandler(hdlr)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)