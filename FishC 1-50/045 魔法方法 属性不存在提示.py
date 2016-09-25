class C:
    def __getattr__(self,name):
        return '该属性不存在！'
