import telebot
bot = telebot.TeleBot('680127281:AAH_1jNMWGbXNWS2hfsBC33wGtMk1_-6lwU')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'картинка':
        bot.send_photo(message.chat.id, 'https://sun6-16.userapi.com/c851428/v851428032/1ebab9/zWJ7BKgG-6w.jpg')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()