"""
классы содержат методы, методы содержат экземпляры. Если переменная глобальая в классе, то она атрибут класса.
Если атрибут экземпляра, то он определяется через self.
_ - использование чего-то внутри, лучше извне не трогать
__ - вообще приватно, нельзя
"""
"""
class Noop:
    a = 1
    def noop(self):
        a = 2
noop.__dict__[a] - сначала оно поищет в методе а, только если в методе не найдет, то пойдет вверх по дереву
"""
class Test:
    __slots__ = ["x"]
test = Test()
test.x = 1
test.foo = 5
print(test.__dict__)
"""
AttributeError: 'Test' object has no attribute 'foo'
AttributeError: 'Test' object has no attribute '__dict__'
"""

print(Test.__dict__)
#{'__module__': '__main__', '__slots__': ['x'], '__return__': None, 'x': <member 'x' of 'Test' objects>, '__doc__': None}

class Test:
    def test(self):
        pass


Test.test
#<function Test.test at 0x7f489df5fea0>
Test().test
#<bound method Test.test of <__main__.Test object at 0x7f4168f7cdd8>>
Test().test()
#None
Test.test()
#TypeError: test() missing 1 required positional argument: 'self'
t = Test()
Test.test(t)
#None


class Test:
    _value = [1, 2, 3, 4, 5, 6, 7, 8]

    @property
    def value(self):
        return self._value[1]

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError('vse ploxo')
        self._value.append(value)


t = Test()
print(t.value)
#2
t.value = -1
#ValueError: vse ploxo

#экземпляр класса А: а=А()
#mro - слева направо
class A:
    pass

class B(A):
    pass

class D(B):
    pass

class C(A):
    pass

class E(C):
    pass

class F(D,E):
    pass

print(F.mro())
#[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

class F():
    pass

f = F()
print({f:1})
#{<__main__.F object at 0x7fef5995bb70>: 1}


