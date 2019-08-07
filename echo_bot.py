import telebot
import pprint
bot = telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, {} how are you doing?". format(message.text))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()