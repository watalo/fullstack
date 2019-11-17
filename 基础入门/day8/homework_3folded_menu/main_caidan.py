#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# date: 2019/9/23

'''
1.用文件操作的方式实现三级菜单，用户可增、删、改、查（1级1级的做）
2.需要用的函数：
    str(),字典转字符串
    eval()，字符串直接调用引号里的内容，内容是字典话，那就。。。
OK，let's go!
【idea&question:】
    1、直接在文件里写好省、市、区名字？
    开头就出现问题，省市区分文件写，还是写在一个文件，分文件写又应该怎么写，难道每个市都要单独命名一个文件？这TM是个问题啊
    1.1、为了自动搞出这些名字来，我决定加一个作业，就是用for循环来写，市的名字简化成 省名_1,区名字简化为，省名_1_1这样。
    写一个menu（）函数来实现。for循环已经循环晕了。
    2、将文件内容变成字典类型，逐渐添加形成一个大字典
    3、用之前学的字典三级菜单（高大上版）循环。>>>>>>>>>>实现了三级菜单的‘查’功能
    4、考虑怎么做增、删、改，基本想法是在while循环的过程中添加功能。
        可以预期的问题，改完后，只是对字典进行了修改，【字典】中的内容怎么返还回去改【文件】。
'''

# 1、自动生成文件
def menu(a): # 用a文件里单行内容为名字，生成新文件，并且给新文件添加内容为
    b = str(a)
    with open(b, 'r', encoding='utf-8') as m:
        for prov in m:
            with open(prov.strip(), 'w', encoding='utf-8') as p:  # 创建以省命名的文件
                for i in range(1, 3):
                    city = str(prov.strip()) + '' + str(i) + '\n'  # 格式化城市名称
                    p.writelines(city)  # 写入格式化城市名称

menu('prov')  # 生成市级文件
with open('prov', 'r', encoding='utf-8') as m:  # 生成区级文件
    for key in m:
        menu(key.strip())


# 2、通过文件生成一个字典
def file_to_dict(a=str(),b={}):
    menu_dict = dict()
    with open(a, 'r', encoding='utf-8') as m:
        for key in m:
            menu_dict.setdefault(key.strip(), {})
    return menu_dict

dict_menu = file_to_dict('prov')
for key in dict_menu:
    dict_menu[key] = file_to_dict(key)
    m = dict_menu[key]
    for key2 in m:
        m[key2] = file_to_dict(key2)

# 3、3级菜单循环
def foldedmenu(dict_menu_c):
    # dict_menu_c = dict_menu #有预感这句话 换个名字对后面‘增删改’功能会有很大的作用
    parent_layer = []
    while True:  # 生成一个循环loop
        for key in dict_menu_c:  # 遍历字典的键值，也就是第一层字典key
            print(key)  # 显示出来
        choice = input('>>>:').strip()  # 输入显示出来的第一层，或者 b 返回
        if len(choice) == 0: continue  # 基本判断，确保没有输入东西的时候重复
        if choice in dict_menu_c:
            parent_layer.append(dict_menu_c)  # 当前层级的字典，直接添加到 列表里面备用
            dict_menu_c = dict_menu_c[choice]  # 循环赋值给dict_menu_c，用于进入下一个层级
        elif choice == 'b':
            if parent_layer:  # [] 空列表 就是 False
                dict_menu_c = parent_layer.pop()  # 取出列表的最后一个值
        elif choice == 'q':
            print('--------END---------')
            break
        # elif choice == 'x':
        #     delete_choice = input('>>>:').strip()
        #     with open('delete_choice','r',encoding='utf-8') as beitai:
        #         m = beitai
        #         del m[delete_choice]
        #     with open('delete_choice','w',encoding='utf-8') as baitai2:
        #         beitai2.writelines(m)

        else:
            print('请正确输入指令')

foldedmenu(dict_menu)

