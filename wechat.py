# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def test():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'Lenovo K50-t5'
    # desired_caps['app'] = PATH('weixin6510android1080.apk')
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = '.ui.LauncherUI'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    sleep(2)

    driver.find_element_by_name('登录').click() #find_element_by_name find_element_by_accessibility_id
    # driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
    sleep(1)

    driver.find_element_by_name('用微信号/QQ号/邮箱登录').click()
    sleep(1)

    textfields = driver.find_elements_by_class_name("android.widget.EditText")
    textfields[0].send_keys("1246643560")
    textfields[1].send_keys("Lxm261295")
    driver.find_element_by_name('登录').click()
    sleep(1)

    driver.quit()

if __name__=="__main__":
    test()
