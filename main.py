import asyncio, os
from Logging.logger import get_logger
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from Base.commands import base_router


load_dotenv()
logger = get_logger(__name__)

async def main():
    token: str = os.getenv("BOT_TOKEN")
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(base_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logger.info('Start bot')
        asyncio.run(main())
    except Exception as e:
        logger.critical(e)
