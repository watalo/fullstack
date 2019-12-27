#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/22 21:59
# @Site    : 
# @File    : 2-方法.py
# @Software: PyCharm

################ 没必要写实例方法 ############
class Foo:
    def __init__(self,name):
        self.name = name

    def func(self):
        print("没必要用实例方法")

obj = Foo('1')
obj.func()

################ 有必要写实例方法 ############
class Foo1:
    def __init__(self,name):
        self.name = name

    def func(self):
        print(self.name)

obj1 = Foo1('有必要写实例方法')
obj1.func()

################### 静态方法 ################
class Foo2:
    def __init__(self,name):
        self.name = name
    # 实例方法（至少有一个方法，self）
    def func(self):
        print(self.name)
    # 静态方法（如果方法中无需使用对象中封装的值没有参数），类似于函数
    @staticmethod
    def display():
        print('666')

Foo2.display()

'''
总结：
    1、编写时：
        - 方法上方写 @staticmethod
        - 方法参数可有可无
    2、调用时
        - 类.方法名（） ** 推荐使用
        - 对象.方法名（） 
    3、什么时候用静态方法？
        - 无需调用对象中已封装的值
'''
################### 类方法 ################
class Foo3:
    def __init__(self,name):
        self.name = name
    # 实例方法（至少有一个参数，self）
    def func(self):
        print(self.name)
    # 静态方法（如果方法中无需使用对象中封装的值没有参数），类似于函数
    @staticmethod
    def display():
        print('666')
    # 类方法(至少有一个参数，cls)
        # 不用实例化对象
        # 需要用当当期类的时候才用
        # 相对于静态方法的一种补充——需要传递类的时候在静态方法中添加 cls 变量
    @classmethod
    def show(cls,x1,x2):
        print(cls,x1,x2)

Foo3.show(1,2)

'''
总结：
    1、定义时：
        - 方法上方写：@classmethod
        - 方法的参数：至少有一个cls参数
    2、执行时：
        - 类名.方法名() # 默认会将当前类传递到
    3、什么时候用？
        - 如果在方法中会使用到当前类，那么就可以使用类方法
'''
################### 方法成员修饰符 ################
class Foo4:
    def __init__(self):
        pass

    def __display(self,arg):
        print('私有方法',arg)

    def show(self):
        self.__display(123)

obj4 = Foo4()
print(obj4.show())