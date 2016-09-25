import os
def searchv(path):
    vediolist = []
    for each in os.walk(r'%s' % path):
        for subeach in each[-1]:
            fileext = subeach.split('.')
            if fileext[-1] in ('mp4','rmvb','avi'):
                num = each[-1].index(subeach)
                vediolist.append(r'%s\%s'%(each[0],each[2][num]))
    txt = open(r'%s\video.txt' % (path),'w')
    for i in vediolist:
        txt.write('%s\n' % i)
    #txt.writelines(vediolist)
    txt.close()
    
path = input('请输入待查找的初始目录：')
searchv(path)

