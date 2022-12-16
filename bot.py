from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import time
import threading


geog1_obj = ''
him1_obj = ''
angl1_obj = ''
doprussk_obj = ''
istor2_obj = ''
litra2_obj = ''
geom2_obj = ''
angl2_obj = ''
algebra3_obj = ''
angl3_obj = ''
russk3_obj = ''
istor4_obj = ''
angl4_obj = ''
obz4_obj = ''
dopinf_obj = ''
algebra5_obj = ''
obsh5_obj = ''
inf5_obj = ''
russk6_obj = ''
litra6_obj = ''
geom6_obj = ''
biolog6_obj = ''
angl6_obj = ''

monday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) # расписание на понедельник


three_monday_lesson = KeyboardButton(text='География')
four_monday_lesson = KeyboardButton(text='Химия')
update_button = KeyboardButton('Обновить')
clear_day = KeyboardButton('Очистить день')
six_monday_lesson = KeyboardButton(text='Английский')
additionally_monday_lesson = KeyboardButton(text='Доп. Русский')
monday_keyboard.add(three_monday_lesson, four_monday_lesson, six_monday_lesson, additionally_monday_lesson, update_button, clear_day)


tuesday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_tuesday_lesson = KeyboardButton(text='История')
two_tuesday_lesson = KeyboardButton(text='Литература')
five_tuesday_lesson = KeyboardButton(text='Геометрия')
six_tuesday_lesson = KeyboardButton(text='Английский')
update_button = KeyboardButton('Обновить')
clear_day = KeyboardButton('Очистить день')
tuesday_keyboard.add(one_tuesday_lesson, two_tuesday_lesson,  five_tuesday_lesson, six_tuesday_lesson, update_button, clear_day)


wednesday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_wednesday_lesson = KeyboardButton(text='Алгебра')
two_wednesday_lesson = KeyboardButton(text='Английский')
three_wednesday_lesson = KeyboardButton(text='Русский Язык')
clear_day = KeyboardButton('Очистить день')

wednesday_keyboard.add(one_wednesday_lesson, two_wednesday_lesson, three_wednesday_lesson, update_button, clear_day)


thursday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
two_thursday_lesson = KeyboardButton(text='История')
three_thursday_lesson = KeyboardButton(text='Английский')
five_thursday_lesson = KeyboardButton(text='ОБЖ')
additionally_thursday_lesson = KeyboardButton(text='Доп. Информатика')
update_button = KeyboardButton('Обновить')
clear_day = KeyboardButton('Очистить день')
thursday_keyboard.add(two_thursday_lesson, three_thursday_lesson, five_thursday_lesson, update_button, clear_day)


friday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
two_friday_lesson = KeyboardButton(text='Алгебра')
four_friday_lesson = KeyboardButton(text='Обществознание')
six_friday_lesson = KeyboardButton(text='Информатика')
update_button = KeyboardButton('Обновить')
friday_keyboard.add(two_friday_lesson, four_friday_lesson, six_friday_lesson, update_button, clear_day)

saturday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_saturday_lesson = KeyboardButton(text='Русский Язык')
two_saturday_lesson = KeyboardButton(text='Литература')
three_saturday_lesson = KeyboardButton(text='Геометрия')
four_saturday_lesson = KeyboardButton(text='Биология')
five_saturday_lesson = KeyboardButton(text='Английский')
clear_day = KeyboardButton('Очистить день')
update_button = KeyboardButton('Обновить')
saturday_keyboard.add(one_saturday_lesson, two_saturday_lesson, three_saturday_lesson, four_saturday_lesson, five_saturday_lesson, update_button, clear_day)


bot = Bot('5733141109:AAEuwSAskLBqyKQtChRXvSw0ixkMgy2E448') # Бот токен
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) # Создание Диспетчера

day_for_school = 1 # Учебный день (будет менятся ежедневно)


