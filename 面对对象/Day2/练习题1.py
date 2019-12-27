#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
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

    def __init__(self, data_list, page, per_page_num=10):
        """
        内置参数
        @param data_list:数据来源
        @param page:显示第几个页码
        @param per_page_num:每页显示的数量
        """
        self.data_list = data_list
        self.page = page
        self.per_page_num = per_page_num

    @property
    def start(self):
        """
        起始数据
        @return:
        """
        return self.per_page_num * (self.page - 1)

    @property
    def end(self):
        """
        结束数据
        @return:
        """
        return self.per_page_num * self.page

    def show(self):
        """
        执行文件
        @return:
        """
        ret = self.data_list[self.start:self.end]
        for item in ret:
            print(item)

    def show_param(self):
        """
        显示内置参数数据
        @param page:
        @param per_page_num:
        @return:
        """
        return (self.page,self.per_page_num)


if __name__ == '__main__':
    data_list = []
    for i in range(1, 300):
        data_list.append('alex-%s' % i)

    while True:
        # 1. 要查看的页面
        page = int(input('请输入要查看的页码:'))
        obj = Pagenation(data_list, page)
        obj.show()
        print(obj.show_param())
        break