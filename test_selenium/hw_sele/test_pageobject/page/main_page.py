#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15:28
# @Author : huangting
# @File : main_page.py 微信主页面
from selenium.webdriver.common.by import By

from test_selenium.hw_sele.test_pageobject.page.add_member_page import AddMemberPage
from test_selenium.hw_sele.test_pageobject.page.base_page import BasePage


class MainPage(BasePage):
    # 跳转到通讯录页面
    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        from test_selenium.hw_sele.test_pageobject.page.contact_page import ContactPage
        return ContactPage(self.driver)

    # 跳转到添加成员页面
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        # 快捷键 alt+回车可以快捷导入
        return AddMemberPage(self.driver)

    # 跳转到导入通讯录页面
    def goto_import_member(self):
        pass
