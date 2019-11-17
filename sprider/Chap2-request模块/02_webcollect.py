#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/16


#UA伪装


import requests

if __name__ == "__main__":
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }#抓包工具抓的身份标识
    url = 'https://www.sogou.com/web'
    kw = input('enter a word:')
    param ={
        'query':kw
    }
    #对指定的uRL发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    file_name = kw+'.html'
    with open(file_name,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_name,"保存成功！！")

