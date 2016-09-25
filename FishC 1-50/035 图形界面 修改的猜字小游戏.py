import random
import easygui as g     #导入easygui模块
import sys
secret = random.randint(1,10)
guess = 0
while guess != secret:
    temp = g.integerbox('猜数字(1-10)：','数字小游戏',lowerbound = 1,upperbound=10)
    if temp == None:
        sys.exit(0)
    guess = int(temp)
    if guess == secret:
        g.msgbox("对了")
        break
    else:
        if guess > secret:
            g.msgbox("大了")
        else:
            g.msgbox("小了")
        if g.ccbox("要再试一次吗?",choices=('要啊','算了')):
                pass
        else:
                sys.exit(0)
        

g.msgbox("game over!")
