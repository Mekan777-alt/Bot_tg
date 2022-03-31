from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import button
from bot import bot
from hendlers import client


class FSMbron(StatesGroup):
    name = State()
    time = State()
    date = State()
    people = State()
    phone_number = State()


# Начало общения с пользователем
#@dp.message_handler(text='📞 Забронировать', state=None)
async def cmd_start(message: types.Message):
    await FSMbron.name.set()
    await message.reply('👤 На чье имя бронируем стол?', reply_markup=button.nacotmBtn)


#@dp.message_handler(text=['name'], state=FSMbron.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "❌ ОТМЕНИТЬ":
            data['name'] = message.text
            await FSMbron.next()
            await message.reply('📅 На какую дату?', reply_markup=button.dataBtn)
        else:
            await message.reply("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=button.mainMenu)
            await state.finish()


#@dp.message_handler(text=['date'], state=FSMbron.date)
async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        await FSMbron.next()
        await message.reply('🕗 Выберите время бронирования: ', reply_markup=button.timeBtn)


#@dp.message_handler(text=['time'], state=FSMbron.time)
async def load_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
        await FSMbron.next()
        await message.reply('👪 На какое количество гостей?', reply_markup=button.pepBtn)


#@dp.message_handler(text=['people'], state=FSMbron.people)
async def load_people(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['people'] = message.text
        await FSMbron.next()
        await message.reply('Введите номер телефона пожалуйста.\n'
                            'Хостес перезвонит Вам для подтверждения брони.', reply_markup=types.ReplyKeyboardRemove())


#@dp.message_handler(text=['phone_number'], state=FSMbron.phone_number)
async def load_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
        await FSMbron.next()
        await message.reply(f"Отлично!\n"
                            f"Будем ждать, {data['time']} в {data['people']}\n"
                            f"на имя {data['name']}", reply_markup=button.otmBtn)


async def cencel_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "✅ ВЕРНО":
            await message.reply("Бронь принята\n"
                                "Ожидайте подтверждения", reply_markup=button.mainMenu)
            await bot.send_message(client.BRON_CHANNEL, f"Бронь\n"
                                            f"Ф.И.О: {data['name']}\n"
                                            f"Время: {data['people']}\n"
                                            f"Дата: {data['time']}\n"
                                            f"Кол-во гостей: {data['date']}\n"
                                            f"Номер телефона: {data['phone_number']}")
        elif message.text == "❌ НЕТ":
            await bot.send_message(message.from_user.id, "Бронь отменена", reply_markup=button.mainMenu)
        await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cmd_start, text='📞 ЗАБРОНИРОВАТЬ', state=None)
    dp.register_message_handler(load_name, state=FSMbron.name)
    dp.register_message_handler(load_date, state=FSMbron.date)
    dp.register_message_handler(load_time, state=FSMbron.time)
    dp.register_message_handler(load_people, state=FSMbron.people)
    dp.register_message_handler(load_phone_number, state=FSMbron.phone_number)
    dp.register_message_handler(cencel_message)
