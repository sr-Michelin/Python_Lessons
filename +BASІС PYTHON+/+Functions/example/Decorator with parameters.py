from functools import wraps
from math import pi, sin


def decorator_param_0(dx=0.001):
    def decorator_func(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # Для збереження властивостей досліджувальної ф-ції
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator_func


def decorator_param(dx=0.001):
    def decorator_func(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # Для збереження властивостей досліджувальної ф-ції
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator_func


@decorator_param(dx=0.000001)
def sin_x(x):
    """Ф-ція для виводу похідної синуса"""
    return sin(x)


ds = sin_x(pi / 3)
print(ds)
print(sin_x.__name__, sin_x.__doc__, sep='\n')
