import telebot
import random
from telebot import types

bot = telebot.TeleBot('6704596447:AAEDAaoT4Rl3oQLcQubnm0fS5udHvq-xuaQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет, говно!)\nподробнее о моих командах тут /help')
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'что помощь нужна??.. пипец ты беспомощный, хорошо, что я есть у тебя \n')
    bot.send_message(message.chat.id, '<b>/calc</b> - <em>посчитать за тебя, ведь ты такой глупый</em>\n<b>/generate</b> - <em>сгенерировать новое слово</em>\nа еще можешь отправить фото я их оценю', parse_mode='html')
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    word = random.choice(['удали это пожалуйста', 'фу че за хуйня'])
    if word == 'удали это пожалуйста':
        markup.add(types.InlineKeyboardButton('Удалить', callback_data='delete'))
        bot.reply_to(message, word, reply_markup=markup)
    else:
        bot.reply_to(message, word)
@bot.message_handler()
def main(message):
    bot.send_message(message.chat.id, 'общайся со мной через команды я тупая собака АФ АФ\n<em>(для тупых, то есть для тебя, это такие штуки которые начинаются с / и содержат английские слова которые ты скорее всего не знаешь)</em>', parse_mode='html')


bot.polling(non_stop=True)