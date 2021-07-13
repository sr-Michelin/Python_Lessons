# "dunder"-методи () "__str__", "__repr__", "__len__", "__abs__"
# "__str__()" - для відображення інформації про обєкт класу через "print()", "str" -- для користувачів
# "__repr__()" - для відображення інформації про обєкт класу у режимі відладки -- для програмістів

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """вивід парамтру обєкту;
        при відсутності "__str__()" виводиться першим """
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


cat = Cat('Мурзик')

print(cat, '-- вивід користувацький')  # вивід через "__str__" - користувацький спосіб


# cat # службовий вивід через "__repr__" -- Out[6]: <class '__main__.Cat'>: Мурзик

# "__len__()" - ф-ція len() для екземплярів класу
# "__abs__()" - ф-ція abs() для екземплярів класу


class Point:
    def __init__(self, *args):
        self.__cords = args

    def __len__(self):
        return len(self.__cords)

    def __abs__(self):
        return list(map(abs, self.__cords))


p = Point(1, 2, -3)

print(f'{len(p) = } -- довжина екземпляру, що складається із координат')
print(f'{abs(p) = } -- абсолютні координати (через модуль)')
