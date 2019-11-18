#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/11/18 22:13
# @Site    : 
# @File    : paqutupian.py
# @Software: PyCharm

import requests

if __name__ == '__main__':
    # 如何爬取图片
    url = ''
    #content 返回 二进制的图片数据
    #text    返回 字符串
    #json（） 返回 对象
    requests.get(url=url).content #返回的是二进制形式的图片数据