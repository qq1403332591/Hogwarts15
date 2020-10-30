from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_test.appium_tools import find_element

from appium_test.app_base import Base
import time


class Test_click(Base):

    def test_daka(self):
        self.driver.update_settings({'waitForIdleTimeout': 0})
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/hgt"]//*[3]').click()
        action = TouchAction(self.driver)
        window = self.driver.get_window_size()
        width = window["width"]
        heigth = window["height"]
        x1 = int(width * 0.5)
        y_start = int(heigth * 0.8)
        y_end = int(heigth * 0.2)
        # 显示等待查找xpath元素是否可见，可见后元素后再执行下面的滑动方法。
        wait = expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@resource-id="com.tencent.wework:id/dha"]/*[1]'))
        WebDriverWait(self.driver, timeout=10).until(wait)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        loc_text = ("text", "打卡")
        find_element(self.driver, loc_text).click()
        waichudaka = ("text", "外出打卡")
        find_element(self.driver, waichudaka).click()
        self.driver.find_element_by_xpath('//*[contains(@text,"次外出")]').click()  # contains匹配一个属性值中包含的次外出的元素
        assert WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
