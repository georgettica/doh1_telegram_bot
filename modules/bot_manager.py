import telebot
from modules.json_manager import *
from pprint import pprint
from modules.exceptions.no_username import NoUsername
from modules.exceptions.unknown_status import UnknownStatus

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
            try:
                update_user_status(parsed_name, parsed_status, message.from_user.id, self.json_data)
            except NoUsername:
                self.bot.send_message(message.from_user.id, "Invalid name {}, not in database".format(parsed_name))
            except UnknownStatus:
                self.bot.send_message(message.from_user.id, "Invalid status {}".format(parsed_status))

            group_reported, group_name = is_group_reported(parsed_name, self.json_data) 
            if group_reported:
                # self.bot.reply_to(message,  "Group {0} was fully reported".format(group_name))
                self.bot.send_message(get_leader_telegram_id(group_name, self.json_data), "Group {0} was fully reported".format(group_name))

    def poll(self):
        self.bot.polling()

    
    
