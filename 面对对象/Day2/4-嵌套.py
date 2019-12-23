#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/22 23:34
# @Site    : 
# @File    : 4-嵌套.py
# @Software: PyCharm

"""
创建三个学校且三个学校的设施都一样
"""
class School(object):

    def __init__(self,name,address):
        self.name = name
        self.address = address

    def teach(self):
        pass

    def chifan(self):
        pass

obj1 = School('1','a')
obj2 = School('2','b')
obj3 = School('3','c')

class Teacher(object):

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary
        self.school = None

t1 = Teacher('alex',22,150000)
t2 = Teacher('tony',23,100000)
t3 = Teacher('alex',13,11111)

######################
t1.school = obj1
t2.school = obj2
t3.school = obj3

print(t1.school.name)
print(t1.school.address)
print(t1.name)
print(t1.age)

# 准则 同类型的全部归入同一个类


