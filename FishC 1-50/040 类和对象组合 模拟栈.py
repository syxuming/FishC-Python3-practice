class Stack:
    LIFO = []
    def isEmpty(self):
        if len(self.LIFO) == 0:
            return True
        else:
            return False
    def push(self,x):
        self.LIFO.append(x)

    def pop(self):
        if not
        return self.LIFO.pop(-1)

    def top(self):
        return self.LIFO[-1]

    def bottom(self):
        return self.LIFO[0]
