import random
times = 3
secret = random.randint(1,10)
guess = 0
print ("猜数字:",end=" ")
while(guess != secret) and (times >0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，请输入整数:")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print ("对了")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
        if times >0:
            print("再试一次吧",end=" ")
        else:
            print("机会没有了")
print ("game over!")
