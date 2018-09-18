#coding=utf-8
from selenium.webdriver.common.by import By
from AppiumUtil.base import Base

class HomePage(Base):#继承Base类里面的方法
    # 手机注册
    phoneregister_loc = (By.ID, "com.carsland.asd:id/before_newClient")

    # 手机登录
    phonelogin_loc = (By.ID, "com.carsland.asd:id/before_phone")

    #微信登录
    webchatlogin_loc=(By.ID,"com.carsland.asd:id/before_wechat")

    #邮箱登录
    emaillogin_loc=(By.ID,"com.carsland.asd:id/tv_email_login")

    #随便看看
    look_loc=(By.ID,"com.carsland.asd:id/before_look")

    #把每一个元素操作封装成一个方法
    def phoneregister(self):
        # self.find_element(self.phoneregister_loc).click()
        self.click(self.phoneregister_loc)

    def webchatlogin(self):
        # self.find_element(self.webchatlogin_loc).click()
        self.click(self.webchatlogin_loc)

    def phonelogin(self):
        # self.find_element(self.phonelogin_loc).click()
        self.click(self.phonelogin_loc)

    def emaillogin(self):
        # self.find_element(self.emaillogin_loc).click()
        self.click(self.emaillogin_loc)

    def look(self):
        # self.find_element(self.look_loc).click()
        self.click()
