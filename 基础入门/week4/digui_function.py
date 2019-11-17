#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/2

'''
递归函数
关于递归的特点：
1、调用自身函数
2、有一个结束条件
3、

【1】但凡递归可以写的，循环都可以解决
【2】递归的效率在很多使用效率很低


'''

# def jiecheng(a):
#     i = 1
#     j = 1
#     while i <= a:
#         j = j*i
#         i += 1
#     return j
#
# def fat(a):
#     j = 1
#     for i in range(1,a+1):
#         j = j*i
#     return j
#
# print(jiecheng(7))
# print(fat(7))
#
# def fact(a):
#     if a ==1:
#         return 1
#     return a*fact(a-1)
#
# print(fact(7))

def fibs(a):
    if  a == 1:
        return 0
    elif a == 2:
        return 1
    return fibs(a-1)+fibs(a-2)

print(fibs(-1))