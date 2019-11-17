#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/5 23:0

'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

b = 0
c = 0
d = 0
a = b*100 + c*10 + d
for b in range(1,5):
    for c in range(1,5):
        for d in range(1,5):
            if b != c and b != d and c != d:
                a = b * 100 + c * 10 + d
                print(a)

