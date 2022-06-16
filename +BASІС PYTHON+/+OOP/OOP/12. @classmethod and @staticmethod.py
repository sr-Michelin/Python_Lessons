# Чим відрізняються методи, означені за допомогою декораторів "@classmethod" і "@staticmethod"?
class Vector:
    min_cord = 0
    max_cord = 100

    def set_cord(self, x=0, y=0):
        """Може працювати із іншими методами класу, так із атрибутами класу (із змінними, наприклад),
        а також із атрибутами і методами екзеипляра класу;

        Використовуєтья для роботи із методами і атрибутами класу та його екземплярів, а також із іншими класами
        """
        if Vector.validate(x) and Vector.validate(y):
            self.x, self.y = x, y

    def get_cords(self):
        """Геттер"""
        if Vector.validate(self.x) and Vector.validate(self.y):
            print(f"{self.x, self.y = }")

    @classmethod
    def validate(cls, arg):
        """Метод із "@classmethod" має доступ до атрибутів та методів тільки поточного класу;
        'cls' == Vector посилається на сам поточний клас (можна викликати інші стат методи та атрибути),
        а не на методи і атрибути екземпляра класу (відсутнє посилання на екземпляр -- 'self')

        Використовуєтья для роботи тільки із атрибутами і методами поточного класу
        """
        if cls.min_cord <= arg <= cls.max_cord:
            """Перевірка входження у проміжок (min_cord, max_cord)"""
            return True
        return False

    @staticmethod
    def norm2(x, y):
        """Метод із "@classmethod" є ізольованим від властивостів та методів поточного класу,
        а також від властивостей екземпляру класу (проста внутрішня ф-ція для локальних потреб класу)

        Використовуєтья для роботи із методом, викликаним із класу без доступу до його атрбутів (без "self", ясна річ)
        """
        return x * x + y * y

    def __del__(self):
        print(f'Видалення екземпляру {self.__str__()}')


v = Vector()
v.set_cord(1, 1)
v.get_cords()
