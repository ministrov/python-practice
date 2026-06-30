""" Сделать функцию генератора паролей """

import string
import random


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 3:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*"

    pool = letters + digits + (symbols if use_symbols else "")

    password_chars: list[str] = []

    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    return "".join(password_chars)


print(generate_password())
print(generate_password(10, False))
