import telebot
from datetime import datetime
import logging
from random import choice
from numpy import array, dot, random

token = "421016646:AAGYFa2cdhjqlDyePFqKkRJkG4FrsGqfu3o"
bot = telebot.TeleBot(token)

#----------------------------------------------------------------------------#
# Логирование
logging.basicConfig\
(
    level=logging.DEBUG,
    format='# %(asctime)s : %(message)s #', filename='error.log'
)

def log(message, answer):
    print('\n@@')
    print(datetime.today())
    print('Сообщение от пользователя:\nИмя: {0}\tФамилия: {1}(id: {2})\nТекст:\n{3}'
          .format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    logging.info(u'Сообщение от пользователя {0}\t{1}({2}) : Текст {3} : Ответ бота {4}'
                .format(message.from_user.first_name, message.from_user.last_name,
                        str(message.from_user.id), message.text, answer))
    for i in range(10): print('-', end = '')
    print('\nОтвет бота: ' + answer + '\n')
#----------------------------------------------------------------------------#

unit_step = lambda x: 0 if x < 0 else 1
#----------------------------------------------------------------------------#
# Обучение
def learning():
    training_data =\
    [
        (array([0,0,1]), 0),
        (array([0,1,1]), 1),
        (array([1,0,1]), 1),
        (array([1,1,1]), 1),
    ] #СЕТ ДЛЯ ТРЕНИ ИЛИ

    global perceptron;
    perceptron = random.rand(3)
    errors = []
    eta = 0.2
    n = 100

    for i in range(n):
        x, expected = choice(training_data)
        result = dot(perceptron, x)                    #ПРОИЗВЕДЕНИЕ ВЕКТОРОВ
        error = expected - unit_step(result)  #НАХОЖДЕНИЕ ОШИБКИ
        errors.append(error)                  #ПОПОЛНЕНИЕ ОШИБОК
        perceptron += eta * error * x                  #ПОВЫШЕНИЕ ИЛИ ПОНИЖЕНИЕ ВЕСОВ В ЗАВИСИМОСТИ ОТ РЕЗУЛЬТАТА ЮНИТ СТЕП

#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
# Ответ на текст
@bot.message_handler(content_types=['text'])
def handle_command_text(message):
    answer = '@Ответил пользователю'
    try:
        user_data = list(map(int, message.text.replace(',', ' ').split()))
        if (len(user_data) == 2 and (user_data.count(0) + user_data.count(1)) == 2):
            user_data.append(1)
            result = dot(user_data, perceptron)
            bot.send_message(message.chat.id, '{}: {} -> {} '.format(user_data[:2], result, unit_step(result)))
        else:
            raise;
    except:
        answer = '@Не ответил пользавателю'
    log(message, answer)

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    logging.debug('\n\n' + '-' * 79 + '\n\n# START')
    try:
        learning()
        bot.polling(none_stop=True, interval=0)
    except:
        logging.debug('Unknown error')
