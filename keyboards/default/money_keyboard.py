from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

smenani_ochish = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text='Открыто'),
  ],
],
                                     resize_keyboard=True)

pul_berish_menu = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="Кечаги пулдан"),
  ],
  [
    KeyboardButton(text="Бугунги пулдан"),
  ],
  [
    KeyboardButton(text='Закрыто'),
  ],
  [
    KeyboardButton(text='Korish'),
  ],
],
                                      resize_keyboard=True)
