list1 = [135,2,666,5,96,'s',22]
summ = 0

for each in list1:
    if type(each) == int or type(each) == float:
        summ += each
    else:
        continue
print(summ)
