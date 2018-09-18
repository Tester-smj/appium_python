#coding = utf-8
# import os
# # with open("2.txt") as f:
# #     print(f.read())
# os.mkdir("21"+".txt")
# coding = utf-8
'''
二次封装元素方法
加入循环查找方法，提高查找元素的稳定性
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        # self.driver = webdriver.Firefox()
        self.driver = driver

    # 查找元素的过程封装了循环查找
    def find_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*locator))
        return element


    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)


    def click(self, locator):
        self.find_element(locator).click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    mydriver = Base(driver)
    # 元组
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
    inp_loc = ("id", "kw")
    # mydriver.find_element(inp_loc)
    mydriver.send_keys(inp_loc, "bai")
    but_loc = ("id", "su")
    mydriver.click(but_loc)