#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/1 21:49
# @Site    : 
# @File    : xpathadd.py
# @Software: PyCharm

import requests
from lxml import etree
import os

'''
    xpath运算中 可以使用 |  提供不同路径的解析，增加通用性     
'''

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    response = requests.get(url=url,headers=headers)
    # response.encoding= 'utf-8'
    page_text = response.text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a         热门城市
    # //div[@class="bottom"]/ul/div[2]/li/a  全部城市
    all_city_name = []
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_name.append(city_name)
    print(all_city_name,len(all_city_name))
