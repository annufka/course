# 1
import functools


def pre(cond, message):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper

    return deco


def sqrt(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return inner


@sqrt
@pre(lambda x: isinstance(x, int), "not intanger")
def dummy(num):
    return num


print(dummy(2))

#2
'''
test_l = lambda *args: all([isinstance(num, int) for num in args])
print(test_l(*range(10)))

list(map(lambda x: x ** 2, range(10)))
'''

def pre(cond, message):  # декоратор пре
    def deco(func):  # декоратор sqrt
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # сама функция
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper

    return deco


def sqrt(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return list(map(lambda x: x ** 2, func(*args, **kwargs)))

    return inner


@sqrt
@pre(lambda x: isinstance(x, int), "not intanger")
def dummy(num):
    return num


print(dummy(2))



# 3
def pre(cond, message):  # декоратор пре
    def deco(func):  # декоратор sqrt
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # сама функция
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper

    return deco


def last_call(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.last_call = args, kwargs
        return func(*args, **kwargs)

    inner.last_call = 'not called'
    return inner


def sqrt(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return list(map(lambda x: x ** 2, func(*args, **kwargs)))

    return inner


@last_call
@sqrt
@pre(lambda x: isinstance(x, int), "not intanger")
def dummy(num):
    return num


print(dummy(2))
print(dummy.last_call)

#4
def pre(cond, message):  # декоратор пре
    def deco(func):  # декоратор sqrt
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # сама функция
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper

    return deco


def last_call(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.last_args = args
        return func(*args, **kwargs)
    def last_call():
        return f"last {inner.last_args}"
    inner.last_args = 'not called'
    inner.last_call = last_call
    return inner


def sqrt(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return list(map(lambda x: x ** 2, func(*args, **kwargs)))

    return inner


@last_call
@sqrt
@pre(lambda x: isinstance(x, int), "not intanger")
def dummy(num):
    return num


print(dummy(2))
print(dummy.last_call())
