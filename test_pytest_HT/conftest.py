#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE{TIME}
# @Author : huangting
# @File : conftest.py

import os

import pytest
import yaml

from test_pytest_HT.calculator import Calculator

# 通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "/data.yml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    # print(datas)
    # 获取文件中key为datas的数据
    add_datas = datas["add"]
    sub_datas = datas["sub"]
    mul_datas = datas["mul"]
    div_datas = datas["div"]
    # 获取文件中key为ids的数据
    add_ids = datas["addids"]
    sub_ids = datas["subids"]
    mul_ids = datas["mulids"]
    div_ids = datas["divids"]

@pytest.fixture(params=add_datas, ids=add_ids)
def get_add_datas(request):
    print("\n开始计算")
    data = request.param
    print(f"\nrequest.param的测试数据是：{data}")
    yield data
    print("\n结束计算")

@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=div_datas, ids=div_ids)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc
