password = "syxuming"
i=3

while i:
    temp = input("请输入密码：")
    if temp == password:
        print ("密码正确，进入系统")
        break
    elif "*" in temp:
        print ("密码中不能包含*号")
        continue
    else:
         print ("密码错误")
         i -= 1
