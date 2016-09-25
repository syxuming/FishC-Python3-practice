def replace(name,old,new):
    f = open(name)
    txt = f.read()
    count = txt.count(old)
    print ('文件%s中共有%d个【%s】'% (name,count,old))
    print ('您确定要把所有的【%s】替换为【%s】吗？'% (old,new))
    confirm = input ('【YES/NO】:')
    if confirm == 'YES':
        newtxt = txt.replace(old,new)
        f.close()
        f = open(name,'w')
        f.write(newtxt)
    elif confirm == 'NO':
        quit

    f.close()







    

name = input('请输入文件名：')
old = input('输入需要替换的字符：')
new = input('输入新的字符：')
replace(name,old,new)
