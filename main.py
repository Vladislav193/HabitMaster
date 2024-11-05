import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.hendlers import router
from database import init_db

async def main():
    load_dotenv()
    API_TOKEN = os.getenv('TOKEN_BOT')
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    dp.include_router(router=router)
    await init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')