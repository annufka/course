class IntegerField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
        #проверим тип возраста, если не int, то вернем сообщение, что это float число либо не число
        if type(instance.__dict__[self.name]) != int:
            instance.__dict__[self.name] = None
        

    def __set_name__(self, owner, name):
        self.name = name

class Person:
    age= IntegerField()

    def __init__(self, name, age):
        self.name = name
        self.age = age

poul = Person('Poul', 25)
print(poul.age)
mary = Person('Mary', 25.0)
print(mary.age)
jone = Person('Jone', 'tk')
print(jone.age)
