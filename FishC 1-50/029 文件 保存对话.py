b =1
g =1

record = open(r'E:\record.txt')
for i in record:
    if i[0:3] == '小甲鱼':
        boy = open(r'E:\boy_%s.txt' %b,'a')
        boy.write(i[4:])
    elif i[0:3] == '小客服':
        girl = open(r'E:\girl_%s.txt' %b,'a')
        girl.write(i[4:])
    elif i[0:3] == '===':
        b += 1
        g += 1

record.close()
boy.close()
girl.close()
