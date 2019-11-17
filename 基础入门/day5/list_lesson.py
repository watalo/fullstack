# __author__:"watalo"
# date: 2019/9/6

# # 列表
name0 = "watalo1"
name1 = "watalo2"
name2 = "watalo3"
name3 = "watalo4"
name4 = "watalo5"

a = ["wuchao", "jinxin", "xiaohu", "sanpang", "ligang"]
# 增、删、改、查
print(a[1])# jinxin
print(a[1:])# ['jinxin', 'xiaohu', 'sanpang', 'ligang']
print(a[1:2])# ['jinxin']
print(a[1:3])# ['jinxin', 'xiaohu']
print(a[1:4])# ['jinxin', 'xiaohu', 'sanpang']
print(a[1:5])# ['jinxin', 'xiaohu', 'sanpang', 'ligang']
print(a[1:6])# ['jinxin', 'xiaohu', 'sanpang', 'ligang']
print(a[1:-1])# ['jinxin', 'xiaohu', 'sanpang']
print(a[1:-1:1])#['jinxin', 'xiaohu', 'sanpang']
print(a[1:-1:2])# ['jinxin', 'sanpang']
print(a[1::2])# ['jinxin', 'sanpang']
print(a[1:-1:-1])#['jinxin', 'xiaohu', 'sanpang']
print(a[1:-1:-2])# ['jinxin', 'sanpang']
print(a[1::-2])# ['jinxin', 'sanpang']

# 增 appeng insert
a.append("wangba")
print(a)
a.insert(1,"zhuzhu")
print(a)

# 改
a[1] = "diss"
print(a)
a[1:] = ["bulls","pops"]
print(a)

# 删 remove pop del
a.remove(a[1])
print(a)
b = a.pop(1)
print(a)
print(b)

del a[0]
print(a)

# del a
# print(a)

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
print(b)

#index 根据内容找位置
a = ["wuchao","jinxin","xiaohu","sanpang","ligang"]

first_lg_index = a.index("ligang")
little_list = a[first_lg_index + 1:]
second_lg_index = little_list.index("ligang")
second_lg_index_in_a = first_lg_index + second_lg_index + 1
print(a[second_lg_index_in_a])

#reverse 反序
a.reverse() #直接操作，无返回值
print(a)

#sort 拍序

x = [1,7,3,2,6]
x.sort(reverse=True)

print(x)

