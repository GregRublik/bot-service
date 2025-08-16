import asyncio
import logging
import sys
from aiogram import Dispatcher, F

from aiogram.filters import CommandStart
from aiohttp import web
from config import bot

from consumer import broker

from handlers.start import command_start_handler
from handlers.vacancy import handler_rag_run, handler_return_to_menu
from handlers.company import get_info_company
from handlers.echo import echo_handler

dp = Dispatcher()

# Регистрация хэндлеров
dp.message.register(command_start_handler, CommandStart())
dp.callback_query.register(handler_rag_run, F.data == "get vacancy")
dp.callback_query.register(handler_return_to_menu, F.data == "return to start menu")
dp.callback_query.register(get_info_company, F.data == "get info company")
dp.message.register(echo_handler)


async def main():

    async with broker:
        await asyncio.gather(
            broker.start(),
            dp.start_polling(bot),
        )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye!")
