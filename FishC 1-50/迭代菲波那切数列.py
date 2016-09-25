def ddfbnq(n):
    n1=1
    n2=1
    n3=1
    if n ==1 or n==2:
        n3 = 1
        
    else:
        while n > 2:
            n3 = n1 +n2
            n1 = n2
            n2 = n3
            n -= 1

    return n3
num = int(input('你想知道第几个数的值:'))
print (ddfbnq(num))
