import functools


def lfu_cache(max_size):
    cache = {}
    hits = misses = 0

    def deco(user_func):
        @functools.wraps(user_func)
        def inner(args):
            key = args
            nonlocal cache
            if key not in cache:
                n = 1
                nonlocal misses
                misses += 1
                if len(cache) < max_size:
                    cache[key] = {'result': user_func(args), 'n': n}
                else:
                    cache_my = cache.copy()
                    cache.clear()
                    list_cache = list(cache_my)
                    list_cache = list_cache.sort(reverse=True)
                    list_cache = list_cache.pop()
                    for item in cache_my:
                        cache[item] = cache_my.get(item)
                    cache[key] = {'result': user_func(args), 'n': n}
            else:
                nonlocal hits
                hits += 1
                cache.get(args)
                n = cache[args]['n']
                n += 1
                cache[args]['n'] = n
            return cache[key]

        def info():
            nonlocal hits, misses, cache, max_size
            return ('hits: {}, misses: {}, size: {}, max_size: {}'.format(hits, misses, len(cache), max_size))

        def clear():
            nonlocal hits, misses
            cache.clear()
            hits = 0
            misses = 0
        inner.clear = clear
        
        inner.info = info
        return inner

    return deco


@lfu_cache(max_size=2)
def fib(n) -> int:
    """
    the Fibonacci Sequence
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


fib(3)
