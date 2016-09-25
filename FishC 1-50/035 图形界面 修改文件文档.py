import easygui as g     #导入easygui模块
import sys
import os
path = g.fileopenbox(filetypes = ['*.txt'])

if path == None:
    sys.exit()
else:
    filename = path.split('\\')[-1]
    file = open(path)
    content = file.read()
    file.close()
newcontent = g.textbox(msg = '【%s】文件内容如下'%filename,title='显示文件内容',text=content)[:-1]
if content == newcontent:
    sys.exit()
else:
    buttonmsg = '检测到文件内容发生改变，请选择以下操作'
    buttontitle = '警告'
    buttonchoices =('覆盖保存','放弃保存','另存为...')
    saveoption = g.buttonbox(buttonmsg,buttontitle,buttonchoices)
if saveoption == '覆盖保存':
    tempfile = open(path,'w')
    tempfile.write(newcontent[:-1])
    tempfile.close()
elif saveoption == '放弃保存':
    sys.exit()
elif saveoption == '另存为...':
    newdir = g.filesavebox(default = '.txt',filetypes = ['*.txt'])
    if os.path.splitext(newdir)[1] != '.txt':
        newdir += '.txt'
    tempfile = open(newdir,'w')
    tempfile.write(newcontent[:-1])
    tempfile.close()
