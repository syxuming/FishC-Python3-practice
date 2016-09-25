class C:
    def __init__(self, size=10):
        self.size = size

    @property
    def x(self):
        return self.size

    @x.setter
    def x(self, value):
        self.size = value

    @x.deleter
    def x(self):
        del self.size
