from aiogram.types import Message, ContentType, CallbackQuery
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from content import phrases, markups
from backend import User, UserRegistration, Birthday, LogIn
from backend import client, functions

async def user_info(callback_query:CallbackQuery):
    data = client.get_user(callback_query.from_user.id)
    text = phrases.person_info(data)

    await callback_query.answer()
    await callback_query.message.answer(text, markups.markup_login)
