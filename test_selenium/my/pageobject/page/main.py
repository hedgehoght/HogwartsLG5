#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20:31
# @Author : huangting
# @File : main.py
from selenium.webdriver.common.by import By

from test_selenium.my.pageobject.page.basepage import BasePage
from test_selenium.my.pageobject.page.login import Login
from test_selenium.my.pageobject.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self._driver)