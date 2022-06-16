import asyncio
import logging
from logging.handlers import RotatingFileHandler
from os import environ

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.handlers import register_handlers


BOT_TOKEN = environ['BOT_TOKEN']


console_out_hundler = logging.StreamHandler()
rotate_file_handler = RotatingFileHandler(
    'logs/bot.log',
    maxBytes=5000000,
    backupCount=2,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(funcName)s: %(message)s',
    handlers=[console_out_hundler, rotate_file_handler],
)


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(bot)

    commands = [
        BotCommand(command='/start', description='начать'),
        BotCommand(command='/help', description='помощь'),
    ]
    await bot.set_my_commands(commands)

    register_handlers(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
