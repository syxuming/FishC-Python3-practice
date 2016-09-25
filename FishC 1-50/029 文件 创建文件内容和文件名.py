
file_name = input('请输入文件名：')
new = open(r'E:\%s.txt'%file_name,'a')
print('请输入内容：【单独输入\':w\'保存退出】：')

content =[]
line = ' '
while line != ':w':
    line = input()
    new.write(line + '\n')

new.close()
