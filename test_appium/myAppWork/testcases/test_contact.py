#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15:01
# @Author : huangting
# @File : test_contact.py
import pytest
import yaml

from test_appium.myAppWork.page.app import App

def get_data():
    with open('../data/data.yaml',encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data

class TestContect():
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,xingbie,phone", get_data())
    def test_add_contact(self, name, xingbie, phone):
        # name = "chengyuan1"
        # xingbie = "女"
        # phone = "12345678901"
        toast = self.main.click_addresslist().add_member().addconect_menual().edit_name(name).edit_gender(xingbie).edit_phonenum(phone).click_save().get_toast()
        assert toast == "添加成功"
