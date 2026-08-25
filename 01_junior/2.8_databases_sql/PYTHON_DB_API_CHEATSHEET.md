# 🐍 Python DB API шпаргалка — sqlite3 vs psycopg

По аналогии с `SQL_CHEATSHEET.md`: каждый объект/метод — с якорем на то,
что ты уже знаешь, и с явным сравнением `sqlite3` ↔ `psycopg`. Оба модуля
следуют одному стандарту — **PEP 249, Python Database API** — поэтому
API почти идентичен. Источники: `01_sql_basics_demo.py`,
`03_dml_transactions_demo.py` (sqlite3), `06_psycopg_practice.py`
(psycopg).

---

## Подключение — `connect()`

Открывает соединение с базой и возвращает объект `Connection`.

```python
import sqlite3
connection = sqlite3.connect(":memory:")          # БД в оперативной памяти

import psycopg
connection = psycopg.connect(                      # БД на настоящем сервере
    host="localhost", port=5432,
    dbname="learning", user="learning", password="learning",
)
```

**Мнемоника:** `connect()` = `open()` для файла, только вместо файла —
база данных. `sqlite3` открывает "файл" (или память), `psycopg` —
сетевое соединение с сервером PostgreSQL (поэтому у него параметры
`host`/`port`, как в любом сетевом клиенте).

**Ключевая разница:** `sqlite3.connect(":memory:")` создаёт пустую БД,
которая исчезает вместе с процессом. `psycopg.connect(...)` подключается
к **персистентной** БД — данные переживают перезапуск скрипта (грабли
`06_psycopg_practice.py`: `CREATE TABLE` падал на втором запуске, пока
не добавили `DROP TABLE IF EXISTS ... CASCADE`).

---

## `Connection` — объект соединения

| Метод/атрибут | Что делает | Есть в обоих? |
|---|---|---|
| `.cursor()` | получить курсор — им выполняются запросы | ✅ |
| `.commit()` | зафиксировать изменения | ✅ |
| `.rollback()` | откатить незафиксированные изменения | ✅ |
| `.close()` | закрыть соединение | ✅ |
| `.total_changes` | сколько строк изменено с момента открытия | только sqlite3 |
| `.autocommit` | режим "коммитить каждый execute сразу" | только psycopg (по умолчанию `False`) |

**Мнемоника:** `Connection` — это сам разговор с базой (как файловый
дескриптор), а `Cursor` — это "рука", которой ты в этом разговоре
что-то делаешь. Соединение можно держать одно, курсоров через него —
сколько угодно.

---

## `Cursor` — объект курсора

Получаешь через `connection.cursor()`. Все запросы идут через него.

| Метод | Что делает |
|---|---|
| `.execute(sql, params)` | выполнить один SQL-запрос |
| `.executemany(sql, rows)` | выполнить запрос для каждой строки из списка |
| `.fetchone()` | забрать ОДНУ строку результата (или `None`) |
| `.fetchmany(n)` | забрать `n` строк результата |
| `.fetchall()` | забрать ВСЕ строки результата — список кортежей |
| `.rowcount` | сколько строк затронул последний запрос |
| `.close()` | закрыть курсор (соединение остаётся открытым) |

Это в точности то, что ты уже использовал в обоих модулях — код
одинаковый:

```python
cursor.execute("SELECT name, salary FROM employees WHERE salary > 2800")
print(cursor.fetchall())
```

**Мнемоника:** `execute` готовит результат, `fetchall`/`fetchone` его
забирают — как генератор и `list(...)`/`next(...)`: запрос сам по себе
данные не возвращает, их нужно явно "вытащить".

---

## Плейсхолдеры — главная ловушка при переходе

Синтаксис параметров **разный** между модулями — это единственное
реальное различие в написании SQL-запросов из Python:

```python
# sqlite3 — знак вопроса (qmark)
cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))

# psycopg — %s (pyformat), даже без % - форматирования
cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
```

**Мнемоника:** `?` — это позиционная "дырка" как `{}` в `.format()` без
номера. `%s` в psycopg выглядит как `%`-форматирование Python
(`"%s" % x`), но это **не оно** — сам psycopg безопасно подставляет
значение и экранирует спецсимволы, поэтому это защита от SQL injection,
а не текстовая замена. **Никогда не делай** `f"...WHERE id = {author_id}"`
ни в одном из двух модулей — это и есть SQL injection.

---

## Транзакции — `commit()` / `rollback()`

Поведение одинаковое в обоих модулях: `INSERT`/`UPDATE`/`DELETE` не
сохраняются, пока не вызван `commit()`; `rollback()` отменяет всё, что
накопилось с последнего `commit()`.

```python
cursor.execute("UPDATE products SET quantity = 0")  # ещё не сохранено
connection.rollback()                                 # отменили
```

**Мнемоника:** commit = "сохранить файл" (Ctrl+S). До этого момента
изменения существуют только в текущей транзакции — как несохранённые
правки в редакторе.

---

## Ловушка: `with connection:` — разное поведение!

Это единственное поведенческое различие, которое реально может
сломать код при переносе с sqlite3 на psycopg.

```python
# sqlite3: with commit()/rollback() делает, но НЕ закрывает соединение
with sqlite3.connect(":memory:") as connection:
    ...
# ⚠️ connection всё ещё открыт — нужен connection.close() отдельно

# psycopg: with делает commit()/rollback() И закрывает соединение
with psycopg.connect(...) as connection:
    ...
# ✅ connection уже закрыт на выходе — close() не нужен
```

**Мнемоника:** в sqlite3 `with connection` страхует только транзакцию,
"свет" (`close()`) гасишь сам (см. `SQL_CHEATSHEET.md`, ловушка про
`with`). В psycopg `with` ведёт себя как привычный `with open(...)` —
и страхует транзакцию, и закрывает соединение. Проверяй, с каким
модулем работаешь, прежде чем полагаться на автоматическое закрытие.

---

## Итог: таблица соответствий

| Действие | sqlite3 | psycopg |
|---|---|---|
| Подключение | `sqlite3.connect(":memory:")` | `psycopg.connect(host=..., ...)` |
| Курсор | `connection.cursor()` | `connection.cursor()` |
| Запрос | `cursor.execute(sql, params)` | `cursor.execute(sql, params)` |
| Плейсхолдер | `?` | `%s` |
| Много строк | `cursor.executemany(sql, rows)` | `cursor.executemany(sql, rows)` |
| Забрать результат | `.fetchone()` / `.fetchall()` | `.fetchone()` / `.fetchall()` |
| Сохранить | `connection.commit()` | `connection.commit()` |
| Откатить | `connection.rollback()` | `connection.rollback()` |
| `with connection:` | коммитит, **не закрывает** | коммитит **и закрывает** |
| Персистентность данных | нет (`:memory:` исчезает с процессом) | да (реальный сервер) |

---

## Исключения (кратко)

Оба модуля бросают исключения из одной иерархии PEP 249 —
`IntegrityError` (нарушение ограничения, например `NOT NULL`/`FOREIGN
KEY`), `OperationalError` (проблема с самим соединением/сервером),
`ProgrammingError` (ошибка в самом SQL-запросе).

**Мнемоника:** имена исключений одинаковые в обоих модулях — если
поймал `sqlite3.IntegrityError` раньше, `psycopg.errors.IntegrityError`
ловится тем же способом (`except psycopg.IntegrityError:` тоже
работает — базовый класс реэкспортирован в корень модуля).
