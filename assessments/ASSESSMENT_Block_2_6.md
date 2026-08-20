# ASSESSMENT: Block 2.6 — Типизация и качество кода

**Дата:** 2026-08-19
**Уровень:** Junior (Блок 2.6)
**Темы:** Аннотации типов (generic-коллекции, `Optional`/`X | None`,
`Union`/`X | Y`), модуль `typing` (`Any`, `Callable`, `Iterable`/
`Sequence`, `TypedDict`) — полная практика; проверка типов (mypy/
pyright), PEP 8/`ruff`/`black`, `venv`/`pip` — ознакомительно
**Критерий прохода:** ≥80% (микровопросы + практика)

---

## ЧАСТЬ 1: Микровопросы (8 вопросов)

**Инструкция:** Отвечай письменно прямо в этом файле, под каждым
вопросом, в поле "Твой ответ". Вопросы 1-7 — по темам с полной
практикой (аннотации, `typing`), вопрос 8 — концептуальный, по
ознакомительным темам (mypy/pyright), без кода.

### Вопрос 1: Аннотации не проверяются в рантайме

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

result = total(["a", "b", "c"])
```

Упадёт ли этот код при выполнении, и если да — то на какой строке и
с какой ошибкой? Объясни, почему аннотация `list[int]` не помешала
передать список строк.

**Твой ответ:**

## Упадёт, но не сразу и не из-за аннотаций — на строке sum(numbers) внутри total, с TypeError: unsupported operand type(s) for +: 'int' and 'str' (sum стартует с 0 и пытается прибавить "a")

### Вопрос 2: `Optional[X]` vs `X | None`

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Ann"
    return None

name = find_user(2)
print(name.upper())
```

Что здесь не так с точки зрения типизации (что покажет
`pyright --strict`), и что произойдёт при реальном запуске?

**Твой ответ:**

## pyright --strict покажет ошибку на строке print(name.upper()): что-то вроде "upper" is not a known attribute of "None" (reportOptionalMemberAccess / reportAttributeAccessIssue). Тип name — str | None, а метод .upper() вызывается без проверки на None, так что pyright не может гарантировать, что вызов безопасен для всех возможных значений.

### Вопрос 3: `Union`/`|` — несколько разрешённых типов

```python
def describe(value: int | str) -> str:
    return value.upper()
```

Что скажет `pyright --strict` про эту функцию, и почему?

**Твой ответ:**

## pyright в strict-режиме выдаст ошибку на value.upper(): примерно "upper" is not a known attribute of "int" (reportAttributeAccessIssue). Тип value — int | str, и pyright проверяет, что вызываемый метод существует у обоих членов union'а, а не хотя бы у одного. upper() есть у str, но у int такого метода нет — поэтому для случая, когда вызовут describe(5), тип-чекер не может гарантировать корректность.

### Вопрос 4: `Any` — полное отключение проверки

```python
def process(data: Any) -> int:
    return data + 1

process("hello")
```

Пропустит ли `pyright --strict` эту функцию без ошибок? А что
произойдёт при вызове `process("hello")` в рантайме? В чём разница
между `Any` и, скажем, `object` в этом смысле?

**Твой ответ:**

Да, pyright --strict пропустит это без ошибок (кроме, может, reportMissingTypeStubs/отсутствия импорта Any, если забыл from typing import Any, но это не про саму логику). Any — это «люк», который отключает проверку типов: pyright считает, что с значением типа Any можно делать вообще что угодно — вызывать любые методы, любые операторы — и не ругается, даже если реальная операция бессмысленна.

## При запуске process("hello"): return data + 1 попытается выполнить "hello" + 1, и упадёт с TypeError: can only concatenate str (not "int") to str.

Ключевое отличие в одном предложении: Any совместим с любым типом в обе стороны (можно присвоить Any куда угодно, и что угодно — в Any), а object — это обычный тип в иерархии типов, просто самый общий из них, и для него действуют обычные правила совместимости — только в одну сторону.

## Проверено (2026-08-19): если бы `data: object`, `pyright --strict` пометил бы `return data + 1` ошибкой (`reportOperatorIssue` — у `object` нет `__add__`, принимающего `int`) — в отличие от `Any`, где проверка полностью отключена и такая же строка проходит без единой ошибки. Ответ засчитан, часть 1 закрыта: **8/8 (100%)**.

### Вопрос 5: `Callable` — аннотация сигнатуры функции

```python
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def concat(a: str, b: str) -> str:
    return a + b

apply(concat, 1, 2)
```

