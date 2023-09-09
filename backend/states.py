from aiogram.dispatcher.filters.state import State, StatesGroup

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
