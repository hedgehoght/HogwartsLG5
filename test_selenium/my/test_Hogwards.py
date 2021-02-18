#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE23:03
# @Author : huangting
# @File : test_Hogwards.py
from selenium import webdriver
from time import sleep

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        # self.driver.get("http://www.ceshiren.com")
        # sleep(1)
        # self.driver.find_element_by_link_text("热门").click()
        # sleep(1)
        # self.driver.find_element_by_link_text("精华帖").click()
        # sleep(1)
        # self.driver.find_element_by_class_name("link-top-line").click()
        # sleep(1)

        self.driver.get("http://www.ceshiren.com")
        self.driver.find_element_by_link_text("热门").click()
        self.driver.find_element_by_link_text("精华帖").click()
        self.driver.find_element_by_class_name("link-top-line").click()