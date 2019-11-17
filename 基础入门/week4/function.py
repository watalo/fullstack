#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/2
def f(n):
    return n*n

def foo(a,b,func):
    return print(func(a) + func(b))

foo(1,2,f)

# foo(1,2,f()) # f()是执行结果
