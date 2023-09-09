# commands
hello = ("Добро пожаловать!\n"
         "Этот бот по организации туторства.\n"
         "Он является частью сервиса, чтобы привязать к своему аккаунту, перейдите в личный кабинет"
         )

cancel = "Вы в главном меню! ☑️"

person = "Личный кабинет 📰"

learning_rate_ph = [
    "Школьник начальных классов", "Школьник среднего звена", "Школьник старших классов",
    "Студент", "Аспирант и далее", "Закончил вуз (Бакалавр)", "Закончил вуз (Магистр, Специалитет)",
    "Закончил вуз (Аспирантура)", "Студент техникума", "Закончил техникум"
    ]
def person_info(data):
    message = ("Личный кабинет📰\n"
               "Ваши данные:\n")
    message += f"Имя и фамилия: {data['first_name']} {data['last_name']}\n"
    message += f"Пароль: ********\n"
    message += f"Описание: {data['description']}\n"
    message += f"Номер телефона: {data['phone']}\n"
    message += f"Ступень обучения: {data['learning_rate']}"
    message += f"День рождения: {data['birthday']}\n"
    message += "\nДля изменения информации, нажмите кнопки ниже🆔"
    return message


get_lesson_name = "Какое название занятия?"
get_description = "Описание занятия: "
get_date = "Выберите дату проведения занятий: "
error_choose_date = "Выберите дату из предложенной клавиатуры"
get_hour = "Выберите час занятия:"
get_min = "Выбери минуты: "
get_place = ("Отправьте место где будет проведено занятие"
             "(Это может быть ссылка на ресурс, кабинет вуза, или коворкинг. Если вход требует пропуска или оплаты, так же укажите это!)")

def lesson_info(data):
    message = ("Проверь заполненнные данные и подтверди занятие\n"
               f"Название занятия: {data['name']}\n"
               f"Описание: {data['description']}\n"
               f"Время и дата проведения: {data['date']}\n"
               f"Место проведения: {data['place']}")
    return message

accept_lesson = "Успешно! Урок отправлен на модерацию"
disagree_lesson = "Ок! Жду от вас других предложений"