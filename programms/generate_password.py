""" Сделать функцию генератора паролей """

import string


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 3:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*"
    print(letters, digits, symbols)


generate_password()
