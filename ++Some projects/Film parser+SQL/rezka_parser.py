from bs4 import BeautifulSoup
import requests
import sqlite3
import re


def parse(depth=int(input('Виберіть глибину пошуку: ')), find=input('Виберіть категорію із [best, fiction, ...]: ')):
    page = 1

    # Проміжний результат (у майбутньому треба позбутися)
    result = []

    while True:

        # Ключове посилання
        url = f"https://rezka.ag/films/{find}/page/{page}/"

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
            if len(films):
                for film, mark in zip(films, marks):
                    # Блок первинних даних
                    f = film.text.strip()

                    if find == "best":
                        m = re.split(pattern='[^0-9,.]',
                                     string=mark.find('i',
                                                      class_="b-category-bestrating rating-green-string").get_text(
                                         strip=1))[1]
                    else:
                        m = None

                    # Блок кінцевих даних
                    name = f.split(',')[0][0:-5]
                    year = [_ for _ in re.split(pattern='[^0-9]', string=f) if len(_) > 3][0]
                    country = f.split(',')[1].strip()
                    genre = f.split(',')[2].strip()

                    result.append([name, year, country, genre, m])

                page += 1
            else:
                print(f'\nПереглянуті усі фільми категорії {find}')

        else:
            print(f'Переглянуті вибрані фільми категорії {find}')
            break

    return result


"""Запис у БД SQLite"""
try:
    with sqlite3.connect('rezka.db') as con:
        print('\nDatabase connected...')
        cursor = con.cursor()

        # Створення БД
        cursor.execute("""CREATE TABLE IF NOT EXISTS {}(
        name VARCHAR(50),
        year INT,
        country VARCHAR(50),
        genre VARCHAR(50),
        mark FLOAT,
        Unique(name));""".format(parse.__defaults__[1]))

        # Огляд наявних записів у БД
        cursor.execute("""SELECT * FROM {}""".format(parse.__defaults__[1]))

        Q = cursor.fetchall()
        q = [Q[i][0] for i in range(len(Q))]

        # Перевірка присутності майбутніх записів у списку існюючих
        for item in parse():
            if not item[0] in q:
                cursor.execute("""INSERT INTO {} VALUES (?,?,?,?,?)""".format(parse.__defaults__[1]), item)
                con.commit()


except Exception as ex:
    print(ex)

finally:
    print('Connection closed...')
    con.close()
