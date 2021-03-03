#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 23:17
# @Author : huangting
# @File : test_dingweipytest.py 没写完
import time

import pytest
from appium import webdriver

class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity '
        desired_caps['noReset'] = "true"
        desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        # 输入中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardowm(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        time.sleep(3)

if __name__  == '__main__':
    pytest.main()