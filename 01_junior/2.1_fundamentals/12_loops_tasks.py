"""
ПРАКТИКА: Циклы — 6 задач для закрепления
Реши эти задачи, используя for, while, break, continue, enumerate, zip

Запусти файл: python 12_loops_tasks.py
"""

print("=" * 55)
print("ЗАДАЧА 1: Сумма чисел от 1 до n")
print("=" * 55)

# Напиши функцию sum_up_to(n: int) -> int
# Суммирует все числа от 1 до n включительно
# Используй for с range()
#
# Пример: sum_up_to(5) = 1+2+3+4+5 = 15


def sum_up_to(n: int) -> int:
    result: int = 0
    for index in range(1, n + 1):
        result += index
    return result

print(sum_up_to(5))    # 15
print(sum_up_to(10))   # 55


print("\n" + "=" * 55)
print("ЗАДАЧА 2: Фильтр чётных чисел")
print("=" * 55)

# Напиши функцию get_evens(numbers: list[int]) -> list[int]
# Возвращает список только чётных чисел
# Используй for и условие if
#
# Пример: get_evens([1,2,3,4,5,6]) → [2,4,6]

def get_evens(numbers: list[int]) -> list[int]:
    evens: list[int] = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(get_evens([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(get_evens([1, 3, 5, 7]))        # []


print("\n" + "=" * 55)
print("ЗАДАЧА 3: Найти первый элемент, где условие истинно")
print("=" * 55)

# Напиши функцию find_first(numbers: list[int], target: int) -> int
# Возвращает ИНДЕКС первого элемента, равного target
# Если не найден — возвращает -1
# Используй for, enumerate и break
#
# Пример: find_first([10, 20, 30, 20], 20) → 1 (индекс, не значение!)

def find_first(numbers: list[int], target: int) -> int:
    found: int = -1
    for index, number in enumerate(numbers):
        if number == target:
            found = index
            break
    return found

print(find_first([10, 20, 30, 20], 20))  # 1
print(find_first([10, 20, 30], 99))      # -1


print("\n" + "=" * 55)
print("ЗАДАЧА 4: Объединить два списка в словарь")
print("=" * 55)

# Напиши функцию zip_to_dict(keys: list[str], values: list[int]) -> dict
# Превращает два списка в словарь: ключи из первого, значения из второго
# Используй zip и словарь
#
# Пример: zip_to_dict(['a', 'b', 'c'], [1, 2, 3]) → {'a': 1, 'b': 2, 'c': 3}

def zip_to_dict(keys: list[str], values: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for key, value in zip(keys, values):
        result[key] = value
    return result

print(zip_to_dict(['a', 'b', 'c'], [1, 2, 3]))        # {'a': 1, 'b': 2, 'c': 3}
print(zip_to_dict(['name', 'age'], [25, 30]))         # {'name': 25, 'age': 30}


print("\n" + "=" * 55)
print("ЗАДАЧА 5: Перемножить элементы со своими индексами")
print("=" * 55)

# Напиши функцию multiply_by_index(numbers: list[int]) -> list[int]
# Каждый элемент умножается на свой индекс
# Используй enumerate
#
# Пример: multiply_by_index([10, 20, 30]) → [0, 20, 60]
# (10*0=0, 20*1=20, 30*2=60)

def multiply_by_index(numbers: list[int]) -> list[int]:
    result: list[int] = []
    for index, number in enumerate(numbers):
        result.append(number * index)
    return result

print(multiply_by_index([10, 20, 30]))   # [0, 20, 60]
print(multiply_by_index([5, 5, 5]))      # [0, 5, 10]


print("\n" + "=" * 55)
print("ЗАДАЧА 6: Угадай число (while)")
print("=" * 55)

# Напиши функцию count_guesses(target: int, guesses: list[int]) -> int
# Возвращает, сколько попыток из списка guesses потребовалось,
# чтобы угадать target
# Используй while и условие
#
# Пример: count_guesses(7, [3, 5, 7, 10]) → 3
# (нужно 3 попытки: 3 неверно, 5 неверно, 7 верно)

def count_guesses(target: int, guesses: list[int]) -> int:
    i = 0
    while i < len(guesses):
        if guesses[i] == target:
            return i + 1
        i += 1
    return len(guesses)
print(count_guesses(7, [3, 5, 7, 10]))    # 3
print(count_guesses(1, [1, 2, 3]))        # 1
