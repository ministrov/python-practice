"""
ПРАКТИКА: 30 заданий по Темам 1-3
Типы данных, is vs ==, Условия (if/elif/else)

Инструкция:
1. Замени каждый TODO на рабочий код
2. Запусти файл: python 08_practice_30_tasks.py
3. Проверь, что все выводы правильные
4. Когда закончишь - скопируй ВСЕ выводы и покажи мне

ПРАВИЛА:
- Не меняй print() строки — только заполняй TODO
- Каждое задание должно вывести результат
- Если ошибка — исправь код
"""

# ============ БЛОК 1: Типы данных (Задания 1-10) ============

print("=" * 50)
print("БЛОК 1: ТИПЫ ДАННЫХ")
print("=" * 50)

print("\n--- Задание 1 ---")
# TODO: Создай переменные a=10, b=3.5, c=True, d="Hello"
a = 10
b = 3.5
c = True
d = "Hello"
print(type(a), type(b), type(c), type(d))
# Выведи тип каждой через type()
# ОЖИДАЕМЫЙ ВЫВОД: <class 'int'>, <class 'float'>, <class 'bool'>, <class 'str'>


print("\n--- Задание 2 ---")
# TODO: Объяви x=10 и y=2
x = 10
y = 2

print(x / y)
print(x // y)
print(x % y)
# Выведи результаты:
# x / y (должно быть float)
# x // y (должно быть int)
# x % y (остаток)
# ОЖИДАЕМЫЙ ВЫВОД: 5.0, 5, 0


print("\n--- Задание 3 ---")
# TODO: Создай переменную price = 99.99
price = 99.99
print(int(price))
# Приведи её к int и выведи
# ОЖИДАЕМЫЙ ВЫВОД: 99


print("\n--- Задание 4 ---")
# TODO: Объяви num = 42

num = 42
print(str(num))
# Приведи к строке и выведи (должна быть строка)
# ОЖИДАЕМЫЙ ВЫВОД: 42 (но это строка, не число)


print("\n--- Задание 5 ---")
# TODO: Создай переменную text = "Python"

text = "Python"
# print(int(text))
# Это вызовет ошибку так как int() не может из строки сделать число
# Приведи к int (попробуй)
# Подумай: это вызовет ошибку? Почему?
# ЗАКОММЕНТИРУЙ эту строку, чтобы файл работал!


print("\n--- Задание 6 ---")
# TODO: Объяви a = 5, b = 5.0

a = 5
b = 5.0

print(a == b)
# Выведи a == b (что будет? True или False?)
# ОЖИДАЕМЫЙ ВЫВОД: True (5 == 5.0, потому что значения одинаковые)


print("\n--- Задание 7 ---")
# TODO: Создай строку long_text = "Hello World"

long_text = "Hello World"

print(len(long_text))
# Выведи длину через len()
# ОЖИДАЕМЫЙ ВЫВОД: 11


print("\n--- Задание 8 ---")
# TODO: Объяви list1 = [1, 2, 3]

list1 = [1, 2, 3]

print(type(list1))
# Выведи тип list1 через type()
# ОЖИДАЕМЫЙ ВЫВОД: <class 'list'>


print("\n--- Задание 9 ---")
# TODO: Объяви dict1 = {"name": "Alice", "age": 25}

dict1: dict[str, str | int] = {"name": "Alice", "age": 25}

print(dict1["name"])
# Выведи значение ключа "name"
# ОЖИДАЕМЫЙ ВЫВОД: Alice


print("\n--- Задание 10 ---")
# TODO: Объяви tuple1 = (10, 20, 30)

tuple1 = (10, 20, 30)
print(tuple1[1])
# Выведи второй элемент (индекс 1)
# ОЖИДАЕМЫЙ ВЫВОД: 20


# ============ БЛОК 2: is vs == (Задания 11-20) ============

print("\n" + "=" * 50)
print("БЛОК 2: is vs ==")
print("=" * 50)

print("\n--- Задание 11 ---")
# TODO: Объяви x = 50, y = 50
x = 50
y = 50

print(x == y)
print(x is y)
# Выведи x == y (True или False?)
# Выведи x is y (True или False?)
# ОЖИДАЕМЫЙ ВЫВОД: True, True (50 интернируется)


print("\n--- Задание 12 ---")
# TODO: Объяви x = 500, y = 500
x = 500
y = 500

print(x == y)
print(x is y)
# Выведи x == y
# Выведи x is y
# ОЖИДАЕМЫЙ ВЫВОД: True, False (500 НЕ интернируется)


print("\n--- Задание 13 ---")
# TODO: Объяви list_a = [1, 2, 3]
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)
print(list_a is list_b)
print(list_a is list_c)
# Объяви list_b = [1, 2, 3]
# Объяви list_c = list_a
# Выведи list_a == list_b
# Выведи list_a is list_b
# Выведи list_a is list_c
# ОЖИДАЕМЫЙ ВЫВОД: True, False, True


