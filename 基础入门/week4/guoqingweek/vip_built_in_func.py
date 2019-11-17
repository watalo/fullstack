#_author:'watalo'

'''
内置函数
filter
map
reduce
lamda

'''

str = ['a', 'b', 'c', 'd']

def fun1(a):
    if a != 'a':
        return a

res = filter(fun1,str) 
#
# print(res)
#
# def fun2(s):
#     return s+'oops'
#
# res1 = map(fun2,str) ##
#
# print(list(res1))


from functools import reduce

def add1(x,y):
    return x + y

print(reduce(add1,range(1,101)))

res = reduce(lambda x,y:x+y,range(1,101))

print(res)


