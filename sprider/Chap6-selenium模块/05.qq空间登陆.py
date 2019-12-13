#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/13 20:17
# @Site    : 
# @File    : 05.qq空间登陆.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

user_name_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
user_name_tag.send_keys('35771274')
sleep(1)
password_tag.send_keys('777')
sleep(1)

btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)

bro.quit()