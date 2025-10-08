import asyncio
import logging
from logging.handlers import RotatingFileHandler
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

# Импортируем роутеры
from handlers import main_router
from middleware.logging import LoggingMiddleware

# Загружаем переменные окружения
load_dotenv()

# Токен бота (получаем из переменных окружения)
BOT_TOKEN = os.getenv('TOKEN')

# Настройка логирования (консоль + файл с ротацией)
def setup_logging() -> logging.Logger:
    log_level_name = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    os.makedirs('logs', exist_ok=True)
    log_file_path = os.getenv('LOG_FILE', 'logs/bot.log')

    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Очищаем предыдущие хендлеры, если перезапускаем
    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Файл с ротацией
    file_handler = RotatingFileHandler(
        filename=log_file_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Шум от urllib3 и aiohttp можно приглушить при необходимости
    logging.getLogger('aiohttp.access').setLevel(logging.WARNING)

    # Логи aiogram на том же уровне
    logging.getLogger('aiogram').setLevel(log_level)

    app_logger = logging.getLogger(__name__)
    app_logger.info('Логирование настроено')
    return app_logger

logger = setup_logging()

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(main_router)

# Подключаем middleware для логирования
dp.message.middleware(LoggingMiddleware())
dp.callback_query.middleware(LoggingMiddleware())


async def main():
    """Основная функция для запуска бота"""
    logger.info("Запуск бота...")
    
    if not BOT_TOKEN:
        logger.error("TOKEN не найден! Создайте файл .env и добавьте TOKEN=your_token или BOT_TOKEN=your_token")
        return
    
    try:
        # На всякий случай снимаем webhook, если он был установлен где-то еще,
        # и очищаем висящие обновления, чтобы избежать конфликта getUpdates
        await bot.delete_webhook(drop_pending_updates=True)

        # Запускаем бота
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
