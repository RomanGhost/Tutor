def exist_login(login: str):
    return False

def add_user(user):
    print(user)
    return True

def change_user_first_name(telegram_id, new_first_name):
    pass
def get_role(user_id=None, login=None, telegram_id=None):
    return ['teacher']


def get_user(user_id=None, login=None, telegram_id=None):
    res = {
        'id': '0',
        'telegram_id': '101010',
        'login': 'Romka',
        'password': '2',
        'first_name': 'Роман',
        'last_name': 'Ильдияров',
        'description': 'Ok',
        'phone': '+79379834455',
        'learning_rate': 3,
        'birthday': '01.08.2003'
    }
    return res