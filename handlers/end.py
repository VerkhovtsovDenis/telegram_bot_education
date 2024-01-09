from handlers.__libs__ import *


router = Router()


@router.callback_query()
async def commands_end_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"Неизвестный обработчик")
    await callback.answer()
    await state.set_state(FSMEvent.waiting_event_title)

@router.message(Command('log'))
async def commands_get_log(message: types.Message, state: FSMContext):
    with open('logger.log') as file:
        await message.answer(f"{file.readlines()}")
        message.text.lower()


@router.message()
async def commands_end_2(message: types.Message, state: FSMContext):
    await message.answer(f"Неизвестный обработчик, состояние={state}, сообщение={message.text}")
    await state.set_state(FSMEvent.waiting_event_title)
