#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/1 21:26
# @Site    : 
# @File    : xpathtrypic.py
# @Software: PyCharm

import requests
from lxml import etree
import os

'''
    出现乱码怎么处理，第23、37 行
'''

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30'
    }
    url = 'http://pic.netbian.com/4kyouxi/'
    response = requests.get(url=url,headers=headers)
    # response.encoding= 'utf-8'
    page_text = response.text

    #解析：src的属性值 alt的属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_src = 'http://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')#通用处理中文乱码的解决方法
        # print(img_name,img_src)
        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src,headers=headers)
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data.content)
            print(img_name,'done')
