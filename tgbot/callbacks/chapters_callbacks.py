from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup
from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot import types, TeleBot
from telebot.util import quick_markup

# from telebot.custom_filters import AdvancedCustomFilter
from tgbot.catalog import catalog, catalog_items

from tgbot.handlers.buttons import BuildButtons

# from messages import Messages
from tgbot.config import TOKEN
from tgbot.constants import URL

ITEMS = catalog_items()

body_chapt = catalog["body"]["items"]
body_msg = catalog["body"]["message"]
body_img = catalog["body"]["chapter_img"]

face_chapt = catalog["face"]["items"]
face_msg = catalog["face"]["message"]
face_img = catalog["face"]["chapter_img"]

hair_chapt = catalog["hair"]["items"]
hair_msg = catalog["hair"]["message"]
hair_img = catalog["hair"]["chapter_img"]

# gift_chapt = catalog["gift_card"]["items"]
gift_msg = catalog["gift_card"]["message"]
gift_img = catalog["gift_card"]["chapter_img"]

bot = TeleBot(TOKEN)
products_factory = CallbackData("product_id", prefix="products")


############        CHAPTERS        ############
def keyboard(chapter):
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=ITEMS[product]["name"],
                    callback_data=products_factory.new(
                        product_id=ITEMS[product]["product_id"]
                    ),
                )
            ]
            for product in chapter
        ]
    )


############          BODY          ############
def body_callback(call: CallbackQuery, bot: TeleBot):
    bot.send_photo(
        chat_id=call.message.chat.id,
        photo=body_img,
        caption=body_msg,
        reply_markup=keyboard(body_chapt),
    )


############        FACE         ############
def face_callback(call: CallbackQuery, bot: TeleBot):
    bot.send_photo(
        chat_id=call.message.chat.id,
        photo=face_img,
        caption=face_msg,
        reply_markup=keyboard(face_chapt),
    )


############        HAIR         ############
def hair_callback(call: CallbackQuery, bot: TeleBot):
    bot.send_photo(
        chat_id=call.message.chat.id,
        photo=hair_img,
        caption=hair_msg,
        reply_markup=keyboard(hair_chapt),
    )


############        GIFT         ############
def gift_callback(call: CallbackQuery, bot: TeleBot):
    bot.send_photo(
        chat_id=call.message.chat.id,
        photo=gift_img,
        caption=gift_msg,
        # reply_markup=gift_keyboard(),
    )


############        CHAPTERS   END        ############


############        CHECKOUT     CALLBACK        ############
def checkout_callback(call: CallbackQuery, bot: TeleBot):
    for items in user_cart.values():
        for item_id, values in items.items():
            id_ = item_id
            qty = values["quantity"]
    checkout_link = f"{URL}/checkout/?add-to-cart={id_}&quantity={qty}"
    markup = quick_markup(
        {"Перейти на anvibodycare.com": {"url": checkout_link}},
        row_width=2,
    )
    bot.edit_message_text(
        "✅ Оформити замовлення",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
    )
