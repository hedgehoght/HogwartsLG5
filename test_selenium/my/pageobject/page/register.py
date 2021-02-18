#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20:44
# @Author : huangting
# @File : register.py
from selenium.webdriver.common.by import By

from test_selenium.my.pageobject.page.basepage import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("hello")
        self.find(By.ID,"manager_name").send_keys("hello2")
        return True

