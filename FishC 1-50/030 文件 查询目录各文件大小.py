import os

infor = dict()
file_list = os.listdir('.')

for each in file_list:
    size = os.path.getsize(each)
    print (each + ' 【%sBytes】'% size)
