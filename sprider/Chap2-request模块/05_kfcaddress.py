#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/11/17 18:29
# @Site    : 
# @File    : 05_kfcaddress.py
# @Software: PyCharm

import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.29 Safari/537.36 Edg/79.0.309.18'
    }
    kw = '北京'
    file_name = kw + '.json'
    fp = open(file_name, 'w', encoding='utf-8')
    for page in range(10):
        data = {
            'cname':'',
            'pid':'',
            'keyword': kw,
            'pageIndex': page,
            'pageSize': '10',
        }
        respone = requests.post(url=url,data=data,headers=headers)
        obj = respone.json()
        json.dump(obj=obj,fp=fp,ensure_ascii=False)

    print('over')



