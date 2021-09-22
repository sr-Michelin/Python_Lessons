import datetime
import telebot
import random
from telebot.types import Message

print("Bot Melisa is working...")

token = "1959028722:AAFdq4dEWWktBumxkBmdSBvH7EnPpTCcmks"
bot = telebot.TeleBot(token)

names = {
    0: 'Далбайоб дня @gosha_k8',
    1: 'Далбайоб дня @po_kaifu_666',
    2: 'Далбаєбеса дня @oxameln',
    3: 'Далбайоб дня @tsucini',
    4: 'Далбайоб дня @chevapchichiu',
    5: 'Далбайоб дня @momodaisukii',
    6: 'Далбайоб дня @Саша Глущук',
    7: 'Далбайоб дня @O͜͡riKAIZEN',
    8: 'Алкаш дня @september_burns',
    9: 'Староста дня @Mike_Shevchenko',
    10: 'Пам\'ять дня @Юра',
    11: 'Підарас дня @Taras',
    12: 'Далбайоб дня @gosha_k8',
    13: 'Далбайоб дня @gosha_k8',
    14: 'Далбайоб дня @gosha_k8',
    15: 'Далбайоб дня @gosha_k8',
    16: 'Далбайоб дня @gosha_k8',
    17: 'Далбайоб дня @gosha_k8',
    18: 'Далбайоб дня @gosha_k8',
    19: 'Далбайоб дня @gosha_k8',
    20: 'Далбайоб дня @gosha_k8'
}


@bot.message_handler(commands=['random'])
def command_handler(message: Message):
    """Вивід далбй@#бів😉"""

    result = random.randint(0, len(names) - 1)

    response = list(names.values())[result] + ' 😉'

    if message.from_user.first_name in ['Міша', 'Taras', 'Коля']:
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name} не бикуй')

    if '/random' in message.text:
        bot.delete_message(message.chat.id, message.message_id)

    with open('tele.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'"{response}": @{message.from_user.username} at {datetime.datetime.now()}\n')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
