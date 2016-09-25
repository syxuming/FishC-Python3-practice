import easygui as g
import sys
import os
extlist = ['.py','.c','.cpp','.pas','.asm']
extcount = {'.py':0,'.c':0,'.cpp':0,'.pas':0,'.asm':0}
filecount ={'.py':0,'.c':0,'.cpp':0,'.pas':0,'.asm':0}
raw = 0

def findcode(getdir):
    os.chdir(getdir)
    filelist = os.listdir(os.curdir)
    for each in filelist:
        if os.path.isfile(each):
            ext = os.path.splitext(each)[1]
            if ext in extlist:
                with open(each,encoding= 'utf-8') as codefile:
                    global extcount                     
                    extcount[ext] += len(codefile.readlines())
                    global filecount
                    filecount[ext] += 1
        if os.path.isdir(each):
            findcode(each)
            os.chdir(os.pardir)


getdir = g.diropenbox()
if getdir == None:
    sys.exit()
else:
    findcode(getdir)#函数调用
for i in extcount.values():#计算总行数
    raw += i

percent = str(round(raw/100000*100,2))+'%'#计算百分比

difference = 100000-raw#距离10W行

#最后显示窗口#
msg='您目前共累计编写了 %d 行代码，完成进度：%s\n离10万行代码还差 %d 行请继续加油'% (raw,percent,difference)
title = '统计结果'
text = []
for i in extlist:
    text.append('【%s】源文件%d个，源代码%d行\n'%(i,filecount[i],extcount[i]))

g.textbox(msg,title,text)
