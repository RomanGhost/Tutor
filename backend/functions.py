import re
import datetime


def is_valid_login(login: str):
    # Регулярное выражение для проверки строки логина
    pattern = r'^[a-zA-Z0-9_]+$'

    # Проверка соответствия строки логина регулярному выражению
    if re.match(pattern, login):
        return True
    else:
        return False


def is_valid_year(year_str: str):
    try:
        year = int(year_str)
    except ValueError:
        return False
    return datetime.datetime.now().year - 100 < year <= datetime.datetime.now().year


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError("Ошибка: Месяц должен быть в диапазоне от 1 до 12.")

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29

    return days_in_month[month-1]
