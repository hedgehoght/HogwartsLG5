#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15:22
# @Author : huangting
# @File : test_frame.py
from test_selenium.my.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)