from tgbot.catalog import catalog, catalog_items

from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot.types import (
    KeyboardButton,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    CallbackQuery,
)


BUTTONS = {
    "catalog": "📒 Каталог",
    "cart": "🛍️ Кошик",
    "about": "🌿 Про Нас",
    "contacts": "💌 Наші контакти",
    ################################
    "description": "Опис продукту",
    "back_to_item": "⬅️ Назад до продукту",
    "back_to_chapter": "⬅️ Назад до категорії",
    "cart_edit": "✏️Редагувати",
    "remove_1": "✏️-1",
    "add_1": "✏️+1",
    "add_to_cart": "Додати у кошик",
    "cart_empty": "❌ Очистити кошик",
    "checkout": "✅ Оформити замовлення",
    "update": "update",
    "schedule_status": "status",
}


class BuildButtons:
    def __init__(self):
        self.btn = BUTTONS

    def get_text(self, key):
        return self.btn.get(key)

    def get_button(self, key):
        return KeyboardButton(self.btn[key])

    def get_inline_button(self, name, callback_data=None):
        return InlineKeyboardButton(text=name, callback_data=callback_data)

    def main(self):
        markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        return markup.add(
            self.get_button("catalog"), self.get_button("cart")
        ).row(self.get_button("about"), self.get_button("contacts"))

    def admin_view(self):
        markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        return markup.add(
            self.get_button("catalog"), self.get_button("cart")
        ).row(
            self.get_button("schedule_status"),
            self.get_button("update"),
        )

    def btn_catalog(self):
        markup = InlineKeyboardMarkup()
        for chapt in catalog.keys():
            chapter = catalog[chapt]["chapter_name"]
            inline_btn = self.get_inline_button(chapter, callback_data=chapter)
            markup.add(inline_btn)
        return markup


# ------------------------------------
# def add_from_cart(self, key):
#     return self.btn.get(key)

# def remove_from_cart(self, key):
#     return KeyboardButton(self.btn[key])

# def add_to_cart(self, message):
#     pass

# def cart_clear(self, message):
#     pass

# def cart_edit(self, message):
#     markup = InlineKeyboardMarkup()
#     return markup.row(
#         self.get_inline_button("plus", plus_product_id.new(id=id_product)),
#         self.get_inline_button(
#             "minus", minus_product_id.new(id=id_product)
#         ),
#         self.get_inline_button(
#             "delete", delete_product_id.new(id=id_product)
#         ),
#     )

# def back_to_chapter(self, message):
#     pass

# def back_to_item(sekf, message):
#     pass

# def checkout(self, message):
#     pass

# def description(self, message):
#     pass
