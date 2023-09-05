from aiogram.dispatcher.filters.state import State, StatesGroup


# New user
class UserRegistration(StatesGroup):
    login = State()
    first_name = State()
    last_name = State()
    description = State()
    phone_number = State()
    learning_rate = State()
    birthday = State()


class LogIn(StatesGroup):
    login = State()
    password = State()
class Birthday(StatesGroup):
    year = State()
    month = State()
    day = State()



# Add lesson
class CreateLesson(StatesGroup):
    name = State()
    description = State()
    date = State()
    time_hour = State()
    time_min = State()
    place = State()
    max_lesson = State()


# Add application
class CreateApplication(StatesGroup):
    name = State()
    description = State()
