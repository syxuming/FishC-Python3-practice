x = 7
i = 1
while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6 == 5):
        print (x)
        x = 7 * (i + 1)
        i = i + 1
    else:
        x = 7 * (i + 1)
        i = i + 1
