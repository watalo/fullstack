#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/22 19:58
# @Site    : 
# @File    : 1-变量.py
# @Software: PyCharm

# class Foo:
#     def __init__(self): # 构造方法
#         self.name = name
#         self.age = 21
#
# obj = Foo('国宴中')

#
# class Food:
#     def func(self):
#         print(self)
#
# obj = Food()
# print(obj.func())


class Circle:
    def __init__(self,r):
        self.r = r
        self.pi = 3.1415927
    def mianji(self):
        return 0.5*self.r*self.r*self.pi
    def zhouchang(self):
        return 2*self.r*self.pi

obj = Circle(3)
r = obj.mianji()
q = obj.zhouchang()
print(r,q)

class Foo:
    #类变量/静态字段
    country = '中国'
    # 方法
    def __init__(self, name):
        self.name = name  # 实例变量/字段
    # 方法
    def func(self):
        pass

# obj:Foo类的对象 或者 Foo类的实例
obj1 = Foo('继红')
obj2 = Foo('阳光')

obj1.country = '美国'
print(obj1.country)
print(obj2.country)

Foo.country = '美国'
print(obj1.country)
print(obj2.country)

# 成员修饰符
#私有实例变量（字段）:self.__name

class Foo:
    country = "CN"
    __city = 'SH'

    def __init__(self,name):
        self.name = name
        self.age = 123
        # 私有实例变量（字段）
        self.__name = name+'a'

    def func(self):
        print(self.name)

    def funs(self):
        print(self.__name)

    def funt(self):
        print(Foo.__city)

obj = Foo('sss')
print(obj.name)
print(obj.age)
obj.func()
obj.funs()
obj.funt()


class Foss:
    country = "CN"
    __city = 'SH'

    def __init__(self, name):
        self.__name = name

obj3 = Foss('大大大')
print(obj3._Foss__name)  # 不推荐
