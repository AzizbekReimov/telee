from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from datatime import datatime as dt
from keyboards.default.money_keyboard import smenani_ochish, smenani_yopish, pul_berish
from states.pul import Pul

@dp.message_handler(text="Открыто")
async def ochildi(msg: Message):
  await msg.answer(f"Uyingizdan qancha pul olib keldingiz?")
  await Pul.narx.set()

@dp.message_handler(state=Pul.narx)
async def uydan_kelgan_pul(msg: Message, state: FSMContext):
  try:
    float(msg.text)
  except ValueError:
    await msg.answer(f"Butun son kiriting!")
  else:
    await state.update_data(
      {"uydan_kelgan_pul":float(msg.text)}
    )
