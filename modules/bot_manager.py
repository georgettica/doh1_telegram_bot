import telebot
from modules.json_manager import *
from pprint import pprint

class BotManager:

    def __init__(self):
        self.bot = telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")
        self.json_data = read_users_and_groups()
        self.group_counters = initialize(self.json_data)

        @self.bot.message_handler(commands=['stop'])
        def stop(self):
            self.bot.stop_bot()

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            parsed_text = message.text[1:]
            splitted_text = parsed_text.split(':')
            parsed_name, parsed_status = splitted_text[0][::-1].strip(), splitted_text[1][::-1].strip()
            update_user_status(parsed_name, parsed_status, self.json_data)
            group_reported, group_name = is_group_reported(parsed_name, self.json_data) 
            if group_reported:
                self.bot.reply_to("Group {0} was fully reported".format(group_name))

    def poll(self):
        self.bot.polling()

    
    