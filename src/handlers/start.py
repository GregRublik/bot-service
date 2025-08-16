from aiogram.types import Message

from keyboards.main_menu import get_main_menu_keyboard
from messages.texts import WELCOME_TEXT

async def command_start_handler(message: Message) -> None:
    keyboard = get_main_menu_keyboard()
    await message.answer(WELCOME_TEXT, reply_markup=keyboard.as_markup())
