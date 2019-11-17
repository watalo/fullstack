#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/7 0:49

'''
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
'''
list1 = [1,2,3,4]
list2 = [5,6,7]

for i in list1:
    list2.append(i)

print(list2)

