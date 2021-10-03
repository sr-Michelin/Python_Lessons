import sqlite3 as sq
import pandas as pd

with sq.connect('data.db') as con:
    cur = con.cursor()

    '''cur.execute("""CREATE TABLE if not exists users(
    name TEXT,
    sex INT,
    age INT,
    score INT)""")'''

    # cur.execute("""INSERT INTO users(name, sex, age, score) VALUES("Mike Shevchenko", "Male", 23, 1770)""")
    # cur.execute("""SELECT DISTINCT * FROM users""")

    # cur.execute("""SELECT * FROM users""")
    # result = cur.fetchall()
    # result = cur.fetchmany(2)
    # result = cur.fetchone()

    # print(result)

df = pd.read_sql(sql='SELECT * FROM users WHERE score > 0', con=sq.connect('data.db'))
# df.drop_duplicates(inplace=True)

for i in range(len(df) - 1):
    if df.name[i] == df.name[i+1]:
        df.drop(index=i, inplace=True)
    else:
        df.index[i] = 0

print('\n', df)
