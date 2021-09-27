import sqlite3 as sq

import matplotlib.pyplot as plt
import pandas as pd

with sq.connect('data.db') as con:
    cur = con.cursor()

    # cur.execute("""CREATE TABLE if not exists users(
    # name TEXT,
    # sex INT,
    # age INT,
    # score INT
    # )""")

    cur.execute("""SELECT * FROM users""")
    # result = cur.fetchall()
    # result = cur.fetchmany(2)

    # result = cur.fetchone()
    # print(result)


df = pd.read_sql(sql='SELECT * FROM users WHERE score > 0', con=sq.connect('data.db'))
print(df)
