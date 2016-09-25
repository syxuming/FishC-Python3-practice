def int_input(temp):
    try:
        num = int(temp)
    except ValueError:
        print ('出错，您输入的不是整数！')
        temp = input('请输入一个整数：')
        int_input(temp)

temp = input('请输入一个整数：')
int_input(temp)
