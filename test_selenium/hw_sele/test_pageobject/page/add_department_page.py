#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19:14
# @Author : huangting
# @File : add_department_page.py 添加部门页面
from selenium.webdriver.common.by import By

from test_selenium.hw_sele.test_pageobject.page.base_page import BasePage
from test_selenium.hw_sele.test_pageobject.page.contact_page import ContactPage


class AddDepartment(BasePage):
    _name = (By.NAME, "name")
    _js_parent_party_name = (By.CSS_SELECTOR, ".js_parent_party_name")
    _firstone = (By.CSS_SELECTOR, '.ww_dialog_body [id="1688851977003953_anchor"]')
    _submit = (By.CSS_SELECTOR, '[id=__dialog__MNDialog__] div>div>a:nth-child(1)')

    # 添加部门成功
    def add_department(self, name):
        # 部门名称，所属部门，第一个部门，确定
        self.find(*self._name).send_keys(name)
        self.find(*self._js_parent_party_name).click()
        self.find(*self._firstone).click()
        self.find(*self._submit).click()
        return ContactPage(self.driver)

    # 添加部门失败
    def add_department_faile(self, name):
        # 部门名称，所属部门，第一个部门，确定，取消
        self.find(*self._name).send_keys(name)
        self.find(*self._js_parent_party_name).click()
        self.find(*self._firstone).click()
        self.find(*self._submit).click()
        return ContactPage(self.driver)
