class Singleton(type):
    def check(cls, call):
        pass
    def __call__(self, *args, **kwargs):
        # создаём новый класс как обычно
        cls = type.__call__(self, *args)
        # возвращаем класс
        return cls

class MyClass(metaclass=Singleton):
    def __init__(self, call = 1):
        self.call = call
    


a = MyClass()
b = MyClass()

print(id(a) == id(b))
