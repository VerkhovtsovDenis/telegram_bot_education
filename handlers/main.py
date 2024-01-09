from handlers.__libs__ import *


router = Router()


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в нашего нового бота", parse_mode="Markdown", reply_markup=kb_menu)
    await state.set_state(FSMClient.waiting_main)

