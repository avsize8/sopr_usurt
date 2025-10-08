import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

class Config:
    """Класс конфигурации для бота"""
    
    # Токен бота
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    # Настройки логирования
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Дополнительные настройки
    ADMIN_IDS = os.getenv('ADMIN_IDS', '').split(',') if os.getenv('ADMIN_IDS') else []
    
    @classmethod
    def validate(cls):
        """Проверяет корректность конфигурации"""
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN не найден в переменных окружения!")
        return True
