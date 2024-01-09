import asyncio
import logging

from create_bot import dp, bot
from handlers import *



async def on_startup(_):
    print('Бот вышел в онлайн')


async def main():
    dp.include_router(handlers_main.router)
    dp.include_router(menu.router)
    dp.include_router(info.router)
    dp.include_router(application.router)
    dp.include_routers(event.router)
    dp.include_router(organization.router)
    dp.include_router(user.router)
    dp.include_router(end.router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == '__main__':
    asyncio.run(main())
