#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/9
import re

# a = '-8+878'
#
# if  re.search('^-', a) == None:
#     tag = True
#     s_z = a
#     print(a)
# ab = '(-4*3)/ (16-3*2)'
# pri = '(-4*3)'  #取最里面的括号和内容
# prio = re.sub('[\(,\)]','',pri) #去掉括号
# ca = eval(prio) #计算
#
# ab = ab.replace(pri,str(ca)) # 想法：（(60-30 +(-40/5) * (30*2)）-->(60-30-8*(30*2))-->(60-30-8*60)
# print(ab)

def priority(a):  #判断括号的优先级，先算最里面的，那就要先找到最里面的
    n = re.search('\([^()]+\)', a) #最经典的语句，从头开始匹配最里面的括号
    if n == None:
        return a   #返回最里面的括号
    else:
        return n

priority('-1.2')