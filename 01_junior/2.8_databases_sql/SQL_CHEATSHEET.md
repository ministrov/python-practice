# 🧠 SQL-шпаргалка — блок 2.8 (мнемоники)

Каждая команда — с якорем на то, что ты уже знаешь из Python
(список словарей, `filter`, `sorted`, срезы, вложенный цикл).
Источники: `01_sql_basics_demo.py` (employees/departments) и
`02_sql_basics_task.py` (categories/products).

---

## Структура данных

### `CREATE TABLE`
Создаёт таблицу — как объявить класс с полями, только хранится не в
памяти, а в файле/движке БД.

```sql
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
```

**Мнемоника:** `CREATE TABLE` = `class` в Python — описываешь форму
строки один раз, потом штампуешь строки по этой форме.

### `PRIMARY KEY` (PK)
Столбец, уникально определяющий строку. Аналог `id()` объекта, но это
значение из данных, а не адрес в памяти.

**Мнемоника:** PK — паспорт строки. Не бывает двух строк с одним PK.

### `FOREIGN KEY ... REFERENCES ...` (FK)
Столбец в одной таблице, ссылающийся на PK другой. Так две таблицы
связаны без дублирования текста.

```sql
FOREIGN KEY (department_id) REFERENCES departments(id)
```

**Мнемоника:** FK — это `department_id` вместо
`department_name`, скопированного в каждую строку сотрудника (раздел 0b
демо-файла). Число вместо повторённого текста.

### `NOT NULL`
Столбец обязан иметь значение — `INSERT` без него упадёт с ошибкой.

**Мнемоника:** как поле без `= None` в аннотации — обязательный
параметр.

---

## Заполнение и изменение данных

### `INSERT INTO ... VALUES (...)`
Добавляет одну строку.

```sql
INSERT INTO departments (id, name) VALUES (1, "Backend")
```

**Мнемоника:** `INSERT INTO` = `list.append(...)`, но append не в
Python-список, а в таблицу.

### `cursor.executemany(sql, [...])`
То же самое `INSERT`, но сразу для списка кортежей — один запрос,
много строк. **Каждая строка — отдельный кортеж в списке**, не общий
список аргументов через запятую (грабли задания 1, коммит `aa31c48`).

```python
cursor.executemany(
    "INSERT INTO departments (id, name) VALUES (?, ?)",
    [(1, "Backend"), (2, "Frontend")],  # список КОРТЕЖЕЙ
)
```

**Мнемоника:** `executemany` = `for row in rows: execute(sql, row)`,
но одним вызовом.

### `UPDATE ... SET ... WHERE ...`
Меняет значение в уже существующих строках.

```sql
UPDATE employees SET salary = salary + 100 WHERE name = 'Ann'
```

**Мнемоника:** как `for emp in employees: if emp["name"] == "Ann":
emp["salary"] += 100` — только БД делает это внутри себя.

### `connection.commit()`
Фиксирует изменения — без этого `INSERT`/`UPDATE` не сохранятся
между запросами (или потеряются при закрытии соединения).

**Мнемоника:** commit = "сохранить файл" после правок. Без Ctrl+S
работа не потеряна сразу, но и не гарантирована.

### Ловушка: `with connection:`
Это **не** `with open(...)` для файлов. `with sqlite3.connect(...) as
conn:` при выходе делает `commit()`/`rollback()`, но **не закрывает**
соединение. Закрывать нужно явным `connection.close()`.

**Мнемоника:** `with connection` страхует только транзакцию, не
"выключает свет" — свет (`close()`) гасишь сам.

---

## Чтение данных

### `SELECT col1, col2 FROM table`
Выбирает столбцы из таблицы.

**Мнемоника:** `SELECT ... FROM` = `[(row["col1"], row["col2"]) for
row in table]` — список кортежей нужных полей.

### `WHERE условие`
Фильтрует строки ДО выборки.

```sql
SELECT name, salary FROM employees WHERE salary > 2800
```

**Мнемоника:** `WHERE` = `filter(lambda row: условие, table)` или
`if` внутри list comprehension.

### `ORDER BY col [ASC|DESC]`
Сортирует результат. `DESC` — по убыванию (по умолчанию `ASC` —
по возрастанию).

**Мнемоника:** `ORDER BY col DESC` = `sorted(table, key=lambda row:
row["col"], reverse=True)`.

