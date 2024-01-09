from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMUser.waiting_user), F.data == 'name')
async def commands_user_1(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите имя")
	await callback.answer()
	await state.set_state(FSMUser.waiting_user_name)


@router.message(StateFilter(FSMUser.waiting_user))
async def commands_user_name_1(message: Message, state: FSMContext):
	pass


@router.callback_query(StateFilter(FSMUser.waiting_user), F.data == 'lname')
async def commands_user_2(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите фамилию")
	await callback.answer()
	await state.set_state(FSMUser.waiting_user_lname)


@router.callback_query(StateFilter(FSMUser.waiting_user), F.data == 'phone')
async def commands_user_3(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите телефон")
	await callback.answer()
	await state.set_state(FSMUser.waiting_user_phone)


@router.callback_query(StateFilter(FSMUser.waiting_user), F.data == 'email')
async def commands_user_4(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите почту")
	await callback.answer()
	await state.set_state(FSMUser.waiting_user_email)


@router.callback_query(StateFilter(FSMUser.waiting_user), F.data == 'user_cancel')
async def commands_user_5(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Заполните поля:", reply_markup=kb_organization)
	await callback.answer()
	await state.set_state(FSMOrganisation.waiting_organisation)
