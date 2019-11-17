#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/7 0:36
'''
斐波那契数列
'''

def fib(n):
    before,after = 0, 1
    if n > 2:
        for i in range(n):
            before, after = after, before+after
        return after
    elif n == 1:
        return before
    elif n == 2:
        return after
    else:
        print('请输入大于1的整数')


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

