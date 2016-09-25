while 1:
    temp = input("请输入一个整数（输入Q结束进程）：")
    while not temp.isdigit():
        if temp == 'Q' or temp == 'q':
            quit
        else:
            temp = input ("抱歉，请输入一个整数：")
    num = int(temp)
    print('十进制 -> 十六进制：', num ,'->','%x' % num)
    print('十进制 -> 八进制：', num ,'->','%o' % num)
    print('十进制 -> 二进制：', num ,'->',bin(num))
