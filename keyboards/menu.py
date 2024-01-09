from keyboards.__libs__ import *


buttons_menu = [
	[InlineKeyboardButton(text='Начать заполнение заявки', callback_data='application_start')],
	[InlineKeyboardButton(text='Посмотреть статистику', callback_data='statistics_info')]
]
kb_menu = InlineKeyboardMarkup(inline_keyboard=buttons_menu)

buttons_info = [
	[InlineKeyboardButton(text='Назад', callback_data='info_cancel')]
]
kb_info = InlineKeyboardMarkup(inline_keyboard=buttons_info)
