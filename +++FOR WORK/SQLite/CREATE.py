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
    curs.execute('SELECT * FROM train;')
    print(curs.fetchall())

    # SELECT DISTINCT [columns] - вивід унікальних значень таблиці
    # WHERE [condition] - умова виводу
    # GROUP BY [column] - групування записів у таблиці (під час виводу)
    # ORDER BY [column] ASC|DESC - сортування за колонкою(-ами) у напрямку зростання чи спадання

    # -----------------------------------------------------------------------------------------------------------------
    # Вивід через бібліотеку Pandas
    p = pd.read_sql('SELECT * FROM train ORDER BY course DESC', con=sqlite3.connect('data.db'))
    print('\n', p.describe().T)
