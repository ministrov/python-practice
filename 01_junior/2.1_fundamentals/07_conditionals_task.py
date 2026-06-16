"""
Микро-задача №3: Условия (if/elif/else)
Запуск: python 07_conditionals_task.py
"""

# ============ ЗАДАНИЕ 1: Проверка возраста ============
print("=== Задание 1: Проверка возраста ===")
# TODO: Напиши код:
# 1. Объяви переменную age = 25
# 2. Если age >= 18 → выведи "Ты совершеннолетний"
# 3. Иначе → выведи "Ты ещё не совершеннолетний"
age = 25
if age >= 18:
    print("Ты совершеннолетний")
else:
    print("Ты ещё не совершеннолетний")


# ============ ЗАДАНИЕ 2: Оценка по баллам ============
print("\n=== Задание 2: Оценка по баллам ===")
# TODO: Напиши код:
# 1. Объяви переменную score = 78
# 2. Используй if/elif/else:
#    - score >= 90 → "Отлично!"
#    - score >= 75 → "Хорошо!"
#    - score >= 60 → "Удовлетворительно"
#    - иначе → "Плохо"

score = 78
if score >= 90:
    print("Отлично")
elif score >= 75:
    print("Хорошо")
elif score >= 60:
    print("Удовлетворительно")
else:
    print("Плохо")


# ============ ЗАДАНИЕ 3: Логические операторы (and) ============
print("\n=== Задание 3: Доступ в клуб (and) ===")
# TODO: Напиши код:
# 1. Объяви переменные: age = 21, has_ticket = True
# 2. Если age >= 18 AND has_ticket → "Добро пожаловать!"
# 3. Иначе → "Вход запрещён"

age = 21
has_ticket = True
if age >= 18 and has_ticket:
    print("Добро пожаловать!")
else:
    print("Вход запрещён")


# ============ ЗАДАНИЕ 4: Логические операторы (or) ============
print("\n=== Задание 4: Скидка (or) ===")
# TODO: Напиши код:
# 1. Объяви переменные: is_student = True, is_elderly = False
# 2. Если is_student OR is_elderly → "Скидка 30%"
# 3. Иначе → "Полная цена"

is_student = True
is_elderly = False

if is_student or is_elderly:
    print("Скидка 30%")


# ============ ЗАДАНИЕ 5: Логический оператор (not) ============
print("\n=== Задание 5: Погода (not) ===")
# TODO: Напиши код:
# 1. Объяви переменную is_raining = False
# 2. Если NOT is_raining → "Можем гулять!"
# 3. Иначе → "Остаемся дома"

is_raining = False
if not is_raining:
    print("Можем гулять!")
else:
    print("Остаемся дома")


# ============ ЗАДАНИЕ 6: Проверка на None ============
print("\n=== Задание 6: Проверка на None ===")
# TODO: Напиши код:
# 1. Объяви переменную username = None
# 2. Если username is None → "Пользователь не установлен"
# 3. Иначе → f"Привет, {username}!"

username = None
if username is None:
    print("Пользователь не установлен")
else:
    print(f"Привет, {username}!") 


# ============ ЗАДАНИЕ 7: Тернарное выражение ============
print("\n=== Задание 7: Тернарное выражение ===")
# TODO: Напиши код:
# 1. Объяви переменную temperature = 30
# 2. Используя ОДНУ строку (тернарное выражение):
#    temperature > 20 → "Жарко", иначе → "Холодно"
# 3. Выведи результат

temperature = 30

one_liner = "Жарко" if temperature > 20 else "Холодно"

print(one_liner)

# ============ ЗАДАНИЕ 8: in для строк ============
print("\n=== Задание 8: Поиск в строке (in) ===")
# TODO: Напиши код:
# 1. Объяви переменную text = "Hello Python World"
# 2. Если "Python" in text → "Python найден!"
# 3. Иначе → "Python не найден"

text = "Hello Python World"

if "Python" in text:
    print("Python найден!")
else:
    print("Python не найден")


# ============ ЗАДАНИЕ 9: Комбинация условий ============
print("\n=== Задание 9: Доступ к премиум-функции ===")
# TODO: Напиши код:
# 1. Объяви переменные: is_premium = True, has_credits = False
# 2. Если is_premium AND (credits > 0 OR is_premium) → "Доступ разрешён"
# 3. Иначе → "Доступ запрещён"
# (Подсказка: можешь использовать скобки для приоритета)

credits = 0
is_premium = True
has_credits = False
if is_premium and (credits > 0 or is_premium):
    print("Доступ разрешён")
else:
    print("Доступ запрещён")
