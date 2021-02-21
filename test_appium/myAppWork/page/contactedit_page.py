#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:54
# @Author : huangting
# @File : contactedit_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.myAppWork.page.base_page import BasePage

# 编辑成员的信息
class ContactEditPage(BasePage):
    def edit_name(self, name):
        self.find_and_text((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText"), name)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        return self

    def edit_gender(self, xingbie):
        # 选择性别
        # 显示等待
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        ele.click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if xingbie == "女":
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        return self

    def edit_phonenum(self, phone):
        # self.driver.find_element_by_id("com.tencent.wework:id/eq7").send_keys(phone)
        self.find_and_text((MobileBy.ID, "com.tencent.wework:id/eq7"), phone)
        return self

    def click_save(self):
        # self.driver.find_element_by_id("com.tencent.wework:id/gur").click()
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/gur"))
        from test_appium.myAppWork.page.memberinvit_page import MemberInvitePage
        return MemberInvitePage(self.driver)