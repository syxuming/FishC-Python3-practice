import easygui as g     #导入easygui模块
import sys



msg = '带*为必填项'
title = '账号中心'
fields=('*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail')
while True:
    data = g.multenterbox(msg,title,fields)
    blank =[]
    if data == None:
        sys.exit()
    if data[0] == '':
        blank.append('用户名')
    if data[1] == '':
        blank.append('真实姓名')
    if data[3] == '':
        blank.append('手机号码')
    if data[5] == '':
        blank.append('E-mail')

    blanks = ','.join(blank)
    if blanks == '':
        g.msgbox('注册成功！')
        break
    else:
        g.msgbox('%s不得为空'%blanks)
