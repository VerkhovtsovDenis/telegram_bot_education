from keyboards.__libs__ import *


buttons_organization = [
	[InlineKeyboardButton(text='Заполнить имя организации', callback_data='org_name')],
	[InlineKeyboardButton(text='Заполнить тип организации', callback_data='org_type')],
	[InlineKeyboardButton(text='Заполнить ответственное лицо', callback_data='user')],
	[InlineKeyboardButton(text="Назад", callback_data='organization_cancel')]
]
kb_organization = InlineKeyboardMarkup(inline_keyboard=buttons_organization)
