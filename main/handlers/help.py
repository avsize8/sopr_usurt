"""Обработчики команд помощи"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help"""
    help_text = """
<b>Доступные команды:</b>

/start - Запуск бота
/help - Показать это сообщение

    """
    await message.answer(help_text)
