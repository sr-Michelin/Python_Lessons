import re
import os
import sqlite3
import requests
from bs4 import BeautifulSoup

genre_dict = {
    1: 'western',
    2: 'crime',
    3: 'fiction',
    4: 'horror',
    5: 'family',
    6: 'action',
    7: 'adventures',
    8: 'comedy',
    9: 'fantasy',
    10: 'military',
    11: 'drama',
    12: 'historical',
    13: 'travel',
    14: 'detective',
    15: 'thriller'
}


def convert_to_binary(filename):
    # Фото у бінарки
    with open(filename, 'rb') as file:
        blobDATA = file.read()
    return blobDATA


# depth = int(input('Виберіть глибину пошуку: '))
# find = input('Виберіть категорію із [best, fiction, ...]: ')


def parse(page=1, depth=1, genre='best', filter_='?filter=popular'):
    # Проміжний результат (у майбутньому треба позбутися)
    result = []

    while True:

        # Ключове посилання
        url = f"https://rezka.ag/films/{genre}/page/{page}/{filter_}"

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
                    # Блок кінцевих даних
                    title = film.find('a').text.strip()
                    year = film.find('div').text.split(', ')[0]
                    country = film.find('div').text.split(', ')[1]
                    genre_ = film.find('div').text.split(', ')[2]
                    link = film.find('a').get('href')
                    rate = re.split('[^0-9,.]', mark.find('i').get_text(strip=1))[-2] if genre == 'best' else None

                    # Медіа файли
                    photo_src = mark.find('img').get('src')
                    img_data = requests.get(photo_src, verify=True).content
                    photo_name = re.sub('[^A-Za-zА-Яа-я,^0-9.+]', '', title) + '.jpg'

                    with open('thumbnails/' + photo_name, 'wb') as handler:
                        handler.write(img_data)

                    result.append(
                        [title, year, country, genre_, rate, link, convert_to_binary('thumbnails/' + photo_name)])

                    # Очищення thumbnails - тимчасової директорії
                    for f in os.listdir('thumbnails'):
                        os.remove(os.path.join('thumbnails', f))

                page += 1
            else:
                print(f'\nПереглянуті усі фільми категорії https://rezka.ag/films/{genre}')

        else:
            print(f'Переглянуті вибрані фільми категорії https://rezka.ag/films/{genre}')
            break

    return result


def sql(genre_='best', depth_=1):
    """Запис у БД SQLite"""

    # Створення тимчасової директорії для бінаризації фото та збереження їх у БД
    if not os.path.exists('thumbnails'):
        os.makedirs('thumbnails')

    try:
        with sqlite3.connect('rezka.db') as con:
            print('\nDatabase connected...')
            cursor = con.cursor()

            # Створення БД
            cursor.execute("""CREATE TABLE IF NOT EXISTS {}(
            title VARCHAR(50),
            year INT,
            country VARCHAR(50),
            genre VARCHAR(50),
            rate FLOAT,
            link VARCHAR(100),
            photo BLOB,
            Unique(title));""".format(parse.__defaults__[2]))

            # Огляд наявних записів у БД
            cursor.execute("""SELECT * FROM {}""".format(parse.__defaults__[2]))

            Q = cursor.fetchall()
            q = [Q[i][0] for i in range(len(Q))]

            # Перевірка присутності майбутніх записів у списку існюючих
            for item in parse(genre=genre_, depth=depth_):
                if not item[0] in q:
                    cursor.execute("""INSERT INTO {} VALUES (?,?,?,?,?,?,?)""".format(parse.__defaults__[2]), item)
                    con.commit()

    except Exception as ex:
        print(ex)

    finally:
        print('Connection closed...')
        con.close()


if __name__ == '__main__':
    sql(depth_=10)
