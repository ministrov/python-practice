"""
Блок 2.1 — Тема 1: Типы данных (ДЕМО, прочитай и запусти).
Запуск:  python 01_types_demo.py
"""

# --- Базовые типы и функция type() ---
age = 42
price = 3.14
name = "Anton"
is_student = True
nothing = None

print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>

print("-" * 30)

# --- Деление: / даёт float, // даёт int ---
print(34 / 2)    # 17.0  <- float!
print(34 // 2)   # 17    <- int
print(35 // 2)   # 17    <- отбрасывает дробную часть
print(35 % 2)    # 1     <- остаток от деления

print("-" * 30)

# --- bool — это подтип int (важная деталь Python) ---
print(True + True)      # 2   (True == 1, False == 0)
print(isinstance(True, int))  # type: ignore # True

print("-" * 30)

# --- int в Python неограничен по размеру ---
print(2 ** 100)  # огромное число без переполнения

print("-" * 30)

# --- Приведение типов (как в твоём hell.py) ---
divider = 34 / 2          # 17.0 (float)
super_divider = int(divider)  # 17 (int) — snake_case, не camelCase!
print(divider, type(divider))
print(super_divider, type(super_divider))
