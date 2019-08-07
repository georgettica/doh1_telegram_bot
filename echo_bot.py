import telebot
import pprint
import json
import pickle
import os 

class User():
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __hash__(self):
        return self.user_id


def create_all_possible_possible_answers():
    possible_answers = {}
    allowed_answered = ['ביח', 'ביחידה', 'מחוץ', 'מח']
    inside_messages = ['ביחידה', 'ביח', 'בדרך']
    outside_messages = ['מחוץ', 'מחוץ ליחידה', 'מח']
    sick_messages = ['מחלה']
    vacation_messages = ['יום חופש', 'חופש']
    dictionary = {'ביחידה': inside_messages, 'מחוץ ליחידה': outside_messages, 'יום מחלה': sick_messages, 'יום חופש': vacation_messages}
    for status, texts in dictionary.items():
        encoded_status = status.encode('UTF-8')
        for text in texts:
            possible_answers[text.encode('UTF-8')] = encoded_status
    return possible_answers


def is_new_user(message):
    user_id = message.from_user.id
    if user_id in users:
        return False
    else:
        new_user = User(message.text.encode('UTF-8'), user_id)
        users[user_id] = new_user
        with open('users.txt', 'wb') as handle:
            pickle.dump(users, handle)

def get_users():
    print(os.listdir())
    with open('users.txt', 'rb') as handle:
        return pickle.loads(handle.read())

def get_bot():
    return telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")
    # chat = bot.get_chat(-336818907)

if __name__ == '__main__':
    possible_answers = create_all_possible_possible_answers()
    users = get_users()
    bot = get_bot()
    bot.polling
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        is_new_user(message)
        parsed = message.text[1:].encode('UTF-8')
        if parsed in possible_answers:
            bot.send_message(message.from_user.id, text = "Got that, adding your status as  {} " .format(possible_answers[parsed].decode('UTF-8')))
        else:
            bot.send_message(message.from_user.id, text = "I don't recognize what you wrote {} " .format(message.from_user.first_name))
