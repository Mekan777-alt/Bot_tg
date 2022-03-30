from aiogram import types, Dispatcher
from bot import bot
from keyboards import button

CHANNEL_ID = "@main_channel2"  # основной канал связи
BRON_CHANNEL = "@test_channel123456765"  # Канал связи для отправки брони


# def check_admin(chat_member):
# if chat_member['status'] == 'administrator' or chat_member['status'] == 'creator':
# return True
# else:
# return False


# @dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    # if check_admin(await bot.get_chat_member(chat_id=BRON_CHANNEL, user_id=message.from_user.id)):
    # await bot.send_message(message.from_user.id, "Функции для МОДЕРАТОРА", reply_markup=button.btnAdm)
    # else:
    await bot.send_message(message.from_user.id, 'ДОБРО ПОЖАЛОВАТЬ {0.first_name}\n'
                                                 'Я Ваш личный бот помощник.\n'
                                                 'Я помогу вам ознокомиться с меню, режимом работы ресторана и '
                                                 'забронировать столик.'.format(
        message.from_user),
                           reply_markup=button.mainMenu)


# @dp.message_handler(commands=['🕗 Режим работы'])
async def time_of_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'Улица Аделя Кутуя 68/2\n'
                                                 'Пн-Чт 9:00-23:00\n'
                                                 'Пт-Сб 9:00-00:00\n'
                                                 'Вс 10:00-23:00')


# @dp.message_handler(commands=['📖 Меню'])
async def menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'ВЫБИРАЙТЕ С УМОМ', reply_markup=button.inlineMenu)


async def bar(message: types.Message):
    await bot.send_message(message.from_user.id, "КОТЕГОРИИ ПО БАРУ", reply_markup=button.barmenu)


async def back(message: types.Message):
    await message.reply("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=button.mainMenu)


"""Блок команд после открытие МЕНЮ"""

async def gor_zak(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/Menyu-03-26-4", reply_markup=button.inlineMenu)


async def dessert(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/MENYU-03-27-3", reply_markup=button.inlineMenu)


async def salaty(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/Menyu-03-26-3", reply_markup=button.inlineMenu)


async def supy(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/MENYU-03-26-7", reply_markup=button.inlineMenu)


async def det_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/MENYU-03-26-8", reply_markup=button.inlineMenu)


async def gor_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/MENYU-03-26-6", reply_markup=button.inlineMenu)


async def grill_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/MENYU-03-26-5", reply_markup=button.inlineMenu)


async def sousy(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/MENYU-03-27-2", reply_markup=button.inlineMenu)
"""БЛОК ОТКРЫТИЯ БАРА"""

async def aperativ(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-30", reply_markup=button.barmenu)

async def bel_vino(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-28-2#_tl_editor", reply_markup=button.barmenu)

async def kras_vino(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-28-3#ВНИЗ", reply_markup=button.barmenu)

async def viski_rom(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-29-3", reply_markup=button.barmenu)

async def vodka_djin(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-29-2", reply_markup=button.barmenu)

async def pivo(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-28-4", reply_markup=button.barmenu)

async def bez_alkogol(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/BAR-03-29-4", reply_markup=button.barmenu)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start', 'help'])
    dp.register_message_handler(time_of_work, text=['🕗 РЕЖИМ РАБОТЫ'])
    dp.register_message_handler(menu, text=['📖 МЕНЮ'])
    dp.register_message_handler(bar, text="🍾 БАР")
    dp.register_message_handler(back, text="🔙 НАЗАД")
    """Блок открытие меню"""
    dp.register_message_handler(gor_zak, text="🍱 ХОЛОДНЫЕ И ГОРЯЧИЕ ЗАКУСКИ")
    dp.register_message_handler(dessert, text="🍮 ДЕСЕРТЫ")
    dp.register_message_handler(salaty, text="🥗 САЛАТЫ")
    dp.register_message_handler(supy, text="🍲 СУПЫ")
    dp.register_message_handler(det_menu, text="👶 ДЕТСКОЕ МЕНЮ")
    dp.register_message_handler(gor_menu, text="🌶 ГОРЯЧИЕ БЛЮДА")
    dp.register_message_handler(grill_menu, text="🥩 GRILL-СТЕЙКИ")
    dp.register_message_handler(sousy, text="🍽 СОУСА И ГОРНИРЫ")
    """Блок открытие бара"""
    dp.register_message_handler(aperativ, text="🍷 АПЕРЕТИВ")
    dp.register_message_handler(bel_vino, text="🍷 БЕЛЫЕ ВИНА")
    dp.register_message_handler(kras_vino, text="🍷 КРАСНЫЕ ВИНА")
    dp.register_message_handler(viski_rom, text="🥃 ВИСКИ, РОМ, КОНЬЯК")
    dp.register_message_handler(vodka_djin, text="🍾 ВОДКА, ДЖИН, ТЕКИЛА")
    dp.register_message_handler(pivo, text="🍺 ПИВО")
    dp.register_message_handler(bez_alkogol, text="🍸 БЕЗ АЛКОГОЛЬНЫЕ НАПИТКИ")
