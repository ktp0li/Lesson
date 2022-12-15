from aiogram import Bot, executor, Dispatcher, types
from lessons_button import *
import datetime
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot('123456') # Бот токен
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) # Создание Диспетчера

day_for_school = 1 # Учебный день (будет менятся ежедневно)
class homework(StatesGroup):
    frs = State()

@dp.message_handler(commands=(['start']))
async def menu(message: types.Message):
    await message.answer(text=f'ты уже корячешься в этой школе {day_for_school} дней', reply_markup=update_date_keyborard)


@dp.message_handler(commands=(['12345']), state=None)
async def firstss(message: types.Message):
    await message.answer('12345 ответ')
    await homework.frs.set()


@dp.message_handler(state=homework.frs)
async def otvet(message: types.Message, state: FSMContext):
    item = message.text
    await state.update_data(
        {
            'item': item
        }
    )
    data = await state.get_data()
    item = data.get('item')
    await message.answer(item)
    await state.finish()



# @dp.message_handler()
# async def lessons_day(message: types.Message):
#     if message.text == 'География' and day_for_school == 1:
#         await message.answer('запиши домашнее задание ')



if __name__ == '__main__':
    executor.start_polling(dp)
