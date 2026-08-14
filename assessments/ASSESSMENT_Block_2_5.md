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

**Твой ответ:** ['apple'], ['apple'], True.

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

**Твой ответ:**

medium ['cheese', 'tomato']

margherita — classmethod-фабрика: cls внутри неё — это сам класс Pizza, поэтому cls("medium", ["cheese", "tomato"]) эквивалентно Pizza("medium", ["cheese", "tomato"]) и создаёт обычный экземпляр с этими атрибутами.

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

**Твой ответ:** \***\*\*\*\*\***\_\_\_\_\***\*\*\*\*\***
Ann 5000 4

## super().**init**(name, salary) вызывает Employee.**init**, который присваивает self.name и self.salary — тип salary остаётся int, каким он был передан (аннотация float не приводит тип, Python её не проверяет). Затем Manager.**init** добавляет self.team_size.

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

**Твой ответ:** \***\*\*\*\*\***\_\_\_\_\***\*\*\*\*\***
Engine started
False

## Car.start() делегирует вызов своему атрибуту self.engine (композиция — Car имеет Engine), поэтому возвращается "Engine started". Второй print — False, потому что Car не наследуется от Engine (это не отношение "является"), а просто хранит его экземпляр как поле.

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

**Твой ответ:** \***\*\*\*\*\***\_\_\_\_\***\*\*\*\*\***

['Alice']
[]

## default_factory=list вызывает list() заново для каждого нового экземпляра, поэтому t1.members и t2.members — разные списки, и добавление в t1 не влияет на t2. (Если бы вместо этого написали members: list[str] = [], все экземпляры делили бы один и тот же список — это и есть та самая ловушка, которую default_factory решает.)

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

**Твой ответ:** \***\*\*\*\*\***\_\_\_\_\***\*\*\*\*\***

Будет TypeError: unhashable type: 'Point'.

## Когда в классе определён **eq**, Python автоматически устанавливает **hash** в None (если сам **hash** не задан явно), потому что дефолтный **hash** (по id) больше не согласуется с новым **eq** — иначе два «равных» объекта могли бы иметь разный хэш, что ломает контракт хэшируемых типов. А множество (set) требует, чтобы его элементы были хэшируемыми, поэтому попытка добавить p1 в {p1} падает с ошибкой.

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

**Твой ответ:** \***\*\*\*\*\***\_\_\_\_\***\*\*\*\*\***

Будет TypeError: Can't instantiate abstract class Thermometer with abstract method unit (в новых версиях Python формулировка может быть чуть другой, например "without an implementation for abstract method 'unit'").

## Sensor наследуется от ABC, а unit помечен как @abstractmethod (обёрнутый в @property). Thermometer наследует Sensor, но не переопределяет unit, поэтому остаётся абстрактным классом — Python не позволяет создать экземпляр класса, в котором есть хотя бы один нереализованный абстрактный метод.

### Вопрос 8: `Enum` без `IntEnum`

```python
from enum import Enum


class Level(Enum):
    LOW = 1
    HIGH = 2


print(Level.HIGH > Level.LOW)
```

**Что произойдёт и почему? Как исправить, если сравнение нужно?**

**Твой ответ:** \***\*\*\*\*\***\_\_\_\_\***\*\*\*\*\***

Будет TypeError: '>' not supported between instances of 'Level' and 'Level'.

## Обычный Enum не поддерживает операторы сравнения (<, > и т.д.) — члены сравнимы только на равенство (==). Значения 1 и 2 — это просто внутренние значения, они не делают члены упорядочиваемыми. Чтобы исправить нужно воспользоваться IntEnum

## ЧАСТЬ 2: Практическая задача (комплексная)

### Задача: Библиотечная система

Соберёшь одну программу из нескольких классов. Каждый шаг — это то,
что ты уже делал в темах 2-8, здесь просто нужно собрать их вместе.
Делай строго по шагам, не забегая вперёд.

**Шаг 1. Enum статуса**

Класс `ItemStatus(Enum)` с двумя членами: `AVAILABLE` и `BORROWED`.
Значения (то, что справа от `=`) — любые строки на твой выбор,
например `"available"` и `"borrowed"`.

**Шаг 2. Property с валидацией для `title`**

Это НЕ отдельный класс. Этот `property` — часть класса `LibraryItem`,
который ты полностью опишешь в Шаге 3. Здесь просто спланируй код,
а пиши его прямо в теле `LibraryItem`, вместе с `__init__` и
остальными методами из Шага 3.

Внутри класса `LibraryItem` добавь:

- Геттер: декоратор `@property` над `def title(self) -> str:`, тело —
  `return self._title`.
- Сеттер: декоратор `@title.setter` над
  `def title(self, value: str) -> None:` — если `value` пустая строка
  (`if not value:` или `if value == "":`), `raise ValueError(...)`;
  иначе `self._title = value`.
