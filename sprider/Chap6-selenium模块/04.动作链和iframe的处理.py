#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/13 19:50
# @Site    : 
# @File    : 04.动作链和iframe的处理.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

#动作链
action = ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17,0).perform()
    # sleep(0.1)

action.release()
bro.quit()



