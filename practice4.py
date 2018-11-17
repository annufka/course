#1
import functools
import time


def timethis(our_function):
    @functools.wraps(our_function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = our_function(*args, **kwargs)
        end = time.time()
        return "result {}, time {}".format(result, end - start)
    return wrapper


@timethis
def dummy(*args):
    time.sleep(1)
    return args


print(dummy('h2bjblkjbl'))


#2
import functools
import time
import datetime

def logger(file_name):
    def deco(func):
        """
        log_format = "{timestamp}"\
        "function_name = {func.__name__}"

        file.write(log_format.format(timestamp, func.__name__))
        """
        @functools.wraps(func)
        def inner(*args, **kwargs):
            timestamp = datetime.datetime.now()
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            file = open(file_name, 'a')
            file.write('date {}, name {}, result{}, time {}\n'.format(timestamp, func.__name__, result, end-start))
            file.close()
            return result
        return inner
    return deco


@logger('text.txt')
def dummy(*args):
    time.sleep(1)
    return args


for i in range(5):
    print(i)
    dummy(i)


#3
import functools
import time
import datetime

def logger(file_name):
    def deco(func):
        file_mode = 'a'
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            file = open(file_name, file_mode)
            file.write('\n{}'.format(result))
            file.close()
            return result
        return inner
    return deco

def lru_cache(max_size):
    cache: dict = {}
    hits = misses = 0

    def deco(user_func):
        @functools.wraps(user_func)
        def inner(*arg_func, **kwargs):
            result = user_func(*arg_func, **kwargs)
            key = arg_func + tuple(sorted(kwargs.items()))
            nonlocal cache, misses, hits
            if cache.get(key):
                hits += 1
                cache[key]['time'] = time.time()
            else:
                if len(cache) < max_size:
                    cache[key] = {'result': result, 'time': time.time()}
                    misses += 1
                elif len(cache) >= max_size:
                    dict_for_max = {}
                    for item in cache:
                        dict_for_max[item] = cache.get(item).get('time')
                    del_key = max([key_for_del for key_for_del, value_for_del in dict_for_max.items() if
                                   value_for_del == max(dict_for_max.values())])
                    del cache[del_key]
                    cache[key] = {'result': result, 'time': time.time()}
                    misses += 1

            return cache[key]['result']
        @logger('text.txt')
        def info():
            nonlocal hits, misses, cache, max_size
            return 'hits: {}, misses: {}, size: {}, max_size: {}'.format(hits, misses, len(cache), max_size)



        def clear():
            nonlocal hits, misses
            cache.clear()
            hits = 0
            misses = 0

        inner.clear = clear
        inner.info = info
        inner.cache = cache
        return inner

    return deco


@lru_cache(max_size=6)
def fib(n) -> int:
    """
    the Fibonacci Sequence
    """
    if n < 2:
        time.sleep(0.005)
        return n
    return fib(n - 1) + fib(n - 2)


fib(10)
fib.info()

#4
def is_ascii(text):
    element_ascii = 0
    for index in range(len(text)):
        if ord(text[index]) <= 256:
            element_ascii += 1
    if element_ascii == len(text):
        return True
    return False


print(is_ascii('tykgj,'))
print(is_ascii('tyы'))

#5
def is_ascii(text):
    return text.isascii()

#6 доделать
import string


def is_ascii(text):
    all(map(lambda x: True if x in string.ascii_letters or string.punctuation or string.digits else False, text))


is_ascii('ygyjsі')

#7
import functools
import time
import datetime


def logger(file_name):
    def deco(func):
        file_mode = 'a'
        @functools.wraps(func)
        def inner(*args, **kwargs):
            timestamp = datetime.datetime.now()
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            file = open(file_name, file_mode)
            file.write('\n\ndate: {}, \nname: {}, \nresult: {}, \ntime: {}'.format(timestamp, func.__name__, result, end-start))
            file.close()
            return result
        return inner
    return deco

def timethis(our_function):
    @functools.wraps(our_function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = our_function(*args, **kwargs)
        end = time.time()
        return "result {}, time {}".format(result, end - start)
    return wrapper

def pre(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)
        return inner
    return wrapper

@pre(lambda x: x.isascii() == True, "I don`t know what do you want")
@timethis
@logger('text.txt')
def get_query_params(url):
    word_1, symbol, words_i_need = url.partition('/?')
    words = words_i_need.split('&')
    result = {}
    for index in range(len(words)):
        key, symbol, value = words[index].partition('=')
        result[key] = value
    time.sleep(0.005)
    return result

get_query_params('gk/?t1=1&t2=2&t3=3')
get_query_params('gыk/?t1=1&t2=2&t3=3')
