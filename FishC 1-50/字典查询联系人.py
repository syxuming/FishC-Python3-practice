print('1：查询联系人')
print('2：插入新联系人')
print('3：删除联系人')
print('4：退出程序')

#通讯录数据库
data = {'小甲鱼':'020-88974651'}

#1：查询联系人函数
def find(n):
    if n in data:
        print('联系电话是：',data[n])
    else:
        print('没有该联系人!')

#2：插入新联系人
def new(n):
    if n in data:
        print ('已存在联系人',n,'：',data[n])
        YON = input('是否对其修改（YES/NO）：')
        if YON == 'NO':
            quit
        if YON == 'YES':
            tel = input('请输入联系方式：')
            data[n] = tel
    else:
        tel = input('请输入联系方式：')
        data[n] = tel

#3：删除联系人
def delete(n):
    if n in data:
        del data[n]
    else:
        print('没有该联系人!')
        
#程序输入框
while 1:
    temp = input("请输入相关指令：")
    if temp == '4':
        break
    if temp == '1':
        n = input('输入联系人姓名：')
        find(n)
    if temp == '2':
        n = input('输入联系人姓名：')
        new(n)
    if temp == '3':
        n = input('输入联系人姓名：')
        delete(n)
    print(' ')
