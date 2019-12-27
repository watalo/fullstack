#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/23 23:33
# @Site    : 
# @File    : 组合补充.py
# @Software: PyCharm

# # 1.类或者对象是否能做字典的key
#
# class Foo:
#     pass
#
# user = {
#     Foo:1,
#     Foo():2
# }
# print(user)
#
# # 2.对象中到底有什么?
# class Foo():
#
#     def __init__(self,age):
#         self.age = age
#
#     def display(self):
#         print(self.age)
#
# data_list = [Foo(8),Foo(9)]
#
# for item in data_list:
#     print(item.age,item.display())
#
# #3.
# class StarkConfig():
#
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self,request):
#         print('666')
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
#
# for item in config_obj_list:
#     print(item.num)
#
# #4.
# class StarkConfig():
#
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
# class RoleConfig(StarkConfig):
#     pass
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
#
# for item in config_obj_list:
#     item.changelist(168)
#
# #(1,168)
# #(2,168)
# #(3,168)
#
# #5.
# class StarkConfig():
#
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self,request):
#         print(self.num,request)
#
# config_obj_list2 = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     item.changelist(168)
#
# #6.
# class StarkConfig():
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666,self.num)
#
# config_obj_list3 = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# config_obj_list3[1].run()
# config_obj_list3[2].run()

# #### 7
#
# class StarkConfig(object):
#
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self,request):
#         print(666,self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self,k,v):
#         self._registry[k] = v
#
# site = AdminSite()
# print(len(site._registry)) # 0
# site.register('range',666)
# site.register('shilei',438)
# print(len(site._registry)) # 2
#
# site.register('lyd',StarkConfig(19))
# site.register('yjl',StarkConfig(20))
# site.register('fgz',RoleConfig(33))
#
# print(len(site._registry)) # 5
#
#
#
# #### 8
# class StarkConfig(object):
#
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self,request):
#         print(666,self.num)
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self,k,v):
#         self._registry[k] = v
#
# site = AdminSite()
# site.register('lyd',StarkConfig(19))
# site.register('yjl',StarkConfig(20))
# site.register('fgz',RoleConfig(33))
# print(len(site._registry)) # 3
#
# for k,row in site._registry.items():
#     row.changelist(5)
#
#
# ## 9
# class StarkConfig(object):
#
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self,request):
#         print(666,self.num)
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self,k,v):
#         self._registry[k] = v
#
# site = AdminSite()
# site.register('lyd',StarkConfig(19))
# site.register('yjl',StarkConfig(20))
# site.register('fgz',RoleConfig(33))
# print(len(site._registry)) # 3
#
# for k,row in site._registry.items():
#     row.run()

# 10

class UserInfo(object):
    pass

class Department(object):
    pass

class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self,k,v):
        self._registry[k] = v(k)

site = AdminSite()
site.register(UserInfo,StarkConfig)
site.register(Department,StarkConfig)
print(len(site._registry)) # 3
for k,row in site._registry.items():
    row.run()

'''
1、对象中封装了什么
2、self到底是谁？
'''



#
# if __name__ == '__main__':