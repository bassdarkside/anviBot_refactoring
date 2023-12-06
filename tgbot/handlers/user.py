from telebot import TeleBot, formatting
from telebot.types import Message, CallbackQuery
from tgbot.handlers.messages import Messages
from tgbot.handlers.buttons import BuildButtons

btn = BuildButtons()
msg = Messages()


def welcome(message: Message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        "Вітаю, {0.first_name}!\n Я допоможу тобі підібрати косметику"
        " 🌱ANVI🌱🥰".format(message.from_user),
        reply_markup=btn.main(),
    )


def contacts(message: Message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        text=msg["contacts"],
        # parse_mode="HTML",
        reply_markup=btn.main(),
    )


def about(message: Message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        text=msg["about"],
        parse_mode="HTML",
        reply_markup=btn.main(),
    )


def btn_catalog(message: Message, bot: TeleBot):
    bot.send_message(
        message.chat.id, msg["present_catalog"], reply_markup=btn.btn_catalog()
    )
