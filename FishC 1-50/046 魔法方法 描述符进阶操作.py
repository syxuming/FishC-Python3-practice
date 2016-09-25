import time

class Record:
    def __init__(self,value,name):
        self.value = value
        self.name = name
        self.filename = 'record.txt'
        
    def __get__(self, instance, owner):
        with open(self.filename,'a') as f:
            f.write('%s 变量于北京时间 %s 被读取，%s = %s \n' % (self.name,time.ctime(),self.name,self.value))
        return self.value
    def __set__(self, instance, value):
        with open(self.filename, 'a') as f:
            f.write('%s 变量于北京时间 %s 被修改，%s = %s \n' % (self.name,time.ctime(),self.name,value))
        self.value = value
