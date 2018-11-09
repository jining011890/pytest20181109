
#表达式：运算符与操作符组成的序列
# a = 0
# print(a > 1 + 2)     # '='其实也是运算符，赋值
# print(1 + 2 + 3)

'''
优先级比较
'''
#次幂、加减乘除等于优先级示例：
# a = 3
# b = 3
# c = 3
# a = a ** 3 * 5 + 3 * 5 - 4 // 2
# print(a)
# b = ((b ** 3) * 5) + (3 * 5) - (4 // 2)
# print(b)

# #比较运算符与等于运算符优先级比较 示例
# a=True  #  >= 优先级高于==  ；换成False或者0时怎么都搞不懂？？？
# print( 3 >= 4 == a )
# print( 3 >= (4 == a) )
# print(( 3 >= 4) == a )

# # 比较 not > and > or优先级
# a = 1
# b = 2
# c = 3
# print(a or b and c)
# print(a or (b and c))  # and > or
# print((a or b) and c)

# a = 0
# b = 2
# c = 3
# print(not a and b)
# print((not a) and b)  # not > and
# print(not (a and b))

# a = 1
# b = 2
# c = 3
# print(not a or b + 2 == c)
# print((not a) or ((b + 2) == c))  # + > == > not > or



