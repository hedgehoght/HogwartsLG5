#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 16:40
# @Author : huangting
# @File : test_dingwei.py
import time

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity '
desired_caps['noReset'] = "true"
desired_caps['dontStopAppOnReset'] = "true"
desired_caps['skipDeviceInitialization'] = "true"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("alibaba")
time.sleep(3)
driver.back()
driver.back()
driver.quit()
