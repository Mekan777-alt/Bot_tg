from aiogram import types, Dispatcher
from bot import bot


# @dp.message_handler(commands=['📞 Забронировать'])
async def register_other(message: types.Message):
    await bot.send_message(message.from_user.id, 'takoy komandy net')

