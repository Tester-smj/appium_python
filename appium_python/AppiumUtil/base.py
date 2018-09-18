#coding=utf-8
#基本层
import sys,os,time
from Log.Log import Logger
from appium import webdriver

mylogger = Logger(logger="Base").getlog()

class Base(object):

    #初始化driver
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    #*参数个数不是固定的（By.ID, 'kw'）
    def find_element(self, loc):
        mylogger.info("开始查找 %s 元素 %s" %(loc))
        try:
            result=self.driver.find_element(*loc)
            mylogger.info("找到了 %s 元素 %s"%(loc))
            return result
        except :
            mylogger.info("没有找到 %s 元素 %s" %(loc))
            self.driver.quit()
            mylogger.error("终止测试")

    def send_keys(self,loc,text):
        mylogger.info("%s正在输入%s" %(loc,text))
        try:
            sendresult = self.find_element(loc).send_keys(text)
            mylogger.warn("%s 已经输入%s" % (loc, text))
            return sendresult
        except :
            mylogger.warning(" %s 没有输入 %s" %(loc,text))

    #封装点击操作
    def click(self,loc):
        # self.find_element(loc).click()
        # mylogger.info("点击了 %s 元素 %s" % (loc))
        try:
            result = self.find_element(loc).click()
            mylogger.info("点击了 %s 元素 %s" %(loc))
            return result
        except :
            mylogger.info("没有点击 %s 元素 %s" % loc)

    #退出操作
    def shut_down(self):
        mylogger.info("******准备关闭app******")
        try:
            result = self.driver.quit()
            mylogger.info("******已经关闭app******")
            return result
        except:
            mylogger.info("******关闭app失败******")

    #滑动操作
    def swipe_Down(self):
        try:
            mylogger.info("******准备下滑"+"*"*5)
            window_size = self.driver.get_window_size()
            width = window_size.get('width')
            height = window_size.get("height")
            time.sleep(1)
            Down=self.driver.swipe(width/2,height/4,width/2,height*3/4,500)
            time.sleep(1)
            mylogger.info("******下滑了%s******" %(width/2))
            return Down
        except:
            mylogger.info("-----下滑异常-----")

    def swipe_Up(self):
        try:
            mylogger.info("-----准备上滑-----")
            window_size = self.driver.get_window_size()
            width = window_size.get("width")
            height = window_size.get("height")
            time.sleep(1)
            Up=self.driver.swipe(width/2,height*3/4,width/2,height/4,500)
            time.sleep(1)
            mylogger.info("-----上滑了%s -----" % (height*3/4))
            return Up
        except:
            mylogger.info("-----上滑异常-----")

    def swipe_Left(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        Left=self.driver.swipe(width/4,height/2,width*3/4,height/2,500)
        return Left

    def swipe_Right(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        Right=self.driver.swipe(width*4/5,height/2,width/5,height/2,500)
        return Right

    #保存图片
    def take_Shot(self, name):
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "..\\Result\\" + day
        tm = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        type = '.png'

        filename = ''
        if os.path.exists(fp):
            filename = fp + "\\" + tm + '_' + name + type
        else:
            os.makedirs(fp)
            filename = fp + "\\" + tm + '_' + name + type
        self.driver.save_screenshot(filename)
