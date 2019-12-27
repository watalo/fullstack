#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/25 1:18
# @Site    : 
# @File    : 特殊方法.py
# @Software: PyCharm

class Foo():

    def __init__(self, a, b):          # 初始化方法
        self.a = a
        self.b = b

    def __new__(cls, *args, **kwargs): # 构造方法
        """

        @param args: 
        @param kwargs:
        """
        return object.__new__(cls)


if __name__ == '__main__':