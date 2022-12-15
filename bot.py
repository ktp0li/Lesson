from aiogram import Bot, executor, Dispatcher, types
from lessons_button import *
import datetime

bot = Bot('BOT_TOKEN') # Бот токен
dp = Dispatcher(bot) # Создание Диспетчера

day_for_school = 1 # Учебный день (будет менятся ежедневно)

@dp.message_handler(commands=(['start']))
async def menu(message: types.Message):
    await message.answer(text=f'ты уже корячешься в этой школе {day_for_school} дней', reply_markup=update_date_keyborard)

@dp.message_handler()
async def lessons_day(message: types.Message):
    if message.text == 'География' and day_for_school == 1:
        await message.answer('запиши домашнее задание ')



if __name__ == '__main__':
    executor.start_polling(dp)
