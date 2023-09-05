from aiogram import Bot, Dispatcher, types

markup_phonenumber = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item = types.KeyboardButton("Отправить номер телефона", request_contact=True)
markup_phonenumber.add(item)

markup_learning_rate = types.InlineKeyboardMarkup()
# Добавляем кнопки для выбора степени обучения
markup_learning_rate.add(types.InlineKeyboardButton("Школьник начальных классов", callback_data="lr_start_school"))
markup_learning_rate.add(types.InlineKeyboardButton("Школьник среднего звена", callback_data="lr_middle_school"))
markup_learning_rate.add(types.InlineKeyboardButton("Школьник старших классов", callback_data="lr_high_school"))
markup_learning_rate.add(types.InlineKeyboardButton("Студент", callback_data="lr_student"))
markup_learning_rate.add(types.InlineKeyboardButton("Аспирант и далее", callback_data="lr_postgraduate"))
markup_learning_rate.add(types.InlineKeyboardButton("Закончил вуз (Бакалавр)", callback_data="lr_bachelor"))
markup_learning_rate.add(types.InlineKeyboardButton("Закончил вуз (Магистр, Специалитет)", callback_data="lr_master"))
markup_learning_rate.add(types.InlineKeyboardButton("Закончил вуз (Аспирантура)", callback_data="lr_doctorate"))
markup_learning_rate.add(types.InlineKeyboardButton("Закончил техникум", callback_data="lr_college"))

months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]
months_col = 4
# Создаем инлайн клавиатуру с месяцами
markup_months = types.InlineKeyboardMarkup(row_width=months_col)
buttons_months = [types.InlineKeyboardButton(text=months[i-1], callback_data=f"month_{i}")
 for i in range(1, len(months)+1)]
markup_months.add(*buttons_months)


days_col = 6
def markup_days(days: int):
    markup = types.InlineKeyboardMarkup(row_width=days_col)
    buttons_months = [types.InlineKeyboardButton(text=str(i), callback_data=f"day_{i}") for i in range(1, days+1)]
    markup.add(*buttons_months)
    return markup
