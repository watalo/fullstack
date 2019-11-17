


age_of_princal = 56

guess_age = int(input(">>:"))

if guess_age == age_of_princal: #几个条件成立一个剩余的都不执行了
	print("yes")
elif guess_age > age_of_princal:
    print("try smaller")
elif guess_age < age_of_princal:
    print("try older")   
else:
	print("no")
