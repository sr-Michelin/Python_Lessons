class Descr:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del self.__value


class D:
    cordX, cordY = Descr(), Descr()

    def __init__(self, x=0, y=0):
        self.cordX, self.cordY = x, y


d = D(1, 1)
d.cordX, d.cordY = 2, 2
print(f'{d.cordX, d.cordY = }')
