# ✅ ASSESSMENT: Block 2.4 — Модули, файлы и дата/время

**Дата:** 2026-08-19
**Уровень:** Junior (Блок 2.4)
**Темы:** Модули и пакеты (`import`, `from`, `as`, `__name__`,
`sys.path`), продвинутая работа с файлами (`pathlib`, CSV, JSON,
бинарные файлы), `datetime`/`date`/`time`/`timedelta`, форматирование
и часовые пояса
**Критерий прохода:** ≥80% (микровопросы + практика)

---

## ЧАСТЬ 1: Микровопросы (8 вопросов) — ОТВЕЧЕНО, 8/8 (100%)

### Вопрос 1: Кэширование импорта

```python
# module_a.py
print("module_a загружается")
VALUE = 42
```

```python
# main.py
import module_a
import module_a
import module_a

print(module_a.VALUE)
```

**Твой ответ:** Напечатается один раз, так как после запуска модуль
закэшируется.

---

### Вопрос 2: `import ... as` vs `from ... import`

```python
# utils.py
def greet():
    return "привет"
```

```python
import utils as u
from utils import greet

def greet():
    return "переопределено"

print(u.greet())
print(greet())
```

**Твой ответ:** Выведет "привет", "переопределено".
`import ... as` даёт доступ через модуль (пространство имён модуля
неприкосновенно), а `from ... import` копирует имя в текущий scope, и
оно ведёт себя как обычная локальная переменная — его можно
перезаписать.

---

### Вопрос 3: `__name__`

```python
# helper.py
def main():
    print(f"__name__ внутри helper.py = {__name__}")

if __name__ == "__main__":
    main()
```

**Твой ответ:** При запуске напрямую (`python helper.py`):
`__name__ внутри helper.py = __main__`. Когда файл запускается
напрямую, интерпретатор присваивает его модулю `__name__ = "__main__"`.
Условие `if __name__ == "__main__"` истинно → `main()` вызывается →
печатается строка.

При импорте (`import helper`) без ручного вызова `helper.main()`:
ничего не напечатается. При импорте `__name__` модуля равен его имени
файла — `"helper"`, а не `"__main__"`. Условие ложно, поэтому `main()`
не вызывается автоматически, функция просто определяется, но не
выполняется.

---

### Вопрос 4: `pathlib.Path`

```python
from pathlib import Path

p = Path("data") / "reports" / "2026.csv"
print(p.name)
print(p.suffix)
print(p.parent)
```

**Твой ответ:**
`p.name` — последний компонент пути (имя файла с расширением) →
`2026.csv`
`p.suffix` — расширение файла (с точкой) → `.csv`
`p.parent` — путь без последнего компонента, т.е. директория, в
которой лежит файл → `data/reports` (на Windows выведется как
`data\reports`, но при печати через `print` pathlib сам подставляет
разделитель нужной ОС)

---

### Вопрос 5: CSV — типы значений

```python
import csv
from io import StringIO

data = StringIO("name,age\nAnn,25\nBob,30\n")
reader = csv.DictReader(data)
rows = list(reader)

print(rows[0]["age"])
print(rows[0]["age"] + 5)
```

**Твой ответ:** Второй `print()` вызовет
`TypeError: can only concatenate str (not "int") to str` —
`csv.DictReader` всегда читает значения как строки, даже `"25"`,
поэтому `"25" + 5` нельзя выполнить без явного `int()`.

---

### Вопрос 6: JSON и несериализуемые типы

```python
import json
from datetime import date

data = {"name": "Ann", "signup_date": date(2026, 1, 1)}
json.dumps(data)
```

**Твой ответ:** Будет
`TypeError: Object of type date is not JSON serializable` — модуль
`json` умеет сериализовывать только базовые типы (`str`, `int`,
`float`, `bool`, `None`, `list`, `dict`), а `date` в этот список не
входит; нужно передать `default=str` или сконвертировать дату в
строку заранее (например, `.isoformat()`).

---

### Вопрос 7: `timedelta` и арифметика дат

```python
from datetime import date, timedelta

start = date(2026, 1, 30)
result = start + timedelta(days=5)
print(result)
```

**Твой ответ:** `2026-02-04` — `timedelta` работает с абсолютным
количеством дней, а не с "календарными" месяцами, поэтому переход
через границу месяца обрабатывается автоматически корректно.

---

### Вопрос 8: naive vs aware datetime

```python
from datetime import datetime

dt = datetime(2026, 8, 19, 12, 0)
print(dt.tzinfo)
```

**Твой ответ:** `print()` выведет `None`. "Naive" datetime — это
объект без информации о часовом поясе (атрибут `tzinfo` не задан), в
отличие от "aware" datetime, где `tzinfo` указывает конкретную зону.
Это важно, потому что naive-объекты нельзя корректно сравнивать/
вычитать с aware-объектами (будет `TypeError`), а при работе с
разными часовыми поясами (API, логи серверов, разные пользователи)
необходимо явно знать, к какой зоне относится время — иначе легко
получить ошибку на несколько часов.

