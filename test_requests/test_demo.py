#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19:29
# @Author : huangting
# @File : test_demo.py
import requests


def test_demo():
    # 获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1feff6a8aa380f82&corpsecret=-EBF-zj-VEAZFAW3rjGi6zkPga0dW8iVjULlvA87r6U"
    r = requests.get(url)
    token = r.json()['access_token']
    # print(token)

    # 利用 requests 的 get 和 post 实现通讯录的增删改查功能
    # 查看成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=chengyuan1"
    r = requests.get(url)
    print(r.json())

    # 增加成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "+86 13800000000",
        "department": [1],
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 更新成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "李四",
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 删除成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
    r = requests.get(url)
    print(r.json())