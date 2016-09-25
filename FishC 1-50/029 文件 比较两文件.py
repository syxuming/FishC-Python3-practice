name1 = input('请输入第一个文件名：')
name2 = input('请输入第二个文件名：')
file1 = open(name1)
file2 = open(name2)

diff = []
a = 0

for line1 in file1:
    line2 = file2.readline()
    a += 1
    if line1 != line2:
        diff.append(str(a))


print ('两个文件共有%d处不同'% len(diff))
for each in diff:
    print ('第'+each+'行不一样')

file1.close()
file2.close()
