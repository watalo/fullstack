# __author__:"watalo"
# date: 2019/9/8

# 商店里的商品列表
com = {
    1: ["iphone", 5800],
    2: ["macbook", 9000],
    3: ["coffee", 320],
    4: ["pythonbook", 80],
    5: ["bicyle", 1500]
}

shoplist = []  # 购物车变量

salary = input("请输入您的预算：")  # 总共有5000改为可以选多少钱
if salary.isdigit():  # 验证
    salary = int(salary)
    yue = salary

    while yue >= 0:  # 形成一个无限循环

        for i in com.keys():  # 打印商品内容
            print(i, '>>>','商品名称：',com[i][0],'单价：',com[i][1],'元/件')
        comd_num = input("输入商品编号（1...5）或退出（q）：")  # 引导选择商品

        if comd_num.isdigit():  # 验证输入是否合法
            comd_num = int(comd_num)
            if comd_num > 0 and comd_num <= len(com):
                p_com = list(com.values())[comd_num - 1]  # 将选择的商品选出来
                if p_com[1] < yue:
                    yue -= p_com[1]  # 买了要扣预算
                    shoplist.append(p_com)
                    print("购物车商品有：", shoplist)
                    print("余额还有：", yue)
                else:
                    print("购物车商品有：", shoplist)  # 用户选商品编号，调用商品价格进行判断钱够不够
                    print("您的余额不足！还有%s" % yue)
            else:
                print("无此商品")
        elif comd_num == "q":
            list1 = [] #过渡列表，装已选商品名称
            for v in shoplist:
                list1.append(v[0]) # 遍历已选商品，v是一个["bicyle", 1500]，不能用到集合里，所以要
            list2 = list(set(list1)) # 用集合去重
            print("-------------您已购买如下商品--------------")
            for i in list2:
                if list1.count(i) >= 2:
                    print(i, "*", list1.count(i))
                else:
                    print(i,'*1')
            print("--------------欢迎下次光临！---------------")
            break
        else:
            print("非法字符")
