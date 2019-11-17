#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/11
'''
计算器程序
【需求】
    1、实现加减乘除及拓号优先级解析
    2、用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
    等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必
    须与真实的计算器所得出的结果一致
    3、支持浮点
【核心内容】
    1、检测（字母，括号数相等）合法性
    2、格式化处理：空格 换成 None''
    3、处理 3 + 3 +3 这种情况
    4、乘法&除法
    5、加法&减法
    6、判断优先级 # 匹配最里层的括号:re.search('\([^()]+\)',s)
    7、主程序
【功能函数】
    1、判断合法性
    2、判断开头负数，返回没有负数的str
    3、 计算括号内的内容:a + b - c * d / e 或 - a - b *d / e
    4、优先级问题：从左往右计算，需要先算乘除，后算加减
    5、乘除的结果是负数，会出现+-,--,*-,/-
    6、整数经过计算可能出现浮点，7/4 = 1.75 -->需要注意浮点数如何处理的问题
    7、.前后的数字应该形成一个数
'''
import re

#1 判断性
#1.1 优先级前：判断合法性（返回没有空格的）
def format(str):
    '''
    格式化：把一些不规范的输入形式调整成合法格式
    :param str:被计算的公式，由合法字符：（0-9）、+、-、*、/ 组成
    :return: 公式中的空格被清除，返回计算过程
             判断非法字符并跳出程序
    '''
    str = str.replace('+-', '+')
    str = str.replace('-+', '-')
    str = str.replace('++', '+')
    str = str.replace('--', '+')
    str = str.replace('*+', '*')
    str = str.replace('/+', '/')
    str = str.replace(' ', '')
    return str

def minu_plus(str_in):
    '''
    str_in = -1+3/2+3*9/4-3*-3  括号内的
    :param str:
    :return:
    '''
    regular = '[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*'




#1.2 优先级后：判断开头是否有负号（返回可计算的内容）
def minus_sign(str_inside):
    '''
    判断开头是否有负号（返回可计算的内容）
    :param str_inside:
    :return:
    '''
    minus = re.match('-',str_inside)
    if minus:
        return str_inside[1:]
    else:
        return str_inside

def plus_minu(str_simple):
    '''
    1-2+3 or -1+2-3-1+2-3-1+2-3-1+2-3 or
    :param str_simple:
    :return:
    '''






#1.3 优先级后：判断（+-）、（--）、（*-）、（/-）并处理
def remove_daul_oper(str_inside):
    '''
    对双运算符进行处理
    :param str_inside:
    :return:
    '''
    str_isdouble = re.search(['+-','--','*-','/-'],str_inside)
    if str_isdouble:
        str_inside.replace('+-', '-')
        str_inside.replace('--', '+')
        if str_isdouble.group() == '*-':
            str_inside.replace('*-','-')

            pass# 计算完了之后再加个负号
        elif str_isdouble.group() == '/-':
            str_inside.replace('/-','-')

            pass #计算完了之后再加个负号
    else:
        return str_inside


#2 计算
#2.1 算乘除
def muti_divi(formula):
    '''
    formula里面只有乘除号的情况，1*2 1/2 1*2/3 1/3*2 ...
    正则分出数字和符号
    :param formula:
    :return:
    '''



def calc_inside(str_inside):
    '''
    计算括号内的内容：
    1、消除str_inside里面的双符号
    2、消除str_inside前面的负号
    3、循环
    4、先乘除再加减
    :return:
    '''
    format(str)



def calculator(str):
    '''
    计算的主程序
        1、检测合法性
        2、计算
            2.1、找出最内层括号的内容：str_inside
            2.2、计算 calc_inside()
            2.3、循环
    :param str:
    :return:
    '''

























