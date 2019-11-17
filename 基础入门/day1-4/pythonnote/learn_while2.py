# while循环
#
#
#
#i = 1
'''
while i <= 100:
  if i % 2 == 1:
  	print(i)
  i += 1

-----------------------------------------
while i <= 100:
  if i % 2 == 0:
  	print(i)
  i += 1
 
-----------------------------------------
age = 50
#1input_age = int(input("age is:"))
flag = True

while flag:
	input_age = int(input("age is:"))
	if input_age == 50:
		print("YES")
		flag = False
	elif input_age > 50:
		print("it's bigger")
	else:
		print("it's smaller")

print("...end...")
-----------------------------------------
# 【break】的实现方式
# break=终止>>>>>>>>>>>>>> 结束while循环
# 
age = 50
#1input_age = int(input("age is:"))
flag = True

while True:
	input_age = int(input("age is:"))
	if input_age == 50:
		print("YES")
		break                  #结束循环
	elif input_age > 50:
		print("it's bigger")
	else:
		print("it's smaller")

print("...end...")
------------------------------------------
#  【continue】
#  跳过3的操作
num = 0
while num <= 10:     # <-+
	num += 1         #   I
	if num == 3:     #   I
		continue     # --+ 结束当次循环，开始下一次循环
	print(num)
	
-------------------------------------------

'''

#[while...else...]

num = 0
while num <= 10:     # <-+
	num += 1         #   I
	if num == 3:     #   I
		break        # --+ 结束当次循环，开始下一次循环
	print(num)
else:
	print("this is else statement")