import telebot
import pprint
bot = telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")

allowed_answered = ['ביח'.encode('UTF-8'), 'ביחידה', 'מחוץ', 'מח']


inside_messages = ['ביחידה', 'ביח', 'בדרך']
outside_messages = ['מחוץ', 'מחוץ ליחידה', 'מח']
sick_messages = ['מחלה']
vacation_messages = ['יום חופש', 'חופש']

dictionary = {'ביחידה': inside_messages, 'מחוץ ליחידה': outside_messages, 'יום מחלה': sick_messages, 'יום חופש': vacation_messages}
possible_answers = {}

def create_all_possible_possible_answers():
    for status, texts in dictionary.items():
        encoded_status = status.encode('UTF-8')
        for text in texts:
            possible_answers[text.encode('UTF-8')] = encoded_status


create_all_possible_possible_answers()

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
    parsed = message.text[1:].encode('UTF-8')
    print(parsed)
    # print(parsed_text)
    if parsed in possible_answers:
        bot.send_message(message.from_user.id, text = "Got that, adding your status as  {} " .format(possible_answers[parsed].decode('UTF-8')))
    else:
        bot.send_message(message.from_user.id, text = "I don't recognize what you wrote {} " .format(message.from_user.first_name))


bot.polling()