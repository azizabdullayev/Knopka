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
taq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)
