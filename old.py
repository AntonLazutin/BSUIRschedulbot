# try:
#     bot = telebot.TeleBot(token=os.environ.get('API_KEY'))
# except Exception as e:
#     print("Error!")


# @bot.message_handler(commands=['start'])
# def start_msg(message):
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
#     item_input = types.KeyboardButton("Ввести группу", callbacks)   
#     markup.add(item_input)
#     msg = bot.reply_to(message, text="Введите номер группы", reply_markup=markup)
#     #bot.register_next_step_handler(msg, process_group)

# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call): # <- passes a CallbackQuery type object to your function
#     pass

# def process_group(message):
#     json_dict = parse(f"{URL}{message.text}")
#     print(pprint.pformat(json_dict['schedules']['Вторник']))
#     schedule =  get_schedule(json_dict['schedules'][get_cur_day_str()])
#     print(schedule)
#     bot.send_message(message.chat.id, f"Сегодня {get_cur_day_str()}")
#     for elem in schedule:
#         bot.send_message(message.chat.id, 
#                         f"Пара: {elem[0]}\nНачало: {elem[1]}\nКонец: {elem[2]}"
#                         )


# def schedule_by_day(json_dict: dict, day: str):
#     schedule = get_schedule(json_dict['schedules'][day])
#     ...