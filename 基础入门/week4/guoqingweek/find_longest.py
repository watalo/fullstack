#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/5 14:35
#
# import time
#
#
# print(time.time())
# print(time.strftime('1'))


import random

def v_code():
    code=''
    for i in range(10):
        add = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        # if i == random.randint(0,4):
        #     add = random.randrange(10)
        # else:
        #     add = chr(random.randrange(65,91))

        code += str(add)
    return code

print(v_code())