def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x,y-1)

numx = int(input('请输入X的值：'))
numy = int(input('请输入Y的值：'))
print(power(numx,numy))
