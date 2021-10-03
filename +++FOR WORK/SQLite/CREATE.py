import sqlite3
import pandas as pd

with sqlite3.connect('data.db') as con:
    curs = con.cursor()

    # Створення таблиці
    curs.execute('CREATE TABLE IF NOT EXISTS train('
                 'id INT PRIMARY KEY AUTOINCREMENT,'
                 'name TEXT NOT NULL,'
                 'course INT NOT NULL CHECK (course BETWEEN 0 AND 6));')

    # Введення даних
    # curs.execute('INSERT INTO train(id, name, course) VALUES(9, "Kata", 5)')

    # Видалення даних
    curs.execute('DELETE FROM train WHERE id IS Null;')

    # Вивід запиту у консоль
    curs.execute('SELECT DISTINCT * FROM train;')
    print("DISTINCT: ",curs.fetchall())

    # Агрегування ф-ціями для чиселних колонок
    curs.execute('SELECT avg(id) AS avg_id, avg(course) AS avg_c FROM train')
    print("Aggregate: ",curs.fetchall())

    # Виділення певних строк
    curs.execute('SELECT * FROM train LIMIT 3')
    print("LIMIT: ", curs.fetchall())

    # SELECT DISTINCT [columns] - вивід унікальних значень таблиці

    # WHERE [condition] - умова виводу
    # GROUP BY [column] - групування записів у таблиці (під час виводу)
    # ORDER BY [column] ASC|DESC - сортування за колонкою(-ами) у напрямку зростання чи спадання

    # Оновлення існуючих записів у таблиці з первною умовою (без неї усі записи стануть одинаковими)
    curs.execute('UPDATE train SET name = "Mike Sh" WHERE name = "Mike"')

    # LIKE Operator - пошук спеціальних символів та їх косбінацій у текстах колонок
    # 'a%' - start with "a"
    # '%a' - end with "a"
    # '%or%' - have "or" in any position
    # '_r%' - have "r" in the second position
    # 'a_%' - start with "a" and are at least 2 characters in length
    # 'a%o' - start with "a" and ends with "o"
    curs.execute('SELECT name FROM train WHERE name LIKE "M%h";')
    print("LIKE: ",curs.fetchall())

    # -----------------------------------------------------------------------------------------------------------------
    # Вивід через бібліотеку Pandas
    p = pd.read_sql('SELECT * FROM train ORDER BY course DESC', con=sqlite3.connect('data.db'))
    print('\n', p)

    p = pd.read_sql('SELECT COUNT(id) AS count, avg(id) AS avg_id, avg(course) AS avg_c FROM train',
                    con=sqlite3.connect('data.db'))
    print('\n', p)
