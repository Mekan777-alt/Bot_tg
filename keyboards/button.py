from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import date, timedelta

"""Main menu"""
btnMenu = KeyboardButton("📖 МЕНЮ")
btnBrn = KeyboardButton("📞 ЗАБРОНИРОВАТЬ")
btnTime = KeyboardButton("🕗 РЕЖИМ РАБОТЫ")
btnbar = KeyboardButton("🍾 БАР")
btndlv = KeyboardButton("🎒 ДОСТАВКА")
btnkor = KeyboardButton("🗑 КОРЗИНА")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnMenu, btnbar, btnTime, btnBrn, btndlv, btnkor)

"""Bron stolov"""
b1 = KeyboardButton("10:00")
b2 = KeyboardButton("10:30")
b3 = KeyboardButton("11:00")
b4 = KeyboardButton("11:30")
b5 = KeyboardButton("12:00")
b6 = KeyboardButton("12:30")
b7 = KeyboardButton("13:00")
b8 = KeyboardButton("13:30")
b9 = KeyboardButton("14:00")
b10 = KeyboardButton("14:30")
b11 = KeyboardButton("15:00")
b12 = KeyboardButton("15:30")
b13 = KeyboardButton("16:00")
b14 = KeyboardButton("16:30")
b15 = KeyboardButton("17:00")
b16 = KeyboardButton("17:30")
b17 = KeyboardButton("18:00")
b18 = KeyboardButton("18:30")
b19 = KeyboardButton("19:00")
b20 = KeyboardButton("19:30")
b21 = KeyboardButton("20:00")
b22 = KeyboardButton("20:30")
b23 = KeyboardButton("21:00")
b24 = KeyboardButton("21:30")
b25 = KeyboardButton("22:00")
timeBtn = ReplyKeyboardMarkup().add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8).add(b9).add(b10)
timeBtn.add(b11).add(b12).add(b13).add(b14).add(b15).add(b16).add(b17).add(b18).add(b19).add(b20).add(b21)\
    .add(b22).add(b23).add(b24).add(b25)

today = date.today()
"""date button"""
b26 = KeyboardButton(f"{today + timedelta(days=0)}")
b27 = KeyboardButton(f"{today + timedelta(days=1)}")
b28 = KeyboardButton(f"{today + timedelta(days=2)}")
b29 = KeyboardButton(f"{today + timedelta(days=3)}")
b30 = KeyboardButton(f"{today + timedelta(days=4)}")
b31 = KeyboardButton(f"{today + timedelta(days=5)}")
b32 = KeyboardButton(f"{today + timedelta(days=6)}")
b33 = KeyboardButton(f"{today + timedelta(days=7)}")
b34 = KeyboardButton(f"{today + timedelta(days=8)}")
b35 = KeyboardButton(f"{today + timedelta(days=9)}")
b36 = KeyboardButton(f"{today + timedelta(days=10)}")
b37 = KeyboardButton(f"{today + timedelta(days=11)}")
b38 = KeyboardButton(f"{today + timedelta(days=12)}")
b39 = KeyboardButton(f"{today + timedelta(days=13)}")
b40 = KeyboardButton(f"{today + timedelta(days=14)}")
dataBtn = ReplyKeyboardMarkup().add(b26).add(b27).add(b28).add(b29).add(b30).add(b31).add(b32).add(b33).add(b34).add(b35)
dataBtn.add(b36).add(b37).add(b38).add(b39).add(b40)

"""People"""
b41 = KeyboardButton("1")
b42 = KeyboardButton("2")
b43 = KeyboardButton("3")
b44 = KeyboardButton("4")
b45 = KeyboardButton("5")
b46 = KeyboardButton("6")
b47 = KeyboardButton("7")
b48 = KeyboardButton("8")
b49 = KeyboardButton("9")
b50 = KeyboardButton("10")
pepBtn = ReplyKeyboardMarkup().add(b41).add(b42).add(b43).add(b44).add(b45).add(b46).add(b47).add(b48).add(b49).add(b50)

"""otmena broni"""
b51 = KeyboardButton("❌ НЕТ")
b52 = KeyboardButton("✅ ВЕРНО")
b53 = KeyboardButton("❌ ОТМЕНИТЬ")
b54 = KeyboardButton("📞 Отправить свой номер", request_contact=True)
send_phone = ReplyKeyboardMarkup(resize_keyboard=True).add(b54)
otmBtn = ReplyKeyboardMarkup(resize_keyboard=True).add(b52).add(b51)
nacotmBtn = ReplyKeyboardMarkup(resize_keyboard=True).add(b53)

"""inline menu"""
btnkitchen = KeyboardButton("🍱 ХОЛОДНЫЕ И ГОРЯЧИЕ ЗАКУСКИ")
btndes = KeyboardButton("🍮 ДЕСЕРТЫ")
btnbzn = KeyboardButton("🥗 САЛАТЫ")
btnsup = KeyboardButton("🍲 СУПЫ")
btnkids = KeyboardButton("👶 ДЕТСКОЕ МЕНЮ")
btngor = KeyboardButton("🥙 ГОРЯЧИЕ БЛЮДА")
btngril = KeyboardButton("🥩 GRILL-СТЕЙКИ")
btnsous = KeyboardButton("🍽 СОУСА И ГАРНИРЫ")
btnnaz = KeyboardButton("🔙 НАЗАД")
inlineMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnkitchen, btnbzn, btngril, btngor,
                                                           btnsup, btnkids, btnsous, btndes, btnnaz)

"""для модераторов"""

btndone = KeyboardButton("✅ Принимать брони")
btnnot = KeyboardButton("❌ Остоновить брони")
btnAdm = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnot, btndone)


"""Кнопки внутри Бара"""

btnvin_po_bakal = KeyboardButton("🍾 АПЕРЕТИВ")
btnvin_bel = KeyboardButton("🥂 БЕЛЫЕ ВИНА")
btnvin_kras = KeyboardButton("🍷 КРАСНЫЕ ВИНА")
btnviski = KeyboardButton("🥃 ВИСКИ, РОМ, КОНЬЯК")
btnvodka = KeyboardButton("🍸 ВОДКА, ДЖИН, ТЕКИЛА")
btnpivo = KeyboardButton("🍺 ПИВО")
btnbez = KeyboardButton("☕ БЕЗ АЛКОГОЛЬНЫЕ НАПИТКИ")
barmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnvin_po_bakal, btnvin_bel, btnvin_kras, btnviski,
                                                        btnvodka, btnpivo, btnbez, btnnaz)
"""Доставка"""




