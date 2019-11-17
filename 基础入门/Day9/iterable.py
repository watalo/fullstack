#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# date: 2019/9/22

'''
1.函数名的运用
    1.1内存地址
    1.2可以赋值给其他变量
    1.3可以当作容器类的元素
    1.4可以当作函数的参数
    1.5可以作为函数的返回值
'''


# def fun1():
#     print('邹步雅大傻逼')
#
#
# def fun2():
#     print('邹步雅大傻逼')
#
#
# def fun3():
#     print('邹步雅大傻逼')
#
#
# def fun4():
#     print('邹步雅大傻逼')
#
#
# flist = [fun1, fun2, fun3, fun4]
#
# for i in flist:
#     i()

# def func_1():
#     print("1")
#     def func_2():
#         print("2")
#     print("3")
#     return func_2
# fn = func_1()
# # 执行函数1.  函数1返回的是函数2, 这时fn指向的就是上面函数2
# fn()    # 执行func_2函数

# s = 'zoubuyashigedashabi'
#
# c = s.__iter__()
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())


# def func():
#     print("111")
#     yield 222
#     print("333")
#     yield 444
# gener = func()
# ret = gener.__next__()
# print(ret)
# ret2 = gener.__next__()
# print(ret2)
# ret3 = gener.__next__()

# def eat():
#     for i in range(1,10000):
#         a = yield '包子'+str(i)
#         print('a is',a)
#         b = yield '窝窝头'
#         print('b is', b)
# e = eat()
# print(e.__next__())
# print(e.send('大葱'))
# print(e.send('大蒜'))
#
#
# def func():
#     lst1 = ['卫龙','老冰棍','北冰洋','牛羊配']
#     lst2 = ['馒头','花卷','豆包','大饼']
#     yield from lst1
#     yield from lst2
# g = func()
# for i in g:
#     print(i)

# list = ['python%s' %i for i in range(1,10) if i % 2 == 0]
# print(list)

def func():
    print(111)
    yield 222
g = func()  # 生成器g
g1 = (i for i in g) # 生成器g1. 但是g1的数据来源于g
g2 = (i for i in g1)    # 生成器g2. 来源g1
# list的底层有for循环,for就是一直执行__next__() 所以可以将生成器放到list中
# print(list(g))   # 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
# print(list(g1))  # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1 也就没有数据了
# print(list(g2))  # 和g1同理理
print(next(g))
print(next(g1))
print(next(g2))   # 可以用next来验证  其实list就是将内容迭代了转换成了列表