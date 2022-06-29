Test_dict = {
    "tree": "дерево",
    "car": ['машина', 'автомобіль'],
    "leaf": 'лист',
    "river": 'річка',
    "go": ['йти', "ходити", "плестися", "лазити", "човгати", "прямувати", "чимчикувати"],
    "milk": "молоко"
}


class Translator:
    """Повторення та напрацювання роботи із локальним параметром "self". \nЛагідна українізація\n"""

    def __init__(self):
        self.tr = {}

    def add(self, eng: str, ua: [str, list]):
        """Добавлення нової ланки словника"""
        if 'tr' not in self.__dict__:
            pass
        self.tr.setdefault(eng, [])
        self.tr[eng].append(ua)

    def remove(self, eng: str):
        """Видалення деяких слів-ключів"""
        print(f"Видаляю {eng=}")
        self.tr.pop(eng, False)

    def translate(self, eng: str) -> str:
        """Повернення значення ключа-словника"""
        return self.tr[eng]


def d_t(e, dict_, world_rmv="", world_tr="") -> str:
    """Розбиття вхідного словника на ланки за кількістю значень та застосування логіки процесу"""
    for k, v in dict_.items():
        if isinstance(v, list):
            for _ in v:
                e.add(k, _)
        else:
            e.add(k, v)

    if world_rmv in dict_.keys():
        e.remove(world_rmv)
    else:
        pass

    if world_tr in dict_.keys():
        return f'Переклад "{world_tr}" - {e.translate(world_tr)}'
    else:
        return "Введене слово не входить у словник!"


tr1 = Translator()

if __name__ == '__main__':
    print(Translator.__doc__)
    # print(d_t(tr1, Test_dict))
    print(d_t(tr1, Test_dict, world_rmv='go', world_tr="car"))
    print(f"Словник після операцій: {tr1.tr}")
