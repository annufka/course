
'''
Function - некоторая последовательность операций, которую некая сущность выполнит.
Имя функции лучше не начинать с цифры

def name_fanction(argument):
	do smth
	return smth
если функция явно ничего не возвращает, то вернется None
вызов функции
name_fanction()

Для документации используют многострочный комментарий в двойных кавычках

После объявления функции документация доступна через атрибут __doc__:
name_fanction.__doc__() или help()
'''

def min(x,y):
	return x if x < y else y

min(3, -2)
#-2
min(x=2, y=10)
#2

'''
позиционне переменные (1, 3, 5) - f(*args) - tuple
ключевые переменные (х = 1, у = 10) - f(**kwargs) - dictionary
'''
def min(*args):
    res = float('inf')#плюс бесконечность - больше всех чисел
    for arg in args:
	if arg < res:
	    res = arg
    return res
'''
* вызов - распаковывает аргументы
* при объявлении значений - упакоывает
c ** аналогично
не делать изменяемые типы данных в объявлении ключевых аргументов, лучше неизменяемые
'''
def test(**kwargs):
	print(kwargs)

	
test(a = 1)
#{'a': 1}
ttt={'a':1, 'c':4}
test(ttt)
'''Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    test(ttt)
TypeError: test() takes 0 positional arguments but 1 was given'''
test(**ttt)
#{'a': 1, 'c': 4}

ttt = [(1,2),(1,2),(1,2),(1,2),(1,2)]
*rest, last = ttt
last
#(1, 2)
*rest,(a,b) = ttt
a
#1
b
#2
a = [(1,2),[(1,2),(1,2,3,4,5,6,7,8)]]
*_, (*rest, (*restt,last))=a
last
#8
#HW - ем отличается распаковка кортежа от распаковки списка
def func(*args, **kwargs):
	print(args, kwargs)
func(1, 2, boo=24, *[3, 4], foo="bar", *[5], **{"baz": 42})
#(1, 2, 3, 4, 5) {'boo': 24, 'foo': 'bar', 'baz': 42}

def wrapper():
    def inner(x):
        return x
    return inner

f = wrapper()
f(42)

'''
LEGB:
L - local
E - enclosing (что-то на уровень выше)
G - global
B - builtin
ищет от L к B
'''
'''
Функц.программирование:
1. лямбда lambda get: recive
2.карирование - в одной функции много дрругих
'''
x = lambda y:y
x(1)
#1

x = map(lambda x,y,z: x+y+z, [1,2], [3,4,5], range(550))
list(x)
#[4, 7]
#list(filter(None, input_list)) - будет преобразоывать к булево
[что делаем с элементом for условие]
