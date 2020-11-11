from until.app import BasePage
from until.appium_tools import find_element, find_by_scroll


class DeitXi(BasePage):

    def editcy(self):  #  编辑成员
        edit_locator = ("id","b91")
        queding_locator = ("xpath",'//*[contains(@text,"确定")]')
        find_element(self.driver,edit_locator).click()
        find_by_scroll(self.driver,"删除成员").click()
        find_element(self.driver,queding_locator).click()
        from page.mainpage import MainPage
        return MainPage(self.driver)