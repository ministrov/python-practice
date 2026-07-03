# -*- coding: utf-8 -*-
"""
Блок 2.3.2: Практика — *args и **kwargs
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 03_args_kwargs_demo.py если застрял.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: *args — переменное число аргументов")
print("=" * 60)
print("""
1.1 Напиши функцию multiply(*args), которая возвращает
    произведение всех переданных чисел.
    Если аргументов нет — возвращает 1.
    multiply(2, 3, 4) -> 24
    multiply(5)       -> 5
    multiply()        -> 1

1.2 Напиши функцию first_and_last(*args), которая возвращает
    кортеж (первый, последний) элемент.
    Если передан один аргумент — оба элемента одинаковы.
    first_and_last(1, 2, 3, 4) -> (1, 4)
    first_and_last(7)           -> (7, 7)
""")

# ТВОЙ КОД ЗДЕСЬ:


def multiply(*args: int) -> int:
    result = 1
    if len(args) == 0:
        return 1
    for item in args:
        result *= item
    return result


print(multiply(1, 3, 5, 6))
print(multiply(6))
print(multiply())


def first_and_last(*args: int) -> tuple[int, int]:
    if len(args) == 1:
        return (args[0], args[0])

    return (args[0], args[-1])


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: **kwargs — именованные аргументы")
print("=" * 60)
print("""
2.1 Напиши функцию build_query(**kwargs), которая собирает
    строку в формате "key1=value1&key2=value2" (порядок сохраняется).
    build_query(name="Alice", age="30") -> "name=Alice&age=30"
    build_query(lang="Python")          -> "lang=Python"

2.2 Напиши функцию has_key(key, **kwargs), которая возвращает
    True если key присутствует среди kwargs.
    has_key("name", name="Bob", age="25") -> True
    has_key("city", name="Bob")           -> False
""")

# ТВОЙ КОД ЗДЕСЬ:


def build_query(**kwargs: str) -> str:
    return "&".join(f"{key}={value}" for key, value in kwargs.items())


print(build_query(name="Alice", age="20"))


def has_key(key: str, **kwargs: str) -> bool:
    return True if key in kwargs else False


print(has_key("name", name="Bob", age="25"))
print(has_key("city", name="Bob"))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Смешанные аргументы")
print("=" * 60)
print("""
3.1 Напиши функцию tagged(tag, *words), которая возвращает
    список слов, каждое из которых обёрнуто в тег:
    tagged("b", "hello", "world") -> ["<b>hello</b>", "<b>world</b>"]
    tagged("i", "Python")         -> ["<i>Python</i>"]

3.2 Напиши функцию report(title, *items, sep="- "), которая
    возвращает строку вида:
    "TITLE\\n- item1\\n- item2\\n- item3"
    Разделитель items настраивается через sep.
    report("Languages", "Python", "Go", "Rust")
    -> "Languages\\n- Python\\n- Go\\n- Rust"
    report("Steps", "open", "read", sep="* ")
    -> "Steps\\n* open\\n* read"
""")

# ТВОЙ КОД ЗДЕСЬ:


def tagged(tag: str, *words: str) -> list[str]:
    tags: list[str] = []
    for word in words:
        tags.append(f"<{tag}>{word}</{tag}>")
    return tags


print(tagged("b", "hello", "world"))


def report(title: str, *items: str, sep: str = "- ") -> str:
    lines = [title] + [f"{sep}{item}" for item in items]
    return "\n".join(lines)


print(report("Languages", "Python", "Go", "Rust"))
# Languages
# - Python
# - Go
# - Rust

print(report("Steps", "open", "read", sep="* "))
# Steps
# * open
# * read

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Распаковка при вызове")
print("=" * 60)
print("""
4.1 Дан список coordinates = [10, 20, 30].
    Напиши функцию move(x, y, z), которая возвращает строку
    "Moving to x=10, y=20, z=30".
    Вызови её с распаковкой списка: move(*coordinates)

4.2 Дан словарь config = {"host": "localhost", "port": "5432", "db": "mydb"}.
    Напиши функцию connect(host, port, db), которая возвращает строку
    "Connecting to host:port/db".
    Вызови её с распаковкой словаря: connect(**config)
""")

# ТВОЙ КОД ЗДЕСЬ:
coordinates = [10, 20, 30]
config = {"host": "localhost", "port": "5432", "db": "mydb"}


def move(x: int, y: int, z: int) -> str:
    return f"Moving to x={x}, y={y}, z={z}"


print(move(*coordinates))


def connect(host: str, port: str, db: str) -> str:
    return f"Connecting to {host}:{port}/{db}"


print(connect(**config))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: *args с обычными параметрами")
print("=" * 60)
print("""
5.1 Напиши функцию clamp(value, *bounds), где bounds — кортеж (min, max).
    Возвращает value, зажатое в диапазон [min, max].
    Если bounds не передан — возвращает value без изменений.
    clamp(5, 0, 10)  -> 5
    clamp(-3, 0, 10) -> 0
    clamp(15, 0, 10) -> 10
    clamp(7)         -> 7

5.2 Напиши функцию join_strings(*strings, separator=" "), которая
    соединяет строки через separator (keyword-only параметр).
    join_strings("Hello", "World")             -> "Hello World"
    join_strings("a", "b", "c", separator="-") -> "a-b-c"
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: **kwargs с обычными параметрами")
print("=" * 60)
print("""
6.1 Напиши функцию create_user(name, age, **extra), которая
    возвращает словарь с обязательными полями name и age,
    плюс все дополнительные поля из extra.
    create_user("Alice", 30, city="Moscow", role="admin")
    -> {"name": "Alice", "age": 30, "city": "Moscow", "role": "admin"}
    create_user("Bob", 25)
    -> {"name": "Bob", "age": 25}

6.2 Напиши функцию override(defaults, **overrides), где defaults — dict.
    Возвращает новый словарь: defaults + все значения из overrides.
    Значения из overrides перезаписывают defaults.
    override({"color": "red", "size": 10}, color="blue", weight=5)
    -> {"color": "blue", "size": 10, "weight": 5}
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: *args и **kwargs вместе")
print("=" * 60)
print("""
7.1 Напиши функцию format_call(func_name, *args, **kwargs), которая
    возвращает строку, имитирующую вызов функции:
    format_call("print", 1, 2, sep=", ", end="!")
    -> 'print(1, 2, sep=", ", end="!")'
    format_call("len", "hello")
    -> 'len("hello")'

    Подсказка: аргументы собери через запятую в одну строку,
    строки оборачивай в кавычки, числа — без кавычек.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное задание")
print("=" * 60)
print("""
Напиши функцию statistics(*numbers, precision=2), которая:
  - Принимает любое количество чисел через *numbers
  - precision — количество знаков после запятой (keyword-only, default=2)
  - Возвращает dict:
    {
      "count": количество чисел,
      "sum": сумма,
      "min": минимум,
      "max": максимум,
      "mean": среднее (round до precision знаков),
      "range": max - min
    }
  - Если чисел нет — возвращает None

Проверь:
  statistics(4, 7, 2, 9, 1)
  -> {"count": 5, "sum": 23, "min": 1, "max": 9, "mean": 4.6, "range": 8}

  statistics(10, 20, 30, precision=1)
  -> {"count": 3, "sum": 60, "min": 10, "max": 30, "mean": 20.0, "range": 20}

  statistics()  -> None
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
