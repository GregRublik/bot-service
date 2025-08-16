from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Узнать о компании", callback_data="get info company")
    builder.button(text="Выбрать вакансию", callback_data="get vacancy")
    return builder

def get_back_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data="return to start menu")
    return builder
