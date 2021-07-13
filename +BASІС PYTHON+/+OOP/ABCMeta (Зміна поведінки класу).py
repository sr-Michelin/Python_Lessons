# Допустим, мы хотим быть уверены, что мы всегда создаём исключительно экземпляры подклассов
# класса SchoolMember,и не создаём экземпляры самого класса SchoolMember.
# Мы можем объявить наш класс как абстрактный базовый класс при помощи встроенного метакласса по имени ABCMeta
import datetime
import time
from abc import *


class uni_Member(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('Створений uni_Member: {0}'.format(self.name))

    @abstractmethod  # abc
    def tell_about_myself(self):
        # Вивід інформації
        print('І\'мя: {0}, вік: {1},'.format(self.name, self.age), end=' ')


class Teacher(uni_Member):
    def __init__(self, name, age, salary):
        uni_Member.__init__(self, name, age)
        self.salary = salary
        print('Створений викладач: {0}'.format(self.name))

    def tell_about_myself(self):
        uni_Member.tell_about_myself(self)
        print('Зарплата: {0}.'.format(self.salary))


class Student(uni_Member):
    def __init__(self, name, age, course):
        uni_Member.__init__(self, name, age)
        self.course = course
        print('Створений студень: {0}'.format(self.name))

    def tell_about_myself(self):
        uni_Member.tell_about_myself(self)
        print('Курс {0}.'.format(self.course))


class I_(uni_Member):
    """Запис через "super()": """

    def __init__(self, name, age, s_, mark, hobby):
        self.s = s_
        self.mark = mark
        self.hobby = hobby
        super().__init__(name, age)
        print(I_.__doc__)
        print('Створений солдат: {0}'.format(self.name))

    def tell_about_myself(self):
        uni_Member.tell_about_myself(self)
        print('рід військ: {0}, звання: {1}, хоббі: {2}.'.format(self.s, self.mark, self.hobby))

    def __del__(self):
        print(f'Солдат {self.name} відкосив по причині "__ще_у_процесі__".')


t = Teacher('Юрій Степанович Криницький', 45, 40000)
t1 = Teacher('Володимир Михайлович Ткачук', 47, 41000)
s = Student('Михайло Сергійович Шевченко', 22, 5)

print()

members = [t, t1, s]
for member in members:
    member.tell_about_myself()

print()
I_('Міша', time.localtime().tm_year - 1998, 'стройбат', 'рядовий', '"Data Science"').tell_about_myself()
