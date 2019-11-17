#__author__:"watalo"
#date: 2019/9/5

name = input("name:")
age = intinput("age:")
salary = input("salary:")
job = input("job:")

# if salary.isdigit(): #长的像不像数字，比如200d，"200"
#     salary = int(salary)
# # else:
# #     exit("must input digit")  # 退出程序

msg = '''
--------------info of %s ----------
Name: %s
Age : %d
Job : %s
Salary : %s
-----------------end-------------------
''' % (name,name,age,job,salary)

print(msg)