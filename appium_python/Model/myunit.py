#coding=utf-8
import unittest,time
from Driver.driver import lauchapp
from Log.Log import Logger
from AppiumUtil.base import Base

mylogger = Logger(logger="MyTest").getlog()


class MyTest(unittest.TestCase):
    '''封装unittest测试套件'''
    def setUp(self):
        mylogger.info("*"*5+"正在启动设备"+"*"*5)
        self.driver = lauchapp()
        self.driver.implicitly_wait(10)
        mylogger.info("*"*5+"设备已经启动"+"*"*5)
        mylogger.info("*"*5+"等待启动页加载"+"*"*5)
        time.sleep(8)

    def tearDown(self):
        qo= Base(self.driver)
        # qo.shut_down()
        mylogger.info("*"*5+'测试结束'+"*"*5)