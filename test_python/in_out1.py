#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : DATEDATE{TIME}
# @Author : huangting
# @File : in_out1.py python输入与输出

import json

# # 字面量插值
# # 格式化输出
# # %的用法:%s %d %f %o %i %x %X %e %E %g %G %c %r %s
# name = lili
# print("my name is %s"%name)

# # formate 支持字符串、列表、字典
# name = 'lili'
# age = 20
# print("my name is {},age is {}".format(name,age))
# print("my name is {0},age is {1}".format(name,age))
# print("my name is {1},age is {0}".format(name,age))
# print("my name is {0},age is {1}{1}".format(name,age))
#
# list1 = [1,2,4]
# dict1 = {'name':'tom','gender':'male'}
# print("my list is {0},dict is {1}".format(list1,dict1))
#
# # 使用*解包list
# namelist = ['lili','tom','jerry']
# print('we name : {},{},{}'.format(*namelist))
#
# # 使用**解包dictionary，并且指定key和value
# print('my name is {name},gender is {gender}'.format(**dict1))


# # F-string
# name = 'lili'
# age = 20
# list1 = [1,2,4]
# dict1 = {'name':'tom','gender':'male'}
# print(f"my name is {name},age is {age},list is {list1},dict is {dict1}")
# print(f"my name is {name},age is {age},list is {list1[1]},dict is {dict1['name']}")
# # 函数
# print(f"my name is {name.upper()}")
# # 表达式
# print(f"my name is {(lambda x:x+1)(2)}")
# # 常数
# print(f"my age is {11}")


# # 文件读取
# # 打开一个IO对象
# # print(open('in_out.txt'))
# # 获取IO值
# f = open('in_out.txt')
# # 是否可读
# print(f.readable())
# # 读取行，列表形式，没有换行，每行都有\n
# # print(f.readlines())
# # 按行读取文件，每次读取一行
# print(f.readline())
# f.close()

# # with 语句块可以将文件打开之后，操作完毕，自动关闭这个文件
# # 图片读取需要使用rb 读取二进制的格式
# # 正常的文本，可以使用rt，也就是它的默认格式即可
# with open('in_out.txt') as f:
#     print(f.readlines())

# with open('in_out.txt') as f:
#     while True:
#         line = f.readline()
#         if line:
#             print(line)
#         else:
#             break

# import json
# json格式转换
# python c c++ java javascript d都可以
# json由字典和列表组成
data = {
    "name":["jerry",'nickname'],
    "age":26,
    "gender":"female"
}

data1 = json.dumps(data)
print(data1)
print(type(data1))

data2=json.loads(data1)
print(data2)
print(type(data2))



