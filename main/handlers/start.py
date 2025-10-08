"""Обработчики команд запуска"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>! 👋\n"
        f"Я простой бот на aiogram.\n"
        f"Используй /help для получения списка команд."
    )
