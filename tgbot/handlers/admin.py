from telebot import TeleBot
from telebot.types import Message
from tgbot.handlers.messages import Messages
from tgbot.handlers.buttons import BuildButtons

msg = Messages()
btn = BuildButtons()


def admin_user(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    bot.send_message(
        message.chat.id, msg["for_admin"], reply_markup=btn.admin_view()
    )
