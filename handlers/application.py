from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMApplication.waiting_application), F.data == 'org')
async def commands_application_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Заполните поля:", reply_markup=kb_organization)
    await callback.answer()
    await state.set_state(FSMOrganisation.waiting_organisation)


@router.callback_query(StateFilter(FSMApplication.waiting_application), F.data == 'event')
async def commands_application_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Заполните поля:", reply_markup=kb_event)
    await callback.answer()
    await state.set_state(FSMEvent.waiting_event)


@router.callback_query(StateFilter(FSMApplication.waiting_application), F.data == 'application_cancel')
async def commands_application_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Добро пожаловать в нашего нового бота", reply_markup=kb_menu)
    await callback.answer()
    await state.set_state(FSMClient.waiting_main)
