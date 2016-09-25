a=[]
x=0
def get_digits(n):
    b=str(n)
    c = len(b)
    global x
    if x<c:
        a.append(b[x])
        x += 1
        return get_digits(n)

get_digits(987654321)
print(a)
