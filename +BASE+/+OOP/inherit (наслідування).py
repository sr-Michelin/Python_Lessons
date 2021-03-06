# Наследование подразумевает то, что дочерний класс содержит все атрибуты родительского класса,
# при этом некоторые из них могут быть переопределены или добавлены в дочернем.

class Mydict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


a = dict(a=1, b=2)
b = Mydict(a=1, b=2)

print('\t', a, b, '\n')


# -----------------------------------------------------------------

class uni_Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('Створений uni_Member: {0}'.format(self.name))

    def tell_about_myself(self):
        # Вивід інформації
        print('І\'мя: {0}. Вік: {1}.'.format(self.name, self.age), end=' ')


class Teacher(uni_Member):
    def __init__(self, name, age, salary):
        uni_Member.__init__(self, name, age)
        self.salary = salary
        print('Створений викладач: {0}'.format(self.name))

    def tell_about_myself(self):
        uni_Member.tell_about_myself(self)
        print('Зарплата: {0:d}.'.format(self.salary))


class Student(uni_Member):
    def __init__(self, name, age, course):
        uni_Member.__init__(self, name, age)
        self.course = course
        print('Створений студень: {0}'.format(self.name))

    def tell_about_myself(self):
        uni_Member.tell_about_myself(self)
        print('Курс {0:d}.'.format(self.course))


t1 = Teacher('Юрій Степанович Криницький', 40, 20000)
s1 = Student('Михайло Сергійович Шевченко', 22, 5)

print()

members = [t1, s1]
for member in members:
    member.tell_about_myself()