Что покажет `pyright --strict` на вызове `apply(concat, 1, 2)`, и
почему?

**Твой ответ:**

pyright покажет ошибку на аргументе concat в вызове apply(concat, 1, 2) — что-то вроде Argument of type "(a: str, b: str) -> str" cannot be assigned to parameter "func" of type "(int, int) -> int" (reportArgumentType).

## Причина: func аннотирован как Callable[[int, int], int] — функция, принимающая два int и возвращающая int. А concat имеет сигнатуру (str, str) -> str. Типы параметров и возврата не совпадают, так что concat не подходит под ожидаемый Callable-контракт: даже если бы это прошло проверку, реальный вызов func(a, b) внутри apply передал бы concat числа 1, 2 вместо строк.

### Вопрос 6: `Iterable` vs `Sequence` vs `list` — выбор типа параметра

Почему для ПАРАМЕТРА функции часто предпочтительнее написать
`Iterable[int]`, а не `list[int]`, даже если внутри функции просто
перебирают элементы в цикле `for`? Какую практическую возможность
теряет вызывающий код, если параметр жёстко типизирован как
`list[int]`?

**Твой ответ:**

Принцип: для параметров бери максимально общий тип, который покрывает реальные потребности функции (это следствие принципа "be liberal in what you accept" / связано с Liskov substitution — чем шире принимаемый тип, тем гибче API).

Если функции нужно только перебрать элементы в for, ей достаточно Iterable[int] — самого широкого протокола, требующего лишь наличие **iter**. А list[int] — это конкретный, узкий тип.

Что теряет вызывающий код при жёстком list[int]: он не может передать любой другой итерируемый объект без явного оборачивания в list(...). Например:

генератор ((x for x in range(10)))
range(10)
кортеж, множество, dict.keys()
результат другой ленивой функции (генератор-функция с yield)
бесконечный или очень большой поток данных, который жёстко не хочется материализовывать в список целиком (лишний расход памяти и времени)

---

### Вопрос 7: `TypedDict`

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def greet(user: User) -> str:
    return f"Привет, {user['name']}"

greet({"name": "Ann"})
```

Что скажет `pyright --strict` про вызов `greet({"name": "Ann"})`?
Чем `TypedDict` в этом смысле отличается от обычного
`dict[str, str | int]`?

**Твой ответ:**

pyright выдаст ошибку на аргументе {"name": "Ann"} в вызове greet(...) — что-то вроде Argument missing key "age" / Expected type "User" (reportArgumentType, конкретно про недостающий обязательный ключ). TypedDict User требует оба ключа — name: str и age: int — а передан словарь только с name, без age.

Отличие TypedDict от dict[str, str | int]:

TypedDict описывает точную структуру — конкретный набор ключей и тип значения для каждого ключа отдельно. pyright проверяет: все ли обязательные ключи присутствуют, нет ли лишних (незнакомых) ключей, и правильный ли тип у значения именно под этим конкретным ключом (name обязан быть str, age обязан быть int, перепутать нельзя).
dict[str, str | int] — это просто «словарь с произвольными строковыми ключами, где значение — либо str, либо int». pyright тут вообще не знает, какие ключи должны быть и в каком количестве. {"name": "Ann"}, {}, {"age": 5, "foo": "bar", "bar": 10} — всё это пройдёт проверку одинаково успешно, потому что типово это валидный dict[str, str | int]. Также при обращении user["name"] pyright не сможет сказать, что тип результата — именно str (он выведет str | int, объединение всех возможных типов значений), тогда как для TypedDict user["name"] даёт точный тип str.

---

### Вопрос 8: mypy vs pyright — ловушка strict-режима (концептуально, без кода)

В сеансе 10 этого курса была найдена реальная проблема: без файла
`pyrightconfig.json` в корне репозитория команда `npx pyright` тихо
проверяла код в режиме `basic`, а не `strict`, показывая ложное
"0 errors" — хотя на самом деле в `strict`-режиме там были ошибки.
Объясни своими словами: почему это произошло, и как теперь в этом
репозитории гарантированно проверять именно `strict`-режим?

**Твой ответ:**

## Почему так вышло: у pyright есть несколько уровней строгости (off, basic, standard, strict), и по умолчанию, если нигде явно не указано иное, он берёт basic/standard, а не strict. strict — это не поведение "по умолчанию", а режим, который надо запросить явно: либо флагом --strict в командной строке, либо полем "typeCheckingMode": "strict" в конфиге (pyrightconfig.json или секция [tool.pyright] в pyproject.toml). Если этого нет — pyright молча откатывается на менее строгий режим, при этом никак не предупреждая, что запрошенный уровень отличается от фактически применённого. Отсюда и ловушка: команда видела "0 errors" и считала, что код чист под strict, хотя на самом деле проверялся более мягкий режим, который часть тех же ошибок (например, неявные Any, отсутствие аннотаций возврата, доступ к Optional без сужения) просто не ловит.

## ЧАСТЬ 2: Практическая задача — «Каталог товаров»

Одна программа, использующая типизацию из блока 2.6: параметризованные
generic-коллекции, `Optional`/`X | None`, `Callable`, `Iterable`/
`Sequence`, `TypedDict`. `Any` использовать НЕ нужно — он отключает
проверку, а задача как раз про то, чтобы pyright реально всё
проверил. Делай по шагам, не забегая вперёд.

**Шаг 1. `TypedDict` для товара**

```python
class Product(TypedDict):
    name: str
    price: float
    in_stock: bool
