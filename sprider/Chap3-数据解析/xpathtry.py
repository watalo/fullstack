#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/1 21:06
# @Site    : 
# @File    : xpathtry.py
# @Software: PyCharm

import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30'
    }
    url = 'https://yc.58.com/ershoufang'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        #局部解析--一定要在前面加 .
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
