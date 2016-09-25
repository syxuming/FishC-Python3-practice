
# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')

# 判断长度
length = len(passwd)

while (passwd.isspace() or length == 0) :
    passwd = input("您输入的密码为空（或空格），请重新输入：")

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0

# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break
    
# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break    

# 打印结果
while 1 :
    print("您的密码安全级别评定为：", end='')
    if flag_len == 1 or flag_con == 1 :
        print("低")
    elif flag_len == 2 or flag_con == 2 :
        print("中")
    else :
        print("高")
        print("请继续保持")
        break

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位'")
    break

