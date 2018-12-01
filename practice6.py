#1
class MemoryField:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        if instance.age <= 25:
            try:
                return instance.__dict__[self.label]
            except:
                return []
        elif instance.age > 25 and instance.age <= 50:
            try:
                return instance.__dict__[self.label][-6:-1]
            except:
                return []
        elif instance.age > 50 and instance.age <= 75:
            try:
                return instance.__dict__[self.label][-3:-1]
            except:
                return []
        else:
            return []

    def __set__(self, instance, value):
        if not instance.__dict__.get(self.label):
            instance.__dict__[self.label] = []
        instance.__dict__[self.label].append({"name": value.name,
                                              "age": value.age,
                                              "related_obj": value})


class Person:
    memory = MemoryField('memory')

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def interact(self, obj):
        self.memory = obj


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

#1 Sasha
class MemoryField:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        """
        age <= 25 - помнит всех с кемв заимодействовал
        25 < age < 50 - пять последних
        50 < age < 75 - двух последних
        75 < age < 100 - никого не помнит
        """
        logic_map = {
            "all": (0, 25),
            5: (25, 50),
            2: (50, 75),
            None: (75, float("inf")),
        }
        for k, v in logic_map.items():
            if v[0] < instance.age <= v[1]:
                if isinstance(k, int):
                    return instance.__dict__[self.label][:k]
                if isinstance(k, str):
                    return instance.__dict__[self.label]
                else:
                    return []

    def __set__(self, instance, value):
        if not instance.__dict__.get(self.label):
            instance.__dict__[self.label] = []
        instance.__dict__[self.label].append({"name": value.name,
                                              "age": value.age,
                                              "related_obj": value})

    # def __set_name__(self, owner, name):
    #     self.name = name


class User:
    memory = MemoryField("memory")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def interact(self, obj):
        self.memory = obj


def get_test_data(bob_age):
    bob = User("bob", bob_age)
    alice = User("alice", 25)
    return bob, alice


def test_user_memory_25():
    bob_age = 25
    range_seq = 50
    bob, alice = get_test_data(bob_age)
    for _ in range(range_seq):
        bob.interact(alice)
    assert len(bob.memory) == range_seq


def test_user_memory_25_50():
    bob_age = 40
    range_seq = 50
    bob, alice = get_test_data(bob_age)
    for _ in range(range_seq):
        bob.interact(alice)
    assert len(bob.memory) == 5


def test_user_memory_50_75():
    bob_age = 72
    range_seq = 50
    bob, alice = get_test_data(bob_age)
    for _ in range(range_seq):
        bob.interact(alice)
    assert len(bob.memory) == 2


def test_user_memory_75_100():
    bob_age = 150
    range_seq = 50
    bob, alice = get_test_data(bob_age)
    for _ in range(range_seq):
        bob.interact(alice)
    assert len(bob.memory) == 0


if __name__ == "__main__":
    test_user_memory_25()
    test_user_memory_25_50()
    test_user_memory_50_75()
    test_user_memory_75_100()

#2
class MemoryField:

    def __get__(self, instance, owner):
        if instance.age <= 25:
            try:
                return instance.__dict__[self.name]
            except:
                return []
        elif instance.age > 25 and instance.age <= 50:
            try:
                return instance.__dict__[self.name][-6:-1]
            except:
                return []
        elif instance.age > 50 and instance.age <= 75:
            try:
                return instance.__dict__[self.name][-3:-1]
            except:
                return []
        else:
            return []

    def __set__(self, instance, value):
        if not instance.__dict__.get(self.name):
            instance.__dict__[self.name] = []
        instance.__dict__[self.name].append({"name": value.name,
                                              "age": value.age,
                                              "related_obj": value})
    def __set_name__(self, owner, name):
        self.name = name

class Person:
    memory = MemoryField()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def interact(self, obj):
        """
        Создание словаря для персоны, которую мы собираемся запомнить
        """
        self.memory = obj


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

tom.interact(serg)
print(tom.memory)

#3
class custom_classmethod:
    def __init__(self, method):
        self._method = method
    def __get__(self, instance, owner):
        return partial(self._method, owner)
class Test:
    @custom_classmethod
    def test(cls, args):
        print(cls, args)
Test.test(1)

#4
class custom_classmethod:
    def __init__(self, method):
        self._method = method
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self._method(owner, *args, **kwargs)
        return wrapper

class Test:
    @custom_classmethod
    def test(cls, args):
        print(cls, args)
Test.test(1)