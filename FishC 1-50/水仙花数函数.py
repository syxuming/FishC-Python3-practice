def sxh():
    listx=[]
    x=100
    while x < 1000:
        if x == (x//100)**3+((x%100)//10)**3+(x%10)**3:
            listx.append(x)
        x += 1
    print(listx)
