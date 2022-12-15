from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

update_date_keyborard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
update_button = KeyboardButton('Обновить')
update_date_keyborard.add(update_button)





monday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) # расписание на понедельник
one_monday_lesson = KeyboardButton(text='Чил и Каеф')
two_monday_lesson = KeyboardButton(text='Астрономия')
three_monday_lesson = KeyboardButton(text='География')
four_monday_lesson = KeyboardButton(text='Химия')
five_monday_lesson = KeyboardButton(text='Шведский')
six_monday_lesson = KeyboardButton(text='Английский')
additionally_monday_lesson = KeyboardButton(text='Доп. Русский')
monday_keyboard.add(one_monday_lesson, two_monday_lesson, three_monday_lesson, four_monday_lesson, five_monday_lesson, six_monday_lesson, additionally_monday_lesson)


tuesday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_tuesday_lesson = KeyboardButton(text='История')
two_tuesday_lesson = KeyboardButton(text='Литра')
three_tuesday_lesson = KeyboardButton(text='Лиература')
four_tuesday_lesson = KeyboardButton(text='История')
five_tuesday_lesson = KeyboardButton(text='Геометрия')
six_tuesday_lesson = KeyboardButton(text='Английский')
seven_tuesday_lesson = KeyboardButton(text='Английский')
tuesday_keyboard.add(one_tuesday_lesson, two_tuesday_lesson, three_tuesday_lesson, four_tuesday_lesson, five_tuesday_lesson, six_tuesday_lesson, seven_tuesday_lesson)


wednesday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_wednesday_lesson = KeyboardButton(text='Алгебра')
two_wednesday_lesson = KeyboardButton(text='Английский')
three_wednesday_lesson = KeyboardButton(text='Русский Язык')
four_wednesday_lesson = KeyboardButton(text='Русский Язык')
five_wednesday_lesson = KeyboardButton(text='Шведский')
six_wednesday_lesson = KeyboardButton(text='Физика')
seven_wednesday_lesson = KeyboardButton(text='Физра')
wednesday_keyboard.add(one_wednesday_lesson, two_wednesday_lesson, three_wednesday_lesson, four_wednesday_lesson, five_wednesday_lesson, six_wednesday_lesson, seven_wednesday_lesson)


thursday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_thursday_lesson = KeyboardButton(text='Физра')
two_thursday_lesson = KeyboardButton(text='История')
three_thursday_lesson = KeyboardButton(text='Английский')
four_thursday_lesson = KeyboardButton(text='Шведский')
five_thursday_lesson = KeyboardButton(text='ОБЖ')
six_thursday_lesson = KeyboardButton(text='Физика')
additionally_thursday_lesson = KeyboardButton(text='Доп. Информатика')
thursday_keyboard.add(one_thursday_lesson, two_thursday_lesson, three_thursday_lesson, four_thursday_lesson, five_thursday_lesson, six_thursday_lesson)


friday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_friday_lesson = KeyboardButton(text='Индивидуальный проект')
two_friday_lesson = KeyboardButton(text='Алгебра')
three_friday_lesson = KeyboardButton(text='Обществознание')
four_friday_lesson = KeyboardButton(text='Обществознание')
five_friday_lesson = KeyboardButton(text='Алгебра')
six_friday_lesson = KeyboardButton(text='Информатика')
friday_keyboard.add(one_friday_lesson, two_friday_lesson, three_friday_lesson, four_friday_lesson, five_friday_lesson, six_friday_lesson)


saturday_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
one_saturday_lesson = KeyboardButton(text='Русский Язык')
two_saturday_lesson = KeyboardButton(text='Литература')
three_saturday_lesson = KeyboardButton(text='Геометрия')
four_saturday_lesson = KeyboardButton(text='Биология')
five_saturday_lesson = KeyboardButton(text='Английский')
six_saturday_lesson = KeyboardButton(text='Физра')
saturday_keyboard.add(one_saturday_lesson, two_saturday_lesson, three_saturday_lesson, four_saturday_lesson, five_saturday_lesson, six_saturday_lesson)
