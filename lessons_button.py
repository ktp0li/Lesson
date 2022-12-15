from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup







monday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) # расписание на понедельник


three_monday_lesson = KeyboardButton(text='География')
four_monday_lesson = KeyboardButton(text='Химия')
update_button = KeyboardButton('Обновить')

six_monday_lesson = KeyboardButton(text='Английский')
additionally_monday_lesson = KeyboardButton(text='Доп. Русский')
monday_keyboard.add(three_monday_lesson, four_monday_lesson, six_monday_lesson, additionally_monday_lesson, update_button)


tuesday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_tuesday_lesson = KeyboardButton(text='История')
two_tuesday_lesson = KeyboardButton(text='Литература')
five_tuesday_lesson = KeyboardButton(text='Геометрия')
six_tuesday_lesson = KeyboardButton(text='Английский')
update_button = KeyboardButton('Обновить')
tuesday_keyboard.add(one_tuesday_lesson, two_tuesday_lesson,  five_tuesday_lesson, six_tuesday_lesson, update_button)


wednesday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_wednesday_lesson = KeyboardButton(text='Алгебра')
two_wednesday_lesson = KeyboardButton(text='Английский')
three_wednesday_lesson = KeyboardButton(text='Русский Язык')


wednesday_keyboard.add(one_wednesday_lesson, two_wednesday_lesson, three_wednesday_lesson, update_button)


thursday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

two_thursday_lesson = KeyboardButton(text='История')
three_thursday_lesson = KeyboardButton(text='Английский')
five_thursday_lesson = KeyboardButton(text='ОБЖ')
additionally_thursday_lesson = KeyboardButton(text='Доп. Информатика')
update_button = KeyboardButton('Обновить')
thursday_keyboard.add(two_thursday_lesson, three_thursday_lesson, five_thursday_lesson, update_button)


friday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

two_friday_lesson = KeyboardButton(text='Алгебра')

four_friday_lesson = KeyboardButton(text='Обществознание')

six_friday_lesson = KeyboardButton(text='Информатика')
update_button = KeyboardButton('Обновить')
friday_keyboard.add(two_friday_lesson, four_friday_lesson, six_friday_lesson, update_button)


saturday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_saturday_lesson = KeyboardButton(text='Русский Язык')
two_saturday_lesson = KeyboardButton(text='Литература')
three_saturday_lesson = KeyboardButton(text='Геометрия')
four_saturday_lesson = KeyboardButton(text='Биология')
five_saturday_lesson = KeyboardButton(text='Английский')

update_button = KeyboardButton('Обновить')
saturday_keyboard.add(one_saturday_lesson, two_saturday_lesson, three_saturday_lesson, four_saturday_lesson, five_saturday_lesson, update_button)
