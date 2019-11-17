#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/8

'''
计算器程序
1\实现加减乘除及拓号优先级解析
2\用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必
须与真实的计算器所得出的结果一致
3\支持浮点

# 匹配成最里层的括号
    re.search('\([^()]+\)',s)
    1、检测（字母，括号数相等）合法性
    2、格式化处理：空格 换成 None''
    3、处理 3 + 3 +3 这种情况
    4、乘法&除法
    5、加法&减法
    6、判断优先级
    7、主程序
'''
import re

def format(original_str): #对原始公式进行标准化，判断合法性
    str = re.sub('\s','',original_str) # 去除字段的空格
    a = re.search('[^(0-9),\+,\-,\*,\/]',str) # 匹配数字和+ - * / 号 输入的数字如果有其他字符就无法计算
    if a:
        return s_noblack
    else:
        return None #如果有其他的字符，返回个空值，后面啥也算不出来


def calc(s): #算最里面一个括号内的运算公式
    # if  re.search('^-', s) == None: #如果是正数开头的情况 #如果是负数开头要进行判断，比如-4*3，这句话可能有问题但是不晓得什么问题
    #     tag = True #用在后面分情况的时候做标记
    #     s_z = s
    # else:   #如果是负数开头的情况
    #     tag = False
    #     s_z = re.sub('^-', '', s) #去掉'-'，字符串格式
    #
    #
    # be = re.search('^\d*', s_z).group() # 运算符前的纯数字部分
    # af = re.search('\d*$', s_z).group() # 运算符后的纯数字部分
    # op = re.search('\D', s_z).group() # 运算符
    #
    #
    # if op == '*': #乘法情况
    #     if tag == True:
    #         return int(be) * int(af)
    #     else:
    #         return - int(be) * int(af)
    # elif op == '/':#除法情况
    #     if tag == True:
    #         return int(be) / int(af)
    #     else:
    #         return -int(be) / int(af)
    # elif op == '+':#加法情况
    #     if tag == True:
    #         return int(be) + int(af)
    #     else:
    #         return -int(be) + int(af)
    # elif op == '-':#减法情况
    #     if tag == True:
    #         return int(be) - int(af)
    #     else:
    #         return -int(be) - int(af)
    # else:
    #     return 'WRONG！'


def priority(a):  #判断括号的优先级，先算最里面的，那就要先找到最里面的
    n = re.search('\([^()]+\)', a) #最经典的语句，从头开始匹配最里面的括号
    if n == None:
        return a   #返回最里面的括号
    else:
        return n


def main(a):
    # if formatdate(a) == None: #先格式化，去空格，判断数据合法性
    #     print('请输入由数字（0-9）和运算符（+ - * /）组成的公式吧！')
    # else:
    tag = True
    ret = None
    while tag:  #就是这个循环有问题！
        n = re.search('\([^()]+\)', a)
        if n:
            pri = priority(ab)  #取最里面的括号和内容
            prio = re.sub('[\(,\)]','',pri) #去掉括号
            ca = eval(prio) #计算
            a = a.replace(pri,str(ca)) # 想法：（(60-30 +(-40/5) * (30*2)）-->(60-30-8*(30*2))-->(60-30-8*60)
        else:                            # 算一个括号 就用结果替换原括号 循环到最后就只剩一个括号，最后算出结果
            ret = calc(ab)
        else:
            break
return ret




