class ToDict:
    def __init__(self, *args, **kwargs):
        print("Dict is tested...")

    def __call__(self, *args, **kwargs):
        return kwargs.values()


test_d = {
    "id": [1, 2, 3],
    "name": ["Сергей", "Федор", "Иван"],
    "old": [35, 23, 43],
    "salary": [130000, 100000, 120000]
}

print([_ for _ in ToDict()(**test_d)])
