#__author__:"watalo"
#date: 2019/9/11

dic111 = {"name":"alex","age":36,"sex":'male'}

# for i in dic111:
#     print(i,dic111[i])
#
# for i in dic111.items():
#     print(i)

for i,v in dic111.items(): #该方法慢
    print(i,v)