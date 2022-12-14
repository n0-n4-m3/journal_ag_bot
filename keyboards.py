from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


kb_start = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Регистрация', callback_data='REGISTER')).add(InlineKeyboardButton('Помощь', callback_data='HELP'))
kb_help = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Регистрация', callback_data='REGISTER'))
kb_in = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Выйти из АГ')).insert(KeyboardButton('Профиль')).insert(KeyboardButton('Помощь')).add(KeyboardButton('Обратная связь'))
kb_out = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Я в АГ')).insert(KeyboardButton('Профиль')).insert(KeyboardButton('Помощь')).add(KeyboardButton('Обратная связь'))
cancel_st_kb = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Отмена', callback_data='cancel_st'))