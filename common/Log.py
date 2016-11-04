import os
import time
from common.Color import Color
from common.singleton import singleton


@singleton
class Log:
    def __init__(self, suite_name):
        if os.path.exists('log/%s.txt' % suite_name):
            os.remove('log/%s.txt' % suite_name)
        self.log = open('log/%s.txt' % suite_name, 'a')

    def __del__(self):
        self.log.close()

    def error(self, info):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        Color.print_red_text(info)
        self.log.write("%s >>> ERROR >>> %s\n" % (ts, info))

    def debug(self, info):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.log.write("%s >>> DEBUG >>> %s\n" % (ts, info))

    def warning(self, info):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.log.write("%s >>> WARNING >>> %s\n" % (ts, info))

    def info(self, info):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.log.write("%s >>> INFO >>> %s\n" % (ts, info))
