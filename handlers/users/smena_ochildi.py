from aiogram import types
from keyboards.default.money_keyboard import pul_berish_menu
from data.config import ochet
from datetime import datetime as dt
from states.pul import Pul
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(text="Открыто")
async def smena_ochildi(msg: types.Message):
  await msg.answer(f"Qancha pul olib keldingiz dokonga?")
  await Pul.narx.set()


@dp.message_handler(state=Pul.narx)
async def uydan_kelgan_pul(msg: types.Message, state: FSMContext):
  try:
    float(msg.text)
  except ValueError:
    await msg.answer(f"Butun son kiriting")
  else:
    await msg.answer(f"Kiritildi", reply_markup=pul_berish_menu)
    ochet[dt.now().strftime("%D")]['uydan_kelgan_pul'] = float(msg.text)
    ochet[dt.now().strftime("%D")]['berilgan_pullar']={}
    ochet[dt.now().strftime("%D")]['berilgan_pullar']['kechagidan_berilgan_pul']=[]
    await state.finish()
