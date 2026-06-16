"""
Тема 3: Условия (if/elif/else)
Запуск: python 06_conditionals_demo.py
"""

# ============ ОСНОВЫ ============

print("=== 1. Базовый if ===")
age = 20
if age >= 18:
    print("Ты совершеннолетний")
# Блок кода выполняется, если условие True

age = 15
if age >= 18:
    print("Ты совершеннолетний")
# Этот блок НЕ выполнится, потому что условие False


print("\n=== 2. if/else ===")
age = 20
if age >= 18:
    print("Ты совершеннолетний")
else:
    print("Ты ещё не совершеннолетний")

# Всегда выполнится ОДИН из двух блоков


print("\n=== 3. if/elif/else ===")
score = 75

if score >= 90:
    print("Отличная оценка!")
elif score >= 70:
    print("Хорошая оценка!")
elif score >= 50:
    print("Средняя оценка")
else:
    print("Плохая оценка")

# Проверяются условия ПО ПОРЯДКУ.
# Выполнится ПЕРВЫЙ elif, который True.
# Если все False → выполнится else


print("\n=== 4. Логические операторы: and ===")
age = 25
has_license = True

if age >= 18 and has_license:
    print("Ты можешь водить машину!")
else:
    print("Нельзя водить")

# `and` — ОБА условия должны быть True


print("\n=== 5. Логические операторы: or ===")
is_student = True
is_elderly = False

if is_student or is_elderly:
    print("Скидка 50%!")
else:
    print("Полная цена")

# `or` — ХОТЯ БЫ ОДНО условие должно быть True


print("\n=== 6. Логические операторы: not ===")
is_raining = False

if not is_raining:
    print("Пойдём гулять!")
else:
    print("Остаемся дома")

# `not` — инвертирует True в False и наоборот


print("\n=== 7. Вложенные условия ===")
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Ты можешь водить!")
    else:
        print("Нужны права")
else:
    print("Ты слишком молодой")

# То же самое, но с вложенностью


print("\n=== 8. Сравнение значений ===")
x = 10

# Операторы сравнения:
print(f"x > 5: {x > 5}")      # True
print(f"x < 5: {x < 5}")      # False
print(f"x >= 10: {x >= 10}")  # True
print(f"x <= 10: {x <= 10}")  # True
print(f"x == 10: {x == 10}")  # True
print(f"x != 5: {x != 5}")    # type: ignore # True


print("\n=== 9. Проверка на None ===")
value = None

if value is None:
    print("Значение не установлено")
else:
    print(f"Значение: {value}")

# Всегда используй `is None`, а не `== None`


print("\n=== 10. Проверка булевых значений ===")
is_active = True

if is_active:
    print("Активно")
else:
    print("Не активно")

# Не нужно писать `if is_active == True` — просто `if is_active`


print("\n=== 11. Тернарное выражение (одна строка) ===")
age = 20
message = "Взрослый" if age >= 18 else "Ребёнок"
print(message)

# Синтаксис: value_if_true if condition else value_if_false
# Полезно для одной простой переменной


print("\n=== 12. in и not in (для строк и списков) ===")
text = "Hello World"

if "World" in text:
    print("'World' найдено в тексте")

if "Python" not in text:
    print("'Python' не найдено в тексте")

# Для проверки наличия подстроки или элемента
