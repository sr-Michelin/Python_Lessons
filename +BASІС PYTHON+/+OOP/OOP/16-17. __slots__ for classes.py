# "__slots__" задає обмеження на створення нових атрибутів класу,
# оптимізує пам'\ять, яку займає екземляр,
# прискорє роботу із локальними методами
import math
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
    f'(виграш у {round(timeit.timeit(pt1.calc) - timeit.timeit(pt2.calc), 4)}s)\n')


# "__slots__" із property
# length стає локальною властивістю
class Point2D:
    __slots__ = ('x', 'y', '__length')  # через кортеж

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = math.sqrt(x * x + y * y)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt = Point2D(1, 2)
print(f'{pt.length = }')  # тепер можливим є виклик методу length ("__slots__" блокує тільки атрибути, а не методи)


class Point3D(Point2D):
    """Дочірні класи не наслідують "__slots__" """
    __slots__ = 'z',  # решта у Point2D.__slots__

    def __init__(self, x, y, z):
        """Конструктор для трьох локальних елементів (два із Point2D)"""
        super().__init__(x, y)
        self.z = z


p3 = Point3D(1, 1, 1)
p3.z = 30  # можливість вносити нові атрибути у дочірний клас
# print(f'{p3.__dict__ = } -- словник дочірного класу, який містить атрибути, які не знаходяться у "__slots__"')
print(f'{p3.__slots__ = } -- самий "__slots__"\n')

# Із екземпляру дочірного класу можна видалити атрибути із "__slots__", а також їх добавляти (якщо є у "__slots__") :
del p3.x
p3.x = 100

print(f"{p3.x = }")
print(f'{p3.x, p3.y, p3.z = }')
# p3.d = 1 # введення нового атрибуту видасть AttributeError
