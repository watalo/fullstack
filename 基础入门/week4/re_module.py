#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/10/7

'''
1 正则表达式
    用来匹配字符串的
2 怎么进行匹配
    正则：模糊匹配
    re 是用C编写的匹配引擎执行
3 表达式语句
    re.findall()：所有结果都返回到一个列表里
    re.search()：返回匹配到的第一个对象（object），对象可以调用.group()方法
    re.match()：只在字符串开始匹配
    re.split()：分割
    re.sub(pattern,repl,)：替换，==string.replace 3个参数
        sub(pattern, repl, string, count=0, flags=0):
    re.compile():编译
        def compile(pattern, flags=0):
            "Compile a regular expression pattern,
            returning a Pattern object."
        return _compile(pattern, flags)

4 元字符（11个）：. ^ $ * + ? {} [] \ () |
    . -->通配符：除了转义符，其他的都可以代指
    ^ -->尖角符：只在开始匹配
    $ -->美元符：只在结束匹配
    * -->重复匹配[0:+oo） =={0，+oo}
    + -->重复匹配[1:+oo） =={1，+oo}
    ？-->[0,1]           =={0，1}
    {}-->{匹配的最小次数:匹配的最大次数} 贪婪匹配 {2}、{1，7}、{}（正无穷）
    []-->字符集
        [a,b,c,]
        [a-z]
        取消元字符的特殊功能（例外：\ ^ -）
        [^t,n,m],取反 非t n m
    \-->转义符，
        后跟“元字符”去除特殊功能
        后跟普通字符实现特殊功能：
            \d  匹配任何十进制数 ==[0-9]
            \D  匹配任何非数字字符 ==[^0-9]
            \s  匹配任何空白字符 ==[ \t\n\r\f\v]
            \S  匹配任何非空白字符 ==[^ \t\n\r\f\v]
            \w  匹配任何字母数字字符 ==[0-9a-zA-Z]
            \W  匹配任何非数字字符 ==[^0-9a-zA-Z]
            \b  匹配一个特殊字符边界，单词和空格间的位置
    ()-->分组
    | -->或
'''

import re

# res = re.findall('w\w{2}l','hello world')
# print(res)

ret = re.findall('s.f','sdfsdassfsdfsaf') #'.'只能代指一个
print(ret)  # ['sdf', 'ssf', 'sdf', 'saf']
res = re.findall('s.f','sssfsdassfsdss') #'.' 不能代指转义符
print(res)  # ['ssf', 'ssf']
res = re.findall('^sf','ssfsdassfsds')
print(res)  # []
res = re.findall('sf$','ssfsdassfsds')
print(res)  # []
res = re.findall('s*f','ssfsdassfsds')
print(res)  # ['ssf', 'ssf']
res = re.findall('s+f','ssfsdassfsds')
print(res)  # ['ssf', 'ssf']
res = re.findall('s?f','ssfsdassfsds')
print(res)  # ['sf', 'sf']
res = re.findall('a{1,5}b','aaaaaaaaaabbbbbbb')
print(res)  # ['aaaaab']
res = re.findall('a[a,v]b','aaaaaaaaaabbbbbbb')
print(res)  # ['aab']
res = re.findall('a[a,*]b','aa*aaaaaabbbbbbb')
print(res)  # ['aab']
res = re.findall('[1-9, a-z, A-Z]','123abcABC')
print(res)  # ['1', '2', '3', 'a', 'b', 'c', 'A', 'B', 'C']
res = re.findall('[^1-9, a-z, A-Z]','123abcABC')
print(res)  # []
print(re.findall("I\b",'hello,I am a LI$T'))
#  []
print(re.search('sb','oiojwodjfosidjfsbsdfjs'))
# <re.Match object; span=(15, 17), match='sb'>
ret = re.search('sb','oiojwodjfosidjfsbsdfjs').group()

ret = re.search('a.','adfsdf').group()
print(ret) # ad
ret = re.search('a\.','a.dfsdf').group()
print(ret) # a.
# ret = re.search('a\\','a\dfsdf').group()
# print(re.findall('\\c','he\co,I am a LI$T'))

ret = re.findall('\\\\','abc\de')
print(ret) # ['\\']
ret = re.findall(r'\\','abc\de')
print(ret) # ['\\']
m = re.search(r'\bblow','I blow you').group()
print(m)   # blow

print(re.search('(ab)|3','3ababababab3cdeffab').group()) # 3

ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeeew34ttt123/ooo')
print(ret.group())  # 123/ooo
print(ret.group('id')) # 123
print(ret.group('name')) # ooo

ret = re.match('asd','fhdsasd')
res = re.match('asd','asdfgeg')
print(res.group()) # asd

ret = re.split('[k,s]','djksalkdasf') #****** 先用k分，在用s 对分组后的再分
'''
1--['dj','sal','da','f']
2--['dj','','al','da','f']
'''
print(ret) # ['dj', '', 'al', 'da', 'f']

ret = re.sub('a..x','s..b','1111111alex222222')
print(ret) # 1111111s..b222222

print(re.findall('\.com','sdfsadfasdf.comsdfsd')) # ['.com']
print(re.findall('\.com','sdf.comsd')) # ['.com']
#==
obj = re.compile('\.com')
ret = obj.findall('sdfsadfasdf.comsdfsd')
res = obj.findall()