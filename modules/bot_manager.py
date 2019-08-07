import telebot
from modules.json_manager import read_users_and_groups, initialize_group_counter

class BotManager:

    def __init__(self):
        self.bot = telebot.TeleBot("630906916:AAHMOb7KomCgbeetwQLnSZEyzPn9w0iYUrg")
        json_data = read_users_and_groups()
        group_counters = initialize_group_counter(json_data)

        @self.bot.message_handler(commands=['stop'])
        def stop(self):
            self.bot.stop_bot()

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            parsed_text = message.text[1:]
            splitted_text = parsed_text.split(':')
            parsed_name, parsed_status = splitted_text[0], splitted_text[1]
            print("PARSED_NAME::", parsed_name)
            print("PARSED_STATUS::", parsed_status)        

    def poll(self):
        self.bot.polling()

    
    