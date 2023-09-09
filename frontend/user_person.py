from aiogram.types import CallbackQuery
from content import phrases, markups
from backend import client
from aiogram import Dispatcher


async def user_info(callback_query:CallbackQuery):
    data = client.get_user(callback_query.from_user.id)
    text = phrases.person_info(data)

    await callback_query.answer()
    await callback_query.message.edit_text(text)
    await callback_query.message.edit_reply_markup(markups.markup_login)


def commands_user(dp: Dispatcher):
    dp.register_callback_query_handler(user_info,
                                       lambda callback_query: callback_query.data == "person_data"
    )