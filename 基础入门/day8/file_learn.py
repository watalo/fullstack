f = open('scrips','r',encoding='utf8')
#
# for i in f: # for将f做成了一个迭代器，用一行取一行
#     print(i.strip())
#
# num = 0
# for i in f:
#     num += 1
#     if num == 6:
#         i = ''.join([i.strip(),'llllllllllll'])
#     print(i.strip())

# #上面这段有问题
# s = f.readlines(2)
# print(f.readline())
# print(s)

#光标操作问题
# print(f.tell()) # 光标默认的初始位置是0
# print(f.read(4) # python3.0 的中文占3个字符
# print(f.tell())

# f.seek(0) 调光标的方法##
f.seek(0)
print(f.read(4))