"""
Практические упражнения для ОСНОВ функций в Python
Начни отсюда, если не знаешь функции или надо освежить память
"""

# ============================================================================
# УРОВЕНЬ 1: Простые функции (основные операции)
# ============================================================================

# Задача 1: Сложение двух чисел

def task1():
    """
    Создай функцию add(a, b), которая возвращает сумму двух чисел
    Пример: add(5, 3) → 8
    """
def add(a: int, b: int) -> int:
    return a + b

sum = add(4, 5)
print(sum)


# Задача 2: Проверка чётности числа
def task2():
    """
    Создай функцию is_even(n), которая возвращает True если число чётное, иначе False
    Пример: is_even(4) → True, is_even(5) → False
    """

def is_even(n: int) -> bool:
    return True if n % 2 == 0 else False

print(is_even(4))
print(is_even(3))

# Задача 3: Преобразование температуры
def task3():
    """
    Создай функцию celsius_to_fahrenheit(celsius), которая переводит градусы Цельсия в Фаренгейт
    Формула: F = C * 9/5 + 32
    Пример: celsius_to_fahrenheit(0) → 32.0
    """
def celsius_to_fahrenheit(celsius: int) -> int:
    return int(celsius * 9 / 5 + 32)

print(celsius_to_fahrenheit(34))
print(celsius_to_fahrenheit(14))
print(celsius_to_fahrenheit(24))


# Задача 4: Длина строки
def task4():
    """
    Создай функцию get_length(text), которая возвращает количество символов
    Пример: get_length("hello") → 5
    """
def get_length(text: str) -> int:
    return len(text)

print(get_length("hello!!!"))


# Задача 5: Проверка отрицательного числа
def task5():
    """
    Создай функцию is_negative(n), которая возвращает True если число отрицательное
    Пример: is_negative(-5) → True, is_negative(10) → False
    """
def is_negative(n: int) -> int:
    return True if n < 0 else False

print(is_negative(-6))
print(is_negative(16))

# ============================================================================
# УРОВЕНЬ 2: Условия и логика
# ============================================================================

# Задача 6: Минимум из двух чисел
def task6():
    """
    Создай функцию min_of_two(a, b), которая возвращает минимальное число
    Не используй встроенную функцию min()
    Пример: min_of_two(5, 3) → 3
    """
