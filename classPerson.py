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
        about_person = {'name': obj.name, 'age': obj.age, 'related_obj': self}
        self.memory.append(about_person)
        return self.memory


bob = Person('bob', 19)
alice = Person('Alice', 25)

bob.interact(alice)
print(bob.memory)  # [{'name': 'Alice', 'age': 25, 'related_obj': <__main__.Person object at 0x054F2550>}]
print(alice.memory)  # []

alice.interact(bob)
print(alice.memory)  # [{'name': 'bob', 'age': 19, 'related_obj': <__main__.Person object at 0x030F2550>}]

steve = Person('Steve', 19)
bob.interact(steve)
print(bob.memory)
# [{'name': 'Alice', 'age': 25, 'related_obj': <__main__.Person object at 0x05AE25F0>},
# {'name': 'Steve', 'age': 19, 'related_obj': <__main__.Person object at 0x05AE2690>}]
