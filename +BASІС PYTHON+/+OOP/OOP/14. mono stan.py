# Паттерн моностану для екземплярів класу у ООП
# Багатопоковий процес із створенням екземплярів певного класу із спільними локальними властивостями
# (ex.__dict__ - спільний для усіх екземплярів)

class ThreadData:
    # __dict__ має посилатися тільки на словник
    __common_attrs = {
        'name': 'thread_data_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.new_attr = None
        self.id = None
        self.__dict__ = ThreadData.__common_attrs


th1 = ThreadData()
th2 = ThreadData()
th3 = ThreadData()
th4 = ThreadData()
th5 = ThreadData()

th = [th1, th2, th3, th4, th5]

# Введенний/створений атрибут стає спільним для усіх екземплярів класу "Thread_Data"
th1.id = 2
th1.new_attr = 'new_attr'

print([t.id for t in th], '-- присвоєний атрибут стає спільним')
print([t.new_attr for t in th], '-- створений атрибут присвоюється усім екземплярам')
print([id(t.__dict__) for t in th], '-- посилання на словник класу є повним')
