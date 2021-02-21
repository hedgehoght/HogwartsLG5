#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 12:10
# @Author : huangting
# @File : test_addMember.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddMenber():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity '
        desired_caps['noReset'] = "true"
        desired_caps["ensureWebviewsHavePages"] = True
        desired_caps['settings[waitForIdleTimeout]'] = 0
        # 输入中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)


    def teardowm(self):
        self.driver.quit()

    def test_add_member(self):
        name = "name2"
        xingbie = "女"
        phone = "18610293847"
        youxiang = "111@qq.com"
        dizhi = "西二旗"
        # 进入添加成员页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='//*[@text='必填']']").send_keys("name2")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # 选择性别
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if xingbie == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 输入手机号
        self.driver.find_element_by_id("com.tencent.wework:id/eq7").send_keys(phone)
        # 输入邮箱
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(youxiang)
        # 输入地址，选择地址，确定
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'地址')]/../android.widget.LinearLayout").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText']").send_keys(dizhi)
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.ListView']/android.widget.RelativeLayout[1]/android.widget.LinearLayout").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        # 点击保存
        self.driver.find_element_by_id("com.tencent.wework:id/gur").click()
        ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ele