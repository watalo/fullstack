#!/usr/bin/env python
# -*- coding = utf-8 -*-
# Author = 'watalo'
# time = 2019/10/6 19:20
'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60
万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总
数？
'''

rev = int(input('当年利润为（万元）>>>:'))
bonus = 0

bonuspol = {
    100:0.01,
    60:0.015,
    40:0.03,
    20:0.05,
    10:0.075,
    0:0.1
}

revp = list(bonuspol.keys()) #[100, 60, 40, 20, 10, 0]
rat = list(bonuspol.values()) #[0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

for i in range(0,6):
    if rev > revp[i]:
        bonus += (rev - revp[i])*rat[i]
        print((rev - revp[i])*rat[i])
        rev = revp[i]

print(bonus)



# if rev <= 10:
#     bonus = 0.1*rev
# elif rev <= 20 and rev > 10:
#     bonus = 0.075*(rev - 10) + 1
# elif rev <= 40 and rev >20:
#     bonus = 0.05*(rev - 20) + 1.75
# elif rev <= 60 and rev >40:
#     bonus = 0.03*(rev - 40) + 2.75
# elif rev <= 100 and rev >60:
#     bonus = 0.015*(rev - 60) + 3.35
# else:
#     bonus = 0.01*(rev - 100) + 3.95

# print(bonus)


