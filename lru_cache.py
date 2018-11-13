import functools
import collections


def lru_cache(max_size):
    cache = collections.OrderedDict()

    def deco(user_func):
        @functools.wraps(user_func)
        def inner(arg_func):
            result = user_func(arg_func)
            key = arg_func
            nonlocal cache
            if key not in cache:
                n = 1
                inner.misses += 1
                if len(cache) < max_size:
                    cache[key] = {'result': result, 'n': n}
                else:
                    cache.popitem()
                    cache[key] = {'result': result, 'n': n}
            else:
                inner.hits += 1
                cache.get(arg_func)
                n = cache[arg_func]['n']
                n += 1
                cache[arg_func]['n'] = n
            return user_func(arg_func)

        inner.hits = inner.misses = 0
        inner.clear = cache.clear()
        inner.cache = cache

        return inner

    return deco


@lru_cache(max_size=12)
def fib(n) -> int:
    """
    the Fibonacci Sequence
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


fib(4)
print(fib.hits)
print(fib.missed)
print(fib.cache)
