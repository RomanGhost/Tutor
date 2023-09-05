import datetime

from aiogram.types import Message, ContentType, CallbackQuery
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from content import phrases, markups
from backend import User, UserRegistration, Birthday, LogIn
from backend import client, functions


async def error_login_exist(message: Message, state: FSMContext):
    text = phrases.error_login_exist(message.text)
    await LogIn.password.set()
    await message.answer(text)


async def error_login_signs(message: Message, state: FSMContext):
    text = phrases.error_login_sign(message.text)
    await message.answer(text)


async def request_first_name(message: Message, state: FSMContext):
    login = message.text[:25]
    async with state.proxy() as data:
        data['user'] = User()
        data['user'].login = login

    await message.answer(phrases.get_first_name)
    await UserRegistration.next()


async def error_first_name(message: Message, state: FSMContext):
    await message.answer(phrases.error_first_name)


async def request_last_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['user'].first_name = message.text[:255]

    await message.answer(phrases.get_last_name)
    await UserRegistration.next()


async def error_last_name(message: Message, state: FSMContext):
    await message.answer(phrases.error_last_name)


async def request_description(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['user'].last_name = message.text[:255]

    # добавить кнопку отмены (пропуск)
    await message.answer(phrases.get_description)
    await UserRegistration.next()


async def request_phone(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['user'].description = message.text[:500]

    await message.answer(phrases.get_phonenumber, reply_markup=markups.markup_phonenumber)
    await UserRegistration.next()


async def request_learning_rate(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['user'].phone = message.contact

    await message.answer(phrases.accept_get_phonenumber,  reply_markup=types.ReplyKeyboardRemove())
    await message.answer(phrases.get_learning_rate, reply_markup=markups.markup_learning_rate)
    await UserRegistration.next()


async def request_birthday(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['user'].phone = callback_query.data[3:]

    await callback_query.answer()
    await callback_query.message.answer(phrases.get_birthday_year)

    await Birthday.year.set()


async def request_birthday_month(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = int(message.text)

    await message.answer(phrases.get_birthday_month, reply_markup=markups.markup_months)
    await Birthday.next()


async def request_birthday_day(callback_query: CallbackQuery, state: FSMContext):
    year = 0
    month = int(callback_query.data[6:])
    async with state.proxy() as data:
        data['month'] = month
        year = data['year']
    days = functions.days_in_month(year, month)
    markup = markups.markup_days(days)

    await callback_query.answer()
    await callback_query.message.answer(phrases.get_birthday_month, reply_markup=markup)
    await UserRegistration.birthday.set()


async def end_of_registration(callback_query: CallbackQuery, state: FSMContext):
    day = int(callback_query.data[4:])
    async with state.proxy() as data:
        data['user'].birthday = datetime.datetime(data['year'], data['month'], day)
        client.add_user(data['user'])

    await callback_query.answer()
    await callback_query.message.answer(phrases.compliments)
    await state.finish()


def registration_controller(dp: Dispatcher):
    dp.register_message_handler(error_login_exist,
                                lambda message: client.exist_login(message.text),
                                state=UserRegistration.login
                                )
    dp.register_message_handler(error_login_signs,
                                lambda message: not functions.is_valid_login(message.text),
                                state=UserRegistration.login
                                )

    dp.register_message_handler(request_first_name, state=UserRegistration.login)
    dp.register_message_handler(error_first_name,
                                lambda message: not message.text.isalpha(),
                                state=UserRegistration.first_name
                                )

    dp.register_message_handler(request_last_name, state=UserRegistration.first_name)
    dp.register_message_handler(error_last_name,
                                lambda message: not message.text.isalpha(),
                                state=UserRegistration.last_name
                                )

    dp.register_message_handler(request_description, state=UserRegistration.last_name)
    dp.register_message_handler(request_phone, state=UserRegistration.description)
    dp.register_message_handler(request_learning_rate,
                                state=UserRegistration.phone_number,
                                content_types=[ContentType.CONTACT]
                                )
    dp.register_callback_query_handler(request_birthday,
                                       lambda callback_query: 'lr' in callback_query.data,
                                       state=UserRegistration.learning_rate
                                       )

    dp.register_message_handler(request_birthday_month, state=Birthday.year)
    dp.register_callback_query_handler(request_birthday_day,
                                       lambda callback_query: 'month' in callback_query.data,
                                       state=Birthday.month
                                       )
    dp.register_callback_query_handler(end_of_registration,
                                       lambda callback_query: 'day' in callback_query.data,
                                       state=UserRegistration.birthday
                                       )
