#  99乘法表
#  
# 
# 
#   
''' 
print("hello world",end=" ") #
print("hello world",end=" ")
print("hello world",end=" ") 
'''
'''
i = 1
j = 1

while i < 10:
	while j < 10:
		print(i,"*",j,"=",i*j,end="\n")
		j += 1
	i += 1
	print() # = print(end="\n")
'''



l = 1
while l <= 9:
	c = 1
	while c <= l:
		print(str(c)+"*"+str(l)+"=",c*l,end="\t") #  \t 制表符，对齐用的
		c += 1
	print()
	l += 1

	
