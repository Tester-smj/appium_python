#coding=utf-8
import unittest,time,sys,os,logging,threading
# import BSTestRunner
from BeautifulReport import BeautifulReport
from AppiumUtil.AppiumServer import AppiumServer
from Log.Log import Logger
from Util.Send_Email import send_mail

mylogger = Logger(logger="RunTest").getlog()

class RunTest():
    def __init__(self):
        print("let's go")

def new_report(testreport):
    '''查找测试报告目录，找到最新生成的测试报告文件'''
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    mylogger.info(file_new)
    return file_new

#指定测试用例为当前文件夹下的test_case目录
test_dir = './Test_Case'
test_report = './TestReport'
discover = unittest.defaultTestLoader.discover(test_dir, pattern = '*_case.py')

if __name__ == "__main__":
    # get devices number
    rt = os.popen("adb devices").readlines()
    n = len(rt) - 2
    #报告模板
    if n==0:
        mylogger.error("*"*5+"当前无设备连接"+"*"*5)
    else:
        now = time.strftime("%Y-%m-%d-%H%M")
        #报告名称
        filename = now + 'Test_Result.html'
        result = BeautifulReport(discover)
        result.report(filename=filename, description='测试deafult报告', log_path='TestReport')
        new_report = new_report(test_report)
        # send_mail(new_report)
