try:
    f = open('myfile.txt')
    print (f.read())
except OSError as reason:
    print ('出错了：'+ str(reason))

finally:
    if 'f' in locals():
        f.close
