from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




class TestTestdemo():
    def __init__(self):
        options = Options() #调试模式开启时必须要配置一个options
        options.debugger_address = "127.0.0.1:9222"  # debug的地址
        self.driver = webdriver.Chrome()   # 传入options=options 可以复用浏览器

    def addressbook(self):  # 点击通讯录
        self.driver.find_element(By.LINK_TEXT,"通讯录").click()

