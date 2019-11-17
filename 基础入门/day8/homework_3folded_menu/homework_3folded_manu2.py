menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

back_tag = False
exit_tag = False


# while not (exit_tag or back_tag):
#     for key_1 in menu:
#         print(key_1)
#     choice_1 = input('1>>>:').strip()
#     # if choice_1 == 'b':
#     #     back_tag = True
#     if choice_1 == 'q':
#         exit_tag = True
#     if choice_1 in menu:
#         while not (exit_tag or back_tag):
#             for key_2 in menu[choice_1]:
#                 print(key_2)
#             choice_2 = input('2>>>:').strip()
#             if choice_2 == 'b':
#                 back_tag = True
#             if choice_2 == 'q':
#                 exit_tag = True
#             if choice_2 in menu[choice_1]:
#                 while not (exit_tag or back_tag):
#                     for key_3 in menu[choice_1][choice_2]:
#                         print(key_3)
#                     choice_3 = input('3>>>:').strip()
#                     if choice_3 == 'b':
#                         back_tag = True
#                     if choice_3 == 'q':
#                         exit_tag = True
#                     if choice_3 in menu[choice_1][choice_2]:
#                         while not exit_tag and not back_tag:
#                             for key_4 in menu[choice_1][choice_2][choice_3]:
#                                 print(key_4)
#                             choice_4 = input('4>>>:')
#                             if choice_4 == 'b':
#                                 back_tag = True
#                             if choice_4 == 'q':
#                                 exit_tag = True
#                         else:
#                             back_tag = False
#                 else:
#                     back_tag = False
#         else:
#             back_tag = False

current_layer = menu
parent_layer = []

while True:# 生成一个循环loop
    for key in current_layer:# 遍历字典的键值，也就是第一层字典key
        print(key)# 显示出来
    choice = input('>>>:').strip()#输入显示出来的第一层，或者 b 返回
    if len(choice) == 0:continue #基本判断，确保没有输入东西的时候重复
    if choice in current_layer:
        parent_layer.append(current_layer) #当前层级的字典，直接添加到 列表里面备用
        current_layer = current_layer[choice] # 循环赋值给current_layer，用于进入下一个层级
    elif choice == 'b':
        if parent_layer:# [] 空列表 就是 False
            current_layer = parent_layer.pop() # 取出列表的最后一个值
    else:
        print('Null.')