print("\n--- Задание 14 ---")
# TODO: Объяви value = None
value = None
print(value is None)
print(value == None)  # pyright: ignore[reportUnnecessaryComparison]
# Выведи value is None
# Выведи value == None
# ОЖИДАЕМЫЙ ВЫВОД: True, True (но используй `is None`)


print("\n--- Задание 15 ---")
# TODO: Объяви f1 = 3.14, f2 = 3.14
f1 = 3.14
f2 = 3.14

print(f1 == f2)
print(f1 is f2)
# Выведи f1 == f2
# Выведи f1 is f2
# ОЖИДАЕМЫЙ ВЫВОД: True, False (float не интернируется)


print("\n--- Задание 16 ---")
# TODO: Объяви str1 = "hello", str2 = "hello"
str1 = "hello"
str2 = "hello"

print(str1 == str2)
print(str1 is str2)
# Выведи str1 == str2
# Выведи str1 is str2
# ОЖИДАЕМЫЙ ВЫВОД: True, True (строки интернируются)


print("\n--- Задание 17 ---")
# TODO: Создай функцию change_list(items):
#   items[0] = 999


def change_list(items: list[int]) -> None:
    items[0] = 999


my_list = [1, 2, 3]

print(my_list)
change_list(my_list)
print(my_list)
# Объяви my_list = [1, 2, 3]
# Выведи my_list ДО вызова
# Вызови change_list(my_list)
# Выведи my_list ПОСЛЕ вызова
# ОЖИДАЕМЫЙ ВЫВОД: [1, 2, 3], потом [999, 2, 3]


print("\n--- Задание 18 ---")
# TODO: Объяви x = [10, 20]
x = [10, 20]
y = x
z = x.copy()
y[0] = 999

print(x, y, z)
# Объяви y = x
# Объяви z = x.copy()  (копия!)
# Измени y[0] = 999
# Выведи x, y, z
# ОЖИДАЕМЫЙ ВЫВОД: [999, 20], [999, 20], [10, 20]


print("\n--- Задание 19 ---")
# TODO: Объяви text1 = "Python"
text1 = "Python"
text2 = "Python"
print(text1 is text2)
# Объяви text2 = "Python"
# Выведи text1 is text2
# ОЖИДАЕМЫЙ ВЫВОД: True (строки интернируются)


print("\n--- Задание 20 ---")
# TODO: Объяви bool1 = True
bool1 = True
bool2 = True
print(bool1 is bool2)
# Объяви bool2 = True
# Выведи bool1 is bool2
# ОЖИДАЕМЫЙ ВЫВОД: True (True и False — синглтоны)


# ============ БЛОК 3: Условия (Задания 21-30) ============

print("\n" + "=" * 50)
print("БЛОК 3: УСЛОВИЯ (if/elif/else)")
print("=" * 50)

print("\n--- Задание 21 ---")
# TODO: Объяви number = 15
number = 15

