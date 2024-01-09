from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMTs.waiting_ts), F.data == 'place')
async def commands_ts_1(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите ТЗ к залу")
	await callback.answer()
	await state.set_state(FSMTs.waiting_ts_place)


@router.callback_query(StateFilter(FSMTs.waiting_ts), F.data == 'sound')
async def commands_ts_2(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите ТЗ на звуковое сопровождение")
	await callback.answer()
	await state.set_state(FSMTs.waiting_ts_sound)


@router.callback_query(StateFilter(FSMTs.waiting_ts), F.data == 'other')
async def commands_ts_3(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Введите иные пожелания")
	await callback.answer()
	await state.set_state(FSMTs.waiting_ts_other)


@router.callback_query(StateFilter(FSMTs.waiting_ts), F.data == 'user_cancel')
async def commands_ts_4(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.edit_text(f"Заполните поля:", reply_markup=kb_event)
	await callback.answer()
	await state.set_state(FSMEvent.waiting_event)
