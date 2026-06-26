# -*- coding: utf-8 -*-
"""
Блок 2.3.1: Основы функций
════════════════════════════════════════════════════════════════════════

Функция — именованный блок кода, который можно вызывать многократно.
Вместо повторения одного и того же кода — пишешь функцию один раз.

Синтаксис:
  def имя_функции(параметры) -> тип_возврата:
      \"\"\"Docstring — что делает функция.\"\"\"
      тело
      return результат
"""

# ===== БАЗОВОЕ ОПРЕДЕЛЕНИЕ И ВЫЗОВ =====
print("=== ОПРЕДЕЛЕНИЕ И ВЫЗОВ ===\n")


def greet(name: str) -> str:
    """Возвращает приветствие для пользователя."""
    return f"Hello, {name}!"


print(greet("Alice"))   # Hello, Alice!
print(greet("Bob"))     # Hello, Bob!

# Функция без return возвращает None
def say_hi() -> None:
    """Просто печатает, ничего не возвращает."""
    print("Hi!")


say_hi()
result: None = say_hi()
print(f"Возвращает: {result}")   # None

print()

# ===== ПОЗИЦИОННЫЕ И ИМЕНОВАННЫЕ АРГУМЕНТЫ =====
print("=== ПОЗИЦИОННЫЕ И ИМЕНОВАННЫЕ АРГУМЕНТЫ ===\n")


def describe_pet(name: str, animal: str, age: int) -> str:
    """Описывает питомца."""
    return f"{name} — это {animal}, возраст {age} лет"


# Позиционные: порядок важен
print(describe_pet("Барсик", "кот", 3))

# Именованные: порядок не важен
print(describe_pet(animal="собака", age=5, name="Рекс"))

# Смешанный вызов: позиционные ПЕРЕД именованными
print(describe_pet("Кеша", age=7, animal="попугай"))

print()

# ===== ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ =====
print("=== ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ ===\n")


def power(base: int, exp: int = 2) -> int:
    """Возводит base в степень exp (по умолчанию — квадрат)."""
    return base ** exp


print(power(3))       # 9  (exp=2 по умолчанию)
print(power(3, 3))    # 27 (exp=3)
print(power(2, 10))   # 1024


# Параметры с дефолтом — после параметров без дефолта
def greet_user(name: str, greeting: str = "Hello", punct: str = "!") -> str:
    """Гибкое приветствие."""
    return f"{greeting}, {name}{punct}"


print(greet_user("Alice"))                    # Hello, Alice!
print(greet_user("Bob", "Hi"))               # Hi, Bob!
print(greet_user("Charlie", punct="..."))    # Hello, Charlie...

print()

# ===== ЛОВУШКА: MUTABLE DEFAULT ARGUMENT =====
print("=== ЛОВУШКА: ИЗМЕНЯЕМЫЙ АРГУМЕНТ ПО УМОЛЧАНИЮ ===\n")


# ПЛОХО: список создаётся ОДИН РАЗ при определении функции
def add_item_bad(item: str, storage: list[str] = []) -> list[str]:
    """Демонстрирует баг с mutable default."""
    storage.append(item)
    return storage


print(add_item_bad("apple"))   # ['apple']
print(add_item_bad("banana"))  # ['apple', 'banana'] -- БАГ! ожидали ['banana']
print(add_item_bad("cherry"))  # ['apple', 'banana', 'cherry'] -- снова БАГ


# ХОРОШО: используй None как sentinel
def add_item_good(item: str, storage: list[str] | None = None) -> list[str]:
    """Правильный способ с изменяемым дефолтом."""
    if storage is None:
        storage = []
    storage.append(item)
    return storage


print(add_item_good("apple"))   # ['apple']
print(add_item_good("banana"))  # ['banana']  -- правильно!

print()

# ===== ВОЗВРАТ НЕСКОЛЬКИХ ЗНАЧЕНИЙ =====
print("=== ВОЗВРАТ НЕСКОЛЬКИХ ЗНАЧЕНИЙ ===\n")


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Возвращает минимум и максимум списка."""
    return min(numbers), max(numbers)


lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"min={lo}, max={hi}")   # min=1, max=9

# Без распаковки — это tuple
result_tuple: tuple[int, int] = min_max([10, 20, 30])
print(f"Как tuple: {result_tuple}")   # (10, 30)

print()

# ===== DOCSTRING И АННОТАЦИИ ТИПОВ =====
print("=== DOCSTRING И АННОТАЦИИ ТИПОВ ===\n")


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Вычисляет индекс массы тела (BMI).

    Args:
        weight_kg: вес в килограммах
        height_m:  рост в метрах

    Returns:
        BMI = вес / рост^2
    """
    return round(weight_kg / height_m ** 2, 1)


bmi: float = calculate_bmi(70, 1.75)
print(f"BMI: {bmi}")              # 22.9
print(f"Docstring: {calculate_bmi.__doc__!r}"[:60] + "...")

print()

# ===== РАННИЙ RETURN (GUARD CLAUSE) =====
print("=== РАННИЙ RETURN ===\n")


def divide(a: float, b: float) -> float | None:
    """Делит a на b; возвращает None при делении на 0."""
    if b == 0:
        print("Ошибка: деление на ноль")
        return None        # ранний выход
    return a / b


print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Ошибка: деление на ноль / None

print()

# ===== ФУНКЦИИ КАК ОБЪЕКТЫ =====
print("=== ФУНКЦИИ — ЭТО ОБЪЕКТЫ ===\n")

# Функцию можно присвоить переменной
alias = greet
print(alias("Diana"))   # Hello, Diana!

# Передать в другую функцию
names: list[str] = ["Charlie", "Alice", "Bob"]
sorted_names: list[str] = sorted(names, key=str.lower)
print(f"Сортировка через key: {sorted_names}")

# Хранить в списке
operations: list[object] = [str.upper, str.lower, str.title]
word: str = "python"
for op in operations:
    print(f"  {op}('{word}') = {op(word)}")  # type: ignore

print()
print("=== ИТОГО ===")
print("""
def имя(позиц, именов=дефолт) -> тип:
    \"\"\"Docstring.\"\"\"
    return значение

Правила:
- Параметры с дефолтом -- после параметров без дефолта
- Дефолт НИКОГДА не list/dict/set -- используй None
- Аннотируй параметры и возврат (-> тип)
- Пиши docstring для нетривиальных функций
""")
