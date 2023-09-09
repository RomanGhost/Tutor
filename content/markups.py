from aiogram import Bot, Dispatcher, types
from .phrases import learning_rate_ph

button_back_person = types.InlineKeyboardButton("Назад", callback_data="back_person")

markup_learning_rate = types.InlineKeyboardMarkup()
# Добавляем кнопки для выбора степени обучения
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[0], callback_data="lr_0"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[1], callback_data="lr_1"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[2], callback_data="lr_2"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[3], callback_data="lr_3"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[4], callback_data="lr_4"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[5], callback_data="lr_5"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[6], callback_data="lr_6"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[7], callback_data="lr_7"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[8], callback_data="lr_8"))
markup_learning_rate.add(types.InlineKeyboardButton(learning_rate_ph[9], callback_data="lr_9"))


person_col = 3
def markup_person(roles:list):
    markup = types.InlineKeyboardMarkup(row_width=person_col)
    markup.add(types.InlineKeyboardButton(text="Личные данные", callback_data=f"person_data"))
    markup.add(
        types.InlineKeyboardButton(text="Предложенные занятия", callback_data=f"applications"),
        types.InlineKeyboardButton(text="Предложить занятие", callback_data=f"add_application")
    )
    markup.add(types.InlineKeyboardButton(text="Доступные занятия", callback_data=f"lessons"))

    for role in roles:
        if role == 'teacher':
            markup.add(types.InlineKeyboardButton(text="Добавить занятие", callback_data=f"add_lesson"),)
            break

    return markup


markup_login = types.InlineKeyboardMarkup(row_width=2)
markup_login.add(button_back_person)

