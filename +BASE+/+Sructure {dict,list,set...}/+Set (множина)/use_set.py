# Множина - невпорядкований набір простих об'єктів
# Створена для пошуку пересічень, належності

# ---------------------Множина-------Set-------frozenset-------------in-------------len---------update------------
# Робота з множинами 'SET'
A = set("hello")  # задаємо множину
f = ['q', 'w', 'e', 'r', 't', 'u', 'u', 'q']  # не Set, а list
B = {'b1', 11}  # Теж Set
print(A, " ", B)
C = {i ** 2 for i in range(10)}  # запис через цикл for
print(type(C))  # Рандомний порядок виводу множини
print(C)

# --------------------------------
D = frozenset('Mike')  # 'Кортежний' (одноразовий) ввід множини
A.add(12)
B.add(13)
print(A, ' ', D)

# --------------------------------
print(set(f))  # Вивід списку f як множини (без повторень одинакових знаків)

# --------------------------------
print(len(f))  # Вивід довини списку f

# --------------------------------
x1 = 'q'
print(x1 in f)  # Показує, чи є 'x' у 'f'

# --------------------------------
x2 = {1, 12, 23, 44, 55, 66, 77, 88, 92, }
f2 = {9, 8, 7, 6, 5, 4, 3, 2, 1}
print(f2.isdisjoint(x2))  # Показує,чи немає  x2 у f2
f2.update(x2)
print(f2)  # Доповрює множину f2 множиною х2

# --------------------------------
x2.remove(66)
print(x2)  # Видаляє вказаний елемент

# --------------------------------
x2.add(66)
print(x2)  # Додає вказаний елемент

# --------------------------------
x2.discard(66)
print(
    x2)  # Видаляє вказаний елемент, якщо він присутній у множині
# (на відміну від remove не видає помилок при відсутності вказаного елемента )

# --------------------------------
x2.pop()
print(x2)  # Видаляє рандомний (перший) елемент

# --------------------------------
x2.clear()
print(x2)  # Очищує множину
