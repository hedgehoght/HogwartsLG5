#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:29
# @Author : huangting
# @File : main_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium.myAppWork.page.addresslist_page import AddressListPage
from test_appium.myAppWork.page.base_page import BasePage


class MainPage(BasePage):
    # 点击通讯录
    def click_addresslist(self):
        # 进入添加成员页面
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        return AddressListPage(self.driver)