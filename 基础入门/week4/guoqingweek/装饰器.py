'''
装饰器（函数）decrator
需要掌握的知识点如下：
1、作用域 L E G B


2、高阶函数
    1 函数名可以作为参数输入
    2 函数名还可以作为返回值

3、闭包 = 内部函数块 + 定义函数时的环境

'''
# def outer():
#     x=10
#     def inner():
#         print(x)
#     return inner
#
# outer()()
#
# f = outer()
# f()

import time

def logger(flag = False):
    def showtime(f):#这个是装饰器函数
        def inner(*x,**y):                            #装饰器
            start = time.time()                 #装饰器
            f(*x,**y)                                 #装饰器
            end = time.time()                   #装饰器
            print('spend %s' % (end - start))   #装饰器
            if flag == True:
                print('rizhijilu')
        return inner                            #装饰器
    return showtime


@logger(True)  #foo = showtime(foo)
def foo(*x,**y): #这是功能函数
    sums = 0
    for i in x:
        sums += i
    print(sums)
    time.sleep(1)


# def bar():
#     print('bar......')
#     time.sleep(3)
#
foo(1,2,3,)




