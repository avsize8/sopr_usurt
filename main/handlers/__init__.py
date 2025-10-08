"""Инициализация всех роутеров"""
from aiogram import Router
from .start import router as start_router
from .help import router as help_router

# Создаем главный роутер
main_router = Router()

# Подключаем все роутеры
main_router.include_router(start_router)
main_router.include_router(help_router)

__all__ = ['main_router']