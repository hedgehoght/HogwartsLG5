#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 13:50
# @Author : huangting
# @File : test_appiumdemo.py
from appium import webdriver

desired_caps={}
desired_caps['platformNane']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='127.0.0.1:7555'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
driver=webdriver.Remote('http://locaLhost:4723/wd/hub', desired_caps )
driver.quit()
