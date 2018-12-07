class OnlyASCII:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        

    def __set__(self, instance, value):
        try:
            value.encode('ascii')
        #если нет, то вернем сообщение
        except UnicodeEncodeError:
            instance.__dict__[self.name] = None
        else:
            instance.__dict__[self.name] = value


    def __set_name__(self, owner, name):
        self.name = name


class Person:
    name = OnlyASCII()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
poul = Person('Poul', 25)
print(poul.name)
mary = Person('¶³±®', 25)
print(mary.name)
