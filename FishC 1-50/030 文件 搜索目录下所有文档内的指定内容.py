import os
def searchw(word):
    txtlist = []
    for each in os.walk(os.getcwd()):
        for subeach in each[-1]:
            fileext = subeach.split('.')
            if fileext[-1] in ('txt'):
                num = each[-1].index(subeach)
                txtlist.append('%s\%s'%(each[0],each[2][num]))

    for eachtxt in txtlist:
        file = open(eachtxt)
        txt = file.readlines()
        for eachline in txt:
            times = eachline.count(word)
            if times > 0:
                print ('在文件【%s】中找到关键词【%s】'%(eachtxt,word))
                break

        if choose == 'YES':
            for eachline in txt:
                site = []
                location = 0
                times = eachline.count(word)
                if times > 0:
                    line = txt.index(eachline)+1
                    while times > 0:
                        site.append(eachline.find(word)+1+location)
                        location = location + len(eachline.partition(word)[0]) + len(word)
                        eachline = eachline.partition(word)[-1]
                        times -= 1
                    print('关键字出现在第%d行，第%s个位置'%(line,site))        
        print('\n')
        
word = input('输入需要查找的关键字（将文件置于查找目录）：')
choose = input('是否需要打印【%s】在文件中的具体位置：'% word)
searchw(word)
