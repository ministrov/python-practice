# -*- coding: utf-8 -*-
"""
Блок 2.5.6: Демо — dunder-методы (__repr__, __str__, __eq__, __hash__,
__len__, __iter__)
════════════════════════════════════════════════════════════════════════
Темы:
  1. __repr__ — "официальное" представление объекта, для разработчика
  2. __str__ — представление для пользователя (print, f-строки)
  3. __eq__ — что значит "равенство" для ДВУХ экземпляров (== вместо is)
  4. __hash__ — нужен, чтобы объект можно было класть в set/использовать
     как ключ dict; тесно связан с __eq__
  5. __len__ — делает объект совместимым с len(obj)
  6. __iter__ — делает объект совместимым с for ... in obj
"""


# ════════════════════════════════════════════════════════════════════════
# 1. Без dunder-методов — представление объекта по умолчанию бесполезно
# ════════════════════════════════════════════════════════════════════════

class PointPlain:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


plain_point = PointPlain(1, 2)
print(plain_point)
# <__main__.PointPlain object at 0x...> — адрес в памяти, бесполезно
# для отладки: не видно ни x, ни y


# ════════════════════════════════════════════════════════════════════════
# 2. __repr__ — представление "для разработчика" (отладка, консоль, repr())
# ════════════════════════════════════════════════════════════════════════

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # конвенция: должно выглядеть как код, которым можно пересоздать
        # объект — Point(1, 2), а не просто "точка (1, 2)"
        return f"Point(x={self.x}, y={self.y})"


point = Point(1, 2)
print(point)          # Point(x=1, y=2) — print использует __repr__,
                       # если __str__ не определён
print(repr(point))    # Point(x=1, y=2) — то же самое явно через repr()
print([point, point])  # [Point(x=1, y=2), Point(x=1, y=2)] — внутри
                        # списка ВСЕГДА используется __repr__, не __str__


# ════════════════════════════════════════════════════════════════════════
# 3. __str__ — представление "для пользователя" (print, f-строки, str())
# ════════════════════════════════════════════════════════════════════════

class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __repr__(self) -> str:
        return f"Money(amount={self.amount}, currency={self.currency!r})"

    def __str__(self) -> str:
        # человекочитаемый вид — то, что видит конечный пользователь
        return f"{self.amount} {self.currency}"


wallet = Money(100, "USD")
print(wallet)          # 100 USD — print() предпочитает __str__, если он есть
print(str(wallet))     # 100 USD — явно через str()
print(repr(wallet))    # Money(amount=100, currency='USD') — repr() всегда
                        # использует __repr__, игнорируя __str__
print(f"Баланс: {wallet}")  # Баланс: 100 USD — f-строки тоже берут __str__

# Если __str__ не определён — Python МОЛЧА использует __repr__ как замену
# (так было с Point выше). Обратное неверно: __repr__ не подменяется
# автоматически на __str__.


# ════════════════════════════════════════════════════════════════════════
# 4. __eq__ — без него == сравнивает ПО ССЫЛКЕ (как is), не по значению
# ════════════════════════════════════════════════════════════════════════

class VectorNoEq:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


v1 = VectorNoEq(1, 2)
v2 = VectorNoEq(1, 2)
print(v1 == v2)   # False — разные объекты в памяти, хотя данные одинаковые
print(v1 == v1)   # True — это буквально один и тот же объект


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        # other: object — на вход может прийти ЧТО УГОДНО, не только Vector
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y


w1 = Vector(1, 2)
w2 = Vector(1, 2)
print(w1 == w2)      # True — теперь сравниваются ЗНАЧЕНИЯ x и y
print(w1 == "1, 2")  # False — сравнение с несовместимым типом, без ошибки


# ════════════════════════════════════════════════════════════════════════
# 5. __hash__ — нужен для set/dict-ключей; ломается автоматически при
#    добавлении __eq__, если не объявить явно
# ════════════════════════════════════════════════════════════════════════

try:
    coords_broken: set[Vector] = {w1, w2}  # type: ignore[misc] # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")
# Ошибка: cannot use 'Vector' as a set element (unhashable type: 'Vector')
# — Python видит, что мы определили
# __eq__ вручную, и на всякий случай ОТКЛЮЧАЕТ унаследованный __hash__
# (иначе объекты, равные по ==, могли бы попасть в set как "разные")


class HashableVector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"HashableVector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashableVector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        # ПРАВИЛО: если a == b, то hash(a) должен быть равен hash(b) —
        # проще всего хэшировать тот же набор полей, что участвует в __eq__
        return hash((self.x, self.y))


h1 = HashableVector(1, 2)
h2 = HashableVector(1, 2)
print(h1 == h2)              # True
print(hash(h1) == hash(h2))  # True — обязательное следствие равенства
coords: set[HashableVector] = {h1, h2}
print(len(coords))            # 1 — h1 и h2 равны, значит это "один и тот
                               # же" элемент множества


# ════════════════════════════════════════════════════════════════════════
# 6. __len__ — делает объект совместимым с len(obj)
# ════════════════════════════════════════════════════════════════════════

class Playlist:
    def __init__(self, tracks: list[str]) -> None:
        self.tracks = tracks

    def __len__(self) -> int:
        return len(self.tracks)


playlist = Playlist(["Song A", "Song B", "Song C"])
print(len(playlist))   # 3 — len() вызывает __len__ под капотом

# Побочный эффект: объект без __bool__, но с __len__, участвует в
# if/bool() через длину — 0 считается "ложным", ненулевое — "истинным"
empty_playlist = Playlist([])
print(bool(empty_playlist))   # False — len() == 0
print(bool(playlist))         # True — len() == 3


# ════════════════════════════════════════════════════════════════════════
# 7. __iter__ — делает объект совместимым с for ... in obj
# ════════════════════════════════════════════════════════════════════════

class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self):
        # генератор — yield по очереди отдаёт значения при каждом шаге for
        current = self.start
        while current > 0:
            yield current
            current -= 1


for number in Countdown(3):
    print(number)
# 3
# 2
# 1

# list()/tuple()/множество из объекта тоже работают через __iter__
print(list(Countdown(3)))   # [3, 2, 1]
