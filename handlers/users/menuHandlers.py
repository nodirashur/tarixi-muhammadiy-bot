import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_data import course_callback, coursebir_callback, courseikki_callback, \
    courseuch_callback, coursetort_callback, coursebesh_callback, courseolti_callback, courseyetti_callback, \
    coursesakkiz_callback, coursetoqqiz_callback, courseon_callback, courseonbir_callback
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, coursesMenubir, coursesMenuikki, \
    coursesMenuuch, coursesMenutort, coursesMenubesh, coursesMenuolti, coursesMenuyetti, coursesMenusakkiz, \
    coursesMenutoqqiz, coursesMenuon, coursesMenuonbir, ortha
from loader import dp


@dp.callback_query_handler(text="tarixikitob")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer_document(document='https://t.me/ndrbke/21', reply_markup=ortha)
    await call.answer(cache_time=60)


@dp.message_handler(text_contains="Boshlash")
async def select_category(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    await message.answer(f"Bu bo`limlardan birini tanlang", reply_markup=categoryMenu)


@dp.message_handler(text_contains="ℹ️Qoʼllanma")
async def select_category(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    await message.answer(f"<b>Mendan Tarixi Muhammadiy Kitobining 📚 barcha audio🎧 qismlarini topa olasiz.</b>"
                         f"\n<i>Buning uchun <b>Boshlash</b>  ⤵ tugmasini bosing</i>. "
                         f"\n<i>👨‍💻Dasturchi: <b>@ashuroff_dev</b></i>")


@dp.callback_query_handler(text="tarixi")
@dp.callback_query_handler(text="cancelbir")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel")
@dp.callback_query_handler(text="tarixiback")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz

    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()


# CallbackData yordamida filtrlash
@dp.callback_query_handler(course_callback.filter(item_name="tarix1"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy/2',
                                    caption='KIRISH. "SO\'Z BOSHI" \n⏳ 1:23 \n💾 700 KB')


@dp.callback_query_handler(course_callback.filter(item_name="tarix3"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/242',
                                    caption='2-qism. "Emizdirilishlari" \n⏳ 4:58 \n💾 4.5 MB')


@dp.callback_query_handler(course_callback.filter(item_name="tarix2"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/241',
                                    caption='1-qism. "Payg\'ambarimizning nasablari va tug\'ulishlari"'
                                            '\n⏳ 6:20 \n💾 5.8 MB')


@dp.callback_query_handler(course_callback.filter(item_name="tarix4"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/243',
                                    caption='3-qism. "Ko\'ksi yorilish voqeasi"'
                                            '\n⏳ 3:33 \n💾 3.2 MB')


@dp.callback_query_handler(course_callback.filter(item_name="tarix5"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/244',
                                    caption='4-qism. "Onalari bilan Madinaga safar va undan qaytishlari"'
                                            '\n⏳ 3:07 \n💾 2.8 MB')


@dp.callback_query_handler(course_callback.filter(item_name="tarix6"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/245',
                                    caption='5-qism. "Amakilari Abu Tolibning tarbiyasiga o\'tishlari"'
                                            '\n⏳ 10:39 \n💾 9.7 MB')


@dp.callback_query_handler(course_callback.filter(item_name="tarix7"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/248',
                                    caption='6-qism. "Xadicha savdogarchiligiga vakil"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix8"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/249',
                                    caption='7-qism. "Xadichaga nikohlanishlari"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix9"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/250',
                                    caption='8-qism. "Baytullohning dastlabki binosi"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix10"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/251',
                                    caption='9-qism. "Hajarul asvad tarixi"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix11"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/252',
                                    caption='10-qism. "Payg\'ambarlik vahiyning kelishi"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix12"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/254',
                                    caption='11-qism. "Amir Hamzaning Islomga kirishi"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix13"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/255',
                                    caption='12-qism. "Hazrati Umarning imon keltirishlari"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix14"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/256',
                                    caption='13-qism. "Islom diniga umumiy da\'vat"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix15"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/257',
                                    caption='14-qism. "Habashistonga ikkinchi hijrat"')


@dp.callback_query_handler(course_callback.filter(item_name="tarix16"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/258',
                                    caption='15-qism. "Najoshiyga qarshi voqea"')


@dp.callback_query_handler(course_callback.filter(item_name="tarixkeyin1"))
@dp.callback_query_handler(text="cancelikki")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenubir)
    await call.answer(cache_time=60)


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix17"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/259',
                                    caption='16-qism. "Sahiyfa voqeasi"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix18"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/260',
                                    caption='17-qism. "Tufayl ibn abu Amrning Islomga kirishi"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix19"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/261',
                                    caption='18-qism. "Bani Qays shoiri A\'shoning voqeasi"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix20"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/262',
                                    caption='19-qism. "Payg\'ambarimizni masxara qilgan"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix21"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/263',
                                    caption='20-qism. "Rukona ibn Abdu Yazid voqeasi "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix22"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/264',
                                    caption='21-qism. "Xadicha onamizning vafotlari "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix23"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/265',
                                    caption='22-qism. "Toif xalqini dinga da\'vat qilish  "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix24"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/266',
                                    caption='23-qism. "Meroj voqeasi"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix25"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy/26',
                                    caption='24-qism. "Qurayshdan boshqa qabilalarni islomga da\'vat qilish"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix26"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/269',
                                    caption='25-qism. "Dorun nadva maslahati"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix27"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/270',
                                    caption='26-qism. "Madinaga hijrat"')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix28"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/271',
                                    caption='27-qism. "Payg\'ambarimizning Madinaga kirishlari "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix29"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/272',
                                    caption='28-qism. "Islom olamida qurilgan birinchi masjid "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix30"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/273',
                                    caption='29-qism. "Azonning joriy etilishi "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix31"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/274',
                                    caption='30-qism. "Madina yahudlarining tarixi "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarix32"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy/33',
                                    caption='31-qism. "G\'azotning boshlanishi  "')


@dp.callback_query_handler(coursebir_callback.filter(item_name="tarixkeyin2"))
@dp.callback_query_handler(text="canceluch")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenuikki)
    await call.answer(cache_time=60)


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix33"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy/34',
                                    caption='32-qism. "Buvot G\'azoti"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix34"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy/35',
                                    caption='33-qism. "Al-Ushayra g\'azoti"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix35"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/275',
                                    caption='34-qism. "Qiblaning o\'zgarishi"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix36"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/276',
                                    caption='35-qism. "Ro\'zaning farz bo\'lishi"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix37"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/277',
                                    caption='36-qism. "Zakotning farz bo\'lishi"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix38"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/278',
                                    caption='37-qism. "Badr \'azoti"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix39"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/279',
                                    caption='38-qism. "Asirlar haqida muzokara"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix40"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/280',
                                    caption='39-qism. "Qaynuqo\' g\'azoti"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix41"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/281',
                                    caption='40-qism. "Saviq g\'azoti"')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix42"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/282',
                                    caption='41-qism. "Ka\'b ibn Ashrafning o\'ldirilishi "')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix43"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/283',
                                    caption='42-qism. "G\'atfon g\'azoti "')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix44"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/284',
                                    caption='43-qism. "Uhud g\'azoti" 1-qism')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix45"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/285',
                                    caption='43-qism. "Uhud g\'azoti" 2-qism')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix46"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/286',
                                    caption='43-qism. "Uhud g\'azoti" 3-qism')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix47"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/287',
                                    caption='43-qism. "Uhud g\'azoti" 4-qism')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarix48"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/288',
                                    caption='43-qism. "Uhud g\'azoti" 5-qism')


@dp.callback_query_handler(courseikki_callback.filter(item_name="tarixkeyin3"))
@dp.callback_query_handler(text="canceltort")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenuuch)
    await call.answer(cache_time=60)


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix49"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/289',
                                    caption='44-qism. "Hamroul Asad g\'azoti"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix50"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/290',
                                    caption='45-qism. "Urana voqeasi"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix51"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/291',
                                    caption='46-qism. "Azal va Qora qabilalarning xiyonatlari"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix52"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/292',
                                    caption='47-qism. "Mauna voqeasi"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix53"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/293',
                                    caption='48-qism. "Bani Nozir g\'azoti "')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix54"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/294',
                                    caption='49-qism. "Zotir Riqo\' g\'azoti "')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix55"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/295',
                                    caption='50-qism. "Ikkinchi Badr g\'azoti "')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix56"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/296',
                                    caption='51-qism. "Dumatul Jandal g\'azoti"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix57"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/297',
                                    caption='52-qism. "Bani mustaqil g\'zoti "')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix58"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/298',
                                    caption='53-qism. "Yana bir voqea"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix59"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/299',
                                    caption='54-qism. "Xandaq g\'azoti"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix60"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/300',
                                    caption='55-qism. "Bani Qurayza g\'azoti"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix61"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/301',
                                    caption='56-qism. "Quruto\' chopulli"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix62"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/302',
                                    caption='57-qism. "Bani Lihyon g\'azoti"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix63"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/303',
                                    caption='58-qism. "G\'oba g\'azoti"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarix64"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/304',
                                    caption='59-qism. "Zayd Ibn Horisaning chopulli"')


@dp.callback_query_handler(courseuch_callback.filter(item_name="tarixkeyin4"))
@dp.callback_query_handler(text='cancelbesh')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenutort)
    await call.answer(cache_time=60)


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix65"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/305',
                                    caption='60-qism. "Hudaybiya qissasi 1-qism"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix66"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/306',
                                    caption='60-qism. "Hudaybiya qissasi 2-qism"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix67"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/307',
                                    caption='61-qism. "Xaybar g\'azoti"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix68"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/308',
                                    caption='62-qism. "G\'atfon qabilasining voqeasi"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix69"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/309',
                                    caption='63-qism "Payg\'ambarimizning podsholarga yozgan nomalari"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix70"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/310',
                                    caption='64-qism "Rum podshosi Qaysarga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix71"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/311',
                                    caption='65-qism "Eron shohi Xisvarga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix72"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/312',
                                    caption='66-qism "Habashiston podshosi Najoshiyga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix73"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/313',
                                    caption='67-qism "Misr podshohi Muqavqisga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix74"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/314',
                                    caption='68-qism "Bahrayn podshohi Munzir Ibn Soviyga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix75"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/315',
                                    caption='69-qism "Ummon podsholariga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix76"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/316',
                                    caption='70-qism "Yomoma o\'kasining amiri Havzaga yuborilgan noma"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix77"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/317',
                                    caption='71-qism "Xoris Ibn Abu Shimrga yuborgan maktublari"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix78"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/318',
                                    caption='72-qism "Vodil Quro voqeasi"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix79"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/319',
                                    caption='73-qism. "Quraysh bahodirlaridan uch kishining iymon keltirishlari"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarix80"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/320',
                                    caption='74-qism. "Havozin voqeasi"')


@dp.callback_query_handler(coursetort_callback.filter(item_name="tarixkeyin5"))
@dp.callback_query_handler(text='cancelolti')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenubesh)
    await call.answer(cache_time=60)


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix81"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/321',
                                    caption='75-qism.  Bani Murra voqeasi')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix82"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/322',
                                    caption='76-qism. Mayfa\'a voqeasi')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix83"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/323',
                                    caption='77-qism. G\'atfon voqeasi')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix84"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/324',
                                    caption='78-qism. Umratul qazo voqeasi')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix85"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/325',
                                    caption='79-qism. G\'olib ibn Abdulloh chopuli')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix86"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/326',
                                    caption='80-qism. Bani Murra qabilasiga chopul')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix87"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/327',
                                    caption='81-qism. Mu\'ta g\'azoti ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix88"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/328',
                                    caption='82-qism. Zotus-Salosil g\'azoti ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix89"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/329',
                                    caption='83-qism. Al-Xabat g\'azoti ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix89"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/329',
                                    caption='83-qism. Al-Xabat g\'azoti ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix90"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/tarixi_muhammadiy_from_azonuzfm/95',
                                    caption='84-qism. Makka shahrining fathi ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix91"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/tarixi_muhammadiy_from_azonuzfm/96',
                                    caption='85-qism. Hunayn g\'azoti ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix92"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/tarixi_muhammadiy_from_azonuzfm/97',
                                    caption='86-qism. Tabuk g\'azoti')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix93"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/336',
                                    caption='87-qism. Najron elchilari ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix94"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/337',
                                    caption='88-qism. Doriyunlar voqeasi ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix95"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/338',
                                    caption='89-qism. Bani Omir elchilari ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarix96"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/339',
                                    caption='90-qism. Zimom ibn Sa\'laba voqeasi ')


@dp.callback_query_handler(coursebesh_callback.filter(item_name="tarixkeyin6"))
@dp.callback_query_handler(text='cancelyetti')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenuolti)
    await call.answer(cache_time=60)


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix97"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/340',
                                    caption='91-qism. Abulqays elchilari')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix98"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/341',
                                    caption='92-qism. Bani Hanifa qabilasining elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix99"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/342',
                                    caption='93-qism. Tay qabilasi elchilari')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix100"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/343',
                                    caption='94-qism. Adiy Ibn Hotam qisasi')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix101"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/344',
                                    caption='95-qism. Kinda qabilasining elchilari')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix102"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/345',
                                    caption='96-qism. Azdi Shanu\'a qabilasining elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix103"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/346',
                                    caption='97-qism. Himyar podshosi elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix104"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/347',
                                    caption='98-qism. Farva ibn Amrul-Juzomiy elchisi')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix105"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/348',
                                    caption='99-qism. Bani Horis qabilasining elchisi ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix106"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/349',
                                    caption='100-qism. Hamdon qabilasi elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix107"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/350',
                                    caption='101-qism. Tujib qabilasidan kelgan elchilar ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix108"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/351',
                                    caption='102-qism. Bani Sa\'laba qabilasining elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix109"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/352',
                                    caption='103-qism. Bani Sa\'d elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix110"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/353',
                                    caption='104-qism. Bani Fazora qabilasining elchilari ')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix111"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/354',
                                    caption='105-qism. Bani Asad qabilasining elchilari')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarix112"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/355',
                                    caption='106-qism. Bani Uzra qabilasining elchilari')


@dp.callback_query_handler(courseolti_callback.filter(item_name="tarixkeyin7"))
@dp.callback_query_handler(text='cancelsakkiz')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenuyetti)
    await call.answer(cache_time=60)


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix113"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/356',
                                    caption='107-qism. Bani Baliy qabilasining elchilari ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix114"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/357',
                                    caption='108-qism. Zi Murra qabilasining elchilari')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix115"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/358',
                                    caption='109-qism. Havlon qabilasining elchilari')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix116"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/359',
                                    caption='110-qism. Bani Muhorib elchilari ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix117"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/360',
                                    caption='111-qism. Sudo qabilasining elchilari ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix118"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/361',
                                    caption='112-qism. Naha\' qabilasining elchilari ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix119"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/362',
                                    caption='113-qism. Rasululloh S.A.Vning mo\'jizalari')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix120"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/363',
                                    caption='114-qism. Ikkinchi mo\'jiza  ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix121"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/364',
                                    caption='115-qism. Uchinchi mo\'jiza')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix122"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/365',
                                    caption='116-qism. To\'rtinchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix123"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/366',
                                    caption='117-qism. Beshinchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix124"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/367',
                                    caption='118-qism. Oltinchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix125"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/368',
                                    caption='120-qism. Yettinchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix126"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/369',
                                    caption='121-qism. Sakkizinchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix127"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/374',
                                    caption='122-qism. To\'qqizinchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarix128"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/375',
                                    caption='122-qism. O\'ninchi mo\'jiza ')


@dp.callback_query_handler(courseyetti_callback.filter(item_name="tarixkeyin8"))
@dp.callback_query_handler(text='canceltoqqiz')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenusakkiz)
    await call.answer(cache_time=60)


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix129"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/376',
                                    caption='123-qism. O\'n birinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix130"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/377',
                                    caption='124-qism. O\'n ikkinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix131"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/378',
                                    caption='125-qism. O\'n uchinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix132"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/379',
                                    caption='126-qism. O\'n to\'rtinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix133"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/380',
                                    caption='127-qism. O\'n beshinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix134"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/381',
                                    caption='128-qism. O\'n oltinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix135"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/382',
                                    caption='129-qism. O\'n yettinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix136"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/383',
                                    caption='130-qism. O\'n sakkizinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix137"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/384',
                                    caption='131-qism. O\'n to\'qqizinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix138"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/385',
                                    caption='132-qism. Yigirmanchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix139"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/386',
                                    caption='133-qism. Yigirma birinchi mo\'jiza ')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix140"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/387',
                                    caption='134-qism. Yigirma ikkinchi mo\'jiza')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix141"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/388',
                                    caption='135-qism. Yigirma uchinchi mo\'jiza')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix142"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/389',
                                    caption='136-qism. Yigirma to\'rtinchi mo\'jiza')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix143"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/390',
                                    caption='137-qism. Yigirma beshinchi mo\'jiza')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarix144"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/391',
                                    caption='138-qism. Yigirma oltinchi mo\'jiza')


@dp.callback_query_handler(coursesakkiz_callback.filter(item_name="tarixkeyin9"))
@dp.callback_query_handler(text='cancelon')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenutoqqiz)
    await call.answer(cache_time=60)


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix145"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/392',
                                    caption='139-qism. Yigirma yettinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix146"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/393',
                                    caption='140-qism. Yigirma sakkizinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix147"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/394',
                                    caption='141-qism. Yigirma to\'qqizinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix148"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/395',
                                    caption='142-qism. O\'ttizinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix149"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/396',
                                    caption='143-qism. O\'ttiz birinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix150"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/397',
                                    caption='144-qism. O\'ttiz ikkinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix151"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/398',
                                    caption='145-qism. O\'ttiz uchinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix152"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/399',
                                    caption='146-qism. O\'ttiz to\'rtinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix153"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/400',
                                    caption='147-qism. O\'ttiz beshinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix154"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/401',
                                    caption='148-qism. O\'ttiz oltinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix155"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/402',
                                    caption='149-qism. O\'ttiz yettinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix156"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/403',
                                    caption='150-qism. O\'ttiz sakkizinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix157"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/404',
                                    caption='151-qism. O\'ttiz to\'qqizinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix158"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/405',
                                    caption='152-qism. Qirqinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix159"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/406',
                                    caption='153-qism. Qirqi birinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarix160"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/407',
                                    caption='154-qism. Qirq ikkinchi mo\'jiza')


@dp.callback_query_handler(coursetoqqiz_callback.filter(item_name="tarixkeyin10"))
@dp.callback_query_handler(text='cancelonbir')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenuon)
    await call.answer(cache_time=60)


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix161"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/408',
                                    caption='155-qism. Qirq uchinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix162"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/409',
                                    caption='156-qism. Qirq to\'rtinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix163"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/410',
                                    caption='157-qism. Qirq beshinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix164"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/411',
                                    caption='158-qism. Qirq oltinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix165"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/412',
                                    caption='159-qism. Qirq yettinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix166"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/413',
                                    caption='160-qism. Qirq sakkizinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix167"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/414',
                                    caption='161-qism. Qirq to\'qqizinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix168"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/415',
                                    caption='162-qism. Elliginchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix169"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/416',
                                    caption='163-qism. Ellik birinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix170"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/417',
                                    caption='163-qism. Ellik ikkinchi mo\'jiza')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix171"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/418',
                                    caption='165-qism. Hajjatul vado\' ')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix172"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/419',
                                    caption='166-qism. Payg\'ambarimizning o\'g\'illari')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix173"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/420',
                                    caption='167-qism. Rasulullohning betob bo\'lishlari')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix174"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/421',
                                    caption='168-qism. Rasulullohning tana tuzilishlari')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix175"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/422',
                                    caption='169-qism. Rasulullohning axloqlari')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarix176"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/423',
                                    caption='170-qism. Rasulullohning bolalari')


@dp.callback_query_handler(courseon_callback.filter(item_name="tarixkeyin11"))
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Tarixi Muhammadiyning qismlarini tanlang", reply_markup=coursesMenuonbir)
    await call.answer(cache_time=15)


@dp.callback_query_handler(courseonbir_callback.filter(item_name="tarix177"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/424',
                                    caption='171-qism. Rasulullohning amaki va ammalari')


@dp.callback_query_handler(courseonbir_callback.filter(item_name="tarix178"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/425',
                                    caption='Onalarimiz-Rasulullohning xotinlari')


@dp.callback_query_handler(courseonbir_callback.filter(item_name="tarix179"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/426',
                                    caption='173-qism. Rasulullohning xodimlari')


@dp.callback_query_handler(courseonbir_callback.filter(item_name="tarix180"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/427',
                                    caption='174-qism. Rasulullohning urush qurollari')


@dp.callback_query_handler(courseonbir_callback.filter(item_name="tarix181"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer_audio(audio='https://t.me/Tarixi_Muhammadiy_mp3/428',
                                    caption='175-qism. Xotima')
