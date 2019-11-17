#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/6 21:12
'''
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

x+100 = n**2
x+100+168 = m**2
（m+n）(m-n)=168
i * j =168
i+j = 2m
i-j = 2n
信息：1、i和j 都是偶数,整数，
      2、i*j=168

'''
for i in range(1,85):
    if 168%i == 0:
        j = 168/i
        if j > i and (j-i)%2 == 0 and (i-j)%2 == 0:
            m = (i+j)/2
            n = (i-j)/2
            x = n**2 - 100
            print(x)




