#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15:29
# @Author : huangting
# @File : add_member_page.py 添加成员页面
from selenium.webdriver.common.by import By

from test_selenium.hw_sele.test_pageobject.page.base_page import BasePage
from test_selenium.hw_sele.test_pageobject.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 用户名，账号ID，手机号
    _username = (By.ID, "username")
    _memberAdd_acctid = (By.ID, "memberAdd_acctid")
    _memberAdd_phone = (By.ID, "memberAdd_phone")
    _js_btn_save = (By.CSS_SELECTOR, ".js_btn_save")
    _js_btn_cancel = (By.CSS_SELECTOR, ".js_btn_cancel")

    # 添加成员成功
    def add_member(self, name, acctid, phone):
        # 输入成员信息，点击保存
        # *代表解元祖，相当于self.find(By.ID, "username")
        # self.find(By.ID, "username").send_keys(name)
        self.find(*self._username).send_keys(name)
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(phone)
        self.find(*self._js_btn_save).click()
        # .代表class
        return ContactPage(self.driver)

    # 添加成员失败
    def add_member_fail(self, name, acctid, phone):
        # 输入成员信息，点击保存
        self.find(*self._username).send_keys(name)
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(phone)
        self.find(*self._js_btn_save).click()
        self.find(*self._js_btn_cancel).click()
        return ContactPage(self.driver)
