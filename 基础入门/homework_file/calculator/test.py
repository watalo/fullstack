#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# date: 2019/10/16
import re

# str = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#
# str_ch = str.replace(' ','')
#
# str_inside = re.search('\([^()]+\)', str_ch)
# str_insided = re.search('[^()]+',str_inside.group())
#
# print(str_insided.group())

formu = '-100000-89/234+23*123/234-39'


def format(str):
    str = str.replace('+-', '-')
    str = str.replace('--', '+')
    str = str.replace('-+', '-')
    str = str.replace('++', '+')
    str = str.replace('*+', '*')
    str = str.replace('/+', '/')
    return str


def mul_div(formula):
    while re.findall('[*/]', formula):
        regular = '\d+\.?\d*[*/][\-]?\d+\.?\d*'
        formula_single = re.search(regular, formula)
        if re.findall('\*', formula_single.group()):
            formula_list = formula_single.group().split('*')
            res = float(formula_list[0]) * float(formula_list[1])
            formula = formula.replace(formula_single.group(), str(res))
            formula = format(formula)
        elif re.findall('/', formula_single.group()):
            formula_list = formula_single.group().split('/')
            res = float(formula_list[0]) / float(formula_list[1])
            formula = formula.replace(formula_single.group(), str(res))
            formula = format(formula)
    else:
        return formula


set = mul_div(formu)


def plu_min(formula):
    '''
    计算加减法
    :param formula: 只剩加减法的公式
    :return:
    '''

    while re.search('[+-]',formula[1:]) is not None:
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



print(plu_min(set))

# formula = '-23.42+2'
# if re.search('[+-]',formula[1:]) is not None:
#     print('ok')

'1w- 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
