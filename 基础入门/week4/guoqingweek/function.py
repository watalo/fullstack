'''
函数
  1减少重复代码
  2方便修改-更易扩展
  3保持代码一致性

数学中的函数 function（）
计算机中的函数 ==subroutine 子程序 procedures 过程

参数：
      1、必须参数：按顺序录入参数
      2、关键字参数：
      3、默认参数（必须放后面）
      4、不定长参数
          无命名参数*args
          命名参数*kwargs
          位置：*args放在*kwargs前面
      【参数位置】：关键参数、默认参数、不定长参数（*args *kwargs）

return语句
    return 返回任意对象 （包括None）
    1、函数里如果没有return，默认返回None
    2、返回多个对象，会自动封装成一个元组

作用域 LEGB
L：Local
E：enclosing    ----> nonlocal
G：Global       ----> global
B：Built-in
优先级是L-E-G-B

L里有执行L，没有则向上一级找

summury
    变量查找顺序：L E G B
    只有函数、模块、类 才能引入新作用域
    对于一个变量，内部作用域先声明就会覆盖外部变量，不声明就直接使用，就会使用外部作用域的变量
    内部作用域要修改外部作用域时，全局用global，嵌套用nonlocal

'''

# count = 10

def outer():
    print(count)
    count = 5
    # print(count)

outer()