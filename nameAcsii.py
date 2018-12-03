class OnlyASCII:
    def __get__(self, instance, owner):
        #проверка, являются ли символы ascii
        try:
            instance.__dict__[self.name].encode('ascii')
        #если нет, то вернем сообщение
        except UnicodeEncodeError:
            return "You entered bad name"
        #если все хорошо, то вернем введенное имя
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
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
