import sqlite3

DL = [
    ['2009-11-01', '111111', 'UA', '0', '2', '2446', 'UAH', '29,25'],
    ['2022-01-14', '111112', 'USA', '1', '1', '100', 'USD', '1'],
    ['2022-03-20', '111114', 'USA', '1', '1', '200', 'USD', '1'],
    ['2022-07-14', '111157', 'PL', '1', '2', '1442', 'EUR', '1'],
    ['2012-05-20', '111113', 'Gb', '0', '1', '213', 'GBR', '1,18'],
    ['2008-01-24', '111115', 'CA', '1', '2', '111', 'CAD', '0,76'],
    ['2008-01-24', '111111', 'UA', '1', '1', '111', 'UAH', '29,25'],
    ['2022-01-24', '111117', 'MX', '0', '1', '111', 'MXN', '0,048'],
    ['2022-04-30', '111118', 'MX', '1', '1', '447', 'MXN', '0,048'],
    ['2022-04-30', '111118', 'MX', '1', '1', '447', 'MXN', '0,048'],
    ['2022-02-30', '111118', 'IRL', '1', '1', '114', 'MXN', '1'],
    ['2022-04-30', '111120', 'IRL', '1', '2', '114', 'MXN', '1'],
]


class SQL:
    def __init__(self):
        print("Database created...")
        with sqlite3.connect('data.db') as con:
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS train('
                           'Date DATE,'
                           'userId INT,'
                           'Country VARCHAR(3),'
                           'TestType INT CHECK (TestType BETWEEN 0 AND 1),'
                           'TransactionStatus INT CHECK (TransactionStatus BETWEEN 1 AND 2),'
                           'PriceAmount FLOAT,'
                           'PriceCurrency VARCHAR(3),'
                           'ExchangeCurrencyRate FLOAT'
                           ');""")

    @staticmethod
    def del_db():
        with sqlite3.connect('data.db') as con:
            cursor = con.cursor()
            cursor.execute("""DELETE FROM train;""")

    @staticmethod
    def insert_db(data: list):
        with sqlite3.connect("data.db") as con:
            cursor = con.cursor()
            for item in data:
                cursor.execute("""INSERT INTO train VALUES (?,?,?,?,?,?,?,?);""", item)
                con.commit()

    @staticmethod
    def task_1():
        with sqlite3.connect("data.db") as con:
            cursor = con.cursor()
            cursor.execute(
                """SELECT Country, count(userId) FROM train 
                GROUP BY Country 
                HAVING TestType=1 AND Date BETWEEN "2022-01-01" AND "2022-04-30";""")
            print(cursor.fetchall())


task_1 = SQL.task_1()

