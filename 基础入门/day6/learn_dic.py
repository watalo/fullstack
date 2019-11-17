#__author__:"watalo"
#date: 2019/9/10

#常用方式
dic1 = {"name":"alex","age":36,"sex":'male','hobby':{"girl_name":"datao","figure":"hot"},'11':True}
#函数方式
dic2 = dict((("a",12),))
dic3 = dict([["a",12],])

print(dic2,dic3)
a = 10
b = a
b = 15

# print(id(a)) # id()查看内存地址
# print(id(b))
# print(a,b)
# print(dic1)
# print(dic1['hobby'])

#增
dic2['b'] = 32
#.setdefault("b",34), 1如果字典里有，不改，返回键值，
#.setdefault("c",34), 2如果没有，添加，返回添加值
dic2.setdefault("b",34)
ret = dic2.setdefault("c",34)
print(dic2)
print(ret)

#查 1\通过键去查找
print(dic1["name"])
#查 2\查键名字
print(dic2.keys())
print(list(dic2.keys()))
#查 3\查值
print(dic2.values())
print(list(dic2.values()))
#查 3\查键值对
print(dic2.items())
print(list(dic2.items()))

#改
dic4 = {"name":"alex","age":36,"sex":'male'}
dic5 = {"a":12,"name":"yang"}

dic4.update(dic5) #更新dic4，如果键存在，更新值，如果键不存在，增加键值对
print(dic4)
print(dic5)

#删
dic6 = {"a":12,"name":"yang"}
dic6.clear() #清空，只剩一个空字典
print(dic6)

dic8 = {"a":12,"name":"yang"}
del dic8["name"]#删除指定键值对
print(dic8)

dic7 = {"a":12,"name":"yang","b":33}
dd = dic7.pop("a") # 删掉指定键值对，并返回值
print(dd)
ss = dic7.popitem() #随机删除键值对，并返回值
print(ss)

dic9 = {"a":12,"name":"yang","b":33}
del dic9 #删除字典

#其他操作
# .fromkeys()
dic10 = {"a":12,"name":"yang","b":33}
dic10 = dict.fromkeys(["1","2","3"],'test')
print(dic10)
#.copy() 深浅拷贝的 以后再说

#嵌套
av_catalog = {
     "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1] = "hhah"
av_catalog["大陆"]["1024"][1] += "hhah"
print(av_catalog)

#排序 sorted()
dicc = {5:"555",6:"666",1:"111"}
print(sorted(dic))



