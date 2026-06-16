"""
ПРАКТИКА: match / case — задачи для закрепления
Реши эти две задачи, используя структурное сопоставление.

Запусти файл: python 10_match_case_tasks.py
"""

print("=" * 55)
print("ЗАДАЧА 1: Определение сезона")
print("=" * 55)

# Напиши функцию get_season(month: int) -> str
# По номеру месяца возвращай сезон:
# - 12, 1, 2 → "Зима"
# - 3, 4, 5 → "Весна"
# - 6, 7, 8 → "Лето"
# - 9, 10, 11 → "Осень"
# - другое → "Неизвестный месяц"
#
# Подсказка: используй case ... | ... | ... для нескольких значений в одном case

def get_season(month: int) -> str:
    match month:
        case 12 | 1 | 2:
            return "Зима"
        case 3 | 4 | 5:
            return "Весна"
        case 6 | 7 | 8:
            return "Лето"
        case 9 | 10 | 11:
            return "Осень"
        case _:
            return "Неизвестный месяц"


print(get_season(1))    # Зима
print(get_season(7))    # Лето
print(get_season(13))   # Неизвестный месяц


print("\n" + "=" * 55)
print("ЗАДАЧА 2: Чётность с guard")
print("=" * 55)

# Напиши функцию describe_number(n: int) -> str
# - Если число < 0 → "Отрицательное"
# - Если число == 0 → "Ноль"
# - Если число > 0 и чётное → "Положительное чётное: {число}"
# - Если число > 0 и нечётное → "Положительное нечётное: {число}"
#
# Подсказка: используй guard (case x if условие)

def describe_number(n: int) -> str:
    match n:
        case x if x < 0:
            return "Отрицательное"
        case 0:
            return "Ноль"
        case x if x % 2 == 0:
            return f"Положительное чётное: {x}"
        case _: 
            return f"Положительное нечётное: {x}"

print(describe_number(-5))   # Отрицательное
print(describe_number(0))    # Ноль
print(describe_number(4))    # Положительное чётное: 4
print(describe_number(7))    # Положительное нечётное: 7
