# ✅ ASSESSMENT: Block 2.3 — Функции

**Дата:** 2026-07-24
**Уровень:** Junior (Блок 2.3)
**Темы:** Основы функций, `*args`/`**kwargs`, LEGB (замыкания), функции как объекты первого класса
**Критерий прохода:** ≥80% (микровопросы + практика)

---

## ЧАСТЬ 1: Микровопросы (8 вопросов)

**Инструкция:** Ответь на вопросы письменно (что выведет код и почему). Правильные ответы — в конце.

### Вопрос 1: Ловушка mutable default

```python
def append_to(value, target=[]):
    target.append(value)
    return target

a = append_to(1)
b = append_to(2)
print(a)
print(b)
print(a is b)
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***

<!-- Изменяемый список по умолчанию (target=[]) создаётся один раз при определении функции и переиспользуется между вызовами без явного аргумента. append_to(1) добавляет 1 в этот единственный список, append_to(2) добавляет 2 в тот же объект — поэтому a и b указывают на один и тот же изменившийся список. -->

[1, 2]
[1, 2]
True

---

### Вопрос 2: `*args` и `**kwargs`

```python
def report(*args, **kwargs):
    print(len(args))
    print(kwargs.get("status", "нет статуса"))

report(1, 2, 3, status="ok", user="Anna")
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***

<!-- args = (1, 2, 3) → длина 3; kwargs = {"status": "ok", "user": "Anna"}. -->

3
ok

---

### Вопрос 3: LEGB — `global` vs локальная переменная

```python
counter = 0

def increment():
    counter += 1
    return counter

increment()
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***

<!-- UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value

Присваивание counter += 1 делает counter локальной переменной для всей функции (включая строки до присваивания), поэтому чтение до присваивания падает без global counter. -->

---

### Вопрос 4: Замыкания — `nonlocal`

```python
def make_counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc

c1 = make_counter()
c2 = make_counter()

print(c1())
print(c1())
print(c2())
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***
1
2
1

## c1 и c2 — независимые замыкания со своей count; nonlocal меняет именно ту count, что принадлежит конкретному вызову make_counter().

### Вопрос 5: Функция как объект — присваивание vs вызов

```python
def cube(x):
    return x ** 3

my_cube = cube
print(my_cube(3))
print(my_cube is cube)
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***
my_cube = cube — просто второе имя той же функции, не вызов.
27
True

---

### Вопрос 6: Dispatch table

```python
operations = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
}

def calculate(op, a, b):
    return operations[op](a, b)

print(calculate("add", 5, 3))
print(calculate("sub", 5, 3))
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***
8
2

---

### Вопрос 7: Ссылка на функцию vs немедленный вызов (классическая ловушка)

```python
def add_tax(price, rate):
    return price * (1 + rate)

prices = [100, 200]

result = list(map(add_tax(0.2), prices))
```

**Что произойдёт при выполнении этого кода и почему? Как исправить?**

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***
TypeError: add_tax() missing 1 required positional argument: 'rate'

## add_tax(0.2) вызывается немедленно при построении аргумента для map — до начала перебора prices. 0.2 интерпретируется как price, а rate не передан. Исправление: map(lambda price: add_tax(price, 0.2), prices).

### Вопрос 8: `sorted(key=...)` и `filter`/`map` в цепочке

```python
words = ["python", "is", "fun", "a", "lot"]

result = sorted(
    filter(lambda w: len(w) > 1, words),
    key=len,
)
print(result)
```

**Твой ответ:** **\*\*\*\***\_\_\_\_**\*\*\*\***
['is', 'fun', 'lot', 'python']

## filter убирает "a" (длина 1). Оставшиеся сортируются по длине: is(2), fun/lot(3), python(6). Сортировка стабильна — fun и lot сохраняют исходный порядок.

## ЧАСТЬ 2: Практическая задача (комплексная)

### Задача: Гибкий калькулятор статистики с журналом вызовов

Напиши программу, которая:

1. Функция `make_logger()` возвращает функцию `log(message)`, которая
   при каждом вызове добавляет `message` во внутренний список
   (через замыкание, `nonlocal`) и возвращает **копию** списка всех
   сообщений на данный момент
2. Функция `stats(*numbers, **options)` принимает произвольное
   количество чисел и именованные опции:
   - всегда возвращает `dict` с ключами `count`, `sum`, `min`, `max`
   - если передан `options["round_to"]` (int) — округляет `sum`
     до этого числа знаков (`round()`), иначе не округляет
   - если чисел нет (`len(numbers) == 0`) — вернуть
     `{"count": 0, "sum": 0, "min": None, "max": None}` (guard clause,
     без деления и без падения на `min()`/`max()` от пустой
     последовательности)
3. Функция `run_operation(op, a, b)` использует **dispatch table**
   (словарь операций `{"add": ..., "mul": ...}` с лямбдами) — не
   `if/elif`
4. Продемонстрируй: вызови `log()` 2-3 раза, вызови `stats()` с
   разными аргументами (включая пустой вызов и вызов с `round_to`),
   вызови `run_operation` для обеих операций

**Требования:**

- ✅ Замыкание с `nonlocal` (`make_logger`)
- ✅ `*args` и `**kwargs` в одной функции (`stats`)
- ✅ Guard clause для пустого случая (без падения)
- ✅ Dispatch table (словарь функций/лямбд), не `if/elif`
- ✅ Аннотации типов, где Pylance strict их требует

**Твой код:**

