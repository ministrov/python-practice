"""
ДЕМО: match / case — структурное сопоставление с образцом (structural pattern matching)
Python 3.10+

Что это: способ "разветвить" логику по форме данных.
Похоже на switch из других языков, но мощнее — умеет смотреть ВНУТРЬ структур.

Правило: Python проверяет case'ы СВЕРХУ ВНИЗ и выполняет ПЕРВЫЙ подходящий.
Запусти файл: python 09_match_case_demo.py
"""

print("=" * 55)
print("1) БАЗА: сравнение с литералами (как switch)")
print("=" * 55)

# match берёт значение и сравнивает его с каждым образцом (case)
def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:            # _ это "wildcard" — ловит ВСЁ остальное (как else)
            return "Unknown"

print(http_status(200))   # OK
print(http_status(404))   # Not Found
print(http_status(123))   # Unknown  (сработал case _)


print("\n" + "=" * 55)
print("2) НЕСКОЛЬКО значений в одном case — оператор |")
print("=" * 55)

def day_type(day: str) -> str:
    match day:
        case "сб" | "вс":          # | означает "или"
            return "Выходной"
        case "пн" | "вт" | "ср" | "чт" | "пт":
            return "Будний"
        case _:
            return "Не день недели"

print(day_type("сб"))   # Выходной
print(day_type("ср"))   # Будний
print(day_type("xyz"))  # Не день недели


print("\n" + "=" * 55)
print("3) ЗАХВАТ значения (capture) — переменная вместо литерала")
print("=" * 55)

# Если в case стоит ИМЯ (а не литерал), оно ЗАХВАТЫВАЕТ значение.
# Это как case _, но ты ещё и получаешь значение в переменную.
def greet(value: int) -> str:
    match value:
        case 0:
            return "Ноль"
        case n:                  # n захватит любое другое значение
            return f"Число {n}"

print(greet(0))    # Ноль
print(greet(42))   # Число 42

# ⚠️ ЛОВУШКА: case с одиночным именем ловит ВСЁ, поэтому ставь его ПОСЛЕДНИМ.
#    case ниже него никогда не сработают (Python даже предупредит).


print("\n" + "=" * 55)
print("4) GUARD — дополнительное условие через if")
print("=" * 55)

# К case можно добавить if — образец сработает, только если условие True.
def classify(n: int) -> str:
    match n:
        case x if x < 0:
            return "Отрицательное"
        case 0:
            return "Ноль"
        case x if x % 2 == 0:
            return "Положительное чётное"
        case _:
            return "Положительное нечётное"

print(classify(-5))  # Отрицательное
print(classify(0))   # Ноль
print(classify(10))  # Положительное чётное
print(classify(7))   # Положительное нечётное


print("\n" + "=" * 55)
print("5) ПОСЛЕДОВАТЕЛЬНОСТИ — заглядываем внутрь списка/кортежа")
print("=" * 55)

# Образец может описывать ФОРМУ структуры и разбирать её на части.
def describe_point(point: tuple[int, int]) -> str:
    match point:
        case (0, 0):
            return "Начало координат"
        case (x, 0):                 # любая точка на оси X
            return f"На оси X, x={x}"
        case (0, y):                 # любая точка на оси Y
            return f"На оси Y, y={y}"
        case (x, y):                 # любая пара — разбираем на x и y
            return f"Точка ({x}, {y})"
        case _:
            return "Не точка"

print(describe_point((0, 0)))   # Начало координат
print(describe_point((5, 0)))   # На оси X, x=5
print(describe_point((3, 4)))   # Точка (3, 4)

# *rest ловит "хвост" списка любой длины
def first_and_rest(items: list[int]) -> str:
    match items:
        case []:
            return "Пусто"
        case [single]:
            return f"Один элемент: {single}"
        case [first, *rest]:         # first = первый, rest = список остальных
            return f"Первый: {first}, остальные: {rest}"
        case _:                      # формально недостижим, но нужен Pylance
            return "Неизвестно"

print(first_and_rest([]))           # Пусто
print(first_and_rest([99]))         # Один элемент: 99
print(first_and_rest([1, 2, 3, 4])) # Первый: 1, остальные: [2, 3, 4]


print("\n" + "=" * 55)
print("6) СЛОВАРИ — сопоставление по ключам")
print("=" * 55)

# Можно проверять наличие ключей и захватывать их значения.
def handle_event(event: dict[str, object]) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"Клик по ({x}, {y})"
        case {"type": "key", "key": k}:
            return f"Нажата клавиша {k}"
        case {"type": t}:
            return f"Неизвестное событие типа {t}"
        case _:
            return "Не событие"

print(handle_event({"type": "click", "x": 10, "y": 20}))  # Клик по (10, 20)
print(handle_event({"type": "key", "key": "Enter"}))      # Нажата клавиша Enter
print(handle_event({"type": "scroll"}))                   # Неизвестное событие типа scroll


print("\n" + "=" * 55)
print("ИТОГ: когда использовать match/case?")
print("=" * 55)
print("""
✅ Когда разветвляешь логику по ФОРМЕ данных (списки, словари, кортежи)
✅ Когда много веток сравнения одного значения с разными вариантами
❌ Для простого "одно условие" — обычный if читается проще
❌ match НЕ нужен, когда хватает if/elif

Ключевые элементы:
  case 200        — литерал (точное совпадение)
  case _          — wildcard (всё остальное, как else)
  case a | b      — несколько вариантов (или)
  case x          — захват значения в переменную x
  case x if ...   — guard (доп. условие)
  case [a, *rest] — разбор последовательности
  case {"k": v}   — разбор словаря по ключам
""")
