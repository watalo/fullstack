'''
#文件操作省、市、区名称形成菜单
 文件名：
    prov_name
    city_name
    dict_name
    已有字典三级菜单的脚本，就是用 脚本--->字典-->文件 来实现将增删改查功能，并存储结果

'''
# with open('vari_file','w',encoding='utf-8') as w:
#     w.write()


def file_to_dict(a=str()):
    with open(a,'r',encoding='utf-8') as f:
        f_dict = eval(f.read())
        if type(f_dict) == {}:
            return f_dict
        else:
            print('无法识别')


def dict_to_file(a,b = False):
    if b == True:
        with open('vari_file','w',encoding='utf-8') as f:
            f.write(str(a))
    else:
        for k,v in a:
            with open(str(k).strip(),'w',encoding='utf-8') as m:
                # for i in m.keys():
                #     m.write(str(i))

m={
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

dict_to_file(m,True)


# f = open('vari_file','r',encoding='utf-8')
# ff = eval(f.read())
# f.close()

# file_to_dict('vari_file')


# def format_file(vari_file):
#     ff_dict = file_to_dict(vari_file)
#     for key in ff_dict:
#         with open('vari_file', 'w', encoding='utf-8') as f:
# #
# #
# format_file('vari_file')
#