from selenium.webdriver.remote.webdriver import WebDriver

from page.index import TestTestdemo


class Address():
    def __init__(self,driver:WebDriver):
        self.driver = driver


    def AddreesPage(self):
        self.driver.find_element()
