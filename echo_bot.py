import telebot
import pprint
import json

bot = telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")

allowed_answered = [u'ביח', 'ביחידה', 'מחוץ', 'מח']


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
    # print(message)
    # bot.reply_to(message, "Howdy, {} how are you doing?". format(message.from_user.first_name))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    parsed_text = message.text[::-1][:len(message.text)-1]
    print(parsed_text)
    username = message.from_user.first_name

    if parsed_text not in allowed_answered:
        bot.reply_to(message, "I don't recognize what you wrote {} " .format(username))
        return
    bot.reply_to(message, "Got that {} " .format(username))

bot.polling()
