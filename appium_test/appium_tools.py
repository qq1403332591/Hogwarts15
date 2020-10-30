from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, locator):
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout=10).until(lambda x: x.find_element(*locator))
