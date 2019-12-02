#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/1 22:36
# @Site    : 
# @File    : xpath_homework.py
# @Software: PyCharm

import requests
from lxml import etree
import os

if __name__ == '__main__':
    #创建一个文件夹
    if not os.path.exists('./jianliLibs'):
        os.mkdir('./jianliLibs')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30'
    }
    url = 'http://sc.chinaz.com/jianli/free.html'
    # 第1页 和 后面页面都不一样
    # 第2页开始，以./free_%d 的形式出现
    # http://sc.chinaz.com/jianli/free_2.html
    response = requests.get(url=url, headers=headers)
    response.encoding= 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    #层级：div[@class="sc_warp  mt20"]//a/href
    list_jianli_url = tree.xpath('//div[@class="sc_warp  mt20"]//p/a/@href')
    # list_jianli_name = tree.xpath('//div[@class="sc_warp  mt20"]//p/a/text()')
    # print(list_jianli_url)

    for jianli_url in list_jianli_url:
        jianli_response = requests.get(url=jianli_url,headers=headers)
        jianli_response.encoding = 'utf-8'
        jianli_page_text = jianli_response.text
        n_tree = etree.HTML(jianli_page_text)

        jianli_name = n_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]+'.rar'
        print(jianli_name)

        download_url = n_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]
        print(download_url)


        jianli_path = 'jianliLibs/'+jianli_name
        print(jianli_path)
        jianli_data = requests.get(url=download_url, headers=headers)

        with open(jianli_path,'wb') as fp:
            fp.write(jianli_data.content)
        print(jianli_name,'下载完成')