class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # список для запоминания людей
        self.memory = []

    def interact(self, obj):
        """
        Создание словаря для персоны, которую мы собираемся запомнить
        """
        #проверка возраста и объема памяти
        self.check(obj)

    def check(self, obj):
        """
        age<=25 - помнит всех с кем взаимодействовал
        25<age<50 - пять последних
        50<age<75 - двух последних
        75<age<100 - никого не помнит :)
        """
        if self.age <= 25:
            #формирование элемента списка
            about_person = {'name': obj.name, 'age': obj.age, 'related_obj': self}
            if self.repeat_check(obj) == True:
                #добавление словаря в список памяти
                self.memory.append(about_person)
        elif self.age > 25 and self.age <= 50:
            about_person = {'name': obj.name, 'age': obj.age, 'related_obj': self}
            # если память меньше 5 элементов, то добавляем в конец последнее взаимодействие
            if self.repeat_check(obj) == True:
                if len(self.memory) < 5:
                    self.memory.append(about_person)
                # если память больше 5 элементов, то сначала удалим первый элемент
                else:
                    self.memory.pop(0)
                    self.memory.append(about_person)
        elif self.age > 50 and self.age <= 75:
            about_person = {'name': obj.name, 'age': obj.age, 'related_obj': self}
            if self.repeat_check(obj) == True:
                if len(self.memory) < 2:
                    self.memory.append(about_person)
                else:
                    self.memory.pop(0)
                    self.memory.append(about_person)
        #если возраст больше 75, то вернется пустой список

    def repeat_check(self, obj):
        """
        Проверка на повторяемость элемента, если имя и возраст совпадают, то добавлять не будем
        """
        #пройдемся по элементам списка, если у них совпадает имя и возраст, то вернем False
        for index_of_memory in range(len(self.memory)):
            if self.memory[index_of_memory].get('name') == obj.name and self.memory[index_of_memory].get(
                    'age') == obj.age:
                return False
        return True


bob = Person('Bob', 24)
alice = Person('Alice', 49)

steve = Person('Steve', 74)

tom = Person('Tom', 99)
kate = Person('Kate', 15)
jone = Person('Jone', 10)
pete = Person('Pete', 15)
poul = Person('Poul', 15)
jack = Person('Jack', 15)
serg = Person('Serg', 15)
mary = Person('Mary', 15)

bob.interact(alice)
print(bob.memory)
print(alice.memory)

alice.interact(bob)
print(alice.memory)

bob.interact(steve)
print(bob.memory)
bob.interact(steve)
print(bob.memory)

bob.interact(tom)
bob.interact(jone)
bob.interact(pete)
bob.interact(poul)
bob.interact(jone)
bob.interact(jack)
bob.interact(serg)
bob.interact(mary)
print(bob.memory)

alice.interact(tom)
alice.interact(jone)
alice.interact(tom)
print(alice.memory)
alice.interact(pete)
alice.interact(poul)
print(alice.memory)
alice.interact(jack)
print(alice.memory)
alice.interact(serg)
print(alice.memory)
alice.interact(mary)
print(alice.memory)

steve.interact(jone)
steve.interact(pete)
print(steve.memory)
steve.interact(pete)
print(steve.memory)
steve.interact(poul)
print(steve.memory)
steve.interact(jack)
print(steve.memory)
steve.interact(serg)
print(steve.memory)
steve.interact(mary)
print(steve.memory)

tom.interact(poul)
print(tom.memory)
tom.interact(jack)
print(tom.memory)
tom.interact(serg)
print(tom.memory)
