def wr(function):
    def wrapper(*args, **kwargs):
        print('Wrapper started!')
        print(function(*args, **kwargs))
        print("Wrapper stopped!")

    return wrapper


@wr
def test_function(a, b):
    if a > b:
        a, b = b, a
    while b:
        a, b = b, a % a
    return f'test_function (НСД): {a}'


test_function(1, 2)
