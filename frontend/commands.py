from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from content import phrases
from backend import UserRegistration



# /start
async def start(message: Message) -> None:
    await message.answer(text=phrases.hello)
    await message.delete()


# /reg
async def registration(message: Message) -> None:
    await message.answer(text=phrases.start_registration)
    await message.delete()
    await UserRegistration.login.set()


# /cancel
async def cancel(message: Message, state: FSMContext) -> None:
    await message.answer(text=phrases.cancel)
    await message.delete()
    if state is not None:
        await state.finish()


def commands_controller(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(cancel, commands=['cancel'])
    dp.register_message_handler(registration, commands=['reg'])