### `LIMIT n`
Берёт только первые `n` строк результата (обычно вместе с `ORDER BY` —
иначе "первые" не имеют гарантированного смысла).

**Мнемоника:** `LIMIT n` = срез `[:n]` в конце.

```sql
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2
```
= "топ-2 по зарплате" = `sorted(...)[:2]` в Python.

---

## Соединение таблиц (JOIN)

### `JOIN ... ON ...` (он же `INNER JOIN`)
Соединяет строки двух таблиц по совпадению столбцов. **Строка без
пары с обеих сторон в результат не попадает** — теряется молча.

```sql
SELECT employees.name, departments.name
FROM employees
JOIN departments ON employees.department_id = departments.id
```

**Мнемоника (см. раздел 0c демо-файла):** это вложенный цикл +
`if совпадение` без `else`:

```python
for emp in employees:               # FROM employees
    for dept in departments:        # JOIN departments
        if dept["id"] == emp["department_id"]:  # ON ...
            print(emp["name"], dept["name"])     # SELECT ...
```
Eve (без отдела) в вывод не попадает — `if` ни разу не сработал.

### `LEFT JOIN ... ON ...`
Как `JOIN`, но **все строки левой таблицы (`FROM ...`) сохраняются**,
даже без пары — недостающие поля справа приходят как `NULL`
(`None` в Python).

```sql
SELECT departments.name, employees.name
FROM departments
LEFT JOIN employees ON employees.department_id = departments.id
```

**Мнемоника (см. раздел 0d демо-файла):** вложенный цикл + флаг
`found` + запасной `print`, если пары не нашлось:

```python
for emp in employees:
    found = False
    for dept in departments:
        if dept["id"] == emp["department_id"]:
            print(emp["name"], dept["name"])
            found = True
    if not found:
        print(emp["name"], None)   # ← это и есть LEFT JOIN
```
"LEFT" = сохраняем ВСЁ из таблицы слева от `LEFT JOIN`, даже без пары.

---

## Группировка и агрегаты

### `GROUP BY col`
Схлопывает строки с одинаковым значением `col` в одну "группу" —
дальше к каждой группе применяется агрегатная функция.

**Мнемоника:** `GROUP BY` = `itertools.groupby` после сортировки, или
`dict` вида `{ключ: [все строки с этим ключом]}`.

### Агрегатные функции: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
Считают одно число по каждой группе (или по всей таблице, если
`GROUP BY` нет).

```sql
SELECT departments.name, AVG(employees.salary), COUNT(employees.id)
FROM employees
JOIN departments ON employees.department_id = departments.id
GROUP BY departments.name
```

**Мнемоника:** для каждой группы — `sum(salaries) / len(salaries)`
(это `AVG`) и `len(rows)` (это `COUNT`). Сотрудник без отдела (Eve)
сюда не попадёт — тот же эффект, что у `JOIN` без `LEFT`.

---

## Python-обвязка (sqlite3)

| Код | Что делает |
|---|---|
| `sqlite3.connect(":memory:")` | открыть БД в оперативной памяти (без файла) |
| `connection.cursor()` | получить курсор — им выполняются запросы |
| `cursor.execute(sql)` | выполнить один SQL-запрос |
| `cursor.executemany(sql, rows)` | выполнить запрос для каждой строки из списка |
| `cursor.fetchall()` | забрать ВСЕ строки результата — список кортежей |
| `cursor.fetchone()` | забрать ОДНУ строку результата (или `None`) |
| `connection.commit()` | зафиксировать изменения |
| `connection.close()` | закрыть соединение (не забывать после `with`!) |

**Мнемоника:** `execute` готовит результат, `fetchall`/`fetchone`
его забирают — это как генератор и `list(...)`/`next(...)`:
запрос не возвращает данные сам по себе, их нужно явно "вытащить".

---

## Нормализация — три правила одной строкой

- **1NF** — в ячейке одно значение, не список/CSV-строка.
- **2NF** — все поля зависят от ВСЕГО составного PK (если PK из
  нескольких столбцов).
- **3NF** — поля зависят ТОЛЬКО от PK, не друг от друга (не хранить
  `category_id` И `category_name` вместе в `products` — имя зависит
  от `category_id`, а не от PK товара).

**Мнемоника:** каждое правило — это отказ от одного вида дублирования
данных, который ты уже видел в разделе 0a демо-файла (`department_name`,
повторённый в каждой строке сотрудника).
