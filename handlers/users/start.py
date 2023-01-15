from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.money_keyboard import smenani_ochish, pul_berish_menu
from data.config import ochet
from datetime import datetime as dt

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
  if dt.now().strftime("%D") not in ochet:
    ochet[dt.now().strftime("%D")] = {}
  await message.answer(f"Salom, {message.from_user.full_name}!",
                       reply_markup=smenani_ochish)