---

## ЧАСТЬ 2: Практическая задача — «Отчёт по дедлайнам»

Одна программа, использующая всё из блока 2.4: свой модуль, pathlib,
csv, json, datetime. Делай по шагам, не забегая вперёд.

**Шаг 1. Свой модуль `date_utils.py`** (создай рядом с этим файлом, в
той же папке `assessments/`)

Функция `days_until(deadline: date, today: date) -> int`, которая
возвращает `(deadline - today).days`. Ничего больше в файле не нужно.

**Шаг 2. Исходные данные — CSV**

В коде ниже (не отдельный файл) создай `csv_text` — обычную
многострочную строку с содержимым:

```
name,deadline
Сдать отчёт,2026-09-01
Ревью PR,2026-08-20
Подготовить презентацию,2026-10-15
```

Прочитай её через `csv.DictReader(io.StringIO(csv_text))` (импортируй
`io`), собери `rows = list(reader)`.

**Шаг 3. Парсинг дат и вычисление дней**

Зафиксируй `today = date(2026, 8, 19)` (не `date.today()` — нужен
воспроизводимый результат). Для каждой строки из `rows`:

- распарси `row["deadline"]` в `date` через `date.fromisoformat(...)`
- вызови импортированную `days_until(deadline, today)` из своего
  модуля (Шаг 1)
- собери словарь
  `{"name": row["name"], "deadline": row["deadline"], "days_left": <результат>}`

Собери все словари в список `report`.

**Шаг 4. Сортировка**

Отсортируй `report` по `"days_left"` по возрастанию
(`sorted(report, key=lambda item: item["days_left"])`).

**Шаг 5. Запись в JSON через pathlib**

Через `Path(__file__).parent / "deadlines_report.json"` получи путь.
Через
`.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")`
запиши отсортированный список в файл.

**Шаг 6. Чтение обратно и вывод**

Прочитай тот же файл через `.read_text(encoding="utf-8")`, преобрази
обратно через `json.loads(...)`, циклом напечатай для каждой задачи:
`f"{item['name']}: {item['days_left']} дней"`.

**Требования:**

- ✅ Свой модуль импортирован и используется (`date_utils.days_until`)
- ✅ `csv.DictReader` для чтения
- ✅ `date.fromisoformat` для парсинга
- ✅ `pathlib.Path` для пути, `write_text`/`read_text`
- ✅ `json.dumps`/`json.loads`
- ✅ Сортировка по `days_left`
- ✅ `pyright --strict`: 0 errors

**Решение (проверено в scratchpad — `pyright --strict` 0 errors,
`ruff` 79 символов/строку чисто, рантайм exit 0; вывод отсортирован
верно: Ревью PR — 1 день, Сдать отчёт — 13 дней, Подготовить
презентацию — 57 дней; `date_utils.py` с функцией `days_until`
проверен так же):**

```python
import csv
import io
import json
from datetime import date
from pathlib import Path

from date_utils import days_until

# YOUR CODE HERE

csv_text = """name,deadline
Сдать отчёт,2026-09-01
Ревью PR,2026-08-20
Подготовить презентацию,2026-10-15
"""

reader = csv.DictReader(io.StringIO(csv_text))
rows = list(reader)

today = date(2026, 8, 19)

report: list[dict[str, str | int]] = []
for row in rows:
    deadline = date.fromisoformat(row["deadline"])
    days_left = days_until(deadline, today)
    report.append(
        {
            "name": row["name"],
            "deadline": row["deadline"],
            "days_left": days_left,
        }
    )

report = sorted(report, key=lambda item: item["days_left"])

path = Path(__file__).parent / "deadlines_report.json"
path.write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
)

data = json.loads(path.read_text(encoding="utf-8"))
for item in data:
    print(f"{item['name']}: {item['days_left']} дней")
```

---

## Критерии оценки

### Микровопросы (8 вопросов)

- **Правильные:** 1 балл каждый
- **Результат:** 8/8 (100%)

### Практическая задача

- **Работает программа:** 3/3 балла
- **Использует все требования (свой модуль, csv, pathlib, json,
  datetime, сортировка):** 3/3 балла
- **Форматирование, читаемость, типизация (`pyright --strict`:
  0 errors):** 1/1 балл — с первой версией была одна строка длиннее
  79 символов (PEP8), исправлено
- **Итог:** 7/7 (100%)

### ФИНАЛЬНЫЙ РЕЗУЛЬТАТ

```
Микровопросы: 8/8 (100%) × 50% вклад = 50%
Практика:     7/7 (100%) × 50% вклад = 50%
Итог: 100%
Проход: ≥80% — ПРОЙДЕНО
```
