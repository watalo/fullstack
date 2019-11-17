#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/16

import requests
import json


if __name__ == "__main__":
    # 1 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2 UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.29 Safari/537.36 Edg/79.0.309.18'
    }
    # 3 post请求数据的参数设置
    word = input('enter:')
    data= {
        'kw':word
    }

    # 4 请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    # 5 获取响应数据
    dic_obj = response.json()
    # 6 持久化存储
    file_name = word+'.json'
    fp = open(file_name,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over')


