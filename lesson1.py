'''Advantages:
1. simple
2. dinamic interpratation
3. a lot interpratator(cython, jython, pypy, ironpython...)'''

a = 3
type(a)
#<class 'int'>

a = 'a'
type(a)
#<class 'str'>

type(type(a))
#<class 'type'>

dir(str)
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#вернет методы

help(int)
#вернет методы, как их использовать и примеры
'''
не забывать отступы, но лучше не табуляциями, а пробелами, т.к. разные интерпретаторы могут по-разному воспринимать табуляцию
'''

'''тип данных:
1. None - неизменяемые'''
if a is None:
    print('None')
else:
    print(a)

'''
2. Bool - неизменяемые:
True
False
Операции:
or (смотрит слева, поєтому если слева Ложь, то выражение Ложь. Если слева Истина, то Истина)
and
not

3. Числа (Numerical) - неизменяемый тип (добавляется новое число с новым значением)
int, float, complex

4. Str - неизменяемый тип
len() - длина
bar[0]- берем элемент по индексу
*10 - повторение строчного элемента 10 раз
b'foo' - кодирование строки в байткод
u'foo' - кодироание строки в юникод
и т.д.

5. Списки (lisr) - изменяемый тип (остается старая переменная)
arr != list
можно использовать то же, что и к строке
.append()-добавляет вконец
.pop() - удаляет по индексу
s[0] == - можно заменить элемент по индексу
'''
#конкатенация
sl = [1, 2, 3]
sl + [5]
#[1, 2, 3, 5]

','.join(['foo','bar']) #объединить

'''Срезы (slices) - работает одинаково для строк и списков
sl[:] - опирование списка, для того чтобы изменить родительский список
[_:_:_]начало, конец, шаг
'''

'''
6. Кортеж (Tuple) - неизменяемый список, контейнер для чего-либо. Нам надо вернуть что-ибо не меняя

7. Множество (Set) - изменяемый тип данных, хэш-сеты (набор ключей)
.add() - добавить вконец
.discard() - убрать элемент со значением
'''

x={1,2,3,4}
y={4,5}
x.intersection(y)
#{4}
x&y
#{4}
x.union(y)
#{1, 2, 3, 4, 5}
x|y
#{1, 2, 3, 4, 5}
x.difference(y)
#{1, 2, 3}
x-y
#{1, 2, 3}

'''
8. Словарь (Dictionary) - хеш-таблица. Изменяемые. Можно брать по ключу, можно брать по элементу

Хэш-таблица - нет одинаковых ключей у двух элементов
'''
hash('ahgh')
# -2077073543

'''
If statements

if
elif
else

тернарный оператор:
'''
'even' if x%2 == 0 else 'odd'
вернуть 'even', если x%2 == 0, иначе вернем 'odd'

'''
While, for
While - циклически повторяется
for - перебирает коллекции, файлы и любые и другие последовательности

break - прекратить цикл
continue - беру след.шиг и возвращаюсь к началу цикла

while можно использовать с else, но это плохо

range sequence - lazy
'''
list(range(0,5,2))
#[0, 2, 4]

#reversed - перечисляет элементы в обратном порядке, lazy
list(reversed([1,2,3]))
#[3, 2, 1]

#DRY - don`t repeat yourself
from __future__ import braces
#SyntaxError: not a chance
import this
#The Zen of Python
import antigravity

#PEP8 - дз







