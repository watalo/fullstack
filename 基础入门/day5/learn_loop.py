# __author__:"watalo"
# date: 2019/9/5
_user = "watalo"
_passwd = "abc123"
counter = 0
while counter < 3:

    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("welcome %s login" % _user)
        break
    else:
        print("Invalid username of password")
        print("你还有" + str(3 - counter) + "次机会！")
    counter += 1
    if counter == 3:
        keep_go_choice = input("还想玩吗？[y/n]:")
        if keep_go_choice == "y":
            counter = 0

else:
    print("你的账户已被锁定，请联系管理员。。。")
