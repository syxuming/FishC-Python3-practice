def cs(*js):
    if js[-1] != 5:
        return sum(js)*3
    else:
        return (sum(js)-5)*5

print (cs(1,2,3,4,9,5))
