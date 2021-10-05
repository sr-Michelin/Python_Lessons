import sqlite3
import pandas as pd

with sqlite3.connect('interview.db') as con:
    cursor = con.cursor()

    # Дублікати

    cursor.execute("""CREATE TABLE IF NOT EXISTS train(
    id INT AUTO INCREMENT PRIMARY KEY,
    name TEXT, 
    age INT CHECK(age >= 18),
    salary INT DEFAULT 5000);""")

    # cursor.execute("""DELETE FROM train""")
    # cursor.execute("""DROP TABLE train""")

    # cursor.execute("""INSERT INTO train(id ,name, age, salary)
    # VALUES (1, 'David', 45, 25000), (2,'Mike', 22, 5000)""")

    # cursor.execute("""DELETE FROM train WHERE id IS null""")

    cursor.execute("""SELECT name, count(*) AS CNT
    FROM train 
    GROUP BY name, age, salary
    HAVING CNT > 1;""")

    print(cursor.fetchall())

    cursor.execute("""DELETE FROM train WHERE id NOT IN (SELECT MIN(id) FROM train GROUP BY name, age, salary)""")

print('\n', pd.read_sql("""SELECT * FROM train""", con=sqlite3.connect('interview.db')))
