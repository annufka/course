class OnlyASCII:
    def __get__(self, instance, owner):
        # magic

    def __set__(self, instance, value):
        # magic

    def __set_name__(self, owner, name):
       # magic


class Person:
    name = OnlyASCII()

    def __init__(self, name, age):
        self.name = name
        self.age = age