- Отдельно писать `self._title = ...` нигде не нужно — это поле
  появится само, когда в `__init__` (Шаг 3) выполнится
  `self.title = title`: это присваивание пройдёт через сеттер, а
  сеттер и создаст `self._title`.

**Шаг 3. Базовый абстрактный класс `LibraryItem(ABC)`**

В ЭТОТ ЖЕ класс `LibraryItem` (где уже лежит `property` из Шага 2)
добавь:

- `__init__(self, title: str) -> None`: присваивает `self.title = title`
  (сработает через property из шага 2 — так значение сразу
  провалидируется) и `self.status = ItemStatus.AVAILABLE`.
- Абстрактный метод: декоратор `@abstractmethod` над
  `def borrow_period_days(self) -> int: ...` —
  без реализации, тела нет, только `...` — у каждого типа предмета
  свой срок выдачи, поэтому базовый класс не может решить сам.
- Обычный метод (БЕЗ `@abstractmethod`) `def borrow(self) -> None`,
  который делает `self.status = ItemStatus.BORROWED`. Он не
  абстрактный, потому что "взять в аренду" работает ОДИНАКОВО для
  любого предмета — менять статус, а не считать срок.
- `def __repr__(self) -> str`, например:
  `return f"{type(self).__name__}({self.title!r}, {self.status})"`.

Итого в теле `LibraryItem` к концу Шага 3 должно быть: `title`
(геттер + сеттер), `__init__`, `borrow_period_days` (абстрактный),
`borrow`, `__repr__` — пять элементов в одном классе.

**Шаг 4. Два наследника**

- `class Book(LibraryItem):` — в теле ТОЛЬКО один метод:
  `def borrow_period_days(self) -> int:` (обычный `def`, БЕЗ
  декоратора `@abstractmethod` — здесь ты даёшь реализацию, а не
  объявляешь абстракцию заново), тело — `return 21`. Это и есть
  переопределение абстрактного метода из Шага 3.
- `class DVD(LibraryItem):` — аналогично, в теле только
  `def borrow_period_days(self) -> int:`, тело — `return 7`.

Обрати внимание: ни `Book`, ни `DVD` НЕ пишут свой `__init__` — им
подходит `__init__` родителя (`LibraryItem`) без изменений, наследуют
его напрямую.

**Шаг 5. `Member` — dataclass с композицией**

```python
@dataclass
class Member:
    name: str
    borrowed_items: list[LibraryItem] = field(
        default_factory=list[LibraryItem]
    )
```

(Синтаксис `field(default_factory=list[LibraryItem])` — та самая
ловушка mutable default из вопроса 5, только на уровне dataclass;
голый `field(default_factory=list)` без `[LibraryItem]` заставит
`pyright --strict` вывести `list[Unknown]`.)

Добавь в `Member` метод:

```python
def borrow(self, item: LibraryItem) -> None:
    item.borrow()
    self.borrowed_items.append(item)
```

`Member` **имеет** список `LibraryItem` — это и есть композиция
(в отличие от наследования в шаге 4).

**Шаг 6. Демонстрация — напиши после всех классов**

1. Создай `book = Book("...")`, `dvd = DVD("...")`, `member = Member("...")`.
2. Вызови `member.borrow(book)` и `member.borrow(dvd)`.
3. Циклом `for item in member.borrowed_items:` напечатай
   `print(item, item.borrow_period_days())` для каждого — это и есть
   полиморфизм: цикл не знает заранее, `Book` перед ним или `DVD`.
4. Оберни в `try/except`:
   `try:` на отдельной строке `LibraryItem("x")`,
   `except TypeError as e:` на отдельной строке `print(e)`.
   Сработает `TypeError`, потому что `LibraryItem` — абстрактный
   класс (Шаг 3), его нельзя создать напрямую.
5. Аналогично оберни в `try/except`:
   `try:` на отдельной строке `Book("")`,
   `except ValueError as e:` на отдельной строке `print(e)`.
   Сработает `ValueError` из сеттера `title` (Шаг 2), потому что
   передана пустая строка.

**Требования:**

- ✅ `Enum` (`ItemStatus`)
- ✅ Абстракция: `abc.ABC` + `@abstractmethod` (`LibraryItem.borrow_period_days`)
- ✅ Инкапсуляция: `title` через `@property` с валидацией
- ✅ Наследование: `Book`/`DVD` наследуют `LibraryItem`, переиспользуя
  его `__init__` без изменений
- ✅ Композиция: `Member` содержит список `LibraryItem`
- ✅ `dataclasses`: `Member` (с `field(default_factory=list[LibraryItem])`,
  не mutable default напрямую)
- ✅ Полиморфизм: цикл по `list[LibraryItem]`
- ✅ Dunder-метод: `__repr__`
- ✅ Аннотации типов, где Pylance strict их требует
- ✅ `pyright --strict`: 0 errors

**Твой код:**

```python
from enum import Enum

# YOUR CODE HERE

class ItemStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"

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
