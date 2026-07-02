""" Сделать функцию генератора паролей
    Создание меню: Приложение должно при запуске показывать меню с опциями для пользователя:
    Показать пароли.
    Добавить пароль.
    Удалить пароль.
    Обновить пароль.
    Выход.
 """

import string
import random


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 3:
        raise ValueError(f"length must be >= 3, got {length}")
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*"

    pool = letters + digits + (symbols if use_symbols else "")

    password_chars: list[str] = []

    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    return "".join(password_chars)


def show_menu():
    print("1. Показать пароли: ")
    print("2. Добавить пароли: ")
    print("3. Удалить пароли: ")
    print("4. Обновить пароль: ")
    print("5. Выход: ")
    user_select = int(input("Ваш выбор: (1, 2, 3, 4, 5)"))
    match user_select:
        case 1:
            print("Показать пароли")
        case 2:
            print("Добавить пароль")
        case 3:
            print("Удалить пароль")
        case 4:
            print("Обновить пароль")
        case _:
            exit()


while True:
    show_menu()
