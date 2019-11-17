#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/7 2:30

import time
t = time.ctime()
st = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
print(t)
print(st)
time.sleep(1)
t = time.ctime()
st = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
print(t)
print(st)