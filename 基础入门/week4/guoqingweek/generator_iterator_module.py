#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/4 22:46

'''
1、生成器
2、迭代器
3、模块 os time json
'''

# #列表生成式
# # def f(n):
# #     return n*n*n
#
# cai = [x*2 for x in range(5)]
# print(cai)
#
# chushi = (x*2 for x in range(5)) #这就是生成器
# print(chushi) #<generator object <genexpr> at 0x0000009D27D5E848>
#
# print(chushi.__next__()) # 这是py2的用法
# print(next(chushi)) #2
# print(next(chushi)) #4
# print(next(chushi)) #6
# print(next(chushi)) #8
# #print(next(chushi)) #StopIteration
#
# #要吃第5盘菜，必须把前面的4盘吃完
# #生成器就是个 可迭代对象<iterable>
#
#
# chushi2 = (x*2 for x in range(5))
# for i in chushi2:
#     print(i)


# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
#
#     # return None #默认有这句话
#
# # g = foo()
# #
# # next(g)
# # next(g)
# for i in foo():
#     print(i)


# for i in 可迭代对象:
# 什么是可迭代对象
# 内部有 __iter__方法的 都是 可迭代对象


#【知识点】
# t = ('123',8)
# a,b,c=t
# print(a)
# print(b)

# def fib(max):
#     n,before,after = 0,0,1
#     while n < max:
#         yield before
#         before, after = after, before + after
#         n = n + 1

def bar():
    print('ok')
    count = yield 1
    print(count)
    yield 2

b = bar()
b.send(None)
# s = b.send(None)  # = next(b) 第一次send前如没有next，只能传send（None）
ret = b.send('eeee')
print(ret)

