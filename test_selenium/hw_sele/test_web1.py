#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 16:42
# @Author : huangting
# @File : test_web1.py
import json
from time import sleep

from selenium import webdriver


class TestWeb():
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        # self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
        # pass

    def test_cookie(self):
        # # 获取cookie
        # cookies = self.driver.get_cookies()
        # with open("cookie.json","w") as f:
        #     json.dump(cookies,f)

        self.driver.get("https://work.weixin.qq.com/")
        # 打开cookie
        with open("cookie.json","r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element_by_id("menu_customer").click()
        sleep(3)

    # def test_menu_customer(self):
    #     self.driver.get("https://work.weixin.qq.com/")
    #     self.driver.find_element_by_id("menu_customer").click()