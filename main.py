import telebot
import data

bot = telebot.TeleBot('680127281:AAH_1jNMWGbXNWS2hfsBC33wGtMk1_-6lwU')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Привет', 'Пока')

l = data.newsLinks()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Гудбай')
   
    elif message.text.lower() == 'новости': 
      for i in range (len(data.contents)):
                    
         bot.send_message(message.chat.id, l[i])
        


def sticker_id(message):
    print(message)

bot.polling()