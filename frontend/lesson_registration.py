from aiogram.types import CallbackQuery, Message
from content import phrases, markups
from backend import client, CreateLesson
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from .calendar_bot import simple_cal_callback, SimpleCalendar


async def request_description(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text[:255]

    await message.answer(phrases.get_description)
    await CreateLesson.next()


async def request_date(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text[:500]

    await message.answer(phrases.get_date, reply_markup=await SimpleCalendar().start_calendar())
    await CreateLesson.next()


async def request_hour(callback_query: CallbackQuery, callback_data, state:FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)

    await callback_query.answer()
    if not selected:
        return

    async with state.proxy() as data:
        data['date'] = date.strftime("%d/%m/%Y")

    await callback_query.message.edit_text(phrases.get_hour)
    await callback_query.message.edit_reply_markup(markups.markup_hour_choose)
    await CreateLesson.next()


async def request_min(callback_query: CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['hour'] = callback_query.data[5:]

    await callback_query.answer()
    await callback_query.message.edit_text(phrases.get_min)
    await callback_query.message.edit_reply_markup(markups.markup_min_choose)
    await CreateLesson.next()


async def request_place(callback_query: CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['min'] = callback_query.data[4:]

    await callback_query.answer()
    await callback_query.message.edit_text(phrases.get_place)
    await CreateLesson.next()


async def request_accept_lesson(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['place'] = message.text[:500]
        time = f"{data['hour']}:{data['min']}"
        data['date'] = f"{time} {data['date']}"

        text = phrases.lesson_info(data)
    print(text)
    await message.answer(text, reply_markup=markups.markup_accept)
    await CreateLesson.next()


async def accept_lesson(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_id = client.get_user()['id']
        data['user_id'] = user_id
        client.send_lesson(data)

    await callback_query.answer()
    await callback_query.message.edit_text(phrases.accept_lesson)
    await state.finish()


async def disagree_lesson(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data.clear()

    await callback_query.answer()
    await callback_query.message.edit_text(phrases.disagree_lesson)
    await state.finish()


def register_lesson_registration(dp: Dispatcher):
    dp.register_message_handler(request_description, state=CreateLesson.name)
    dp.register_message_handler(request_date, state=CreateLesson.description)

    dp.register_callback_query_handler(request_hour, simple_cal_callback.filter(), state=CreateLesson.date)
    dp.register_callback_query_handler(request_min, lambda call: 'hour' in call.data, state=CreateLesson.time_hour)
    dp.register_callback_query_handler(request_place, lambda call: 'min' in call.data, state=CreateLesson.time_min)
    dp.register_message_handler(request_accept_lesson, state=CreateLesson.place)

    dp.register_callback_query_handler(accept_lesson, lambda call: 'accept' == call.data, state=CreateLesson.accept)
    dp.register_callback_query_handler(disagree_lesson, lambda call: 'disagree' == call.data, state=CreateLesson.accept)
