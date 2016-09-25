list1 = ['1.1','2.2','3.3','4.4']
list2 = ['4','2','3','1']
list3 = [name + '：' + slogan[2:] for slogan in
          list1 for name in list2 if slogan[0] == name[0]]
for each in list3:
    print (each)
