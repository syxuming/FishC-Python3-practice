a = []
def bin(n):
    if n > 0:
        x = n%2
        a.insert(0,x)
        return bin(n//2)

bin(30)
print(str(a))
