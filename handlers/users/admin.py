import time

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="admin", user_id=ADMINS)
async def get_all_users(message: types.Message):
    await message.answer(text=f'/allusers - Foydalanuvchilarni ko`rish \n/reklama - Reklama yuborish '
                              f'\n/juma - Foydalanuvchilarni juma ayyomi bilan tabriklash'
                              f'\n/cleandb - Xotirani tozalash')


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="<i>Assalomu alaykum👋 <u>hurmatli "
                                                     "yangi kelgan foydalanuvchilar</u></i>"
                                                     "\n<b><i>Bizni tanlaganingizdan hursandmiz 🤗</i></b>",
                               parse_mode='HTML')
        time.sleep(1)


@dp.message_handler(text="/juma", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id,
                             photo='https://im0-tub-com.yandex.net/i?id=49e60701c8e30822b9a11cd03f5ea7d5&n=13' ,
                             caption="<i>Assalomu alaykum👋 <u>hurmatli "
                             "foydalanuvchilar</u></i>"
                             "\n<b><i>🕌Juma ayyomingiz muborak bo`lsin🤗</i></b>"
                                     "@tarixi_muhammadiybot", parse_mode='HTML')
        time.sleep(1)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
