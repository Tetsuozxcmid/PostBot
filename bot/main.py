import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from config import settings
from database.db import session_maker, engine, Base
from handlers.routes.start import router as start_router
from handlers.routes.create_order import router as create_order_router

bot = Bot(token=settings.BOT_TOKEN)

dp = Dispatcher()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_db()
    dp.include_router(start_router)
    dp.include_router(create_order_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
