num = 100
while num <= 999:
    hun = int(num / 100)
    ten = int(num / 10) % 10
    uni = int(num % 10)
    if hun ** 3 + ten ** 3 + uni ** 3 == num:
        print(num)
    num += 1
    
