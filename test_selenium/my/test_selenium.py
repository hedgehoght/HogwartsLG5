#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE22:22
# @Author : huangting
# @File : test_selenium.py
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
