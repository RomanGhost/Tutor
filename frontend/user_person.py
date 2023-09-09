from aiogram.types import CallbackQuery
from content import phrases, markups
from backend import client, functions
from aiogram import Dispatcher, types


async def user_info(callback_query:CallbackQuery):
    data = client.get_user(callback_query.from_user.id)
    text = phrases.person_info(data)

    await callback_query.answer()
    await callback_query.message.edit_text(text)
    await callback_query.message.edit_reply_markup(markups.markup_login)


async def back_button(callback_query: CallbackQuery):
    await callback_query.answer()

    roles = client.get_role(telegram_id=callback_query.from_user.id)
    markup = markups.markup_person(roles)

    await callback_query.message.edit_text(phrases.person)
    await callback_query.message.edit_reply_markup(markup)


def commands_user(dp: Dispatcher):
    dp.register_callback_query_handler(user_info,
                                       lambda callback_query: callback_query.data == "person_data"
                                       )
    dp.register_callback_query_handler(back_button,
                                       lambda callback_query: callback_query.data == "back_person"
                                       )