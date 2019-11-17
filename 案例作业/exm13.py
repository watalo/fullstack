#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/7 12:58
'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1
的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
'''

for i in range(100,1000):
    a = int(list(str(i))[0])
    b = int(list(str(i))[1])
    c = int(list(str(i))[2])
    if a**3 + b**3 + c**3 == i:
        print(i)