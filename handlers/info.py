from handlers.__libs__ import *


router = Router()


@router.callback_query(StateFilter(FSMInfo.waiting_info), F.data == 'info_cancel')
async def commands_info_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Добро пожаловать в нашего нового бота", reply_markup=kb_menu)
    await callback.answer()
    await state.set_state(FSMClient.waiting_main)
