class Canshu:
    def __init__(self,*arg):
        l = len(arg)
        if l:
            print ('传入了%d个参数，分别是%s' % (len(arg),arg))
        else:
            print ('并没有传入参数')
