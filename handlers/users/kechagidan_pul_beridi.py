from aiogram import types
from keyboards.default.money_keyboard import pul_berish_menu
from data.config import ochet
from datetime import datetime as dt
from states.pul import Pul
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(text="Кечаги пулдан")
async def smena_ochildi(msg: types.Message):
  await msg.answer(f"Qancha pul berdingiz?")
  await Pul.narx.set()


@dp.message_handler(state=Pul.narx)
async def uydan_kelgan_pul(msg: types.Message, state: FSMContext):
  try:
    float(msg.text)
  except ValueError:
    await msg.answer(f"Butun son kiriting")
  else:
    await state.update_data(
      {"berilgan_pul":float(msg.text),
      "pul_berilgan_vaqt":f"{dt.now().hour}:{dt.now().minute}:{dt.now().second}"}
    )
    await msg.answer(f"Kimga berdingiz?")
    await Pul.next()

@dp.message_handler(state=Pul.narx)
async def uydan_kelgan_pul(msg: types.Message, state: FSMContext):
  await state.update_data(
       {"kimga_berildi":msg.text}
  )
  data = await state.get_data()
  berilgan_pul = data.get("berilgan_pul")
  pul_berilgan_vaqt = data.get("pul_berilgan_vaqt")
  kimga_berildi = data.get("kimga_berildi")
  ochet[dt.now().strftime("%D")]['berilgan_pullar']['kechagidan_berilgan_pul']=[]
  ochet[dt.now().strftime("%D")]['berilgan_pullar']['kechagidan_berilgan_pul'].append(list(berilgan_pul, pul_berilgan_vaqt, kimga_berildi))
  await state.finish()
