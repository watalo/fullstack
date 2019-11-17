# 创建的关键字 set（）
# 功能:【去重】【关系测试】
# set()的内容必须是可哈希的（不可变），set本身是非可哈希的
# 特性：无序的-----没有索引
# 取set的值：（1）for 循环 （2）迭代器
# 可变集合set()，不可变集合 frozenset()
# 访问集合(遍历)
#   set.add() 括号内的内容直接进入到set里面
#   set.update() 括号内作为序列，然后序列内的每个元素都添加进去
#   set.update() 括号内 要可迭代
#   set.pop() 随机删除，并返回
#   set.clear() 内容全部删除
# set的操作符
# 属于    in / not in
# 等价    == / |=
# 包含    < / > / <= / >=
# 并集    union()             | / and 求并集
# 交集    intersection()      &
# 差集    difference()有方向的
# 反向交集 symmetric_difference() 取交集之外的 ^
# 父集superset   issuperset()
# 子集subset     issubset



a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a.intersection(b)) #{3, 4, 5}
print(a & b)

print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7}
print(a | b)

print(a.difference(b))
print(b.difference(a))
print(a-b)
print(b-a)

print(a.symmetric_difference(b))
print(a ^ b)

print(a and b)
print(b and a)

print(a or b)
print(b or a)




# s = set('alex li')
# print(s)  #{' ', 'i', 'l', 'a', 'e', 'x'}
#
# s1 = list(s)
# print(s1,type(s1))
#
# # m = [[1,2],3,4]
# # s3 = set(m)
#
# # print(s3)
#
# # d ={s:s1}
# # print(d)
#
# s.add('u')
# print(s)
# s.update('ale')
# s.update(['ale',999])
# print(s)
# s.pop()
# print(s,s.pop())
# s.clear()
# print(s,s.clear())
#
#
# s4 = frozenset('alex li')

