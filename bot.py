import logging
from tgbot.filters.admin_filter import AdminFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import about, welcome, contacts, btn_catalog

from telebot import TeleBot
from tgbot import config
from tgbot.callbacks.chapters_callbacks import (
    body_callback,
    face_callback,
    hair_callback,
    gift_callback,
    checkout_callback,
)


# db = Database()
# remove this if you won't use middlewares:
# from telebot import apihelper

# apihelper.ENABLE_MIDDLEWARE = True
# I recommend increasing num_threads
bot = TeleBot(config.TOKEN, num_threads=5)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    filename="bot.log",
    filemode="w",
    encoding="utf-8",
    datefmt="%d.%m.%Y %H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.info("Bot started")


def register_handlers():
    bot.register_message_handler(anti_spam, commands=["spam"], pass_bot=True)
    bot.register_message_handler(
        admin_user, commands=["start"], admin=True, pass_bot=True
    )
    bot.register_message_handler(
        welcome, commands=["start"], admin=False, pass_bot=True
    )
    bot.register_message_handler(
        contacts,
        func=lambda message: message.text == "💌 Наші контакти",
        admin=False,
        pass_bot=True,
    )
    bot.register_message_handler(
        about,
        func=lambda message: message.text == "🌿 Про Нас",
        admin=False,
        pass_bot=True,
    )
    bot.register_message_handler(
        btn_catalog,
        func=lambda message: message.text == "📒 Каталог",
        admin=False,
        pass_bot=True,
    )


def register_callbacks():
    bot.register_callback_query_handler(
        callback=body_callback,
        func=lambda callback: callback.data == "Тіло",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        callback=face_callback,
        func=lambda callback: callback.data == "Бальзами для губ",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        callback=hair_callback,
        func=lambda callback: callback.data == "Волосся",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        callback=gift_callback,
        func=lambda callback: callback.data == "Подарункова карта",
        pass_bot=True,
    )
    bot.register_callback_query_handler(
        callback=checkout_callback,
        func=lambda callback: callback.data == "checkout",
    )


register_handlers()
register_callbacks()

# custom filters
bot.add_custom_filter(AdminFilter())


def run():
    bot.infinity_polling()


run()
