# Опрацювання виключень через ООП
# Вводячи "Exception" замість якоїсь конкретної, можна автоматично отримати виключення під помилку

try:
    print(1. / 0.)
except Exception as e:
    print(e)


class Exception_Print(Exception):
    """Загальний клас власних виключень"""
    pass


class Print_sent_data(Exception_Print):
    """Конкретний клас власних виключень"""

    def __init__(self, *args):
        super().__init__(*args)
        self.msg = args[0] if args else None

    def __str__(self):
        return f'Помилка: {self.msg}'


class Print_Data:
    def print(self, data):
        self.send_data(data)
        print(f'print: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Print_sent_data('Принтеер не відповідає на запит!')

    @staticmethod
    def send_to_print(data):
        return False


p = Print_Data()
try:
    p.print('123')
except Print_sent_data as pr:
    print(pr)
except Exception_Print:
    print('Помилка друку!')
