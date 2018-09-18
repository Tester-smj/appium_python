#coding=utf-8
from time import sleep
import sys
from Model import myunit,function
from Page_Object.loginpage import LoginPage
from Page_Object.homepage import HomePage
from Log.Log import Logger
# from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

mylogger = Logger(logger="LoginTest").getlog()

'''
继承myunit.MyTest类里面的方法
'''
class LoginTest(myunit.MyTest):

    def test_login_user_pwd_wrong(self):
        '''用户名、密码为错误登录'''
        ho = HomePage(self.driver)
        ho.phonelogin()
        po = LoginPage(self.driver)
        po.login('18707148477','111110')
        sleep(2)

    def test_login_user_pwd_ok(self):
        '''用 户名、密码为正确登录'''
        ho = HomePage(self.driver)
        ho.phonelogin()
        po = LoginPage(self.driver)
        po.login('18707148477','111111')
        sleep(2)