if number > 10:
    print("Больше 10")
else:
    print("Меньше или равно 10")
# Если number > 10 → выведи "Больше 10"
# Иначе → выведи "Меньше или равно 10"
# ОЖИДАЕМЫЙ ВЫВОД: Больше 10


print("\n--- Задание 22 ---")
# TODO: Объяви age = 25
age = 25

if age >= 18:
    print("Взрослый")
else:
    print("Ребёнок")
# Если age >= 18 → выведи "Взрослый"
# Иначе → выведи "Ребёнок"
# ОЖИДАЕМЫЙ ВЫВОД: Взрослый


print("\n--- Задание 23 ---")
# TODO: Объяви score = 82
score = 82

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
# Если score >= 90 → "A"
# elif score >= 80 → "B"
# elif score >= 70 → "C"
# else → "F"
# ОЖИДАЕМЫЙ ВЫВОД: B


print("\n--- Задание 24 ---")
# TODO: Объяви is_sunny = True
is_sunny = True
is_warm = False

if is_sunny and is_warm:
    print("Идеально для пляжа")
else:
    print("Не подходит")
# Объяви is_warm = False
# Если is_sunny AND is_warm → "Идеально для пляжа"
# Иначе → "Не подходит"
# ОЖИДАЕМЫЙ ВЫВОД: Не подходит


print("\n--- Задание 25 ---")
# TODO: Объяви has_money = True
has_money = True
has_time = True

if has_money or has_time:
    print("Можем пойти")
else:
    print("Нельзя пойти")
# Объяви has_time = False
# Если has_money OR has_time → "Можем пойти"
# Иначе → "Нельзя пойти"
# ОЖИДАЕМЫЙ ВЫВОД: Можем пойти


print("\n--- Задание 26 ---")
# TODO: Объяви is_admin = False
is_admin = False

if not is_admin:
    print("Обычный пользователь")
else:
    print("Администратор")
# Если NOT is_admin → "Обычный пользователь"
# Иначе → "Администратор"
# ОЖИДАЕМЫЙ ВЫВОД: Обычный пользователь


print("\n--- Задание 27 ---")
# TODO: Объяви name = None
name = None

if name is None:
    print("Имя не установлено")
else:
    print(f"Привет, {name}!")
# Если name is None → "Имя не установлено"
# Иначе → f"Привет, {name}!"
# ОЖИДАЕМЫЙ ВЫВОД: Имя не установлено


print("\n--- Задание 28 ---")
# TODO: Объяви text = "Python"
text = "Python"

if "P" in text:
    print("Найдена буква P")
else:
    print("P не найдена")
# Если "P" in text → "Найдена буква P"
# Иначе → "P не найдена"
# ОЖИДАЕМЫЙ ВЫВОД: Найдена буква P


print("\n--- Задание 29 ---")
# TODO: Объяви temp = 25
temp = 25

print("Жарко" if temp > 20 else "Холодно")
# Используя ТЕРНАРНОЕ ВЫРАЖЕНИЕ (одна строка):
# Если temp > 20 → "Жарко"
# Иначе → "Холодно"
# Выведи результат
# ОЖИДАЕМЫЙ ВЫВОД: Жарко


print("\n--- Задание 30 (КОМБИНАЦИЯ) ---")
# TODO: Объяви переменные:
age = 22
is_student = True
balance = 150

if age >= 18 and (is_student or balance >= 100):
    print("Доступ разрешён")
else:
    print("Доступ запрещён")
#   age = 22
#   is_student = True
#   balance = 150
# Условие:
#   Если age >= 18 AND (is_student OR balance >= 100) → "Доступ разрешён"
#   Иначе → "Доступ запрещён"
# ОЖИДАЕМЫЙ ВЫВОД: Доступ разрешён


print("\n" + "=" * 50)
print("✅ ВСЕ ЗАДАНИЯ ЗАВЕРШЕНЫ!")
print("=" * 50)
