from aiogram.types import CallbackQuery

from keyboards.main_menu import get_back_keyboard

async def get_info_company(callback: CallbackQuery):
    keyboard = get_back_keyboard()
    await callback.message.edit_text(
        """Я языковой помощник! ✨
Пожалуйста, задавайте ваши вопросы! 
        """,
        reply_markup=keyboard.as_markup()
    )