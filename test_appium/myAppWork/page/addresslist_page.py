#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:47
# @Author : huangting
# @File : addresslist_page.py
from appium.webdriver.common.mobileby import MobileBy

from test_appium.myAppWork.page.base_page import BasePage
from test_appium.myAppWork.page.memberinvit_page import MemberInvitePage


class AddressListPage(BasePage):
    # 点击添加成员
    def add_member(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.scroll_find_click("添加成员")
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        return MemberInvitePage(self.driver)