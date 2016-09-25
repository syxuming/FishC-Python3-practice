def FB(n):
    if n == 1 or n == 2:
        return 1
    else:
        return FB(n-1) + FB(n-2)
num = int(input('你想知道第几个数的值:'))
print(FB(num))
 
