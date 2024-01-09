from keyboards.__libs__ import *


buttons_application = [
	[InlineKeyboardButton(text='Заполнить поле организация', callback_data='org')],
	[InlineKeyboardButton(text='Заполнить поле мероприятие', callback_data='event')],
	[InlineKeyboardButton(text="Назад", callback_data='application_cancel')]
]

kb_application = InlineKeyboardMarkup(inline_keyboard=buttons_application)
