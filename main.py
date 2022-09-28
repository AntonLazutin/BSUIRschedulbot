import os
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.bot_command import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from backend.config import *
from backend.parser import parse
from backend.services import *

from handlers.schedule import register_handlers_schedule
from handlers.common import register_handlers_common

from dotenv import load_dotenv, find_dotenv

from database.db_handler import Database


load_dotenv(find_dotenv())

bot = Bot(os.environ.get('API_KEY'))

dp = Dispatcher(bot=bot, storage=MemoryStorage())

db = Database()


async def set_commands(bot: Bot):
    commands = [
        BotCommand('/start', description='Начинаем 🌅'),
        BotCommand('/schedule', description='Получить расписание необходимой группы'),
        BotCommand('/favorites', description='Избранные группы'),
        BotCommand('/cancel', description='Отмена'),
    ]
    await bot.set_my_commands(commands=commands)


# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Расписание для группы", "Избранные группы", "Отмена"]
#     keyboard.row(*buttons)
#     await bot.send_message(message.from_id, text="Helloooooo", reply_markup=keyboard)


# @dp.message_handler(lambda message: message.text=="Расписание для группы")
# async def group_schedule(message: types.Message):
#     await message.answer("Тут будет расписание")


# @dp.message_handler(lambda message: message.text=="Избранные группы")
# async def favorites(message: types.Message):
#     await message.answer("Тут будет избранное")


# @dp.message_handler(lambda message: message.text=="Отмена")
# async def exit(message: types.Message):
#     await message.answer(text="Пока, пока!", reply_markup=types.ReplyKeyboardRemove())




async def main():

    register_handlers_schedule(dp=dp)
    register_handlers_common(dp=dp)

    await set_commands(bot=bot)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())