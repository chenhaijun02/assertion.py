#!/usr/bin/env python
# _*_coding:utf-8 _*_
import os, time, logging
log_path=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)


class Log(object):
    """
    log日志类
    """

    def __init__(self):
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s]-%(levelname)s:%(message)s')

    def __console(self, level, message):
        fh=logging.FileHandler(self.logname, 'a', 'utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    log = Log()
    log.info("---测试---")