import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv


def main():
    load_dotenv()
    API_TOKEN = os.getenv('TOKEN_BOT')
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)