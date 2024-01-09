from keyboards.__libs__ import *


buttons_event = [
	[InlineKeyboardButton(text='Заполнить название мероприятия', callback_data='title')],
	[InlineKeyboardButton(text='Заполнить тип мероприятия', callback_data='event_type')],
	[InlineKeyboardButton(text='Заполнить дату начала', callback_data='start_date')],
	[InlineKeyboardButton(text='Заполнить дату окончания', callback_data='end_date')],
	[InlineKeyboardButton(text='Заполнить ТЗ', callback_data='ts')],
	[InlineKeyboardButton(text="Назад", callback_data='event_cancel')]
]

kb_event = InlineKeyboardMarkup(inline_keyboard=buttons_event)
