#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:46
# @Author : huangting
# @File : test_form.py
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://www.zhihu.com/signin?next=%2F")
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()
        self.driver.find_element_by_name("username").send_keys("test")
        self.driver.find_element_by_name("password").send_keys("mima")
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button')
        sleep(3)

