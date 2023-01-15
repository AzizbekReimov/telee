from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

smenani_ochish = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='Открыто'),
    ],
  ],
resize_keyboard=True
)

smenani_yopish = ReplyKeyboardMarkup(keyboard=[[
  KeyboardButton(text='Закрыто'),
]])

pul_berish = ReplyKeyboardMarkup(keyboard=[[
  KeyboardButton(text="Кечаги пулдан"),
  KeyboardButton(text="Бугунги пулдан")
]])
