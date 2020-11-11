from page.deit import DeitXi
from until.app import BasePage
from until.appium_tools import find_element


class Information(BasePage):
    def person_data(self):  # 个人资料
        shezhi = ("id","hxm")
        find_element(self.driver, shezhi).click()
        return DeitXi(self.driver)
