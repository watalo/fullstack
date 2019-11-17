#__author__:"watalo"
#date: 2019/9/13

# 字符串的方法
st = 'hello kitty'

print(st.count('l'))       # 统计元素个数
print(st.capitalize())     # 首字母大写
print(st.center(50,'$'))      # 居中
print(st.endswith('ty'))    # 判断以某个内容结尾
print(st.startswith('ty'))    # 判断以某个内容开头
print(st.expandtabs(tabsize=20))  #扩大空格
print(st.find('t')) # 查找第一个元素，返回第一个索引值

ts = 'hello kitty {name} is {age}'
print(ts.format(name ='alex',age = 37)) # 格式化输出
print(ts.format_map({'name':'alex','age':22}))
print(ts.index('t'))
print('333'.isalnum())      #判断是否都是数字和字母
print('22'.isdecimal())     #判断是否是十进制
print('22'.isdigit())     #判断是否整型
print('22.44uuu'.isnumeric())     #判断是
print('         03230 \n 2323\n'.strip())
print('123123123123'.replace('1','a'))
print('1AadgBerwerw3'.lower())
print('1AadgBerwerw3'.upper())


print('hello kitty ooo'.split(' '))
print('hello kitty ooo'.split(' '))

