#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 9:37
# @Author : huangting
# @File : test_xpath.py
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestXpath():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_xpath(self):
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID,'su').click()