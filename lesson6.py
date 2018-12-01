class Descr:
    def __set__(self, instance, value):
        print(instance, value)
class A:
    attr= Descr()
instance = A()
instance.attr = 42 #будет работать с дескриптором
A.attr= 42 #далит дескриптор и установит 42

class Descr:
    def __delete__(self, instance):
        print(instance)
class A:
    attr= Descr()
del A().x #удалит значение
del A.x #удалит дескриптор


class Descr:
    def __get__(self, instance, owner):
        print(instance, owner)


class A:
    attr = Descr


a = A()
print(a.attr)

print(a.__dict__)

a.__dict__['1'] = 1
print(a.__dict__)


#дескриптор перехатівает поведение

class B:
    def get(self):
        pass


print(B.get) #<function B.get at 0x7ff1c6f1aea0>

print(B().get) #<bound method B.get of <__main__.B object at 0x7ff1c6f23dd8>>

print(B().get()) #None

#не требует селф
class B:
    @staticmethod
    def get():
        print('get')

B.get()

#мы работаем с классом
class B:
    @classmethod
    def get(cls):
        print(cls)
        print('get')

B.get()


class B:
    pass

b = B() #экземпляр
print(b) #<__main__.B object at 0x7fed5b587dd8>
print(B) #<class '__main__.B'>
print(type(B)) #<class 'type'>
print(type(b)) #<class '__main__.B'>

y = type("Y", (parents, ), {attr})

