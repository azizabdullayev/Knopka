from aiogram import executor
from config import dp
from aiogram.types import Message
from repleykeyboards import start_btn

@dp.message_handler(commands=['start'])
async def start(msg: Message):
    image = open('fotos/rasm.jpg', 'rb')
    text = f"Xush kelibsiz! {msg.from_user.full_name}"
    await msg.answer_photo(image, caption=text , reply_markup=start_btn)

@dp.message_handler(text='BOSHQA NARSALAR')
async def found(msg: Message):
    img = open('fotos/foto иди домой.jpg', 'rb')
    await msg.answer_photo(img)


@dp.message_handler(text='KITOBLAR')
async def kitob(msg: Message):
    await msg.answer_document(open('book/kitob.pdf', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp)
