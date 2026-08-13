# ✅ ASSESSMENT: Block 2.5 — ООП и модель данных

**Дата:** _не пройдена_
**Уровень:** Junior (Блок 2.5)
**Темы:** Классы и `self`, методы (`@classmethod`/`@staticmethod`/`@property`), наследование и `super()`, композиция, `dataclasses`, dunder-методы, абстракция (`abc.ABC`), `Enum`/`IntEnum`, 4 столпа ООП
**Критерий прохода:** ≥80% (микровопросы + практика)

---

## ЧАСТЬ 1: Микровопросы (8 вопросов)

**Инструкция:** Ответь на вопросы письменно (что выведет код и почему). Правильные ответы ментор сверит после того, как ты ответишь на все 8 — не подглядывай в код заранее, если не уверен.

### Вопрос 1: Атрибут класса vs атрибут экземпляра

```python
class Cart:
    items = []  # объявлено в теле класса, а не в __init__

    def add(self, item):
        self.items.append(item)


cart_a = Cart()
cart_b = Cart()
cart_a.add("apple")
print(cart_a.items)
print(cart_b.items)
print(cart_a.items is cart_b.items)
```

**Что выведут все три `print()` и почему?**

**Твой ответ:** ________________________

---

### Вопрос 2: `@classmethod` как фабрика

```python
class Pizza:
    def __init__(self, size: str, toppings: list[str]) -> None:
        self.size = size
        self.toppings = toppings

    @classmethod
    def margherita(cls) -> "Pizza":
        return cls("medium", ["cheese", "tomato"])


p = Pizza.margherita()
print(p.size, p.toppings)
```

**Что выведет `print()` и почему?**

**Твой ответ:** ________________________

---

### Вопрос 3: Наследование и `super().__init__()`

```python
class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size = team_size


m = Manager("Ann", 5000, 4)
print(m.name, m.salary, m.team_size)
```

**Что выведет `print()` и почему? Обрати внимание на ТИП значения `m.salary`.**

**Твой ответ:** ________________________

---

### Вопрос 4: Композиция — "имеет", а не "является"

```python
class Engine:
    def start(self) -> str:
        return "Engine started"


class Car:
    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> str:
        return self.engine.start()


car = Car()
print(car.start())
print(isinstance(car, Engine))
```

**Что выведут оба `print()` и почему?**

**Твой ответ:** ________________________

---

### Вопрос 5: `dataclasses` — ловушка изменяемого поля по умолчанию

```python
from dataclasses import dataclass, field


@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)


t1 = Team("A")
t2 = Team("B")
t1.members.append("Alice")
print(t1.members)
print(t2.members)
```

**Что выведут оба `print()` и почему?**

**Твой ответ:** ________________________

---

### Вопрос 6: `__eq__` без `__hash__`

```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
points = {p1}
```

**Что произойдёт при выполнении последней строки и почему?**

**Твой ответ:** ________________________

---

### Вопрос 7: Абстрактное свойство

```python
from abc import ABC, abstractmethod


class Sensor(ABC):
    @property
    @abstractmethod
    def unit(self) -> str:
        ...


class Thermometer(Sensor):
    pass


t = Thermometer()
```

**Что произойдёт при выполнении последней строки и почему?**

**Твой ответ:** ________________________

---

### Вопрос 8: `Enum` без `IntEnum`

```python
from enum import Enum


class Level(Enum):
    LOW = 1
    HIGH = 2


print(Level.HIGH > Level.LOW)
```

**Что произойдёт и почему? Как исправить, если сравнение нужно?**

**Твой ответ:** ________________________

---

## ЧАСТЬ 2: Практическая задача (комплексная)

### Задача: Библиотечная система

Напиши программу, которая объединяет все темы блока 2.5 в одну систему:

1. `ItemStatus(Enum)` с членами `AVAILABLE` и `BORROWED` (значения —
   строки на твой выбор).
