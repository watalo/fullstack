#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/13 0:03
# @Site    : 
# @File    : 02.selenium_basic_point.py
# @Software: PyCharm
from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com')

#标签定位
search_input = bro.find_elements_by_id('q')
#标签交互
search_input.send_keys('iphone')

#点击搜索按钮
btn = bro.find_elements_by_css_selector('.btn-search')
btn.click()

sleep(5)

bro.quit()