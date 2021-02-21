#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:41
# @Author : huangting
# @File : app.py

# 启动app、关闭app、重启app、进入首页。。。
from appium import webdriver

from test_appium.myAppWork.page.base_page import BasePage
from test_appium.myAppWork.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity '
            # 不清空本地缓存，启动app
            desired_caps['noReset'] = "true"
            desired_caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间为0秒
            desired_caps['settings[waitForIdleTimeout]'] = 1
            # 输入中文
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self)->MainPage:
        return MainPage(self.driver)