from keyboards.__libs__ import *


buttons_ts = [
	[InlineKeyboardButton(text='Заполнить ТЗ на помещение', callback_data='place')],
	[InlineKeyboardButton(text='Заполнить ТЗ на звук', callback_data='sound')],
	[InlineKeyboardButton(text='Заполнить ТЗ на остальное', callback_data='other')],
	[InlineKeyboardButton(text="Назад", callback_data='ts_cancel')]
]

kb_ts = InlineKeyboardMarkup(inline_keyboard=buttons_ts)
