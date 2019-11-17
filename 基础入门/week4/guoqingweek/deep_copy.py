
'''
深浅拷贝

'''

# s = [[0,1],'sjd','abc']
#
#
# s1 = s
# s1[1]= 'aaa'
# print(s1)
# print(s)
#
# s2 = s
# s[2]= 'bbb'
# print(s,s2)

import copy # copy库


husband = ['a',123,[10000,3000]]

wife = husband.copy() # 浅拷贝
wife[0]='b'
wife[1]=456

xiaosan = copy.deepcopy(husband)  # 深拷贝要用的 copy库
xiaosan[0] = 'c'
xiaosan[1] = 666

xiaosan[2][1] -= 500

print(wife,xiaosan)