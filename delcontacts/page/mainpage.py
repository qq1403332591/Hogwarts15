from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from until.app import BasePage
from until.appium_tools import find_element
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def click_txl(self):  # 点击通讯录
        tongxunlu = ("text","通讯录")
        lianxiren = ("xpath","//*[@resource-id='com.tencent.wework:id/i4l']/*[@text='hogwarts']")
        find_element(self.driver,tongxunlu).click()
        find_element(self.driver,lianxiren).click()
        from page.gerenzhongxin import Information
        return  Information(self.driver)  # 个人信息

    def search(self):
        search_locator = ('id','hxw')
        input_box = ("id", "ghu")
        search_lxrlocator = ('//android.widget.RelativeLayout/android.widget.RelativeLayout//android.widget.TextView[@text="hogwarts"]')
        find_element(self.driver,search_locator).click()
        contact_locator = ("class name","android.widget.TextView")
        find_element(self.driver,input_box).send_keys("hogwarts")
        try:
            WebDriverWait(self.driver,timeout=10).until(EC.visibility_of_element_located(By.XPATH,search_locator))
        except:
            return False




