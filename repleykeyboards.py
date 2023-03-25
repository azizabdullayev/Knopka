from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KITOBLAR"),
            KeyboardButton(text="BOSHQA NARSALAR")
        ]
    ],

    resize_keyboard=True
)
