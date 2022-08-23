from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Boshlash'),
            KeyboardButton(text="ℹ️Qoʼllanma"),
        ],
    ],
    resize_keyboard=True
)