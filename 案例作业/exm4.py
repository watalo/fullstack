#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/6 21:54
'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
#
y = int(input('year:'))
m = int(input('month:'))
d = int(input('day:'))

list_d = [0,31,28,31,30,31,30,31,31,30,31,30]
sum = 0
leap = False

for i in range(m):
    sum += list_d[i]

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    leap = True
    if leap == True and m > 2:
        sum += d+1
else:
    sum += d

print(sum)


