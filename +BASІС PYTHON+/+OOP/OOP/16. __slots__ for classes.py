# "__slots__" задає обмеження на створення нових атрибутів класу,
# оптимізує пам'\ять, яку займає екземляр,
# прискорє роботу із локальними методами
import timeit


class Point:
    """Займає більше пам\'яті, бо присутня колекція "__dict__" """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc(self):
        """Для демонстрації швидкості роботи без "__slots__" """
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    """Дозволенні тільки дві координати -- локальні атрибути"""
    __slots__ = ('x', 'y')  # через кортеж
    CONST = 10  # глобальний атрибут

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc(self):
        """Для демонстрації швидкості роботи із "__slots__" """
        self.x += 1
        del self.y
        self.y = 0


pt1 = Point(1, 1)
pt2 = Point2D(1, 1)
print(f'{pt2.x, pt2.y = }')

# видалення одного із атрибутів, вказаного у "__slots__" і його створення:
del pt2.x
pt2.x = 1
print(f'{pt2.x = }')

# вивід глобального атрибуту в обхід "__slots__"
print(f'{pt2.CONST = }')

# перевірка оптимізації:
print(f'\n{pt1.__sizeof__(), pt1.__dict__.__sizeof__() = }bit')
print(f"{pt2.__sizeof__() = }bit -- очевидна оптимізація по пам\'яті, бо колекція '__dict__' є відсутньою")

print(f'\n{timeit.timeit(pt1.calc) = }')
print(
    f'{timeit.timeit(pt2.calc) = } -- оптимізація оптимізація по часу '
    f'(виграш у {round(timeit.timeit(pt1.calc) - timeit.timeit(pt2.calc), 4)}s)')
