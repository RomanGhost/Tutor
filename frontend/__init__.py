from .commands import commands_controller
from .user_registration import registration_controller


def controllers(dp):
    registration_controller(dp)
    commands_controller(dp)