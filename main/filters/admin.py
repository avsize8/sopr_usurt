"""Фильтры для администраторов"""
from aiogram.filters import BaseFilter
from aiogram.types import Message
from main.config import Config


class IsAdmin(BaseFilter):
    """Фильтр для проверки, является ли пользователь администратором"""

    async def __call__(self, message: Message) -> bool:
        if not Config.ADMIN_IDS:
            return False
        
        user_id = str(message.from_user.id)
        return user_id in Config.ADMIN_IDS
