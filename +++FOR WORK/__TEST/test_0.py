from os import getlogin


class WB:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Welcome back, buddy {self.name.title()}!"


if __name__ == '__main__':
    print(WB(getlogin()))

