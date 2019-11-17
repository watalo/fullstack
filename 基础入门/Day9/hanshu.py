#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# date: 2019/9/21

# def eat( a, b, *args):
#
#     print('I want eat',args,a,b)
#
# eat('dabian','xiaobian','pi')

# ====函数嵌套的顺序问题====
# def fun2():        #1
#     print(222)     #4
#     def fun3():    #5
#         print(444) #8
#     print(333)     #6
#     fun3()         #7
#     print(555)     #9
# print(111)         #2
# fun2()             #3
# print(666)         #10
#==========================


#global\nonlocal 变量的运用====
#
# a = 108
# def fun():
#     global a
#     a = 29
# print(a)
# fun()
# print(a)

# a = 1
# def fun_1():            #2.1
#     a = 2
#     def fun_2():        #2.2
#         nonlocal a
#         a = 3
#         def fun_3():    #2.2.2
#             a = 4
#             print(a)    #2.2.2.1
#         print(a)        #2.2.1    >>>3
#         fun_3()         #2.2.2    >>>4
#         print(a)        #2.2.3    >>>3
#     print(a)            #2.1      >>>2
#     fun_2()             #2.2      >>>3-4-3
#     print(a)            #2.3      >>>3
# print(a)                #1        >>>1
# fun_1()                 #2        >>>2-3-4-3-3
# print(a)                #3        >>>1
# # 结果：1-2-3-4-3-3-1



# # repr 输出一个字符串的官方表示形式.
# print(repr('大家好,\n \t我叫周杰伦'))
# print('大家好我叫周杰伦')
# # %r %r用的就是repr
# name = 'taibai'
# print('我叫%r' % name)

# lst = ['alex','wusir','taibai']
# for i,k in enumerate(lst):
#     print('这是序号',i)
#     print('这是元素',k)

a = iter([1,2,3,])
print(a)