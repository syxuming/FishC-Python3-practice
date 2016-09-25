name = input('请输入文件名：')
file = open(name)
num = input('需要显示前几行：')
i = 1
while i <= int(num):
    print (file.readline(),end='')
    i += 1

file.close()