def min_of_two(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b

print(min_of_two(3, 7))
print(min_of_two(5, 7))
print(min_of_two(7, 2))

# Задача 7: Классификация числа
def task7():
    """
    Создай функцию classify_number(n), которая возвращает:
    "positive" если число > 0
    "negative" если число < 0
    "zero" если число == 0

    Пример: classify_number(5) → "positive"
    """
def classify_number(n: int):
    match n:
        case _ if n > 0:
            return "positive"
        case _ if n < 0:
            return "negative"
        case _ if n == 0:
            return "zero"

print(classify_number(-34))
print(classify_number(-3))
print(classify_number(23))

# Задача 8: Категория возраста
def task8():
    """
    Создай функцию get_age_category(age), которая возвращает:
    "child" если возраст < 13
    "teenager" если 13 <= возраст < 18
    "adult" если 18 <= возраст < 65
    "senior" если возраст >= 65

    Пример: get_age_category(25) → "adult"
    """
def get_age_category(age: int) -> str:
    if age < 13:
        return "child"
    elif age < 18:
        return "teenager"
    elif age < 65:
        return "adult"
    else:
        return "senior"

print(get_age_category(45))

# Задача 9: Проверка пароля
def task9():
    """
    Создай функцию is_strong_password(password), которая проверяет:
    - длина >= 8 символов
    - содержит хотя бы одну цифру
    - содержит хотя бы одну заглавную букву
    Возвращает True только если все условия выполнены

    Пример: is_strong_password("MyPass123") → True
    """
def is_strong_password(password: str) -> bool:
    has_digit = False
    has_upper = False
    for c in password:
        if c.isdigit():
            has_digit = True
        if c.isupper():
            has_upper = True

    return has_upper and has_digit and len(password) >= 8

print(is_strong_password("sfsfID343"))

# Задача 10: Расчёт скидки
def task10():
    """
    Создай функцию calculate_discount(price, discount_percent), которая:
    - возвращает цену со скидкой
    - если скидка > 50%, используй максимум 50% скидку

    Пример: calculate_discount(100, 30) → 70.0
    """
def calculate_discount(price: int, discount_percent: int) -> float:
    # 1. если discount_percent > 50, ограничить его до 50
    # 2. посчитать итоговую цену: price минус (price * процент / 100)
    if discount_percent > 50:
        discount_percent = 50
    return price - (price * discount_percent / 100)

print(calculate_discount(23, 45))

# ============================================================================
# УРОВЕНЬ 3: Работа со списками (List Operations)
# ============================================================================

# Задача 11: Сумма элементов списка
def task11():
    """
    Создай функцию sum_list(numbers), которая возвращает сумму всех элементов
    Не используй встроенную функцию sum()

    Пример: sum_list([1, 2, 3, 4]) → 10
    """
def sum_list(numbers: list[int]) -> int:
    result: int = 0

    for num in numbers:
        result += num
    return result

print(sum_list([1, 2, 3, 4]))


# Задача 12: Максимум в списке
def task12():
    """
    Создай функцию max_in_list(numbers), которая возвращает максимальное число
    Не используй встроенную функцию max()

    Пример: max_in_list([5, 2, 8, 1]) → 8
    """
def max_in_list(numbers: list[int]) -> int:
    # max_number = 0

    # for num, inx in enumerate(numbers):
    #     if num > numbers[inx + 1]:
    #         max_number += num
    #     else:
    return 0



# Задача 13: Обратный список
def task13():
    """
    Создай функцию reverse_list(lst), которая возвращает список в обратном порядке
    Не используй встроенный метод reverse()

    Пример: reverse_list([1, 2, 3]) → [3, 2, 1]
    """
    pass


# Задача 14: Подсчёт количества элемента
def task14():
    """
    Создай функцию count_element(lst, element), которая считает сколько раз
    элемент встречается в списке

    Пример: count_element([1, 2, 2, 3, 2], 2) → 3
    """
    pass


# Задача 15: Только чётные числа
def task15():
    """
    Создай функцию get_even_numbers(numbers), которая возвращает новый список
    содержащий только чётные числа

    Пример: get_even_numbers([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
    """
    pass


# ============================================================================
# УРОВЕНЬ 4: Работа со строками (String Operations)
# ============================================================================

# Задача 16: Подсчёт гласных
def task16():
    """
    Создай функцию count_vowels(text), которая возвращает количество гласных
    Гласные: a, e, i, o, u (учитывай оба варианта регистра)

    Пример: count_vowels("hello") → 2
    """
    pass


# Задача 17: Проверка палиндрома
def task17():
    """
    Создай функцию is_palindrome(text), которая проверяет является ли строка палиндромом
    Игнорируй пробелы и регистр букв

    Пример: is_palindrome("racecar") → True
             is_palindrome("hello") → False
    """
    pass


# Задача 18: Развернуть порядок слов
def task18():
    """
    Создай функцию reverse_words(text), которая разворачивает порядок слов

    Пример: reverse_words("hello world") → "world hello"
             reverse_words("one two three") → "three two one"
    """
    pass


# Задача 19: Частота символов в строке
def task19():
    """
    Создай функцию char_frequency(text), которая возвращает словарь
    где ключи — символы, значения — количество повторений
    Учитывай регистр букв

    Пример: char_frequency("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    pass


# Задача 20: Капитализация каждого слова
def task20():
    """
    Создай функцию capitalize_words(text), которая переводит в заглавную первую букву каждого слова

    Пример: capitalize_words("hello world") → "Hello World"
    Не используй встроенный метод title()
    """
    pass


# ============================================================================
# УРОВЕНЬ 5: Параметры функций (*args, **kwargs)
# ============================================================================

# Задача 21: Суммирование любого количества чисел
def task21():
    """
    Создай функцию sum_all(*numbers), которая суммирует любое количество аргументов

    Пример: sum_all(1, 2, 3, 4, 5) → 15
             sum_all(10, 20) → 30
    """
    pass


# Задача 22: Информация о персоне
def task22():
    """
    Создай функцию person_info(**info), которая возвращает отформатированную строку
    Формат: "name is age years old and lives in city"

    Пример: person_info(name="Alice", age=30, city="NYC") →
            "Alice is 30 years old and lives in NYC"
    """
    pass


# Задача 23: Объединение списков
def task23():
    """
    Создай функцию merge_lists(*lists), которая объединяет несколько списков в один

    Пример: merge_lists([1, 2], [3, 4], [5, 6]) → [1, 2, 3, 4, 5, 6]
    """
    pass


# Задача 24: Поиск максимума и минимума
def task24():
    """
    Создай функцию min_max(*numbers), которая возвращает кортеж (минимум, максимум)
    Используй *args для любого количества чисел

    Пример: min_max(5, 2, 8, 1, 9) → (1, 9)
    """
    pass


# Задача 25: Печать информации с **kwargs
def task25():
    """
    Создай функцию print_info(**kwargs), которая выводит информацию в формате
    "ключ: значение" для каждого параметра

    Пример: print_info(name="Alice", age=30)
    Вывод:
    name: Alice
    age: 30
    """
    pass


# ============================================================================
# УРОВЕНЬ 6: Лямбда-функции и встроенные функции
# ============================================================================

# Задача 26: Возведение в квадрат через map()
def task26():
    """
    Создай функцию square_all(numbers), которая возвращает новый список
    с квадратом каждого числа, используя map()

    Пример: square_all([1, 2, 3, 4]) → [1, 4, 9, 16]
    """
    pass


# Задача 27: Фильтр чисел через filter()
def task27():
    """
    Создай функцию greater_than(numbers, threshold), которая возвращает список
    чисел больших чем threshold, используя filter()

    Пример: greater_than([1, 5, 3, 8, 2], 3) → [5, 8]
    """
    pass


# Задача 28: Сортировка с lambda
def task28():
    """
    Создай функцию sort_students(students), которая сортирует студентов по оценкам (от меньшего к большему)
    students — список кортежей (имя, оценка)

    Пример: sort_students([("Alice", 85), ("Bob", 92), ("Charlie", 78)])
            → [("Charlie", 78), ("Alice", 85), ("Bob", 92)]
    """
    pass


# Задача 29: Преобразование и фильтрация
def task29():
    """
    Создай функцию process_numbers(numbers), которая:
    - возводит каждое число в квадрат
    - оставляет только числа > 10

    Пример: process_numbers([1, 2, 3, 4, 5]) → [16, 25]
            (2^2=4, 3^2=9, 4^2=16, 5^2=25; > 10 → [16, 25])
    """
    pass


# Задача 30: Слова определённой длины
def task30():
    """
    Создай функцию words_with_length(words, length), которая возвращает
    слова определённой длины, используя filter()

    Пример: words_with_length(["apple", "cat", "banana", "dog"], 4)
            → ["apple"]
    """
    pass


# ============================================================================
# УРОВЕНЬ 7: Рекурсия (базовая)
# ============================================================================

# Задача 31: Факториал
def task31():
    """
    Создай функцию factorial(n), которая вычисляет факториал числа рекурсивно
    n! = n * (n-1) * (n-2) * ... * 1

    Пример: factorial(5) → 120
             factorial(0) → 1
    """
    pass


# Задача 32: Степень числа
def task32():
    """
    Создай функцию power(base, exponent), которая вычисляет base в степени exponent рекурсивно
    Не используй встроенный оператор **

    Пример: power(2, 3) → 8
             power(5, 0) → 1
    """
    pass


# Задача 33: Сумма цифр числа
def task33():
    """
    Создай функцию sum_of_digits(n), которая рекурсивно суммирует все цифры числа

    Пример: sum_of_digits(123) → 6  (1+2+3)
             sum_of_digits(999) → 27 (9+9+9)
    """
    pass


# Задача 34: Сумма чисел в списке
def task34():
    """
    Создай функцию sum_list_recursive(lst), которая рекурсивно суммирует элементы списка

    Пример: sum_list_recursive([1, 2, 3, 4]) → 10
    """
    pass


# Задача 35: Поиск элемента в списке
def task35():
    """
    Создай функцию find_element(lst, target), которая рекурсивно ищет элемент в списке
    Возвращает индекс или -1 если не найден

    Пример: find_element([1, 5, 3, 8, 2], 8) → 3
             find_element([1, 5, 3], 7) → -1
    """
    pass


# ============================================================================
# ИТОГОВЫЕ ЗАДАЧИ
# ============================================================================

# Задача 36: Комбинированная функция
def task36():
    """
    Создай функцию process_grades(**students), которая:
    - принимает студентов и их оценки как **kwargs (например: Alice=85, Bob=92)
    - возвращает словарь со статистикой:
      {
        "students": ["Alice", "Bob"],
        "average": среднее арифметическое,
        "best_student": имя студента с лучшей оценкой,
        "count": количество студентов
      }

    Пример: process_grades(Alice=85, Bob=92, Charlie=78)
    """
    pass


# Задача 37: Валидация данных
def task37():
    """
    Создай функцию validate_user(name, email, age), которая проверяет:
    - name: не пусто, минимум 2 символа
    - email: содержит @ и точку
    - age: число между 18 и 120

    Возвращает (True, "") если всё ОК или (False, "сообщение об ошибке")
    """
    pass


# Задача 38: Преобразование текста
def task38():
    """
    Создай функцию transform_text(text), которая:
    - переводит в нижний регистр
    - удаляет лишние пробелы (в начале и конце)
    - заменяет несколько пробелов подряд на один
    - возвращает преобразованный текст

    Пример: transform_text("  Hello    World  ") → "hello world"
    """
    pass


# Задача 39: Работа со словарями
def task39():
    """
    Создай функцию merge_dicts(*dicts), которая объединяет несколько словарей
    Если ключи повторяются, позже идущий словарь перезаписывает значения

    Пример: merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
            → {"a": 1, "b": 3, "c": 4}
    """
    pass


# Задача 40: Фильтрация и трансформация
def task40():
    """
    Создай функцию filter_and_transform(words, min_length), которая:
    - оставляет слова длиннее min_length
    - преобразует их в ВЕРХНИЙ РЕГИСТР
    - возвращает отсортированный список

    Пример: filter_and_transform(["apple", "cat", "banana", "dog"], 3)
            → ["APPLE", "BANANA"]
    """
    pass


# ============================================================================
# ТЕСТИРОВАНИЕ
# ============================================================================

if __name__ == "__main__":
    print("=== ОСНОВЫ ФУНКЦИЙ В PYTHON ===\n")
    print("Выполни все задачи выше и проверь их работу здесь!\n")

    print("Примеры для тестирования (раскомментируй когда напишешь функции):\n")

    # # УРОВЕНЬ 1
    # print("Task 1 - add(5, 3):", task1())
    # print("Task 2 - is_even(4):", task2())

    # # УРОВЕНЬ 2
    # print("Task 7 - classify_number(5):", task7())
    # print("Task 8 - get_age_category(25):", task8())

    # # УРОВЕНЬ 3
    # print("Task 11 - sum_list([1,2,3,4]):", task11())
    # print("Task 15 - get_even_numbers([1,2,3,4,5,6]):", task15())

    # # УРОВЕНЬ 4
    # print("Task 17 - is_palindrome('racecar'):", task17())
    # print("Task 19 - char_frequency('hello'):", task19())

    # # И так далее...
