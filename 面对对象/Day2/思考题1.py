#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/22 21:49
# @Site    : 
# @File    : 思考题1.py
# @Software: PyCharm

'''
    如何验证私有字段儿子都不知道
'''
class Base:
    __secret = '受贿'
    #
    # def __init__(self,):
    #     self.__name =
    def zt(self):
        print(Base.__secret)


class Foo(Base):

   def func(self):
        print(self.__secret)
        print(Foo.__secret)

if __name__ == '__main__':

    obj = Foo()
    obj.func()

    obj1= Base()
    obj1.zt()