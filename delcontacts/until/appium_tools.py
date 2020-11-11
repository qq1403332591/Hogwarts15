from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver,locator, timeout=10):
    """
        名字：动态查找元素
        参数：
            driver: 浏览器的实例化对象
            locator: 元素定位的方法 ("id", "username") / ("xpath", "xxxxx") /("aid", "xxxxx") /("aui", "xxxxx")
                类型：
                    ID = "id"
                    XPATH = "xpath"
                    accessibility_id = "aid"
                    android_uiautomator = "aui"
            timeout: 超时时间：默认10
    """

    if locator[0] == "aid":
        locator = ("accessibility id", locator[1])  # locator:appium能够识别
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout=10).until(lambda x: x.find_element(*locator))

def click(driver, locator):
    find_element(driver, locator).click()

def is_element_exsit(driver, locator):
    '''
    判断元素是否存在
    :param driver:
    :param locator:
    :return:
    '''
    try:
        find_element(driver, locator)
        return True
    except:
        return False

def elements(driver,locator,timeout=10):
    return  WebDriverWait(driver, 10).until(lambda driver : driver.find_elements(*locator))


def get_toast_text(driver):
    result = find_element(driver,("xpath","//*[@class='android.widget.Toast']")).text
    return result


def find_by_scroll(driver, text_value):
    '''
    滚动查找元素的方法
    :param driver:需要传入的driver
    :param text_value:文本值
    :return:
    '''
    return driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                               'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{}").instance(0));'.format(
                                   text_value))