#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19:10
# @Author : huangting
# @File : test_add_department.py
from test_selenium.hw_sele.test_pageobject.page.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        # 实例化MainPage类
        self.main = MainPage()

    # 测试用例-添加部门成功
    def test_add_department(self):
        result = self.main.goto_contact().goto_add_department().add_department("name1").get_department_list()
        assert "name1" in result
        # assert result == "name1111"

    # 测试用例-添加部门失败
    def test_add_department_fail(self):
        result = self.main.goto_contact().goto_add_department().add_department_faile("name1").get_department_list()
        assert "name1" not in result
