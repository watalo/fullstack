#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2019/12/22 23:05
# @Site    : 
# @File    : 练习题1.py
# @Software: PyCharm

'''
    练习题：
'''
class Pagenation:
    """
    处理分页显示的操作
    """
    def __init__(self,data_list,page,per_page_num = 10):
        """
        初始化
        :param:page:


        """
        self.data_list = data_list
        self.page = page
        self.per_page_num = per_page_num

    @property
    def start(self):
        return self.per_page_num * (self.page-1)

    @property
    def end(self):
        return self.per_page_num * self.page

    def show(self):
        ret = self.data_list[self.start,self.end]
        for item in ret:
            print(item)




if __name__ == '__main__':
    data_list = []
    for i in range(1, 300):
        data_list.append('alex-%s' % i)

    obj = Pagenation()
