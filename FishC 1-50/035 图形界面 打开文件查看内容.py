import easygui as g     #导入easygui模块
import sys

path = g.fileopenbox(filetypes = '*.txt')


if path == None:
    sys.exit()
else:
    filename = path.split('\\')[-1]
    file = open(path)
    content = file.read()
    g.textbox(msg = '【%s】文件内容如下'%filename,title='显示文件内容',text=content)