def seconds():
    while True:
        global day_for_school
        time.sleep(1)
        if time.localtime().tm_hour == 0 and time.localtime().tm_min == 0 and time.localtime().tm_sec == 0:
            day_for_school += 1
        elif day_for_school > 7:
            day_for_school = 1

class homework(StatesGroup):
    geog1 = State()
    him1 = State()
    angl1 = State()
    doprussk = State()
    istor2 = State()
    litra2 = State()
    geom2 = State()
    angl2 = State()
    algebra3 = State()
    angl3 = State()
    russk3 = State()
    istor4 = State()
    angl4 = State()
    obz4 = State()
    dopinf = State()
    algebra5 = State()
    obsh5 = State()
    inf5 = State()
    russk6 = State()
    litra6 = State()
    geom6 = State()
    biolog6 = State()
    angl6 = State()
    clear_days = State()

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
        await homework.geog1.set()
    elif message.text == 'Химия' and day_for_school == 1:
        await message.answer('Запиши домашнее задание')
        await homework.him1.set()
    elif message.text == 'Английский' and day_for_school == 1:
        await message.answer('Запиши домашнее задание')
        await homework.angl1.set()
    elif message.text == 'Доп. Русский':
        await message.answer('Запиши домашнее задание')
        await homework.doprussk.set()
    elif message.text == 'История' and day_for_school == 2:
        await message.answer('Запиши домашнее задание')
        await homework.istor2.set()
    elif message.text == 'Литература' and day_for_school == 2:
        await message.answer('Запиши домашнее задание')
        await homework.litra2.set()
    elif message.text == 'Геометрия' and day_for_school == 2:
        await message.answer('Запиши домашнее задание')
        await homework.geom2.set()
    elif message.text == 'Английский' and day_for_school == 2:
        await message.answer('Запиши домашнее задание')
        await homework.angl2.set()
    elif message.text == 'Алгебра' and day_for_school == 3:
        await message.answer('Запиши домашнее задание')
        await homework.algebra3.set()
    elif message.text == 'Английский' and day_for_school == 3:
        await message.answer('Запиши домашнее задание')
        await homework.angl3.set()
    elif message.text == 'Русский Язык' and day_for_school == 3:
        await message.answer('Запиши домашнее задание')
        await homework.russk3.set()
    elif message.text == 'История' and day_for_school == 4:
        await message.answer('Запиши домашнее задание')
        await homework.istor4.set()
    elif message.text == 'Английский' and day_for_school == 4:
        await message.answer('Запиши домашнее задание')
        await homework.angl4.set()
    elif message.text == 'ОБЖ' and day_for_school == 4:
        await message.answer('Запиши домашнее задание')
        await homework.obz4.set()
    elif message.text == 'Допю Информатика':
        await message.answer('Запиши домашнее задание')
        await homework.dopinf.set()
    elif message.text == 'Алгебра' and day_for_school == 5:
        await message.answer('Запиши домашнее задание')
        await homework.algebra5.set()
    elif message.text == 'Обществознание' and day_for_school == 5:
        await message.answer('Запиши домашнее задание')
        await homework.obsh5.set()
    elif message.text == 'Информатика' and day_for_school == 5:
        await message.answer('Запиши домашнее задание')
        await homework.inf5.set()
    elif message.text == 'Русский Язык' and day_for_school == 6:
        await message.answer('Запиши домашнее задание')
        await homework.russk6.set()
    elif message.text == 'Литература' and day_for_school == 6:
        await message.answer('Запиши домашнее задание')
        await homework.litra6.set()
    elif message.text == 'Биология' and day_for_school == 6:
        await message.answer('Запиши домашнее задание')
        await homework.biolog6.set()
    elif message.text == 'Геометрия' and day_for_school == 6:
        await message.answer('Запиши домашнее задание')
        await homework.geom6.set()
    elif message.text == 'Английский' and day_for_school == 6:
        await message.answer('Запиши домашнее задание')
        await homework.angl6.set()
    elif message.text == 'Очистить день':
        await message.answer('Выбери день')
        await homework.clear_days.set()
    elif message.text == 'Обновить':
        if day_for_school == 1:
            await message.answer('''Расписание на понедельник
            Чил и Каеф
            Астрономия
            География
            Химия
            Шведский
            Английский
            Доп. Русский''', reply_markup=monday_keyboard)
        if day_for_school == 2:
            await message.answer('''Расписание на вторник
            История
            Литература
            Литература
            История
            Геометрия
            Английский
            Английский''', reply_markup=tuesday_keyboard)
        if day_for_school == 3:
            await message.answer('''Расписание на среду
            Алгебра
            Английский
            Русский Язык
            Русский Язык
            Шведский
            Физика
            Физра''', reply_markup=wednesday_keyboard)
        if day_for_school == 4:
            await message.answer('''Расписание на четверг
            Физра
            История
            Английский
            Шведский
            ОБЖ
            Физика
            Доп. Информатика''', reply_markup=thursday_keyboard)
        if day_for_school == 5:
            await message.answer('''Расписание на пятницу
            Индивидульный проект
            Алгебра
            Обществознание
            Обществознание
            Алгебра
            Информатика''', reply_markup=friday_keyboard)
        if day_for_school == 6:
            await message.answer('''Расписание на субботу
            Русский Язык
            Литература
            Геометрия
            Биология
            Английский
            Физра''', reply_markup=saturday_keyboard)


