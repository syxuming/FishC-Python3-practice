def binary(x):
    a= []
    while x:
        a.insert(0,x%2)
        x=x//2
    return a
print(binary(1))
