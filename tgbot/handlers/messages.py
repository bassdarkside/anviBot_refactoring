from tgbot.constants import ABOUT, CONTACTS
import json


def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


MESSAGES = {
    "for_admin": "Hello admin! You can use update for update catalog "
    + "or status for show current schedule.",
    "when_cart_empty": "Чекаю на нові товари 🐣\n \n Твій кошик 🌱",
    "when_cart_empty2": "Чекаю на товари для тебе 😌\n \n Твій кошик 🌱",
    "after_cart_clean": "Товари видалено 🫡",
    "after_cart_clea2": "Кошик порожній 🍃",
    "present_catalog": "Дивись, що в нас є 🥰",
    "start_upd": "Start update..",
    "after_upd": "Catalog is up-to-date!",
    "contacts": read_json(CONTACTS),
    "about": read_json(ABOUT),
}


class Messages:
    def __init__(self):
        self.messages = MESSAGES

    def __getitem__(self, key):
        return self.messages.get(key)
