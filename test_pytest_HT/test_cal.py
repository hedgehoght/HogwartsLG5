#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE{TIME}
# @Author : huangting
# @File : test_cal.py

import pytest
import yaml
from test_pytest_HT.calculator import Calculator

def open_file():
    with open("./data.yml") as f:
        data = yaml.safe_load(f)
        # print(data)
    return data

class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def setup(self):
        print("\n开始计算")
    def teardown(self):
        print("\n计算结束")

    # 加
    @pytest.mark.parametrize("a,b,expect",open_file()["add"],ids=open_file()["addids"])
    def test_add(self,a,b,expect):
        result = None
        try:
            result = self.calc.add(a,b)
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == expect

    # 减
    @pytest.mark.parametrize("a,b,expect",open_file()["sub"],ids=open_file()["subids"])
    def test_sub(self, a, b, expect):
        result = None
        try:
            result = self.calc.sub(a, b)
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == expect

    # 乘
    @pytest.mark.parametrize("a,b,expect",open_file()["mul"],ids=open_file()["mulids"])
    def test_mul(self, a, b, expect):
        result = None
        try:
            result = self.calc.mul(a, b)
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == expect

    # 除
    @pytest.mark.parametrize("a,b,expect",open_file()["div"],ids=open_file()["divids"])
    def test_div(self, a, b, expect):
        result = None
        try:
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == expect


