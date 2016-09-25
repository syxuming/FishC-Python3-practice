import pickle
import os

class MyDes:
    def __init__(self,name):
        self.name = name
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        with open('%s.pkl' % self.name,'wb') as f:
            pickle.dump(value, f)
        self.value = value
    def __delete__(self, instance):
        del self.name
        os.remove('%s.pkl' % self.name)
