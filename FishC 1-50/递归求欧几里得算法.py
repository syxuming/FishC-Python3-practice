def gcd(x,y):
#    if x < y:
#        x,y=y,x
    if x%y == 0:
        return y
    else:
        return gcd(y,(x%y))

numx = int(input('请输入X的值：'))
numy = int(input('请输入Y的值：'))
print(gcd(numx,numy))
