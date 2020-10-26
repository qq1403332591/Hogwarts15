import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_webdriverwait():
    def setup(self):
        options = Options()  # 调试模式开启时必须要配置一个options
        options.debugger_address = "127.0.0.1:9222"  # debug的地址
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def test01_case(self):
        self.driver.find_element(By.XPATH, '//*[@id="ember43"]').click()

        # def wait(x):
        #     return len(self.driver.find_elements(By.CLASS_NAME, 'category-name')) >= 1
        wait = expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'category-name'))
        expected_conditions.visibility_of_element_located
        WebDriverWait(self.driver, 10).until(wait)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="ember194"]/a/div/span').click()
