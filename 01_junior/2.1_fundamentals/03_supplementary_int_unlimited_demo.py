"""
Демо: int в Python неограничен по размеру.
Запуск:  python 03_int_unlimited_demo.py
"""

import sys

print("=== Маленькие числа ===")
small = 42
print(f"small = {small}")
print(f"Размер в памяти: {sys.getsizeof(small)} байт")
print()

print("=== Большие числа ===")
big = 2 ** 100
print(f"big = 2^100 = {big}")
print(f"Размер в памяти: {sys.getsizeof(big)} байт")
print()

print("=== Очень большие числа ===")
huge = 2 ** 10000
print(f"huge = 2^10000 = {huge}")
print(f"Размер в памяти: {sys.getsizeof(huge)} байт")
print(f"Количество цифр в decimal: {len(str(huge))}")  # сколько цифр, если написать в 10-ичной системе
print()

print("=== Факториал — типичный пример ===")
# Факториал растёт ОЧЕНЬ быстро
factorial_100 = 1
for i in range(1, 101):
    factorial_100 *= i

print(f"100! = {factorial_100}")
print(f"Размер: {sys.getsizeof(factorial_100)} байт")
print(f"Цифр в этом числе: {len(str(factorial_100))}")
print()

print("=== Сравнение: Python vs JavaScript ===")
# В JavaScript 2^53 уже теряет точность:
# console.log(2**53 + 1 === 2**53)  // true (потеря точности!)

# В Python нет потери:
x = 2 ** 53
print(f"Python: 2^53 = {x}")
print(f"Python: 2^53 + 1 = {x + 1}")
print(f"Они разные? {x != x + 1}")  # type: ignore # True!
