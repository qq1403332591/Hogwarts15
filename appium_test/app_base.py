from appium import webdriver


class Base():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
        desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.release
        desired_caps['deviceName'] = 'V1938T'  # 手机/模拟器的型号：adb shell getprop ro.product.model
        desired_caps['appPackage'] = 'com.tencent.wework'  # app的名字：adb shell dumpsys package XXX
        desired_caps[
            'appActivity'] = '.launch.LaunchSplashActivity'  # 同上↑  # .pages.splash.SplashActivity   pages.main.MainActivity
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['unicodeKeyboard'] = True  # 为了支持中文
        desired_caps['resetKeyboard'] = True  # 设置成appium自带的键盘
        desired_caps['noReset'] = True  # 使用app的缓存
        desired_caps['skipDeviceInitialization'] = True  # 跳过设备初始化
        # desired_caps['autoLaunch'] = False # 直接使用打开的app进行测试
        # desired_caps['settings[settingsKey]'] = 0  # 动态元素查找的最大等待时间
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
