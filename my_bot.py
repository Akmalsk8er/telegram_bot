import telebot
bot = telebot.TeleBot('1636619058:AAFmFhullbR6HViijiOL8G12A7sxO-BclN4')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Салют, мой создатель!!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'Пока, мой создатель!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю что это значит.')

bot.polling(none_stop=True)
