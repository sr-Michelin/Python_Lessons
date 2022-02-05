class ShortInputException(Exception):
    def __init__(self, length, atleast):
        # Exception.__init__(self)
        super().__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Введіть щось: ')

    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except ShortInputException as ex:
    print(
        'ShortInputException: Длина введённой строки -- {0}; ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Все ок!')
