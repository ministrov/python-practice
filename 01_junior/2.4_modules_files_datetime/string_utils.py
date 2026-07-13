""" Функции, которые возвращает строку задом наперед и считает гласные в строке"""


def reverse_string(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    vowels = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
    return sum(text.lower().count(v) for v in vowels)


if __name__ == "__main__":
    print("тестовый вызов функций")
