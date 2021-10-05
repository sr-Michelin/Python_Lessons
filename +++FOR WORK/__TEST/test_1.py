import sqlite3
import pandas as pd

with sqlite3.connect('interview.db') as con:
    cursor = con.cursor()

    cursor.execute("""INSERT INTO train(id,name, age, salary) VALUES(1,'Mike', 22, 5000)""")

    cursor.execute("""DELETE FROM train 
    WHERE id NOT IN (SELECT MIN(ID) FROM train GROUP BY name, age, salary)
    OR id IS NULL;""")

print('\n', pd.read_sql(sql="""SELECT * FROM train""", con=sqlite3.connect('interview.db')))

