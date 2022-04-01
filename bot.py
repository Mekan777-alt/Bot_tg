from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
token = '1467114889:AAFGgflM3wphkxsZkn3frxV_cD0T19S19ZE'

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

