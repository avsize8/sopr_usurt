"""Reply клавиатуры"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    """Главная reply клавиатура"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="⚙️ Настройки")],
            [KeyboardButton(text="ℹ️ Помощь"), KeyboardButton(text="🔗 Ссылки")],
            [KeyboardButton(text="📞 Контакты")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard


def get_contact_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для запроса контакта"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📞 Поделиться контактом", request_contact=True)],
            [KeyboardButton(text="⬅️ Назад")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard
