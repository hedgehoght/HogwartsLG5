#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 10:40
# @Author : huangting
# @File : test_ActionChains.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("https://www.baidu.com/")
        element_click = self.driver.find_element_by_xpath('//*[@id="su"]')
        element_doubleclick = self.driver.find_element_by_xpath('//*[@id="su"]')
        element_rightclick = self.driver.find_element_by_xpath('//*[@id="su"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        action.perform()

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com/")
        ele = self.driver.find_element_by_link_text("更多")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://www.baidu.com/")
        drag = self.driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]')
        drop = self.driver.find_element_by_xpath('//*[@id="kw"]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag,drop).perform()
        # action.click_and_hold(drag).release(drop).perform()
        action.click_and_hold(drag).move_to_element(drop).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://www.baidu.com/")
        ele = self.driver.find_element_by_xpath('//*[@id="kw"]')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


# if __name__ == '__main__':
#     pytest.main(['-v','-s','TestActionChains'])