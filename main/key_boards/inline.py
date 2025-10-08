"""Inline клавиатуры"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu() -> InlineKeyboardMarkup:
    """Главное меню с inline кнопками"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📊 Статистика", callback_data="stats"),
                InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")
            ],
            [
                InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help"),
                InlineKeyboardButton(text="🔗 Ссылки", callback_data="links")
            ]
        ]
    )
    return keyboard


def get_back_button() -> InlineKeyboardMarkup:
    """Кнопка "Назад" """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
        ]
    )
    return keyboard
