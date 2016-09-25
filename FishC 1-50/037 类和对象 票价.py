class Ticket():
    def __init__(self,weekend=False,child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self,num):
        return self.exp * self.inc *self.discount * num

adult = Ticket()
child = Ticket(child = True)
print ('2个大人+1个小孩平日票价为:%.2f' % (adult.calcPrice(2) +child.calcPrice(1)))
