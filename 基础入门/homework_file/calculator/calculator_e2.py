#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/16

import re

def check_str(str):
    str = str.replace(' ', '')
    if re.findall('[^0-9\+\-\*\/\(\)\.]',str):
        return False
    else:
        return True


def format(str):
    str = str.replace('+-','-')
    str = str.replace('--','+')
    str = str.replace('-+','-')
    str = str.replace('++','+')
    str = str.replace('*+','*')
    str = str.replace('/+','/')
    str = str.replace(' ','')
    return str

def find_inside(str):
    str_inside = re.search('\([^()]+\)', str)
    formula = re.search('[^()]+',str_inside.group())
    return formula


def mul_div(formula):
    '''
        优先级：算括号里面的公式的乘除法，返回只剩加减法的公式
        :param formula:最里层括号的计算公式
        :return: 只剩加减法的公式
        '''
    while re.findall('[*/]', formula):
        regular = '\d+\.?\d*[*/][\-]?\d+\.?\d*'
        formula_single = re.search(regular, formula)
        if re.findall('\*', formula_single.group()):
            formula_list = formula_single.group().split('*')
            res = float(formula_list[0]) * float(formula_list[1])
            formula = formula.replace(formula_single.group(),str(res))
            formula = format(formula)
        elif re.findall('/', formula_single.group()):
            formula_list = formula_single.group().split('/')
            res = float(formula_list[0]) / float(formula_list[1])
            formula = formula.replace(formula_single.group(),str(res))
            formula = format(formula)
        elif re.findall('[]',):
            return formula
    else:
        return formula

def plu_min(formula):
    '''
    计算加减法
    :param formula: 只剩加减法的公式
    :return:
    '''
    while re.search('[+-]', formula[1:]) is not None:
        regular = '[\-]?\d+\.?\d*[+-][\-]?\d+\.?\d*'
        formula_single = re.search(regular, formula)
        res = 0
        if formula_single.group().split('-')[0] == '':
            formula_single_x = formula_single.group()[1:]
            if re.findall('\+', formula_single_x):
                formula_list = formula_single_x.split('+')
                res = float(formula_list[1]) - float(formula_list[0])
            elif re.findall('-', formula_single_x):
                formula_list = formula_single_x.split('-')
                res = -(float(formula_list[0]) + float(formula_list[1]))
            formula = formula.replace(formula_single.group(), str(res))
            formula = format(formula)
        else:
            if re.findall('\+', formula_single.group()):
                formula_list = formula_single.group().split('+')
                res = float(formula_list[0]) + float(formula_list[1])
            elif re.findall('-', formula_single.group()):
                formula_list = formula_single.group().split('-')
                res = float(formula_list[0]) + float(formula_list[1])
            formula = formula.replace(formula_single.group(), str(res))
            formula = format(formula)
    else:
        return formula



def calculator(str):
    '''
    1.合法性
    2.标准化
    3.优先级：1>括号里面先算，2>先乘除再加减。
    4.循环处理优先级：算括号里面的公式的乘除法，返回只剩加减法的公式
    :param formula:整个公式
    :return：最后结果
    '''
    str = format(str)
    if check_str(str):
        while re.findall('\(\)',str):
            str = format(str)
            str_in = find_inside(str)
            str_in = mul_div(str_in)
            str_in = plu_min(str_in)
            str = str_in
        else:
            str = format(str)
            str = mul_div(str)
            str = plu_min(str)
            res = str
        return res
    else:
        print('CANNOT BE CALCULATED!')

a = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

calculator(a)

