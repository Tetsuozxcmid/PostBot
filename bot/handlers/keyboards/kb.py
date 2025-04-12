from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Проверить номер",
                                  callback_data="create_order_btn")]
        ]
    )
    return kb
