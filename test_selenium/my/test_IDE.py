#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE22:47
# @Author : huangting
# @File : test_IDE.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOpen():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = 0

    def test_open(self):
        self.driver.get("https://home.testing-studio.com/")
        time.sleep(2)
        self.driver.set_window_size(1478,825)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT,"热门").click()
        time.sleep(2)
        self.driver.close()