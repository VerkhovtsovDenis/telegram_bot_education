from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMClient.waiting_main), F.data == 'application_start')
async def commands_menu_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Начните заполнять поля заявки", reply_markup=kb_application)
    await callback.answer()
    await state.set_state(FSMApplication.waiting_application)


@router.callback_query(StateFilter(FSMClient.waiting_main), F.data == 'statistics_info')
async def commands_menu_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Вот ваша статистика за день: ...", reply_markup=kb_info)
    await callback.answer()
    await state.set_state(FSMInfo.waiting_info)

