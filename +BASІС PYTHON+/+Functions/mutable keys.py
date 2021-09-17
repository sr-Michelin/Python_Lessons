def func(*value, lst=[]):
    """При створенні екземпляра ф-ції, йоого значення доповнюють список lst.
    Корисно для лічильників та тимчасових баз даних"""

    for v in value:
        lst.append(v)

    return lst


f = func(1, 2)
f = func(3, 4, 'f')

print(f)


# --------------------------------------------------


def gis(dict_=dict(), **dc):
    for k, v in dc.items():
        dict_.update({k: v})

    return dict_


g0 = gis(a='1', b='2', c='3')
g0 |= gis(d='4', )
g0 = gis(e='5')
print(g0)
