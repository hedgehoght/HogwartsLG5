#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20:52
# @Author : huangting
# @File : login.py
from selenium.webdriver.common.by import By

from test_selenium.my.pageobject.page.basepage import BasePage
from test_selenium.my.pageobject.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)