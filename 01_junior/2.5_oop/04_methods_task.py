# -*- coding: utf-8 -*-
"""
Блок 2.5.2: Практика — методы: обычные, @classmethod, @staticmethod,
@property
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 03_methods_demo.py, если застрял с синтаксисом.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: @staticmethod — независимая от состояния утилита")
print("=" * 60)
print("""
1.1 Создай класс StringUtils с @staticmethod is_palindrome(text: str)
    -> bool, проверяющим, что text одинаково читается в обе стороны
    (без учёта регистра).
1.2 Вызови is_palindrome через ИМЯ КЛАССА для "topot" и "python",
    напечатай оба результата.
""")

# ТВОЙ КОД ЗДЕСЬ:


class StringUtils:
    @staticmethod
    def is_palindrome(text: str) -> bool:
        reversed_text = text[::-1]
        return text.lower() == reversed_text.lower()


print(StringUtils.is_palindrome("topot"))
print(StringUtils.is_palindrome("python"))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: несколько @staticmethod в одном классе")
print("=" * 60)
print("""
2.1 Создай класс Validator с двумя @staticmethod:
    - is_valid_age(age: int) -> bool (True, если 0 <= age <= 150)
    - is_valid_email(email: str) -> bool (True, если в строке есть "@"
      и есть хотя бы один символ до и после "@")
2.2 Проверь is_valid_age на 30 и на 200, is_valid_email на
    "a@b.com" и на "not-an-email" — напечатай все 4 результата.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: @classmethod как альтернативный конструктор")
print("=" * 60)
print("""
3.1 Создай класс Point с __init__(self, x: float, y: float).
3.2 Добавь @classmethod origin(cls), возвращающий Point(0, 0).
3.3 Добавь @classmethod from_tuple(cls, coords: tuple[float, float]),
    возвращающий Point с распакованными координатами.
3.4 Создай точку через origin(), через from_tuple((3, 4)) и напрямую
    Point(1, 2) — напечатай x и y всех трёх.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: @classmethod, считающий экземпляры (атрибут класса)")
print("=" * 60)
print("""
4.1 Создай класс User с атрибутом КЛАССА count = 0.
4.2 В __init__(self, name: str) увеличивай User.count на 1 при
    создании каждого экземпляра.
4.3 Добавь @classmethod get_count(cls), возвращающий текущее
    значение count.
4.4 Создай 3 экземпляра User, напечатай get_count() до и после
    создания всех трёх (должно быть 0, затем 3).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: @property — вычисляемое значение без хранения")
print("=" * 60)
print("""
5.1 Создай класс Temperature с __init__(self, celsius: float),
    сохраняющим celsius как атрибут экземпляра.
5.2 Добавь @property fahrenheit, возвращающий celsius, переведённый
    в градусы Фаренгейта: celsius * 9 / 5 + 32.
5.3 Создай Temperature(0) и Temperature(100), напечатай fahrenheit
    у обоих БЕЗ скобок (как атрибут).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: @property + @x.setter с валидацией")
print("=" * 60)
print("""
6.1 Создай класс Product с __init__(self, name: str, price: float),
    сохраняющим name напрямую и price ЧЕРЕЗ property-сеттер (то есть
    внутри __init__ напиши self.price = price, а не self._price).
6.2 Сделай price property: геттер возвращает self._price, сеттер
    проверяет price >= 0 и бросает ValueError("Цена не может быть
    отрицательной"), если условие нарушено.
6.3 Создай Product("Книга", 500), напечатай price, затем присвой
    price = 700 и снова напечатай.
6.4 Попробуй присвоить price = -100 в try/except ValueError,
    напечатай текст ошибки, затем убедись что price не изменился.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: property без setter — только для чтения")
print("=" * 60)
print("""
7.1 Создай класс Circle с __init__(self, radius: float).
7.2 Добавь @property diameter, возвращающий radius * 2 (setter НЕ
    добавляй).
7.3 Создай Circle(5), напечатай diameter.
7.4 Попробуй присвоить circle.diameter = 20 в try/except
    AttributeError, напечатай текст ошибки.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: комплексное — обычный метод + classmethod + property")
print("=" * 60)
print("""
8.1 Создай класс Order с __init__(self, item: str, quantity: int,
    unit_price: float).
8.2 Добавь ОБЫЧНЫЙ метод total(self) -> float, возвращающий
    quantity * unit_price.
8.3 Добавь @classmethod single(cls, item: str, unit_price: float),
    возвращающий Order с quantity=1.
8.4 Добавь @property description, возвращающий строку вида
    "<quantity> x <item> = <total>" (используй total() внутри).
8.5 Создай Order("яблоко", 3, 50.0) и Order.single("хлеб", 80.0),
    напечатай total() и description у обоих.
""")

# ТВОЙ КОД ЗДЕСЬ:
