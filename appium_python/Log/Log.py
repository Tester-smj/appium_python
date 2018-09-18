#coding=utf-8
import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):

        #创建logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = os.getcwd() + './Log/logs/'
        log_name = log_path+rq+'.log'
        # os.mkdir(log_name)
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #在创建一个handler，用于控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出形式
        formatter = logging.Formatter('%(asctime)s -%(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


def demo():
    a=os.getcwd()
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path =os.getcwd() + '/logs/'
    log_name = log_path + rq + '.log'
    print(a,log_name)
demo()