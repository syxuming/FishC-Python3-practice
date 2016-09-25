import os
file_type = []
removal = []
file_list = os.listdir('.')

for each in file_list:
    if os.path.isdir(each):
        file_type.append('文件夹')
    else:
        ext = os.path.splitext(each)[1]
        file_type.append(ext)

for i in file_type:
    if i not in removal:
        removal.append(i)

for each_type in removal:
    time = file_type.count(each_type)
    print ('该文件夹下共有类型为【%s】的文件%d个'%(each_type,time))
    
