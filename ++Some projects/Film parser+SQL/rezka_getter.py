import sqlite3
import pandas as pd
import random

# ['title', 'year', 'country', 'genre', 'rate', 'link', 'photo']

with sqlite3.connect('rezka.db') as con:
    p = pd.read_sql(sql='SELECT * FROM best', con=con)
    print(p.pivot_table(['title', 'rate'], ['genre'], aggfunc='max'))
    print('\n',p[p['title'] == 'Интерстеллар'].T)
