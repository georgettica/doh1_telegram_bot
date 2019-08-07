import telebot
import pprint
import json
import pickle
import os 

class User():
    def __init__(self, user_name, user_id, user_status=u""):
        self.user_name = user_name
        self.user_id = user_id
        self.user_status = user_status

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __hash__(self):
        return self.user_id

    def __str__(self):
        return self.user_name.decode('UTF-8') + self.user_status.decode('UTF-8')

    def set_status(self, user_status):
        self.user_status = user_status


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


def is_new_user(message, users):
    user_id = message.from_user.id
    if user_id in users:
        return False
    else:
        new_user = User(message.text[1:].encode('UTF-8'), user_id)
        users[user_id] = new_user
        with open('users.txt', 'wb') as handle:
            pickle.dump(users, handle)
        return True

def get_users():
    with open('users.txt', 'rb') as handle:
        try:
            users =  pickle.loads(handle.read())
            return users
        except:
            return {}
         

def get_bot():
    return telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")
    # chat = bot.get_chat(-336818907)

if __name__ == '__main__':
    possible_answers = create_all_possible_possible_answers()
    users = get_users()
    bot = get_bot()
    @bot.message_handler(commands=['stop'])
    def print_summary(message):
        print("In stop")
        bot_response = ""
        for user in users.values():
            bot_response += "**{}: {}\n".format(user.user_name.decode('UTF-8') , user.user_status.decode('UTF-8'))
        bot.send_message(message.from_user.id,text=bot_response)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        user_id = message.from_user.id
        is_new_user(message, users)
        parsed = message.text[1:].encode('UTF-8')
        if parsed in possible_answers:
            answer = possible_answers[parsed]
            print(answer)
            print(answer.decode('UTF-8'))
            users[user_id].set_status(possible_answers[parsed])
            # bot.send_message(message.from_user.id, text = "Got that, adding your status as  {} " .format(possible_answers[parsed].decode('UTF-8')))
        else:
            bot.send_message(message.from_user.id, text = "I don't recognize what you wrote {} " .format(message.from_user.first_name))
    bot.polling()
    
