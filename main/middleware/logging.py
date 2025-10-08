"""Middleware для логирования"""
import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    """Middleware для логирования сообщений и callback'ов"""

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # Логируем входящие сообщения
        if isinstance(event, Message):
            logger.info(
                f"Получено сообщение от {event.from_user.full_name} "
                f"({event.from_user.id}): {event.text}"
            )
        elif isinstance(event, CallbackQuery):
            logger.info(
                f"Получен callback от {event.from_user.full_name} "
                f"({event.from_user.id}): {event.data}"
            )

        # Продолжаем обработку
        return await handler(event, data)
