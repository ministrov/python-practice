""" Модуль создает функцию которая печатет финальное 
    отчет используя другой модуль string_utils.py 
"""
import string_utils


def report(text: str) -> str:
    return (
        f"Текст: {text} | Наоборот: {string_utils.reverse_string(text)} | "
        f"Гласных: {string_utils.count_vowels(text)}"
    )
