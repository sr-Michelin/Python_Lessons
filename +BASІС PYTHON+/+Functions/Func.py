s = 'Mike'
w = 'MMM'
print(s, w, sep="**", end="  ")
print(s.upper())  # Запис з капсом

print()
f = open('123.txt')
r = f.read()
print(r)

print()


def max(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Equal..'
    else:
        return y


print(max(10, 10))

print()


def nummax(x, y):
    """Something good"""

    x = int(x)
    y = int(y)

    if x > y:
        print('X - найбільше')
    elif x == y:
        print('X=Y')
    else:
        print('Y - найбільше')


print(nummax.__doc__)
nummax(10, 11)
