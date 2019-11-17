#!/usr/bin/env python
# -*- coding:utf-8 -*-

i = 1
j = 0

while i <= 100:
	if i % 2 == 1:
		j = j + i
	else:
		j = j - i
	i += 1
print(j)