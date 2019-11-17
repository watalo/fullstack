#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# date: 2019/9/21

'''
CONTENT
文件操作
    只读
        r模式
        rb模式
    路径
        相对路径
        绝对路径
    读操作
        read()
        readline()
        readlines()
    写模式
        覆盖
        追加
    读写模式
        r+ 模式
        r+ 模式的坑
    写读模式
        w+
        追加读（a+,a+b)
    其他操作
        seek（）
        tell()
        truncate()
        修改文件
'''

# f = open('scrips','r',encoding='utf-8')
# # content1 = f.readline().strip()
# # content2 = f.readline().strip()
# # content3 = f.readline().strip()
# # content4 = f.readline().strip()
# # f.close()
# print(content1)
# print(content2)
# print(content3)
# print(content4)


# for line in f:
#     print(line.strip())
# f.close()

# f1 = open('scrips2','w',encoding='utf-8')
#
# f1.write('邹步雅是个疯婆子')
# f1.flush()
# f1.close

# f2 = open('scrips2','a+r',encoding='utf-8')
# msg = f2.write("5555")
# print(msg)
# f2.close()

# f2 = open('scrips2',mode='r+',encoding='utf-8')
# msg = f2.read()
# f2.write('shs')
# f2.flush()
# f2.close()
# print(msg)

# f2 = open('scrips2',mode='a',encoding='utf-8')
# f2.truncate(5)
# f2.write('hello world')
# f2.close()
#
# f2 = open('scrips2',mode='r+',encoding='utf-8')
# print(f2.readline()) #从头读
# f2.write('yuefei') # r+ 模式下，write 就是在最后写
# f2.close()

# f4 = open('scrips',mode='w+',encoding='utf-8')
# # print(f4.readline())
# # f4.write('yuefei') # w+ 模式下，先清空，再写
# # print(f4.tell())
# # f4.seek(0)
# # print(f4.readline())
# # f4.close()

# f4 = open('scrips',mode='a+',encoding='utf-8')
# print(f4.readline()) # 光标直接在最后
# f4.write('yuefei') # a+ 模式下，write 就是在最后写
# print(f4.tell())
# f4.seek(0)
# print(f4.readline())
# f4.close()

# f = open('scrips2', mode='r', encoding='utf-8')
# f_n = open('scrips3',mode='w',encoding='utf-8')
# num = 0
# for line in f:
#     num += 1
#     if num == 3:
#         f_n.write("alex\n")
#     f_n.write(line)
# f.close()
# f_n.close()

 


