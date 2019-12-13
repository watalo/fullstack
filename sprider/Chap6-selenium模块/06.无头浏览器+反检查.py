#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/13 20:27
# @Site    : 
# @File    : 06.无头浏览器+反检查.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver import ChromeOptions


#无头浏览器操作
chr_options = Options()
chr_options.add_argument('--headless')
chr_options.add_argument('--disable-gpu')

#实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwithes',['enable-automation'])


bro = webdriver.Chrome(executable_path='./chromedriver.exe', options=chr_options)

#无可视化界面（无头浏览器） phantomJs
bro.get('http://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()
#无可视化界面 = 无头浏览器