```python
# YOUR CODE HERE

from typing import Callable, Optional, Union

def make_logger() -> Callable[[str], list[str]]:
    messages: list[str] = []

    def log(message: str) -> list[str]:
        nonlocal messages
        messages.append(message)
        return messages.copy()

    return log


def stats(*numbers: float, **options: int) -> dict[str, Optional[Union[int, float]]]:
    if len(numbers) == 0:
        return {"count": 0, "sum": 0, "min": None, "max": None}

    total: Union[int, float] = sum(numbers)
    round_to = options.get("round_to")
    if round_to is not None:
        total = round(total, round_to)

    return {
        "count": len(numbers),
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
    }


def run_operation(op: str, a: float, b: float) -> float:
    operations: dict[str, Callable[[float, float], float]] = {
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
    }
    return operations[op](a, b)


if __name__ == "__main__":
    log = make_logger()
    print(log("first"))
    print(log("second"))
    print(log("third"))

    print(stats())
    print(stats(1, 2, 3))
    print(stats(1.5, 2.7, 3.1, round_to=1))

    print(run_operation("add", 5, 3))
    print(run_operation("mul", 5, 3))

```

---

## Правильные ответы

### Микровопросы

**Вопрос 1:**

```
a = [1, 2]
b = [1, 2]
a is b → True
```

Изменяемый список по умолчанию создаётся ОДИН раз при определении
функции и переиспользуется между всеми вызовами без явного аргумента —
классическая ловушка Python.

**Вопрос 2:**

```
3
ok
```

`args = (1, 2, 3)` → `len(args) == 3`; `kwargs = {"status": "ok", "user": "Anna"}`.

**Вопрос 3:**

```
UnboundLocalError: cannot access local variable 'counter' where it is
not associated with a value
```

Присваивание `counter += 1` внутри функции делает `counter` ЛОКАЛЬНОЙ
переменной для всей функции (включая строки до присваивания) — без
`global counter` чтение до присваивания падает.

**Вопрос 4:**

```
1
2
1
```

`c1` и `c2` — независимые замыкания с собственной `count`; `nonlocal`
изменяет именно ту `count`, что в области видимости конкретного
вызова `make_counter()`.

**Вопрос 5:**

```
27
True
```

`my_cube = cube` — второе имя той же функции, не вызов.

**Вопрос 6:**

```
8
2
```

**Вопрос 7:**

```
TypeError: add_tax() missing 1 required positional argument: 'rate'
```

`add_tax(0.2)` вызывается СРАЗУ при построении аргумента для `map`,
до начала перебора `prices`, и падает — там передан только `0.2`
(интерпретируется как `price`), `rate` не хватает. Исправление:
`map(lambda price: add_tax(price, 0.2), prices)`.

**Вопрос 8:**

```
['is', 'fun', 'lot', 'python']
```

`filter` убирает `"a"` (`len("a") > 1` ложно). Оставшиеся
`["python", "is", "fun", "lot"]` сортируются по длине
(`is`=2, `fun`=`lot`=3, `python`=6); `fun` и `lot` одной длины —
сортировка стабильна, порядок между ними сохраняется как в исходном
списке.

---

## Критерии оценки

### Микровопросы (8 вопросов)

- **Правильные:** 1 балл каждый
- **Проходной балл:** 6–8 правильных (75–100%)

### Практическая задача

- **Работает программа:** 3 балла
- **Использует все требования (замыкание/nonlocal, args+kwargs, guard clause, dispatch table):** 2 балла
- **Форматирование, читаемость, типизация:** 1 балл
- **Проходной балл:** 5+ баллов из 6

### ФИНАЛЬНЫЙ РЕЗУЛЬТАТ

```
Микровопросы: X/8 (Y%) × 50% вклад
Практика:     X/6 (Y%) × 50% вклад
Проход: ≥80%
```

---

## 📊 ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ (2026-07-24)

### Микровопросы: 8/8 ✅ (100%)
- Вопрос 1 (mutable default): ✅
- Вопрос 2 (`*args`/`**kwargs`): ✅
- Вопрос 3 (LEGB, `UnboundLocalError`): ✅
- Вопрос 4 (замыкания, `nonlocal`): ✅
- Вопрос 5 (функция как объект): ✅
- Вопрос 6 (dispatch table): ✅
- Вопрос 7 (вызов вместо ссылки): ✅
- Вопрос 8 (`sorted(key=)` + `filter`): ✅

**Баллы за микровопросы:** 8 × 1 = 8 баллов (из 8)

### Практическая задача: 6/6 ✅
- **Работает программа:** 3/3 — рантайм проверен, вывод верный
  (журнал накапливается через замыкание; `stats()` верно обрабатывает
  пустой вызов, обычный вызов и `round_to`; `run_operation` возвращает
  верные результаты для `add`/`mul`)
- **Использует все требования:** 2/2 — замыкание с `nonlocal`
  (`make_logger`), `*args`+`**kwargs` в одной функции (`stats`),
  guard clause для пустого случая, dispatch table (словарь лямбд) в
  `run_operation`
- **Форматирование, читаемость, типизация:** 1/1 — `pyright --strict`:
  0 errors с первой попытки, правок не потребовалось

**Баллы за практику:** 6/6 баллов

### 🎯 ИТОГОВЫЙ РЕЗУЛЬТАТ

```
Микровопросы: 8/8 (100%) × 50% вклад = 50%
Практика:     6/6 (100%) × 50% вклад = 50%
────────────────────────────────
ИТОГО:        100%

✅ СТАТУС: БЛОК 2.3 ПРОЙДЕН
```

---

## Инструкция по прохождению

1. **Ответь на микровопросы** (запиши ответы в этот файл или устно)
2. **Напиши код для практической задачи**
3. **Протестируй свой код**
4. **Покажи результаты** для проверки
