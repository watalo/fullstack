#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/16
import requests

if __name__ == "__main__":
    #01:指定url
    url = 'https://www.sogo.com/'
    #02：发起请求
    # - get 方法会返回一个响应对象
    respone = requests.get(url=url)
    #03:获取数据
    page_text = respone.text
    print(page_text)
    #04:持久化存储
    with open('./sogo.html','w',encoding='utf-8') as fp:
        fp.write(page_text)

    print('---end--')