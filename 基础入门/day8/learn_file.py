#
# # 打开一个文件
# f = open('scrips','r',encoding='utf-8')# 文件句柄
#
# # 读取（'r'）
# data = f.read(5) #参数是5个字符
# print(data) #操作
# f.close() #关闭
#
# # 写文件('w')
#
# f2 = open('scrips2','w',encoding='utf-8') #创建一个文件w模式
#
# f2.write('hello world') #
#
# f2.close()
#
# #添加 （'a'）
# f3 = open('scrips','a',encoding='utf-8')
# f3.write('\n hhhhhhhhhhhhhhhhhh\n')
#
# f3.close()

f4 = open('scrips','r',encoding='utf8')

a = f4.readlines(123456789)
a.append('ilikeit')
for i in a:
    print(i.strip())
f4.close()


a.