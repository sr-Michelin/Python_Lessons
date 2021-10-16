import random
import sqlite3
import telebot
from rezka_parser import sql
from telebot.types import Message, ReplyKeyboardMarkup

print("Bot RandomFilm is working...")

token = "2071046556:AAHfW3e-nFgvqmgEBsGHkgvrR6y24pDFPZc"
bot = telebot.TeleBot(token)

genre_list = ['Драмы', 'Биографические', 'Приключения', 'Военные', 'Криминал', 'Боевики', 'Фантастика', 'Детективы',
              'Комедии', 'Триллеры', 'Мелодрамы', 'Фэнтези', 'Семейные', 'Вестерны', 'Исторические', 'Ужасы']


@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'Привіт) \nЯ @random_f_bot, і я допоможу обрати фільм на вечір.')


@bot.message_handler(commands=['get_new'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, f'Поповнення бази фільмів...')
    bot.send_message(message.chat.id, f'База поповнена: \n{sql(genre_="best", depth_=20)}')


@bot.message_handler(commands=['random'])
def command_handler(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for value in genre_list:
        markup.add(value)

    bot.send_message(message.chat.id, 'Виберіть жанр:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def command_handler(message):
    if message.text in genre_list:
        bot.send_message(message.chat.id, f'Підбираю випадковий фільм жанру "{message.text}"...')

        try:
            print('\nDatabase connected...')
            with sqlite3.connect('rezka.db') as con:
                c = con.cursor()
                c.execute(
                    'SELECT title,year,country,genre, rate, link FROM best WHERE genre = "{}"'.format(message.text))

            film_list = c.fetchall()

            if len(film_list) > 0:
                r_f = film_list[random.randint(0, len(film_list) - 1)]
                random_name = f'Зараз глянемо: \n{r_f[0]} ({r_f[1]}) \n{r_f[2]}, {r_f[3]}, {r_f[4]} \n\n{r_f[5]}'

                bot.send_message(message.chat.id, random_name)

                c.execute('DELETE FROM best WHERE link = "{}"'.format(r_f[5]))
                con.commit()

                film_left = f'Залишилося фільмів жанру "{message.text}" - {len(film_list) - 1} шт'
                bot.send_message(message.chat.id, film_left)
                print(film_left)

            else:
                bot.send_message(message.chat.id, f'Жанр "{message.text}" відсутній у базі...')

        except Exception as e:
            print(f'We have a problem: \n{e}')

        finally:
            con.close()
            print('Connection closed...')

    else:
        bot.send_message(message.chat.id, f'"{message.text}" - невідома команда')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
