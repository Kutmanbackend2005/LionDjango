import asyncio
from aiogram import Bot, Dispatcher,executor, types
import logging,os

from aiohttp.helpers import TOKEN
from decouple import config

token = config(TOKEN)"7718054171:AAHraTP7CFhB2Gzscx5xwyKR3bTKeE22nZw"
bot = Bot(token=token)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def command_start_handler(message:types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет,{name}!")


@dp.message_handler(commands=['photo'])
async def send_picture_handler(message:types.Message):
    photo_path = os.path.join("images","1484471.jpg")
    with open(photo_path,"wb") as photo:
        await message.answer_photo(
            photo=photo,
            caption="SIUUUU!!!"
        )

@dp.message_handler()
async def echo_handler(message:types.Message):
    text=message.text
    await message.answer(text)

@dp.message_handler()
async def number_handler(message:types.Message):
    number = int(message.text)
    squared = number**2
    await message.answer(f"Квадрат числа {number} равен {squared}")



if __name__ =='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)