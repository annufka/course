class Singleton(type):
    def __call__(self, *args, **kwargs):
        # создаём новый класс как обычно
        cls = type.__call__(self, *args)
        self.call += 1
        if self.call <= 1:
        # возвращаем класс
            return cls
        else:
            return None

class MyClass(metaclass=Singleton):
    call = 0
    def useless(self):
        return 42
        
a = MyClass()
b = MyClass()
print(id(a) == id(b))
