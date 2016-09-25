class Word(str):
    def __init__(self,arg=''):
        if isinstance(arg,str):
            self.length = len(arg.split(' ')[0])

    def __lt__(self,other):
        return int.__lt__(self.length,other.length)
