#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# date: 2019/10/2


str = ['a', 'b', 'c', 'd']


def fun1(s):
    if s != 'a':
        return s


ret = filter(fun1, str)
print(ret)
print(list(ret))
