import random

secret = random.randint(1,10)
print ('----------xm-----------')
x = 1
while x:
    temp = input('不妨猜猜一下小甲鱼想的哪个数字：')
    try:
        x = 0
        guess = int(temp)
    except ValueError:
        print ('要输入整数哦')
        x = 1
while guess != secret:
    temp = input('请重新输入吧：')
    try:
        guess = int(temp)
    except ValueError:
        print ('要输入整数哦')
        continue
    if guess == secret:
        print ('我艹对了')
    else:
        if guess > secret:
            print ('大了')
        else:
            print ('小了')
print ('game over')
