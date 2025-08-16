from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_vacancy_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data="return to start menu")
    builder.button(text="Python Developer", callback_data="get test task")
    builder.button(text="Java Developer", callback_data="get test task")
    return builder
