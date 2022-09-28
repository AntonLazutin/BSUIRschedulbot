from logging import handlers
from multiprocessing.reduction import steal_handle
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text


from backend.config import weekdays
from backend.services import get_cur_day_str, get_schedule, get_json

class GetSchedule(StatesGroup):
    waiting_for_group = State()
    day_prompt = State()
    waiting_for_day = State()


async def prompt_group(message: types.Message, state: FSMContext):
    await message.answer("Введите номер группы")
    await state.set_state(GetSchedule.waiting_for_group.state)


async def process_group(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text.lower())
    await state.set_state(GetSchedule.day_prompt.state)


async def day_prompt(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    values = weekdays.values()
    for value in values:
        keyboard.add(value)
    keyboard.add("Отмена")
    await message.answer(text=f"Сегодня {get_cur_day_str()}\nНа какой день показать расписание?", reply_markup=keyboard)
    await state.set_state(GetSchedule.waiting_for_day.state)    


async def process_schedule(message: types.Message, state:FSMContext):
    if message.text == "Отмена":
        await state.finish()
    elif message.text == "Воскресенье":
        await message.answer("В воскресенье выходной🙆‍♂️")
    #day = message.text
    #await message.answer(text=day)
    data = await state.get_data()
    for elem in get_schedule(get_json(data['group'])[message.text]):
        await message.answer(text=f"Пара: {elem[0]}\nНачало: {elem[1]}\nКонец: {elem[2]}")
    await state.set_state(GetSchedule.waiting_for_day.state)


def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(prompt_group, commands='schedule', state='*')
    dp.register_message_handler(prompt_group, Text(equals="Меню группы"), state='*')
    dp.register_message_handler(process_group, state=GetSchedule.waiting_for_group)
    dp.register_message_handler(day_prompt, state=GetSchedule.day_prompt) 
    dp.register_message_handler(process_schedule, state=GetSchedule.waiting_for_day)