# -*- coding: utf-8 -*-
"""
Блок 2.8.1: Демо — реляционная модель и основы SQL (SELECT/WHERE/JOIN/
GROUP BY/ORDER BY/LIMIT)
════════════════════════════════════════════════════════════════════════
Темы:
  1. Реляционная модель на пальцах: таблицы, строки, столбцы, PK, FK
  2. Нормализация 1NF-3NF — коротко, без академизма
  3. sqlite3 — встроенный движок, без установки, синтаксис SQL близок
     к PostgreSQL (различия будут отдельно отмечены при переходе на Postgres)
  4. SELECT, WHERE, ORDER BY, LIMIT
  5. JOIN (INNER, LEFT)
  6. GROUP BY + агрегатные функции (COUNT, AVG, SUM)
  7. Транзакции и sqlite3.connect как контекстный менеджер — ловушка
"""

import sqlite3

# ════════════════════════════════════════════════════════════════════════
# 1. Реляционная модель на пальцах
# ════════════════════════════════════════════════════════════════════════
# Таблица (table) — как список словарей с одинаковыми ключами: строки
# (rows) — записи, столбцы (columns) — поля с фиксированным типом.
#
# PRIMARY KEY (PK) — столбец (или набор столбцов), уникально
# идентифицирующий строку в этой таблице. Аналог id() у объекта Python,
# но это значение, а не адрес в памяти — оно живёт в самих данных.
#
# FOREIGN KEY (FK) — столбец в одной таблице, ссылающийся на PK другой
# таблицы. Это способ связать строки двух таблиц, не дублируя данные
# (department.name хранится один раз, а не в каждой строке employees).
#
# Нормализация (1NF-3NF) — набор правил "не дублируй данные, не смешивай
# независимые сущности в одной таблице":
#   1NF — каждая ячейка хранит одно атомарное значение (не список, не
#         "Python,SQL,Git" одной строкой)
#   2NF — все не-ключевые столбцы зависят от ВСЕГО первичного ключа
#         (актуально для составных PK)
#   3NF — не-ключевые столбцы зависят ТОЛЬКО от PK, не друг от друга
#         (пример нарушения: хранить и department_id, и department_name
#         в employees — name зависит от department_id, а не от PK employees)


# ════════════════════════════════════════════════════════════════════════
# 2. Подготовка: две связанные таблицы в sqlite3 (in-memory)
# ════════════════════════════════════════════════════════════════════════

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
""")

cursor.executemany(
    "INSERT INTO departments (id, name) VALUES (?, ?)",
    [
        (1, "Backend"),
        (2, "Frontend"),
        (3, "DevOps"),  # в отделе пока нет сотрудников — пригодится для LEFT JOIN
    ],
)

cursor.executemany(
    "INSERT INTO employees (id, name, salary, department_id) VALUES (?, ?, ?, ?)",
    [
        (1, "Ann", 3000.0, 1),
        (2, "Bob", 2500.0, 1),
        (3, "Cara", 3200.0, 2),
        (4, "Dan", 2800.0, 2),
        (5, "Eve", 4000.0, None),  # сотрудник без отдела — department_id NULL
    ],
)

connection.commit()


# ════════════════════════════════════════════════════════════════════════
# 3. SELECT, WHERE, ORDER BY, LIMIT
# ════════════════════════════════════════════════════════════════════════

cursor.execute("SELECT name, salary FROM employees WHERE salary > 2800")
print(cursor.fetchall())
# [('Ann', 3000.0), ('Cara', 3200.0), ('Eve', 4000.0)]

cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2")
print(cursor.fetchall())
# [('Eve', 4000.0), ('Cara', 3200.0)]


# ════════════════════════════════════════════════════════════════════════
# 4. INNER JOIN — только строки, у которых есть совпадение с обеих сторон
# ════════════════════════════════════════════════════════════════════════
# Eve (department_id=NULL) и DevOps (нет сотрудников) сюда НЕ попадут —
# INNER JOIN требует совпадения по обе стороны.

cursor.execute("""
    SELECT employees.name, departments.name
    FROM employees
    JOIN departments ON employees.department_id = departments.id
    ORDER BY employees.name
""")
print(cursor.fetchall())
# [('Ann', 'Backend'), ('Bob', 'Backend'), ('Cara', 'Frontend'), ('Dan', 'Frontend')]


# ════════════════════════════════════════════════════════════════════════
# 5. LEFT JOIN — все строки левой таблицы, даже без совпадения справа
# ════════════════════════════════════════════════════════════════════════
# Отделы без сотрудников (DevOps) попадут в результат, employees.name
# будет NULL (в Python это придёт как None).

cursor.execute("""
    SELECT departments.name, employees.name
    FROM departments
    LEFT JOIN employees ON employees.department_id = departments.id
    ORDER BY departments.name
""")
print(cursor.fetchall())
# [('Backend', 'Ann'), ('Backend', 'Bob'), ('DevOps', None),
#  ('Frontend', 'Cara'), ('Frontend', 'Dan')]


# ════════════════════════════════════════════════════════════════════════
# 6. GROUP BY + агрегатные функции
# ════════════════════════════════════════════════════════════════════════
# GROUP BY схлопывает строки с одинаковым значением столбца в одну,
# а агрегатная функция (AVG/COUNT/SUM/MIN/MAX) считает что-то по каждой
# такой группе. Eve (без отдела) сюда не попадёт — тот же эффект, что
# и у INNER JOIN выше.

cursor.execute("""
    SELECT departments.name, AVG(employees.salary), COUNT(employees.id)
    FROM employees
    JOIN departments ON employees.department_id = departments.id
    GROUP BY departments.name
    ORDER BY departments.name
""")
print(cursor.fetchall())
# [('Backend', 2750.0, 2), ('Frontend', 3000.0, 2)]


# ════════════════════════════════════════════════════════════════════════
# 7. Ловушка: sqlite3.connect(...) как context manager НЕ закрывает
#    соединение сам
# ════════════════════════════════════════════════════════════════════════
# В отличие от open() для файлов, `with sqlite3.connect(...) as conn:`
# при выходе из блока делает COMMIT (без ошибок) или ROLLBACK (при
# исключении) — но САМО соединение остаётся открытым. Закрывать нужно
# явно через conn.close(), иначе — утечка соединений.

with connection:
    cursor.execute(
        "UPDATE employees SET salary = salary + 100 WHERE name = 'Ann'"
    )
    # здесь неявный commit при успешном выходе из блока

cursor.execute("SELECT salary FROM employees WHERE name = 'Ann'")
print(cursor.fetchone())
# (3100.0,)

print(connection.total_changes > 0)
# True — соединение всё ещё живое и рабочее, `with` его не закрыл

connection.close()
