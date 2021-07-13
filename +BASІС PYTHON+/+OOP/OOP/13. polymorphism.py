# Можливість працювати із різними об\'єктами однаковим чином

class Rectangle:
    """Прямокутник"""

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per_rect(self):
        return 2 * (self.w + self.h)

    def get_per(self):
        """для реалізації поліморфізму"""
        return 2 * (self.w + self.h)


class Square:
    """Квадрат"""

    def __init__(self, a):
        self.a = a

    def get_per_sq(self):
        return 4 * self.a

    def get_per(self):
        """для реалізації поліморфізму"""
        return 4 * self.a


class Triangle:
    """Трикутник"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_per(self):
        """для реалізації поліморфізму"""
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(4, 5)
print(f'{r1.get_per_rect(), r2.get_per_rect() = }')

s1 = Square(10)
s2 = Square(20)
print(f'{s1.get_per_sq(), s2.get_per_sq() = }\n')

t1 = Triangle(1, 2, 3)
t2 = Triangle(3, 2, 1)

# Колекція geom та її перебір із дотриманнм isinstance:
geom = [r1, r2, s1, s2, t1, t2]


def collection(coll):
    """Негнучкий метод (без поліморфізму), захаращує код ялинками із "if", "elif": """
    print(collection.__doc__)
    c1 = [f'{c.get_per_rect() = }' for c in coll if isinstance(c, Rectangle)]
    c2 = [f'{c.get_per_sq() = }' for c in coll if isinstance(c, Square)]
    print(f'Через генератор:\n{",".join(c1 + c2)} \n\nАбо через цикл:')

    # або
    for c in coll:
        if isinstance(c, Rectangle):
            print(f'{c.get_per_rect() = }')
        elif isinstance(c, Square):
            print(f'{c.get_per_sq() = }')


collection(geom)


def collection_poly(coll):
    """\nМетод, застосований через поліморфізм:"""
    print(collection_poly.__doc__)
    c1 = [f'{c.get_per() = }' for c in coll]
    print(' , '.join(c1))


collection_poly(geom)
