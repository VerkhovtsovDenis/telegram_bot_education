from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMOrganisation.waiting_organisation), F.data == 'org_name')
async def commands_organisation_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Введите имя организации")
    await callback.answer()
    await state.set_state(FSMOrganisation.waiting_organisation_name)


@router.message(StateFilter(FSMOrganisation.waiting_organisation_name))
async def commands_organisation_name(message: Message, state: FSMContext):
    # Подключение к БД,
    print(message.text)
    await state.set_state(FSMOrganisation.waiting_organisation)


@router.callback_query(StateFilter(FSMOrganisation.waiting_organisation), F.data == 'org_type')
async def commands_organisation_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Введите тип организации")
    await callback.answer()
    await state.set_state(FSMOrganisation.waiting_organisation_type)


@router.callback_query(StateFilter(FSMOrganisation.waiting_organisation), F.data == 'user')
async def commands_organisation_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Заполнить поля:", reply_markup=kb_user)
    await callback.answer()
    await state.set_state(FSMUser.waiting_user)


@router.callback_query(StateFilter(FSMOrganisation.waiting_organisation), F.data == 'organization_cancel')
async def commands_organisation_4(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Начните заполнять поля заявки", reply_markup=kb_application)
    await callback.answer()
    await state.set_state(FSMApplication.waiting_application)
