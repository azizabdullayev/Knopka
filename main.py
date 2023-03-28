from aiogram import executor
from config import dp
from aiogram.types import Message
from repleykeyboards import start_btn, taq


@dp.message_handler(commands=['start'])
async def start(msg: Message):
    image = open('fotos/rasm.jpg', 'rb')
    text = f"Xush kelibsiz! {msg.from_user.full_name}"
    await msg.answer_photo(image, caption=text, reply_markup=start_btn)


@dp.message_handler(text='BOSHQA NARSALAR')
async def found(msg: Message):
    img = open('fotos/not foto.webp', 'rb')
    await msg.answer_photo(img)


@dp.message_handler(text='KITOBLAR')
async def kitob(msg: Message):
    ttg = f"Kitob tanlang!\n1. НЕ ТУПИ\n2. БУТЬ ЛУЧШЕЙ ВЕРСИЕЙ СЕБЯ\n3. СМЫСЛ СУЩЕСТВОВАНИЯ ЧЕЛОВЕКА\n"
    await msg.answer(ttg, reply_markup=taq)


@dp.message_handler(text='1')
async def bir(msg: Message):
    await msg.answer_document(open('book/kitob1.pdf', 'rb'))


@dp.message_handler(text='2')
async def ikki(msg: Message):
    await msg.answer_document(open('book/kitob.pdf', 'rb'))


@dp.message_handler(text='3')
async def uch(msg: Message):
    await msg.answer_document(open('book/kitob2.pdf', 'rb'))


@dp.message_handler(text='Ortga')
async def ortga(msg: Message):
    ttg2 = f"Kitob tanlang!\n1. НЕ ТУПИ\n2. БУТЬ ЛУЧШЕЙ ВЕРСИЕЙ СЕБЯ\n3. СМЫСЛ СУЩЕСТВОВАНИЯ ЧЕЛОВЕКА\n"
    await msg.answer(ttg2, reply_markup=taq)


if __name__ == '__main__':
    executor.start_polling(dp)
