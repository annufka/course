import functools


def lru_cache(max_size):
    cache = {}

    def deco(user_func):
        @functools.wraps(user_func)
        def inner(*args, **kwargs):
            if key not in cache:
                if len(cache) < max_size:
                    result = user_func(*args, **kwargs)
                    n = 1
                    cache[args] = {'result': result, 'n': n}
            return user_func(*args, **kwargs)

        return inner

    return deco


@lru_cache(max_size=64)
def func(smth):
    return len(smth)


'''
def with_arguments(deco):
    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func
            return result
        return decorator
    return wrapper
'''
