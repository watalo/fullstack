#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/16
import requests

if __name__ == "__main__":
    #01:指定url
    company_name = '宜昌东阳光火力发电有限公司'
    # company_id = '2326337857'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }  # 抓包工具抓的身份标识
    url = 'https://www.tianyancha.com/company/244790386'
    #02：发起请求
    # - get 方法会返回一个响应对象
    respone = requests.get(url=url,headers=headers)
    #03:获取数据
    page_text = respone.text
    print(page_text)
    #04:持久化存储
    with open('./'+company_name+'.html','w',encoding='utf-8') as fp:
        fp.write(page_text)

    print('---end--')