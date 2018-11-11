"""
Декоратор —функция, которая принимает другую функцию и что-то возвращает.
@name
либо
foo = name(foo)
подмена нашей функции
"""
'''
def trace(func):#берем функцию
    def inner(*args, **kwargs):#принимает ключевые и позиционные элементы нашей функции
        ...
        return func(*args, **kwargs)#возвращаем нашу функцию
    return inner
'''
"""
если мы добавляем декоратору переменную, то мы добавляем вложенность
"""

def humb(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
    
@humb
def beef():
    return 'beef'

beef()
#'beef'
beef.__name__
#'wrapper'
import functools
def humb(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		result = "bread {} bread"
		return result.format(func(*args, **kwargs))
	return wrapper

def humb(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		result = "bread {} bread"
		return result.format(func(*args, **kwargs))
	return wrapper

def humb(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		result = "bread {} bread"
		wrapper.ncalls += 1
		return result.format(func(*args, **kwargs))
	wrapper.ncalls = 0
	return wrapper

def test_funk_1(x):
    return 'blablabla'

def test_funk_2(x):
    return x

test_funk_1.__code__=test_funk_2.__code__
test_funk_1(42)
#42

