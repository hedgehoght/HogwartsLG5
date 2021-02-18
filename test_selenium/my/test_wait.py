#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 17:37
# @Author : huangting
# @File : test_wait.py
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@href="/categories"]').click()
        # 直接等待
        # sleep(3)
        # 显式等待
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]')) >= 1
        # WebDriverWait(self.driver,10).until(wait)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
