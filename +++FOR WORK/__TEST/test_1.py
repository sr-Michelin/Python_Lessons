import time


def time_check(func):
    def wrapper(*args, **kwargs):
        st = time.time_ns()
        func(*args, **kwargs)
        print(f'Time spend: {(time.time_ns() - st) / pow(10, 9)} s')
        return func

    return wrapper


@time_check
def slow_euclid(a, b):
    while a != b:
        if a > b:
            a -= b
        if a < b:
            b -= a
    print(f'slow НСД = {a}')
    return a


@time_check
def fast_euclid(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % 2
    print(f'fast НСД = {a}')
    return a


digits = 2, 100000000

slow_euclid(*digits)
fast_euclid(*digits)
