# -*- coding: utf-8 -*-
"""
Блок 2.5.6: Практика — dunder-методы (__repr__, __str__, __eq__,
__hash__, __len__, __iter__)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 11_dunder_methods_demo.py, если застрял с синтаксисом.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: __repr__")
print("=" * 60)
print("""
1.1 Создай класс Book с __init__(self, title: str, author: str)
    и __repr__(self) -> str, возвращающим
    f"Book(title={title!r}, author={author!r})".
1.2 Создай Book("1984", "Orwell"), напечатай его (print) и напечатай
    repr(...) явно — оба вывода должны совпасть.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: __str__ отдельно от __repr__")
print("=" * 60)
print("""
2.1 Используя Book из задания 1, добавь __str__(self) -> str,
    возвращающий f"{title} автора {author}" (человекочитаемый вид).
2.2 Создай Book("Dune", "Herbert"). Напечатай его через print()
    (должен использоваться __str__), затем напечатай repr(...)
    явно (должен использоваться __repr__ — другой текст).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: __eq__ — сравнение по значению, а не по ссылке")
print("=" * 60)
print("""
3.1 Создай класс Fraction с __init__(self, numerator: int,
    denominator: int).
3.2 Добавь __eq__(self, other: object) -> bool: сравнивай numerator
    и denominator (используй isinstance для проверки типа other,
    верни NotImplemented, если other не Fraction).
3.3 Создай Fraction(1, 2) и Fraction(1, 2) в двух РАЗНЫХ переменных,
    сравни их через == — должно быть True.
3.4 Сравни Fraction(1, 2) с Fraction(2, 3) — должно быть False.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: __eq__ без __hash__ — ловушка unhashable")
print("=" * 60)
print("""
4.1 Используя Fraction из задания 3, попробуй положить два экземпляра
    в set: {Fraction(1, 2), Fraction(1, 2)}.
4.2 Оберни это в try/except TypeError as e, напечатай f"Ошибка: {e}".
    Объясни в комментарии, ПОЧЕМУ так происходит (что Python делает
    автоматически, когда видишь __eq__ без __hash__).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: __hash__ — чинит ловушку из задания 4")
print("=" * 60)
print("""
5.1 Создай класс HashableFraction — как Fraction из задания 3
    (__init__, __eq__), но добавь __hash__(self) -> int,
    возвращающий hash((self.numerator, self.denominator)).
5.2 Создай HashableFraction(1, 2) и HashableFraction(1, 2) в двух
    переменных, положи оба в set, напечатай len(...) — должно быть 1
    (объекты равны по __eq__, значит это один элемент множества).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: __len__")
print("=" * 60)
print("""
6.1 Создай класс Basket с __init__(self, items: list[str]) и
    __len__(self) -> int, возвращающим len(self.items).
6.2 Создай Basket(["apple", "bread", "milk"]), напечатай len(...).
6.3 Создай пустой Basket([]), напечатай bool(...) — должно быть
    False (сравни с непустой корзиной — там bool(...) должен быть
    True).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: __iter__")
print("=" * 60)
print("""
7.1 Создай класс Range2 с __init__(self, start: int, stop: int).
7.2 Добавь __iter__(self) как генератор: yield числа от start
    ДО stop НЕ включительно (аналог range(start, stop), но свой).
7.3 Создай Range2(1, 5), пройдись циклом for и напечатай каждое
    число.
7.4 Напечатай list(Range2(1, 5)) — должно получиться [1, 2, 3, 4].
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: комплексное — класс Card с несколькими dunder-методами")
print("=" * 60)
print("""
8.1 Создай класс Card с __init__(self, rank: str, suit: str).
8.2 Добавь __repr__(self) -> str: f"Card({rank!r}, {suit!r})".
8.3 Добавь __str__(self) -> str: f"{rank} of {suit}".
8.4 Добавь __eq__(self, other: object) -> bool: сравнение по rank
    И suit (с isinstance-проверкой и NotImplemented для чужих типов).
8.5 Добавь __hash__(self) -> int: hash((self.rank, self.suit)).
8.6 Создай card_one = Card("A", "Spades"), card_two = Card("A",
    "Spades") — напечатай print(card_one) (str), repr(card_one),
    card_one == card_two (True), len({card_one, card_two}) (1, за
    счёт __eq__ + __hash__ вместе).
""")

# ТВОЙ КОД ЗДЕСЬ:
