from .commands import commands_controller
from .user_person import commands_user


def controllers(dp):
    commands_controller(dp)

    commands_user(dp)
    registration_controller(dp)
