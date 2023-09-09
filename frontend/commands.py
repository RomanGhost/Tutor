from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from content import phrases, markups
from backend import client


# /start
async def start(message: Message) -> None:
    await message.answer(text=phrases.hello)
    await message.delete()


# /person
async def person(message: Message) -> None:
    await message.delete()
    roles = client.get_role(telegram_id=message.from_user.id)
    markup = markups.markup_person(roles)
    await message.answer(phrases.person, reply_markup=markup)


# /cancel
async def cancel(message: Message, state: FSMContext) -> None:
    await message.answer(text=phrases.cancel, reply_markup=ReplyKeyboardRemove())
    await message.delete()
    if state is not None:
        await state.finish()


def commands_controller(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(person, commands=['person'])
    dp.register_message_handler(cancel,state='*', commands=['cancel'])
