from aiogram import Bot, executor, Dispatcher, types
from lessons_button import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time
import threading





bot = Bot('121212') # Бот токен
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) # Создание Диспетчера

day_for_school = 1 # Учебный день (будет менятся ежедневно)

def seconds():
    while True:
        global day_for_school
        time.sleep(1)
        if time.localtime().tm_hour == 0 and time.localtime().tm_min == 0 and time.localtime().tm_sec == 0 and day_for_school < 7:
            day_for_school += 1

class homework(StatesGroup):
    frs = State()

@dp.message_handler(commands=(['start']))
async def menu(message: types.Message):
    # await message.answer(text=f'ты уже корячешься в этой школе {day_for_school} дней', reply_markup=update_date_keyborard)
    await message.answer(f'{day_for_school}')

# @dp.message_handler(commands=(['12345']), state=None)
# async def firstss(message: types.Message):
#     await message.answer('12345 ответ')
#     await homework.frs.set()
#
#
# @dp.message_handler(state=homework.frs)
# async def otvet(message: types.Message, state: FSMContext):
#     item = message.text
#     await state.update_data(
#         {
#             'item': item
#         }
#     )
#     data = await state.get_data()
#     item = data.get('item')
#     await message.answer(item)
#     await state.finish()



@dp.message_handler()
async def lessons_day(message: types.Message, state=None):
    if message.text == 'География' and day_for_school == 1:
        await message.answer('Запиши домашнее задание')
        await homework.frs.set()


@dp.message_handler(state=homework.frs)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    await message.answer(f'Day={day_for_school}, word={lesson}')
    await state.finish()



threading.Thread(target=seconds).start()

if __name__ == '__main__':
    executor.start_polling(dp)
