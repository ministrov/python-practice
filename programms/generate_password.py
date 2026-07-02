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

passwords: dict[str, str] = {}


def get_password():
    password = input("Введите пароль (пустой для генерации): ")
    if password == "":
        password = generate_password()
    return password


def show_passwords():
    print("Key".ljust(20), "Value")
    print("-" * 40)
    for key, value in passwords.items():
        print(key.ljust(20), " | ", value)


def add_password():
    domain = input("Введите домен: ")
    password = get_password()
    passwords[domain] = password


def delete_password():
    domain = input("Введите домен: ")
    if domain not in passwords:
        print("Такого пароля нет")
        return
    passwords.pop(domain)
    print("Пароль удален")


def update_password():
    domain = input("Введите домен: ")
    password = get_password()

    if domain not in passwords:
        print("Такого пароля нет")
        return
    passwords[domain] = password
    print("Пароль обновлен")


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
            show_passwords()
        case 2:
            add_password()
        case 3:
            delete_password()
        case 4:
            update_password()
        case 5:
            exit()
        case _:
            print("Неверный выбор, попробуй снова")


while True:
    show_menu()
