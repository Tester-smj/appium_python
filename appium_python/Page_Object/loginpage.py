#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from AppiumUtil.base import Base

#页面对象（PO）登录页面
class LoginPage(Base):
    #返回
    return_loc = (By.ID,"com.carsland.asd:id/login_back")

    #国家地区选择
    area_loc = (By.ID,"com.carsland.asd:id/ll_area_code")

    #手机号码
    phonenumber_loc =(By.ID,"com.carsland.asd:id/login_phone")

    #密码
    password_loc = (By.ID,"com.carsland.asd:id/login_password")

    #登录按钮
    login_loc = (By.ID,"com.carsland.asd:id/login")

    #元素操作
    def fh(self):
        self.find_element(*self.return_loc).click()

    def area(self):
        self.find_element(*self.area_loc).click()

    def login_phonenumber(self,text):
        self.send_keys(self.phonenumber_loc,text)

    def login_password(self,text):
        self.send_keys(self.password_loc,text)

    def login_click(self):
        # self.find_element(self.login_loc).click()
        self.click(self.login_loc)

    #登录操作
    def login(self,phone,password):
        self.login_phonenumber(phone)
        self.login_password(password)
        self.login_click()







