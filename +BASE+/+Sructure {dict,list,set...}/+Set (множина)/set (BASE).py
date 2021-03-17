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
# --------------------------------
x2.remove(66)  # Видаляє вказаний елемент
# --------------------------------
x2.add(66)  # Додає вказаний елемент
# --------------------------------
x2.discard(66)  # Видаляє вказаний елемент, якщо він присутній у множині
# (на відміну від remove не видає помилок при відсутності вказаного елемента )
# --------------------------------
x2.pop()  # Видаляє рандомний (перший) елемент
# --------------------------------
x2.difference(x2)  # видає множиину - різицю між двома множинами
x2.difference_update(x2)  # видаляє цю різницю
# --------------------------------
x2.intersection(x1)  # видає нову множину, яка складається із елементів, що воодночас присутні у двох множинах
x2.intersection_update(x1)  # залишає у множині x2 дані елементи
# --------------------------------
x2.isdisjoint(x1)  # True, якщо дві множини немають спільних елементів
# --------------------------------
x2.issubset(x1)  # True, якщо множина x2 є еквіваленим х1, або є його підмножиною
# --------------------------------
x2.issuperset(x1)  # True, якщо множина x2 є еквіваленим х1, або є його надмножиною
# --------------------------------
x2.symmetric_difference(x1)  # видає нову множину, яка складається із елементів цих двох множин, окрім таких,
# які присутні у множинах воодночас
x2.symmetric_difference_update(x1)  # записує у множину x2 результат строгої диз\'юнкції двох множин (див. вище)
# --------------------------------
x2.union(x1)  # видає нову множину, яка включає усі елементи множини x2, а також усі із x1, що відсутні у x2
# --------------------------------
x2.update(x1) # доповнює множину x2 множиною x1
# --------------------------------
x2.clear()  # Очищує множину
print(x2)