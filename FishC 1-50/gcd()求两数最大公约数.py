def gcd(x,y):
    listx =[]
    listy =[]
    listc =[]
    a=x
    b=y
    while a:
        if x % a == 0:
            listx.append(a)
        a -= 1
    while b:
        if y % b == 0:
            listy.append(b)
        b -= 1
        
    for c in listx:
        if c in listy:
            listc.append(c)
    d = max(listc)
    return d

print(gcd(24,36))
        
