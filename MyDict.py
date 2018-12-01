class MyDict(dict):
    def __getattr__(self, key):
        return self[key]
    def __selfater__(self, key, value):
        self[key]=value

md = MyDict()
md['test'] = 1
md.test

md['attribute'] = 2
md.attribute
