#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 14:30
# @Author : huangting
# @File : base_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver



class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_text(self, locator, text):
        return self.find(locator).send_keys(text)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        return self.find_and_click(element)

    def find_and_get_text(self, locator):
        return self.find(locator).text
