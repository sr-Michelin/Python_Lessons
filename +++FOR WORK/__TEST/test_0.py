from os import getlogin


class WB:
    def __init__(self, name: str):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __delete__(self, instance):
        del self.__name


class Test(WB):

    def __init__(self, name: str = 'Mike', *args, **kwargs):
        super().__init__(name)
        self.name = name

    def __str__(self):
        return f'Welcome to dungeon, buddy {self.name.title()}!'

    def __repr__(self):
        return f'Console tests, buddy {self.name.title()}!'


if __name__ == '__main__':
    print(Test(getlogin()))
    print(Test())
