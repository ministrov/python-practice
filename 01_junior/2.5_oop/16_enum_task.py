# -*- coding: utf-8 -*-
"""
Блок 2.5.8: Практика — Enum (перечисления)
════════════════════════════════════════════════════════════════════════
7 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 15_enum_demo.py, если застрял с синтаксисом.
"""

from enum import Enum, IntEnum, auto


print("=" * 60)
print("ЗАДАНИЕ 1: базовый Enum")
print("=" * 60)
print("""
1.1 Создай класс Color(Enum) с членами RED, GREEN, BLUE, значения —
    строки "red", "green", "blue".
1.2 Напечатай Color.RED, Color.RED.name, Color.RED.value.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: auto()")
print("=" * 60)
print("""
2.1 Создай класс Weekday(Enum) с членами MONDAY..SUNDAY (7 штук),
    значения — через auto() (конкретные числа не важны).
2.2 Напечатай Weekday.MONDAY.value и Weekday.SUNDAY.value.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: сравнение членов")
print("=" * 60)
print("""
3.1 Используя Color из задания 1, создай переменную
    chosen = Color.GREEN.
3.2 Напечатай результат chosen == Color.GREEN и chosen is Color.GREEN
    (оба должны быть True).
3.3 Напечатай результат chosen == Color.RED (должно быть False).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: итерация по Enum")
print("=" * 60)
print("""
4.1 Пройдись циклом for по всем членам Weekday из задания 2.
4.2 Для каждого напечатай member.name и member.value через " -> ".
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: IntEnum")
print("=" * 60)
print("""
5.1 Создай класс TaskPriority(IntEnum) с членами LOW = 1, MEDIUM = 2,
    HIGH = 3.
5.2 Напечатай результат TaskPriority.HIGH > TaskPriority.MEDIUM
    (должно быть True — IntEnum поддерживает сравнение как int).
5.3 Напечатай sorted([...]) из всех трёх членов в случайном порядке
    в списке (например [TaskPriority.HIGH, TaskPriority.LOW,
    TaskPriority.MEDIUM]).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Enum в аннотации типа функции")
print("=" * 60)
print("""
6.1 Напиши функцию describe_priority(priority: TaskPriority) -> str,
    которая через match/case (или if/elif) возвращает разный текст
    для LOW / MEDIUM / HIGH.
6.2 Вызови её для TaskPriority.MEDIUM, напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: комплексное — светофор")
print("=" * 60)
print("""
7.1 Создай класс TrafficLight(Enum) с членами RED, YELLOW, GREEN.
7.2 Напиши функцию next_light(current: TrafficLight) -> TrafficLight,
    возвращающую следующий свет по кругу: RED -> GREEN -> YELLOW ->
    RED (используй match/case или if/elif, не полагайся на порядок
    объявления).
7.3 Начни с TrafficLight.RED, вызови next_light() 4 раза подряд,
    печатая каждый результат — проверь, что цикл замкнулся правильно.
""")

# ТВОЙ КОД ЗДЕСЬ:
