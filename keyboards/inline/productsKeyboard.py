from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, coursebir_callback, courseikki_callback, \
    courseuch_callback, coursetort_callback, coursebesh_callback, courseolti_callback, courseyetti_callback, \
    coursesakkiz_callback, coursetoqqiz_callback, courseon_callback, courseonbir_callback


ortha = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="tarixiback"),
        ]
    ])


# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tarixi Muhammadiy Audiosi🎧", callback_data="tarixi"),
        ],
        [
            InlineKeyboardButton(text="Tarixi Muhammadiy 📚Kitobi📚", callback_data="tarixikitob"),
        ],
        [
            InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Tarixi Muhammadiyning barcha "
                                                                        "audiolarini ⬅️shu botdan topishingiz mumkin"),
        ],
    ])

# 2-usul
coursesMenu = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="1", callback_data=course_callback.new(item_name="tarix1"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="2", callback_data=course_callback.new(item_name="tarix2"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="3", callback_data=course_callback.new(item_name="tarix3"))
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(text="4", callback_data=course_callback.new(item_name="tarix4"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="5", callback_data=course_callback.new(item_name="tarix5"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="6", callback_data=course_callback.new(item_name="tarix6"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="7", callback_data=course_callback.new(item_name="tarix7"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="8", callback_data=course_callback.new(item_name="tarix8"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="9", callback_data=course_callback.new(item_name="tarix9"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="10", callback_data=course_callback.new(item_name="tarix10"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="11", callback_data=course_callback.new(item_name="tarix11"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="12", callback_data=course_callback.new(item_name="tarix12"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="13", callback_data=course_callback.new(item_name="tarix13"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="14", callback_data=course_callback.new(item_name="tarix14"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="15", callback_data=course_callback.new(item_name="tarix15"))
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text="16", callback_data=course_callback.new(item_name="tarix16"))
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=course_callback.new(item_name="tarixkeyin1"))
coursesMenu.insert(algorithm)

coursesMenubir = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="17", callback_data=coursebir_callback.new(item_name="tarix17"))
coursesMenubir.insert(python)

django = InlineKeyboardButton(text="18", callback_data=coursebir_callback.new(item_name="tarix18"))
coursesMenubir.insert(django)

telegram = InlineKeyboardButton(text="19", callback_data=coursebir_callback.new(item_name="tarix19"))
coursesMenubir.insert(telegram)

algorithm = InlineKeyboardButton(text="20", callback_data=coursebir_callback.new(item_name="tarix20"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="21", callback_data=coursebir_callback.new(item_name="tarix21"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="22", callback_data=coursebir_callback.new(item_name="tarix22"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="23", callback_data=coursebir_callback.new(item_name="tarix23"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="24", callback_data=coursebir_callback.new(item_name="tarix24"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="25", callback_data=coursebir_callback.new(item_name="tarix25"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="26", callback_data=coursebir_callback.new(item_name="tarix26"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="27", callback_data=coursebir_callback.new(item_name="tarix27"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="28", callback_data=coursebir_callback.new(item_name="tarix28"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="29", callback_data=coursebir_callback.new(item_name="tarix29"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="30", callback_data=coursebir_callback.new(item_name="tarix30"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="31", callback_data=coursebir_callback.new(item_name="tarix31"))
coursesMenubir.insert(algorithm)

algorithm = InlineKeyboardButton(text="32", callback_data=coursebir_callback.new(item_name="tarix32"))
coursesMenubir.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelbir")
coursesMenubir.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=coursebir_callback.new(item_name="tarixkeyin2"))
coursesMenubir.insert(algorithm)

coursesMenuikki = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="33", callback_data=courseikki_callback.new(item_name="tarix33"))
coursesMenuikki.insert(python)

django = InlineKeyboardButton(text="34", callback_data=courseikki_callback.new(item_name="tarix34"))
coursesMenuikki.insert(django)

telegram = InlineKeyboardButton(text="35", callback_data=courseikki_callback.new(item_name="tarix35"))
coursesMenuikki.insert(telegram)

algorithm = InlineKeyboardButton(text="36", callback_data=courseikki_callback.new(item_name="tarix36"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="37", callback_data=courseikki_callback.new(item_name="tarix37"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="38", callback_data=courseikki_callback.new(item_name="tarix38"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="39", callback_data=courseikki_callback.new(item_name="tarix39"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="40", callback_data=courseikki_callback.new(item_name="tarix40"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="41", callback_data=courseikki_callback.new(item_name="tarix41"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="42", callback_data=courseikki_callback.new(item_name="tarix42"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="43", callback_data=courseikki_callback.new(item_name="tarix43"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="44", callback_data=courseikki_callback.new(item_name="tarix44"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="45", callback_data=courseikki_callback.new(item_name="tarix45"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="46", callback_data=courseikki_callback.new(item_name="tarix46"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="47", callback_data=courseikki_callback.new(item_name="tarix47"))
coursesMenuikki.insert(algorithm)

algorithm = InlineKeyboardButton(text="48", callback_data=courseikki_callback.new(item_name="tarix48"))
coursesMenuikki.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelikki")
coursesMenuikki.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=courseikki_callback.new(item_name="tarixkeyin3"))
coursesMenuikki.insert(algorithm)

coursesMenuuch = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="49", callback_data=courseuch_callback.new(item_name="tarix49"))
coursesMenuuch.insert(python)

django = InlineKeyboardButton(text="50", callback_data=courseuch_callback.new(item_name="tarix50"))
coursesMenuuch.insert(django)

telegram = InlineKeyboardButton(text="51", callback_data=courseuch_callback.new(item_name="tarix51"))
coursesMenuuch.insert(telegram)

algorithm = InlineKeyboardButton(text="52", callback_data=courseuch_callback.new(item_name="tarix52"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="53", callback_data=courseuch_callback.new(item_name="tarix53"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="54", callback_data=courseuch_callback.new(item_name="tarix54"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="55", callback_data=courseuch_callback.new(item_name="tarix55"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="56", callback_data=courseuch_callback.new(item_name="tarix56"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="57", callback_data=courseuch_callback.new(item_name="tarix57"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="58", callback_data=courseuch_callback.new(item_name="tarix58"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="59", callback_data=courseuch_callback.new(item_name="tarix59"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="60", callback_data=courseuch_callback.new(item_name="tarix60"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="61", callback_data=courseuch_callback.new(item_name="tarix61"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="62", callback_data=courseuch_callback.new(item_name="tarix62"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="63", callback_data=courseuch_callback.new(item_name="tarix63"))
coursesMenuuch.insert(algorithm)

algorithm = InlineKeyboardButton(text="64", callback_data=courseuch_callback.new(item_name="tarix64"))
coursesMenuuch.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="canceluch")
coursesMenuuch.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=courseuch_callback.new(item_name="tarixkeyin4"))
coursesMenuuch.insert(algorithm)

coursesMenutort = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="65", callback_data=coursetort_callback.new(item_name="tarix65"))
coursesMenutort.insert(python)

django = InlineKeyboardButton(text="66", callback_data=coursetort_callback.new(item_name="tarix66"))
coursesMenutort.insert(django)

telegram = InlineKeyboardButton(text="67", callback_data=coursetort_callback.new(item_name="tarix67"))
coursesMenutort.insert(telegram)

algorithm = InlineKeyboardButton(text="68", callback_data=coursetort_callback.new(item_name="tarix68"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="69", callback_data=coursetort_callback.new(item_name="tarix69"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="70", callback_data=coursetort_callback.new(item_name="tarix70"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="71", callback_data=coursetort_callback.new(item_name="tarix71"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="72", callback_data=coursetort_callback.new(item_name="tarix72"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="73", callback_data=coursetort_callback.new(item_name="tarix73"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="74", callback_data=coursetort_callback.new(item_name="tarix74"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="75", callback_data=coursetort_callback.new(item_name="tarix75"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="76", callback_data=coursetort_callback.new(item_name="tarix76"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="77", callback_data=coursetort_callback.new(item_name="tarix77"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="78", callback_data=coursetort_callback.new(item_name="tarix78"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="79", callback_data=coursetort_callback.new(item_name="tarix79"))
coursesMenutort.insert(algorithm)

algorithm = InlineKeyboardButton(text="80", callback_data=coursetort_callback.new(item_name="tarix80"))
coursesMenutort.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="canceltort")
coursesMenutort.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=coursetort_callback.new(item_name="tarixkeyin5"))
coursesMenutort.insert(algorithm)


coursesMenubesh = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="81", callback_data=coursebesh_callback.new(item_name="tarix81"))
coursesMenubesh.insert(python)

django = InlineKeyboardButton(text="82", callback_data=coursebesh_callback.new(item_name="tarix82"))
coursesMenubesh.insert(django)

telegram = InlineKeyboardButton(text="83", callback_data=coursebesh_callback.new(item_name="tarix83"))
coursesMenubesh.insert(telegram)

algorithm = InlineKeyboardButton(text="84", callback_data=coursebesh_callback.new(item_name="tarix84"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="85", callback_data=coursebesh_callback.new(item_name="tarix85"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="86", callback_data=coursebesh_callback.new(item_name="tarix86"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="87", callback_data=coursebesh_callback.new(item_name="tarix87"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="88", callback_data=coursebesh_callback.new(item_name="tarix88"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="89", callback_data=coursebesh_callback.new(item_name="tarix89"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="90", callback_data=coursebesh_callback.new(item_name="tarix90"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="91", callback_data=coursebesh_callback.new(item_name="tarix91"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="92", callback_data=coursebesh_callback.new(item_name="tarix92"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="93", callback_data=coursebesh_callback.new(item_name="tarix93"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="94", callback_data=coursebesh_callback.new(item_name="tarix94"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="95", callback_data=coursebesh_callback.new(item_name="tarix95"))
coursesMenubesh.insert(algorithm)

algorithm = InlineKeyboardButton(text="96", callback_data=coursebesh_callback.new(item_name="tarix96"))
coursesMenubesh.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelbesh")
coursesMenubesh.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=coursebesh_callback.new(item_name="tarixkeyin6"))
coursesMenubesh.insert(algorithm)


coursesMenuolti = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="97", callback_data=courseolti_callback.new(item_name="tarix97"))
coursesMenuolti.insert(python)

django = InlineKeyboardButton(text="98", callback_data=courseolti_callback.new(item_name="tarix98"))
coursesMenuolti.insert(django)

telegram = InlineKeyboardButton(text="99", callback_data=courseolti_callback.new(item_name="tarix99"))
coursesMenuolti.insert(telegram)

algorithm = InlineKeyboardButton(text="100", callback_data=courseolti_callback.new(item_name="tarix100"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="101", callback_data=courseolti_callback.new(item_name="tarix101"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="102", callback_data=courseolti_callback.new(item_name="tarix102"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="103", callback_data=courseolti_callback.new(item_name="tarix103"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="104", callback_data=courseolti_callback.new(item_name="tarix104"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="105", callback_data=courseolti_callback.new(item_name="tarix105"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="106", callback_data=courseolti_callback.new(item_name="tarix106"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="107", callback_data=courseolti_callback.new(item_name="tarix107"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="108", callback_data=courseolti_callback.new(item_name="tarix108"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="109", callback_data=courseolti_callback.new(item_name="tarix109"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="110", callback_data=courseolti_callback.new(item_name="tarix110"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="111", callback_data=courseolti_callback.new(item_name="tarix111"))
coursesMenuolti.insert(algorithm)

algorithm = InlineKeyboardButton(text="112", callback_data=courseolti_callback.new(item_name="tarix112"))
coursesMenuolti.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelolti")
coursesMenuolti.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=courseolti_callback.new(item_name="tarixkeyin7"))
coursesMenuolti.insert(algorithm)


coursesMenuyetti = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="113", callback_data=courseyetti_callback.new(item_name="tarix113"))
coursesMenuyetti.insert(python)

django = InlineKeyboardButton(text="114", callback_data=courseyetti_callback.new(item_name="tarix114"))
coursesMenuyetti.insert(django)

telegram = InlineKeyboardButton(text="115", callback_data=courseyetti_callback.new(item_name="tarix115"))
coursesMenuyetti.insert(telegram)

algorithm = InlineKeyboardButton(text="116", callback_data=courseyetti_callback.new(item_name="tarix116"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="117", callback_data=courseyetti_callback.new(item_name="tarix117"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="118", callback_data=courseyetti_callback.new(item_name="tarix118"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="119", callback_data=courseyetti_callback.new(item_name="tarix119"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="120", callback_data=courseyetti_callback.new(item_name="tarix120"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="121", callback_data=courseyetti_callback.new(item_name="tarix121"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="122", callback_data=courseyetti_callback.new(item_name="tarix122"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="123", callback_data=courseyetti_callback.new(item_name="tarix123"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="124", callback_data=courseyetti_callback.new(item_name="tarix124"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="125", callback_data=courseyetti_callback.new(item_name="tarix125"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="126", callback_data=courseyetti_callback.new(item_name="tarix126"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="127", callback_data=courseyetti_callback.new(item_name="tarix127"))
coursesMenuyetti.insert(algorithm)

algorithm = InlineKeyboardButton(text="128", callback_data=courseyetti_callback.new(item_name="tarix128"))
coursesMenuyetti.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelyetti")
coursesMenuyetti.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=courseyetti_callback.new(item_name="tarixkeyin8"))
coursesMenuyetti.insert(algorithm)


coursesMenusakkiz = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="129", callback_data=coursesakkiz_callback.new(item_name="tarix129"))
coursesMenusakkiz.insert(python)

django = InlineKeyboardButton(text="130", callback_data=coursesakkiz_callback.new(item_name="tarix130"))
coursesMenusakkiz.insert(django)

telegram = InlineKeyboardButton(text="131", callback_data=coursesakkiz_callback.new(item_name="tarix131"))
coursesMenusakkiz.insert(telegram)

algorithm = InlineKeyboardButton(text="132", callback_data=coursesakkiz_callback.new(item_name="tarix132"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="133", callback_data=coursesakkiz_callback.new(item_name="tarix133"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="134", callback_data=coursesakkiz_callback.new(item_name="tarix134"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="135", callback_data=coursesakkiz_callback.new(item_name="tarix135"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="136", callback_data=coursesakkiz_callback.new(item_name="tarix136"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="137", callback_data=coursesakkiz_callback.new(item_name="tarix137"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="138", callback_data=coursesakkiz_callback.new(item_name="tarix138"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="139", callback_data=coursesakkiz_callback.new(item_name="tarix139"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="140", callback_data=coursesakkiz_callback.new(item_name="tarix140"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="141", callback_data=coursesakkiz_callback.new(item_name="tarix141"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="142", callback_data=coursesakkiz_callback.new(item_name="tarix142"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="143", callback_data=coursesakkiz_callback.new(item_name="tarix143"))
coursesMenusakkiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="144", callback_data=coursesakkiz_callback.new(item_name="tarix144"))
coursesMenusakkiz.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelsakkiz")
coursesMenusakkiz.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=coursesakkiz_callback.new(item_name="tarixkeyin9"))
coursesMenusakkiz.insert(algorithm)


coursesMenutoqqiz = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="145", callback_data=coursetoqqiz_callback.new(item_name="tarix145"))
coursesMenutoqqiz.insert(python)

django = InlineKeyboardButton(text="146", callback_data=coursetoqqiz_callback.new(item_name="tarix146"))
coursesMenutoqqiz.insert(django)

telegram = InlineKeyboardButton(text="147", callback_data=coursetoqqiz_callback.new(item_name="tarix147"))
coursesMenutoqqiz.insert(telegram)

algorithm = InlineKeyboardButton(text="148", callback_data=coursetoqqiz_callback.new(item_name="tarix148"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="149", callback_data=coursetoqqiz_callback.new(item_name="tarix149"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="150", callback_data=coursetoqqiz_callback.new(item_name="tarix150"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="151", callback_data=coursetoqqiz_callback.new(item_name="tarix151"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="152", callback_data=coursetoqqiz_callback.new(item_name="tarix152"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="153", callback_data=coursetoqqiz_callback.new(item_name="tarix153"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="154", callback_data=coursetoqqiz_callback.new(item_name="tarix154"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="155", callback_data=coursetoqqiz_callback.new(item_name="tarix155"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="156", callback_data=coursetoqqiz_callback.new(item_name="tarix156"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="157", callback_data=coursetoqqiz_callback.new(item_name="tarix157"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="158", callback_data=coursetoqqiz_callback.new(item_name="tarix158"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="159", callback_data=coursetoqqiz_callback.new(item_name="tarix159"))
coursesMenutoqqiz.insert(algorithm)

algorithm = InlineKeyboardButton(text="160", callback_data=coursetoqqiz_callback.new(item_name="tarix160"))
coursesMenutoqqiz.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="canceltoqqiz")
coursesMenutoqqiz.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=coursetoqqiz_callback.new(item_name="tarixkeyin10"))
coursesMenutoqqiz.insert(algorithm)


coursesMenuon = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="161", callback_data=courseon_callback.new(item_name="tarix161"))
coursesMenuon.insert(python)

django = InlineKeyboardButton(text="162", callback_data=courseon_callback.new(item_name="tarix162"))
coursesMenuon.insert(django)

telegram = InlineKeyboardButton(text="163", callback_data=courseon_callback.new(item_name="tarix163"))
coursesMenuon.insert(telegram)

algorithm = InlineKeyboardButton(text="164", callback_data=courseon_callback.new(item_name="tarix164"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="165", callback_data=courseon_callback.new(item_name="tarix165"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="166", callback_data=courseon_callback.new(item_name="tarix166"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="167", callback_data=courseon_callback.new(item_name="tarix167"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="168", callback_data=courseon_callback.new(item_name="tarix168"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="169", callback_data=courseon_callback.new(item_name="tarix169"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="170", callback_data=courseon_callback.new(item_name="tarix170"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="171", callback_data=courseon_callback.new(item_name="tarix171"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="172", callback_data=courseon_callback.new(item_name="tarix172"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="173", callback_data=courseon_callback.new(item_name="tarix173"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="174", callback_data=courseon_callback.new(item_name="tarix174"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="175", callback_data=courseon_callback.new(item_name="tarix175"))
coursesMenuon.insert(algorithm)

algorithm = InlineKeyboardButton(text="176", callback_data=courseon_callback.new(item_name="tarix176"))
coursesMenuon.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelon")
coursesMenuon.insert(back_button)

algorithm = InlineKeyboardButton(text="Keyingisi🔜", callback_data=courseon_callback.new(item_name="tarixkeyin11"))
coursesMenuon.insert(algorithm)


coursesMenuonbir = InlineKeyboardMarkup(row_width=4)

python = InlineKeyboardButton(text="177", callback_data=courseonbir_callback.new(item_name="tarix177"))
coursesMenuonbir.insert(python)

django = InlineKeyboardButton(text="178", callback_data=courseonbir_callback.new(item_name="tarix178"))
coursesMenuonbir.insert(django)

telegram = InlineKeyboardButton(text="179", callback_data=courseonbir_callback.new(item_name="tarix179"))
coursesMenuonbir.insert(telegram)

algorithm = InlineKeyboardButton(text="180", callback_data=courseonbir_callback.new(item_name="tarix180"))
coursesMenuonbir.insert(algorithm)

algorithm = InlineKeyboardButton(text="181", callback_data=courseonbir_callback.new(item_name="tarix181"))
coursesMenuonbir.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelonbir")
coursesMenuonbir.insert(back_button)
