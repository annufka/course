#1
"""
list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6]))
[2, 4, 6]
"""
def filter(func, list_range):
    for item in list_range:
        if func(item):
            yield item
    
    
print(list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6])))


#2
def filter(func, list_range):
    func = func if func is not None else bool
    for item in list_range:
        if func(item):
            yield item
    
    
print(list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6])))
print(list(filter(None, [1, '', 3, 42, [], 0])))

#3
def enumerate(some_list):
    for letter in some_list:
        yield some_list.index(letter), letter
print(list(enumerate("abcd")))

#4
def enumerate(some_list):
    it = iter(some_list)    
    for index in range(len(some_list)):
        yield index, next(it)
print(list(enumerate("abcd")))

#5
def zip(*args):
    for num_in_range in range(len(args[0])):
        try:
            yield tuple(args[x][num_in_range] for x in range(len(args)))
        except:
            return
        
    
print(list(zip([1,4,1,6,1,7,9,2], "ahbxl")))
        

#5 
def zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, None)
            if elem is None:
                return
            result.append(elem)
        yield tuple(result)

zip([1,4,1,6,1,7,9,2], "ahbxl")

#6
import functools
def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res =func()
        next(res)
        return res
    return wrapper

@coroutine
def echo():
    while True:
        boo = yield
        if boo:
            print('{}...{}...{}'.format(boo, boo, boo))

echo = echo()
echo.send('boo')

#7
import functools
def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res
    return wrapper

@coroutine
def echo():
    while True:
        boo = yield
        if boo:
            print('{}...{}...{}'.format(boo, boo, boo))

@coroutine
def bar(target):
    yield from target()
    
b = bar(echo)
b.send("Boo")