@dp.message_handler(state=homework.geog1)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    geog1_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.him1)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    him1_obj = lesson
    await message.answer('Готово!')

    await state.finish()

@dp.message_handler(state=homework.angl1)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    angl1_obj = lesson
    await message.answer('Готово!')

    await state.finish()

@dp.message_handler(state=homework.doprussk)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    doprussk_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.istor2)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    istor2_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.litra2)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    litra2_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.angl2)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    angl2_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.geom2)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    geom2_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.algebra3)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    algebra3_obj= lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.angl3)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    angl3_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.russk3)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    russk3_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.istor4)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    istor4_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.angl4)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    angl4_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.obz4)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    obz4_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.algebra5)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    algebra5_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.obsh5)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    obsh5_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.algebra5)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    algebra5_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.inf5)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    inf5_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.russk6)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    russk6_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.litra6)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    litra6_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.geom6)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    geom6_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.biolog6)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    biolog6_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.angl6)
async def otvet(message: types.Message, state: FSMContext):
    lesson = message.text
    await state.update_data(
        {
            'lesson': lesson
        }
    )
    data = await state.get_data()
    lesson = data.get('lesson')
    angl6_obj = lesson
    await message.answer('Готово!')
    await state.finish()

@dp.message_handler(state=homework.clear_days)
async def otvet(message: types.Message, state: FSMContext):
    day = message.text
    await state.update_data(
        {
            'day': day
        }
    )
    data = await state.get_data()
    day = data.get('day')
    if day == 'Понедельник':
        geog1_obj = ''
        him1_obj = ''
        angl1_obj = ''
        doprussk_obj = ''
    elif day == 'Вторник':
        istor2_obj = ''
        litra2_obj = ''
        geom2_obj = ''
        angl2_obj = ''
    elif day == 'Среда':
        algebra3_obj = ''
        angl3_obj = ''
        russk3_obj = ''
    elif day == 'Четверг':
        istor4_obj = ''
        angl4_obj = ''
        obz4_obj = ''
        dopinf_obj = ''
    elif day == 'Пятница':
        algebra5_obj = ''
        obsh5_obj = ''
        inf5_obj = ''
    elif day == 'Суббота':
        russk6_obj = ''
        litra6_obj = ''
        geom6_obj = ''
        biolog6_obj = ''
        angl6_obj = ''



    await message.answer(f'{day} очистен')
    await state.finish()
threading.Thread(target=seconds).start()



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