2. `LibraryItem(ABC)` — базовый класс:
   - `__init__(self, title: str)`: сохраняет `title` через **property**
     с валидацией (пустая строка → `raise ValueError`); `self.status`
     инициализируется как `ItemStatus.AVAILABLE`.
   - Абстрактный метод `borrow_period_days(self) -> int` — у каждого
     типа предмета свой срок выдачи.
   - Обычный (НЕ абстрактный) метод `borrow(self) -> None` —
     переводит `status` в `ItemStatus.BORROWED` (шаблонный метод,
     использует контракт `borrow_period_days` через наследников, но
     сам не абстрактный).
   - `__repr__(self) -> str`, возвращающий что-то читаемое вроде
     `f"{type(self).__name__}({self.title!r}, {self.status})"`.
3. `Book(LibraryItem)` и `DVD(LibraryItem)` — реализуют
   `borrow_period_days()` по-разному (например 21 и 7 дней).
4. `Member` — **dataclass** с полями `name: str` и
   `borrowed_items: list[LibraryItem]` (через `field(default_factory=list)`,
   не голый `[]`) — Member **имеет** список предметов (композиция).
   Подсказка: голый `field(default_factory=list)` заставит pyright
   --strict вывести `list[Unknown]` (`reportUnknownVariableType`) —
   параметризуй: `field(default_factory=list[LibraryItem])`.
   Добавь метод `borrow(self, item: LibraryItem) -> None`, который
   вызывает `item.borrow()` и добавляет `item` в `borrowed_items`.
5. Продемонстрируй:
   - Создай `Book(...)` и `DVD(...)`, создай `Member(...)`.
   - `member.borrow(book)`, `member.borrow(dvd)`.
   - Пройдись циклом `for` по `member.borrowed_items` (`list[LibraryItem]`)
     — напечатай для каждого `item` его `repr` и `item.borrow_period_days()`
     — код цикла не должен знать заранее, `Book` перед ним или `DVD`
     (полиморфизм).
   - Попробуй создать `LibraryItem("x")` напрямую — поймай `TypeError`.
   - Попробуй создать `Book("")` (пустой title) — поймай `ValueError`.

**Требования:**

- ✅ `Enum` (`ItemStatus`)
- ✅ Абстракция: `abc.ABC` + `@abstractmethod` (`LibraryItem.borrow_period_days`)
- ✅ Инкапсуляция: `title` через `@property` с валидацией
- ✅ Наследование: `Book`/`DVD` + `super().__init__()`
- ✅ Композиция: `Member` содержит список `LibraryItem`
- ✅ `dataclasses`: `Member` (с `field(default_factory=list)`, не mutable
  default напрямую)
- ✅ Полиморфизм: цикл по `list[LibraryItem]`
- ✅ Dunder-метод: `__repr__`
- ✅ Аннотации типов, где Pylance strict их требует
- ✅ `pyright --strict`: 0 errors

**Твой код:**

```python
# YOUR CODE HERE
```

---

## Критерии оценки

### Микровопросы (8 вопросов)

- **Правильные:** 1 балл каждый
- **Проходной балл:** 6–8 правильных (75–100%)

### Практическая задача

- **Работает программа:** 3 балла
- **Использует все требования (Enum, ABC, property, наследование,
  композиция, dataclass, полиморфизм, dunder):** 3 балла
- **Форматирование, читаемость, типизация (`pyright --strict`: 0 errors):** 1 балл
- **Проходной балл:** 6+ баллов из 7

### ФИНАЛЬНЫЙ РЕЗУЛЬТАТ

```
Микровопросы: X/8 (Y%) × 50% вклад
Практика:     X/7 (Y%) × 50% вклад
Проход: ≥80%
```

---

## Инструкция по прохождению

1. **Ответь на микровопросы** (запиши ответы в этот файл или устно) —
   без запуска кода, по чтению
2. **Напиши код для практической задачи**
3. **Протестируй свой код**
4. **Покажи результаты** для проверки