```

**Шаг 2. `total_price(products: Iterable[Product]) -> float`**

Суммирует `price` только у товаров с `in_stock=True`. Параметр —
именно `Iterable[Product]`, не `list[Product]` (см. вопрос 6).

**Шаг 3. `find_product(products: Sequence[Product], name: str) -> Product | None`**

Возвращает первый товар с совпадающим `name`, либо `None`, если не
найден. Параметр — `Sequence[Product]` (нужен доступ по индексу или
хотя бы предсказуемый повторный проход — `Iterable` здесь не
подошёл бы, если реализация использует что-то кроме одного `for`;
если у тебя реализация — простой `for` без индексов, `Iterable`
тоже допустим, обоснуй свой выбор в комментарии).

**Шаг 4. `apply_discount(products: list[Product], discount_func: Callable[[float], float]) -> list[Product]`**

Возвращает НОВЫЙ список товаров, где `price` каждого пересчитан через
`discount_func(product["price"])`, остальные поля — без изменений.

**Шаг 5. Демонстрация**

1. Создай `catalog: list[Product]` из 3-4 товаров (литералами словарей,
   часть `in_stock=True`, часть `False`).
2. Вызови `total_price(catalog)`, напечатай результат.
3. Вызови `find_product(catalog, "...")` дважды — с существующим и
   несуществующим именем. Для каждого результата — проверка на `None`
   ПЕРЕД использованием (`if result is not None:` или аналог), иначе
   pyright справедливо укажет на потенциальный `None`.
4. Определи функцию `def apply_10_percent_off(price: float) -> float:`
   (возвращает `price * 0.9`), передай её в `apply_discount`, напечатай
   новый список.

**Требования:**

- ✅ `TypedDict` (`Product`)
- ✅ `Iterable`/`Sequence` для параметров-коллекций (не голый `list`,
  если функции достаточно просто перебора/последовательного доступа)
- ✅ `X | None` для функции, которая может не найти результат
- ✅ Безопасная обработка `None` ПЕРЕД использованием результата
- ✅ `Callable[[float], float]` для функции-трансформации
- ✅ Без `Any` нигде
- ✅ `pyright --strict`: 0 errors

**Твой код:**

```python
from typing import Callable, Iterable, Sequence, TypedDict

# ТВОЙ КОД ЗДЕСЬ

class Product(TypedDict):
    name: str
    price: float
    in_stock: bool

def total_price(products: Iterable[Product]) -> float:
    total_price: float = 0

    for product in products:
        if product["in_stock"]:
            total_price += product["price"]

    return total_price

def find_product(products: Sequence[Product], name: str) -> Product | None:
    for product in products:
        if name == product["name"]:
            return product
    return None


```

---

## Критерии оценки

### Микровопросы (8 вопросов)

- **Правильные:** 1 балл каждый
- **Проходной балл:** 6-8 правильных (75-100%)

### Практическая задача

- **Работает программа:** 3 балла
- **Использует все требования (`TypedDict`, `Iterable`/`Sequence`,
  `Optional`, безопасная обработка `None`, `Callable`, без `Any`):**
  3 балла
- **Форматирование, читаемость, типизация (`pyright --strict`:
  0 errors):** 1 балл
- **Проходной балл:** 6+ баллов из 7

### ФИНАЛЬНЫЙ РЕЗУЛЬТАТ (заполняется после проверки)

```
Микровопросы: ?/8 × 50% вклад = ?
Практика:     ?/7 × 50% вклад = ?
Итог: ?
Проход: ≥80%?
```
