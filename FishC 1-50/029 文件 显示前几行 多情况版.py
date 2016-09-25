def display(name,num):
    file = open(name)
    temp = num.split(':')

    #'13:20'类型
    if num[0].isdigit() and num[-1].isdigit():      
        i = 1
        start = int(temp[0])
        end = int(temp[1])
        while start <= end:
            if i < start:
                file.readline()
                i += 1
            else:
                print (file.readline(),end='')
                start += 1
                i += 1
                
    #'11:'类型
    if num[0].isdigit() and not num[-1].isdigit():
        length = len(file.readlines())
        file.seek(0,0)
        i = 1
        start = int(temp[0])
        while start <= length:
            if i < start:
                file.readline()
                i += 1
            else:
                print (file.readline(),end='')
                start += 1
                i += 1
                
    #':21'类型
    if not num[0].isdigit() and num[-1].isdigit():
        start = 1
        end = int(temp[1])
        while start <= end:
                print (file.readline(),end='')
                start += 1

    file.close()

name = input('请输入文件名：')
num = input('需要显示哪几行(如13:20 或 11: 或 :21 )：')
display(name,num)
