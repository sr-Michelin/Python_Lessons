import sqlite3
import pandas as pd

with sqlite3.connect('data.db') as con:
    curs = con.cursor()

    # Створення таблиці
    curs.execute('CREATE TABLE IF NOT EXISTS train('
                 'id INT PRIMARY KEY AUTOINCREMENT,'
                 'name TEXT NOT NULL,'
                 'course INT NOT NULL CHECK (course BETWEEN 0 AND 6));')

    # Створення таблиці ssh(стипендій)
    curs.execute('CREATE TABLE IF NOT EXISTS ssh('
                 'id INT AUTO INCREMENT PRIMARY KEY,'
                 'sh INT NOT NULL);')

    # Введення даних
    # curs.execute('INSERT INTO train(id, name, course) VALUES(9, "Kata", 5)')
    # curs.execute('INSERT INTO ssh(id, sh) VALUES(1, 1770), (2, 1770), (3, 0), (4, 0), (5,0), (6, 0), (7, 0)')

    # Видалення даних
    curs.execute('DELETE FROM train WHERE id IS Null;')

    # Вивід запиту у консоль
    curs.execute('SELECT DISTINCT * FROM train;')
    print("DISTINCT: ", curs.fetchall())

    # Агрегування ф-ціями для чиселних колонок
    curs.execute('SELECT avg(id) AS avg_id, avg(course) AS avg_c FROM train')
    print("Aggregate: ", curs.fetchall())

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
    print("LIKE: ", curs.fetchall())

    # IN Operator - як у Пітоні
    curs.execute('SELECT * FROM train WHERE name IN ("Mike Sh", "Taras", "Vanya")')
    print("IN: ", curs.fetchall())

    # JOINs - входження таблиць. Для троьох та більше працює вкладення.
    # # INNER JOIN - спільна область для двох таблиць
    curs.execute('SELECT train.name, train.course, ssh.sh FROM train INNER JOIN ssh ON train.id=ssh.id')
    print('INNER JOIN:', curs.fetchall())
    # # LEFT JOIN - повна ліва (зазначена першою) таблиця і співпадаючі дані із правої
    curs.execute('SELECT train.name, train.course, ssh.sh FROM train LEFT JOIN ssh ON train.id=ssh.id')
    print('LEFT JOIN:', curs.fetchall())
    # # RIGHT JOIN - повна права таблиця і співпадаючі дані із лівої
    # curs.execute('SELECT train.name, train.course, ssh.sh FROM train RIGHT JOIN ssh ON train.id=ssh.id')
    # print('RIGHT JOIN:', curs.fetchall())
    # # FULL JOIN - усі дані
    # curs.execute('SELECT train.name, train.course, ssh.sh FROM train FULL JOIN ssh ON train.id=ssh.id')
    # print('FULL JOIN:', curs.fetchall())

    # UNION - оператор поєднання вибірок
    curs.execute('SELECT COUNT(*) FROM train as CNT_tr UNION SELECT COUNT(*) FROM ssh as CNT_ssh')
    print('UNION:', curs.fetchall())

    #   -----------------------------------------------------------------------------------------------------------------
    # Вивід через бібліотеку Pandas
    print('\n', pd.read_sql('SELECT * FROM train ORDER BY course DESC', con=con))

    print('\n', pd.read_sql('SELECT COUNT(id) AS count, avg(id) AS avg_id, avg(course) AS avg_c FROM train', con=con))

    print('\n', pd.read_sql(sql='SELECT train.name, train.course, ssh.sh FROM train INNER JOIN ssh ON train.id=ssh.id',
                            con=con))

    print('\n', pd.read_sql(sql='SELECT COUNT(*) FROM train as CNT_tr UNION SELECT COUNT(*) FROM ssh as CNT_ssh',
                            con=con))
