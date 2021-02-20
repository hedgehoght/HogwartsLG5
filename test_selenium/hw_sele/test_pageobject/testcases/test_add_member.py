#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 16:06
# @Author : huangting
# @File : test_add_member.py
from test_selenium.hw_sele.test_pageobject.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        # 实例化MainPage类
        self.main = MainPage()

    # 测试用例-添加成员成功
    def test_add_member(self):
        # 1. 首页跳转到添加成员页面 2. 添加成员 3. 获取成员信息
        result = self.main.goto_add_member().add_member("崔丝塔娜", "1111", "13191011811").get_list()
        assert "崔丝塔娜" in result

    # 测试用例-添加成员失败
    def test_add_member_fail(self):
        # 1. 描述业务场景， 不是描述具体的行为操作
        result = self.main.goto_add_member().add_member_fail("test2", "111", "13191011819").get_list()
        assert "test2" not in result
