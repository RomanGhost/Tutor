from aiogram.types import CallbackQuery
from content import phrases, markups
from backend import client, CreateLesson
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext


async def back_button(callback_query: CallbackQuery):
    await callback_query.answer()

    roles = client.get_role(telegram_id=callback_query.from_user.id)
    markup = markups.markup_person(roles)

    await callback_query.message.edit_text(phrases.person)
    await callback_query.message.edit_reply_markup(markup)


async def add_lesson_button(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(phrases.get_lesson_name)
    await CreateLesson.name.set()


def register_buttons(dp: Dispatcher):
    dp.register_callback_query_handler(back_button,
                                   lambda callback_query: callback_query.data == "back_person"
    )

    dp.register_callback_query_handler(add_lesson_button,
                                   lambda callback_query: callback_query.data == "add_lesson"
    )