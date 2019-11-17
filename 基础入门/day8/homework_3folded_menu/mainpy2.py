'''
#文件操作省、市、区名称形成菜单
 文件名：
    prov_name
    city_name
    dict_name
    已有字典三级菜单的脚本，就是用 脚本--->字典-->文件 来实现将增删改查功能，并存储结果
    内容部分分为：
    1、文件部分：
    2、字典脚本



'''
menu = {
    '北京':{'海淀':{
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
        },'昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },'朝阳':{},'东城':{}},
    '上海':{'闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },'闸北':{
            '火车战':{
                '携程':{}
            }
        },'浦东':{}},
    '山东':{}
}

# 1-功能函数
# 1.1-文件和字典转换，条件是文件的内容必须是字典
def file_to_dict(a=str()):
    with open(a,'r',encoding='utf-8') as f:
        f_dict = eval(f.read())
        if type(f_dict) == {}:
            return f_dict
        else:
            print('无法识别')

def filefunc(a):
    with open('vari_file','w',encoding='utf-8') as f:
        f.write(str(a))

def dict_to_file(a=dict()):
    parent_layer = a
    for k in parent_layer:
        if type(parent_layer[k]) == dict:
            with open(k,'w',encoding='utf-8') as m:
                for i in parent_layer[k].keys():
                    m.write(i+'\n')

#2-三级菜单的循环
def folded_menu(dict_menu_c):
    dict_menu = dict_menu_c #有预感这句话 换个名字对后面‘增删改’功能会有很大的作用
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
        elif choice == 'x':
            delete_choice = input('删除哪项>>>:').strip()
                del m[delete_choice] #
            # with open('delete_choice','w',encoding='utf-8') as baitai2:
            #     beitai2.writelines(m)
        else:
            print('请正确输入指令')

folded_menu(menu)
