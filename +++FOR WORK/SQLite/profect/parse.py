from bs4 import BeautifulSoup
import requests
import sqlite3
import re


def parse(depth=5):
    page = 1

    # Проміжний результат (у майбутньому треба позбутися)
    result = []

    while True:

        # Ключове посилання
        url = f"https://rezka.ag/films/best/page/{page}/"

        # Клієнт
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95'
        }

        request = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(request.text, "html.parser")

        # HTML - результати
        films = soup.find_all("div", class_="b-content__inline_item-link")
        marks = soup.find_all("div", class_="b-content__inline_item-cover")

        # Перевірка умов пробігу сайту
        if page <= depth:
            for film, mark in zip(films, marks):
                # Блок первинних даних
                f = film.text.strip()
                m = re.split(pattern='[^0-9,.]',
                             string=mark.find('i',
                                              class_="b-category-bestrating rating-green-string").get_text(strip=1))[1]

                # Блок кінцевих даних
                name = f.split(',')[0][0:-5]
                year = [_ for _ in re.split(pattern='[^0-9]', string=f) if len(_) > 3][0]
                country = f.split(',')[1].strip()
                genre = f.split(',')[2].strip()

                result.append([name, year, country, genre, m])

            page += 1

        else:
            break

    return result


"""Запис у БД SQLite"""
try:
    with sqlite3.connect('films.db') as con:
        print('Database connected...')
        cursor = con.cursor()

        # Створення БД
        cursor.execute("""CREATE TABLE IF NOT EXISTS rezka(
        name VARCHAR(50),
        year INT,
        country VARCHAR(50),
        genre VARCHAR(50),
        mark FLOAT,
        Unique(name));""")

        # Огляд наявних записів у БД
        cursor.execute("""SELECT * FROM rezka""")

        Q = cursor.fetchall()
        q = [Q[i][0] for i in range(len(Q))]

        # Перевірка присутності майбутніх записів у списку існюючих
        for item in parse(depth=1):
            if not item[0] in q:
                cursor.execute("""INSERT INTO rezka VALUES (?,?,?,?,?)""", item)
                con.commit()


except Exception as ex:
    print(ex)

finally:
    print('\nConnection closed...')
    con.close()
