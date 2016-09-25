print ('新建用户：N/n')
print ('登陆账号：E/e')
print ('退出程序：Q/q')

data ={'小甲鱼':123456}

#新建用户
def new(username):
    while username in data:
        username = input('该用户名已被注册，请重新输入：')
    password = input('请输入密码：')
    data[username]=password
    print ('注册成功！')
    
#登录账号
def login(username):
    while username not in data:
        username = input('用户名不存在，请重新输入：')
    password = input('请输入密码：')
    if password == data[username]:
        print ('登陆成功！')
    else:
        print ('密码错误')


        
while 1:
    temp = input('请输入指令代码：')
    if temp == 'N' or temp == 'n':
        username = input('请输入用户名：')
        new(username)
    elif temp == 'E' or temp == 'e':
        username = input('请输入用户名：')
        login(username)
    elif temp == 'Q' or temp == 'q':
        break
