#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE{TIME}
# @Author : huangting
# @File : except1.py python错误与异常

try:
    num1 = int(input("输入被除数"))
    num2 = int(input("输入除数"))
    print(num1/num2)
# except ZeroDivisionError:
#     print("除数不能为0")
# except ValueError:
#     print("输入的值必须是数值型整数")
except:
    print("这是一个通用型异常")
else:
    print("程序没有发生异常")
finally:
    print("无论发没发生异常都执行")

# x = 10
# if x>5:
#     raise Exception("这是抛出的异常信息")
#
# class MyException(Exception):
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2
#
# raise MyException("value1","value2")
