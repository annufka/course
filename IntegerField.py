class IntegerField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        
        #проверим тип возраста, если не int, то вернем None
        if type(value) != int:
            instance.__dict__[self.name] = None
        else:
            instance.__dict__[self.name] = value
        

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
