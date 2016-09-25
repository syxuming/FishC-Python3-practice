name = input('请输入待查找的用户名：')
score = [['迷途', 85], ['黑夜', 80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
IsFind = False

for each in score:
    if name == each[0]:
        print(name + '的得分是：', each[1])
        IsFind = True
        break
    
if IsFind == False:
    print('查找的数据不存在！')

