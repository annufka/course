import functools


# декоратор
def lru_cache(max_size = 64):
    def deco(user_func):
        @functools.wraps(user_func)
        cache = {}
        def inner(key):
            if key not in cache:
                if len(cache) < max_size:
                    result = user_func(key)

                    cache[key] =

            return user_func(key)
        return inner
    return deco