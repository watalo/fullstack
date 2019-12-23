#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/22 22:44
# @Site    : 
# @File    : 3-属性.py
# @Software: PyCharm

class Foo:
    def __init__(self):
        pass

    @property #
    def start(self):
        return 1

    @property
    def end(self):
        return 2

obj = Foo()
print(obj.start) #
print(obj.end)

'''
总结：
    1、编写时
        - 方法上方写 @property
        - 方法参数：只有一个self
    2、调用时：无需加括号 对象.方法
    3、应用场景:对于简单的方法，当无需传参且有返回值时，可以使用@property
    
共有/私有(__ccc)
'''