#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/6


'''
正则表达式
'''


import re

#匹配的方法

# re.match()    #从头开始匹配
# re.search()   #匹配包含
# re.findall()  #把所有匹配到的字符放到以列表中的元素返回
# re.split()    #以匹配到的字符当做列表分隔符
# re.sub()      #匹配字符并替换

re.search("\Aabc\Z","abcabc")

id_number = "420505198509037011"

a = re.search("(?P<pro>[0-9]{4})(?P<city>[0-9]{2})(2)",id_number)
