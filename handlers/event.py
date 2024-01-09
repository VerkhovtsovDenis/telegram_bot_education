from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMEvent.waiting_event), F.data == 'title')
async def commands_event_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Введите название мероприятия")
    await callback.answer()
    await state.set_state(FSMEvent.waiting_event_title)


@router.callback_query(StateFilter(FSMEvent.waiting_event), F.data == 'event_type')
async def commands_event_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Какого уровня ваше мероприятие?")
    await callback.answer()
    await state.set_state(FSMEvent.waiting_event_type)


@router.callback_query(StateFilter(FSMEvent.waiting_event), F.data == 'start_date')
async def commands_event_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Введите дату и время начала мероприятия")
    await callback.answer()
    await state.set_state(FSMEvent.waiting_event_sdate)


@router.callback_query(StateFilter(FSMEvent.waiting_event), F.data == 'end_date')
async def commands_event_4(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Введите дату и время окончания мероприятия")
    await callback.answer()
    await state.set_state(FSMEvent.waiting_event_edate)


@router.callback_query(StateFilter(FSMEvent.waiting_event), F.data == 'ts')
async def commands_event_5(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Заполнить поля:", reply_markup=kb_ts)
    await callback.answer()
    await state.set_state(FSMTs.waiting_ts)


@router.callback_query(StateFilter(FSMEvent.waiting_event), F.data == 'event_cancel')
async def commands_event_6(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Начните заполнять поля заявки", reply_markup=kb_application)
    await callback.answer()
    await state.set_state(FSMApplication.waiting_application)
