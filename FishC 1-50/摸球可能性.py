print("red\tyellow\tgreen")
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print(red,"\t",yellow,"\t",green)
