#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:50
# @Author : huangting
# @File : memberinvit_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium.myAppWork.page.base_page import BasePage
from test_appium.myAppWork.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    # 点击手动添加
    def addconect_menual(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        return ContactEditPage(self.driver)

    def get_toast(self):
        # ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        ele = self.find_and_get_text((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        return ele