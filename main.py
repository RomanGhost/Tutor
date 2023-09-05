from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import frontend
import spech

storage = MemoryStorage()
bot = Bot(token=spech.api_key)
dp = Dispatcher(bot=bot, storage=storage)
frontend.controllers(dp)

executor.start_polling(dp, skip_updates=True)