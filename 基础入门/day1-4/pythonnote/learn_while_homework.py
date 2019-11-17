#!/usr/bin/env python
# -*- coding:utf-8 -*-

sumo = 0
start = 1

while start<=100:	
	if start % 2 == 1:
		sumo = sumo + start
	start += 1
print(sumo)

"""
while start<=100:	
	if start % 2 == 0:
		sumo = sumo + start
	start += 1
print(sumo)
"""