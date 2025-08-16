from aiogram.types import CallbackQuery

from keyboards.main_menu import get_main_menu_keyboard
from keyboards.vacancy_menu import get_vacancy_menu_keyboard

from messages.texts import WELCOME_TEXT

async def handler_rag_run(callback: CallbackQuery):
    keyboard = get_vacancy_menu_keyboard()
    await callback.message.edit_text(
        "Выберите вакансию для получения тестового задания",
        reply_markup=keyboard.as_markup()
    )

async def handler_return_to_menu(callback: CallbackQuery):
    keyboard = get_main_menu_keyboard()
    await callback.message.edit_text(WELCOME_TEXT, reply_markup=keyboard.as_markup())