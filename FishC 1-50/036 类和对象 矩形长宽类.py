class Rectangle:
    length = 5
    width = 4
    

    def getRect(self):
        print ('这个矩形的长是：%.2f，宽是：%.2f' % (self.length,self.width))
    def setRect(self):
        print ('请输入矩形的长和宽...')
        self.length = float(input('长：'))
        self.width = float(input('宽：'))
    def getArea(self):
        print (self.length*self.width)
