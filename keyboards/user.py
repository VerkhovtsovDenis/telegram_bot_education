from keyboards.__libs__ import *


buttons_user = [

	[InlineKeyboardButton(text='Заполнить Имя', callback_data='name')],
	[InlineKeyboardButton(text='Заполнить Фамилию', callback_data='lname')],
	[InlineKeyboardButton(text='Заполнить телефон', callback_data='phone')],
	[InlineKeyboardButton(text='Заполнить почту', callback_data='email')],
	[InlineKeyboardButton(text="Назад", callback_data='user_cancel')]
]

kb_user = InlineKeyboardMarkup(inline_keyboard=buttons_user)
