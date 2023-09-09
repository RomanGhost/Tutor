from .commands import commands_controller
from .user_person import commands_user
from .lesson_registration import register_lesson_registration
from .person_buttons import register_buttons


def controllers(dp):
    commands_controller(dp)

    commands_user(dp)
    register_lesson_registration(dp)
    register_buttons(dp)


