# -*- coding: utf-8 -*-
"""
Блок 2.3.4: Практика — функции как объекты первого класса
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 07_functions_as_objects_demo.py если застрял.
"""

from collections.abc import Callable


print("=" * 60)
print("ЗАДАНИЕ 1: Функция как объект")
print("=" * 60)
print("""
1.1 Напиши функцию cube(x), возвращающую x в кубе.
1.2 Присвой её другой переменной my_cube (без вызова, без скобок).
1.3 Вызови my_cube(3) и напечатай результат.
1.4 Напечатай my_cube is cube, чтобы показать — это один объект.
""")

# ТВОЙ КОД ЗДЕСЬ:


def cube(x: int):
    return x ** 3


my_cube = cube
print(my_cube(3))

print(my_cube is cube)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Функция высшего порядка")
print("=" * 60)
print("""
2.1 Напиши apply_operation(func, a, b), которая вызывает func(a, b)
    и возвращает результат.
2.2 Напиши add(a, b) и multiply(a, b).
2.3 Вызови apply_operation(add, 3, 4) -> 7
    и apply_operation(multiply, 3, 4) -> 12
""")

# ТВОЙ КОД ЗДЕСЬ:


def apply_operation(func: Callable[[int, int], int], a: int, b: int):
    return func(a, b)


def add(a: int, b: int):
    return a + b


def multiply(a: int, b: int):
    return a * b


add_sum = apply_operation(add, 3, 8)
multiplier = apply_operation(multiply, 3, 4)

print(add_sum)
print(multiplier)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Dispatch table (таблица диспетчеризации)")
print("=" * 60)
print("""
3.1 Дан словарь operations = {"+": add, "-": subtract, "*": multiply}
    (напиши недостающую subtract(a, b)).
3.2 Напиши calculate(op: str, a, b), которая находит нужную функцию
    в operations по ключу op и вызывает её с a, b.
    calculate("+", 5, 3) -> 8
    calculate("-", 5, 3) -> 2
    calculate("*", 5, 3) -> 15
3.3 Что должно произойти, если op не найден в словаре? Обработай
    этот случай (raise ValueError с понятным сообщением).
""")

# ТВОЙ КОД ЗДЕСЬ:


def subtract(a: int, b: int):
    return a - b


operations: dict[str, Callable[[int, int], int]] = {
    "+": add, "-": subtract, "*": multiply}


def calculate(op: str, a: int, b: int):
    if op not in operations:
        raise ValueError("Такой операции нет")
    func = operations[op]
    return func(a, b)


print(calculate("+", 2, 12))
print(calculate("-", 2, 12))
print(calculate("*", 2, 12))
try:
    print(calculate("ываыва", 2, 12))
except ValueError as e:
    print(f"Ошибка: {e}")


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Функция возвращает функцию (без замыкания)")
print("=" * 60)
print("""
4.1 Напиши is_even(x) и is_positive(x) — обе возвращают bool.
4.2 Напиши pick_checker(kind: str), которая возвращает is_even если
    kind == "even", is_positive если kind == "positive".
4.3 checker = pick_checker("even")
    print(checker(4))   -> True
    print(checker(7))   -> False
""")

# ТВОЙ КОД ЗДЕСЬ:


def is_even(x: int):
    return x % 2 == 0


def is_positive(x: int):
    return x > 0


def pick_checker(kind: str):
    match kind:
        case "even":
            return is_even
        case "positive":
            return is_positive
        case _:
            raise ValueError("Такой операции несуществует, выберите другую")


checker = pick_checker("even")
print(checker(4))
print(checker(7))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: lambda и sorted с ключом")
print("=" * 60)
print("""
5.1 Дан список кортежей:
    students = [("Anna", 82), ("Boris", 91), ("Vera", 76)]
    Отсортируй по оценке (второй элемент) по убыванию через
    sorted(..., key=lambda ..., reverse=True).
5.2 Дан список слов words = ["a", "bbb", "cc", "dddd"].
    Отсортируй по длине слова через sorted с key=lambda.
""")

# ТВОЙ КОД ЗДЕСЬ:
students: list[tuple[str, int]] = [("Anna", 82), ("Boris", 91), ("Vera", 76)]
words = ["a", "bbb", "cc", "dddd"]
by_grade = sorted(students, key=lambda student: student[1], reverse=True)
by_words_len = sorted(words, key=lambda word: len(word))
print(by_grade)
print(by_words_len)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: map и filter")
print("=" * 60)
print("""
6.1 Дан список чисел nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    Через filter + lambda оставь только числа, кратные 3.
6.2 Через map + lambda переведи каждое оставшееся число в его квадрат.
    Результат должен получиться из ОДНОЙ цепочки:
    filter -> map -> list.
""")

# ТВОЙ КОД ЗДЕСЬ:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, nums)))
print(result)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Атрибуты функций")
print("=" * 60)
print("""
7.1 Дан список функций funcs = [cube, add, multiply].
    В цикле напечатай func.__name__ для каждой функции из списка.
""")

# ТВОЙ КОД ЗДЕСЬ:
funcs = [cube, add, multiply]

for fun in funcs:
    print(f"Имя функции {fun.__name__}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное — калькулятор на dispatch table")
print("=" * 60)
print("""
8.1 Напиши функцию run_calculator(operations: list), которая
    принимает список кортежей вида (op, a, b), например:
    [("+", 2, 3), ("*", 4, 5), ("-", 10, 4)]
    и для каждого кортежа вызывает calculate(op, a, b) из Задания 3,
    печатая результат в формате f"{a} {op} {b} = {result}".
""")

# ТВОЙ КОД ЗДЕСЬ:


def run_calculator(operations_list: list[tuple[str, int, int]]):
    for op, a, b in operations_list:
        result = calculate(op, a, b)
        print(f"{a} {op} {b} = {result}")


run_calculator([("+", 2, 3), ("*", 4, 5), ("-", 10, 4)])

print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
