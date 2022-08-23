import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startMenuKeys import menuStart
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f'<i>Assalom alaykum,👋 </i>{message.from_user.full_name}! '
                         f'<a href="https://t.me/tarixi_muhammadiybot"><i>Tarixi Muhammadiy Bot</i></a>ga xush kelibsiz 🤗'
                         f"\n<b>Mendan <i>📖Tarixi Muhammadiy Kitobining</i> "
                         f"Audolarini🎧</b> topa olasiz", reply_markup=menuStart)

    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)