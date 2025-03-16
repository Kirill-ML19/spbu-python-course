from functools import wraps
from typing import OrderedDict


def cached(max_size=None):
    """
    Decorator for caching function results.

    Caches the results of executing a function based on the arguments passed.
    If a function is called with the same arguments multiple times, the result
    will be taken from the cache, which speeds up execution.

    Args:
        max_size (int, optional):
            Maximum size of the cache. If None, the cache is unlimited. If specified, the oldest items are removed when the cache size is exceeded.

    Returns:
        Callable:
            Decorated function with caching support.
    """

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            if max_size is not None:
                if len(cache) >= max_size:
                    cache.popitem(last=False)
                cache[key] = result
            return result

        return wrapper

    return decorator
