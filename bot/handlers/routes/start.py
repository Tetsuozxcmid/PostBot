from aiogram import Router

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters import Filter as f
from handlers.keyboards.kb import get_main_kb


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Здравствуйте, ваш заказ RA644000001RU", reply_markup=get_main_kb())
