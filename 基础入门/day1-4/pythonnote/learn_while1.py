#!/usr/bin/env python
# -*- coding:utf-8 -*-

# while 循环

import time


n1 = True

while  n1:
	print("1")
	time.sleep(1)
	n1 = False

print("END")



#输出到1.2.3.4.5

"""
n2 = 1
n3 = True
while n3:
	print(n2)
	# n2 = n2 + 1

	if n2 == 10:
		n3 = False
	n2 = n2 + 1

	time.sleep(1)
print("END")

kaishi = 1

while True:
	print(kaishi)
	if kaishi == 10:
		break               #用于跳出当前循环，并且不再执行以下命令
	kaishi = kaishi +1
	time.sleep(1)


	




