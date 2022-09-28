from socket import AI_CANONNAME
from tracemalloc import start
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from ..main import db

main_menu = ['Меню группы', 'Избранное', 'Отмена']


async def start_cmd(message: Message, state: FSMContext):
    await state.finish()
    db.add_user(user_id=message.from_user.id)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for elem in main_menu:
        keyboard.add(elem)
    await message.answer("Привет 👋, что выбираешь?", reply_markup=keyboard)
    

async def cancel_cmd(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Отмена", reply_markup=ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands='start', state='*')
    dp.register_message_handler(cancel_cmd, commands='cancel', state='*')
    dp.register_message_handler(cancel_cmd, Text(equals='Отмена', ignore_case=True), state='*')