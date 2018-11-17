import functools


def lfu_cache(max_size):
    cache: dict = {}
    hits = misses = 0

    def deco(user_func):
        @functools.wraps(user_func)
        def inner(*arg_func, **kwargs):
            
            key = arg_func + tuple(sorted(kwargs.items()))
            nonlocal cache, misses, hits
            if cache.get(key):
                hits += 1
                cache[key]['n'] += 1
            else:
                result = user_func(*arg_func, **kwargs)
                if len(cache) < max_size:
                    cache[key] = {'result': result, 'n': 1}
                    misses += 1
                elif len(cache) >= max_size:
                    dict_for_min = {}
                    for item in cache:
                        dict_for_min[item] = cache.get(item).get('n')
                    del_key = min([key_for_del for key_for_del, value_for_del in dict_for_min.items() if
                                   value_for_del == min(dict_for_min.values())])
                    del cache[del_key]
                    cache[key] = {'result': result, 'n': 1}
                    misses += 1
            
            return cache[key]['result']

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


@lfu_cache(max_size=4)
def fib(n) -> int:
    """
    the Fibonacci Sequence
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


fib(8)
print(fib.info())
print(fib.cache)
