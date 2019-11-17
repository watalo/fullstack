#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/7 0:21
'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''
from typing import List

# x = int(input('1>>:'))
# y = int(input('2>>:'))
# z = int(input('3>>:'))
# max = 0
# # listxyz = [x,y,z]
# print(max(listxyz))

# if x > y:
#     a = x
#     if x < z:
#         a = z
# else:
#     a = y
#     if y < z:
#         a = z
#
# print(a)

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)