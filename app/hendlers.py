from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
router= Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот для остлеживания твоих привычек.")

    user_id = message.from_user.id
    user_name = message.from_user.first_name
