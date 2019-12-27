#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/24 0:31
# @Site    : 
# @File    : 主动调用其他类的成员.py
# @Software: PyCharm

### 方式1
class Base():

    def f1(self):
        print('5个功能')


class Foo():

    def f1(self):
        print('3个功能')
        Base.f1(self)

obj = Foo()
obj.f1()


### 方式2
class Base():

    def f1(self):
        super().f1()
        print('5个功能')


class Foo(Base):

    def f1(self):
        print('3个功能')
        super().f1()


obj = Foo()
obj.f1()
