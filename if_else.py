
# if bool值或者 变量:
#     执行语句
# else:
#     执行语句

# mood = True    #bool
# if mood:
#     {
# print('go to left.')
#     }

# mood = True  # bool
# if mood:
#     print('go to left.')
#
#
# mood = False
# if mood:
#     print('go to left.')
# else:
#     print('go to right')
#     #print('back away.')
# #  不同级别的相同代码逻辑上有差别。python的代码不能压缩，压缩就会吧空格等格式给取消掉会导致与预期逻辑不一致
# print('back away.')

#if 后面是表达式
# a = 1
# b = 2
# if a == b:
#    print('go to left')
# else:
#    print('go to right')

# if后面是空值的情况
# d = []
# if d:
#     print('go go')
# else:
#     print('Expression is False.')

'''
一个小程序
通过账号密码登录
'''
account = 'qiyue'
password = 123456
print("please input account：")
user_account = input()   #接收用户输入的关键词

print("please input password：")
user_password = input()
# input()输入变量类型为<str>
#user_password = int(user_password)
if account ==user_account and password==user_password :
    print('sucess!')
else:
    print('fail1')