import shelve
import time
import yaml
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from testing.appium_tools import find_element


class TestTestdemo():
    def setup_class(self):
        options = Options() #调试模式开启时必须要配置一个options
        options.debugger_address = "127.0.0.1:9222"  # debug的地址
        self.driver = webdriver.Chrome()   # 传入options=options 可以复用浏览器
        self.driver.implicitly_wait()

    def test_cookies(self):
        # driver.get_cookies 可获取当前打开页面的cookies
        # add_cookie 把获取的cookie添加到当前的页面中去
        data = yaml.safe_load(open('./cookies.yml'))
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for i in data:
            self.driver.add_cookie(i)  # 加入cookie

        self.driver.refresh()  # 刷新当前网页
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #  这里又打开了一次的url是因为我们首次打开了一个网页，然后将准备好的cookie加了进去，这时候我们要重新打开一下页面或者刷新一下页面才会显示登录成功
        time.sleep(3)

    def test_AddressBook(self):
        Upload = ("class name",'<input type="file" accept=".xls,.xlsx" class="ww_fileImporter_fileContainer_uploadInputMask">')
        self.driver.find_element(By.LINK_TEXT,"通讯录").click()


    def test_cook(self):
        data = yaml.safe_load(open('./cookies.yml'))
        db = shelve.open("data")
        db["cookieaa"] = data
        print(db["cookieaa"])
    def teardown_class(self):
        self.driver.quit()

