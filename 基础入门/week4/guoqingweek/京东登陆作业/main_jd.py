#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/3 20:12

login_status = False

def logger(auth_type): #带参数的装饰器，要在原装饰器wraplogin上面再加一层
    filename = str(auth_type)
    def login(f):  #装饰器：实现验证是否登陆，没有登陆就登陆
        def inner():
            global  login_status, username
            nonlocal filename
            if login_status == False:
                if auth_type == 'jingdong':
                    username = input('请输入京东账号:')
                elif auth_type == 'weixin':
                    username = input('请输入微信账号:')
                else:
                    print("内部错误")
                password = input('请输入账号密码:')
                with open(filename, 'r', encoding='utf-8') as filedict:
                    dict_f = eval(filedict.read())
                    if username in dict_f and dict_f[username] == password:
                        f()
                        login_status = True
                    else:
                        print('请输入正确的用户名和密码')
            else:
                f()
        return inner
    return login

@logger(auth_type='jingdong')
def home():
    print('欢迎进入主页面！')

@logger(auth_type='weixin')
def finance():
    print('欢迎进入金融页面！')

@logger(auth_type='jingdong')
def books():
    print('欢迎进入书籍页面！')


def main():
    print('1、主页\n2、金融\n3、书籍\n[退出:q]')
    pages = input('请选择您要进入的页面>>>:')
    while True:
        if pages == '1':
            home()
            pages = input('请选择您要进入的页面>>>:')
        elif pages == '2':
            finance()
            pages = input('请选择您要进入的页面>>>:')
        elif pages == '3':
            books()
            pages = input('请选择您要进入的页面>>>:')
        elif pages == 'q':
            exit()
        else:
            pages = input('无此页面\n请重新选择您要进入的页面>>>:')
main()