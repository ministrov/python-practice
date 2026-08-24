# -*- coding: utf-8 -*-
"""
Блок 2.8.2: Практика — INSERT/UPDATE/DELETE и транзакции
════════════════════════════════════════════════════════════════════════
6 ЗАДАНИЙ для самостоятельного решения.
Домен: банковские счета — accounts (id, owner, balance).

ВАЖНО: задание 1 создаёт connection/cursor и заполняет таблицу — все
следующие задания используют ЭТИ ЖЕ connection/cursor (не создавай новые
подключения в других заданиях).

Совет: посмотри 03_dml_transactions_demo.py, если застрял — там другой
домен (products/quantity), просто скопировать не получится.
"""

import sqlite3

print("=" * 60)
print("ЗАДАНИЕ 1: Схема и данные")
print("=" * 60)
print("""
1.1 Создай connection = sqlite3.connect(":memory:") и
    cursor = connection.cursor().
1.2 Создай таблицу accounts(id INTEGER PRIMARY KEY, owner TEXT NOT
    NULL, balance REAL NOT NULL).
1.3 Наполни таблицу минимум 3 строками с разными balance (одному из
    счетов дай баланс поменьше — понадобится в задании 5).
1.4 Сделай connection.commit().
""")

# ТВОЙ КОД ЗДЕСЬ:
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY,
        owner TEXT NOT NULL,
        balance REAL NOT NULL
    )
""")

accounts_data = [
    ("Alice", 1000.0),
    ("Bob", 50.0),
    ("Charlie", 5000.0),
]

cursor.executemany(
    "INSERT INTO accounts (owner, balance) VALUES (?, ?)",
    accounts_data
)

connection.commit()
cursor.execute("SELECT * FROM accounts")
print(cursor.fetchall())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: INSERT")
print("=" * 60)
print("""
2.1 Добавь ещё один счёт через cursor.execute(...) (одна строка, не
    executemany) и сделай commit().
2.2 Выведи SELECT * FROM accounts, чтобы убедиться, что счёт добавлен.
""")

# ТВОЙ КОД ЗДЕСЬ:
cursor.execute(
    "INSERT INTO accounts (owner, balance) VALUES (?, ?)",
    ("Kate", 2000.9)
)

connection.commit()

cursor.execute("SELECT * FROM accounts")
print(cursor.fetchall())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: UPDATE")
print("=" * 60)
print("""
3.1 Увеличь balance одного конкретного счёта (по id) на выбранную тобой
    сумму — обязательно с WHERE. Сделай commit().
3.2 Выведи balance этого счёта после обновления, чтобы проверить.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: DELETE")
print("=" * 60)
print("""
4.1 Удали один счёт по id — обязательно с WHERE. Сделай commit().
4.2 Выведи SELECT * FROM accounts — убедись, что удалённого счёта
    больше нет, а остальные на месте.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Транзакция — перевод между счетами")
print("=" * 60)
print("""
5.1 Напиши функцию transfer(cur, conn, from_id, to_id, amount):
    - прочитать текущий balance счёта from_id (SELECT ... WHERE id = ?)
    - если balance < amount: raise ValueError("insufficient funds")
      ДО каких-либо UPDATE (деньги ещё нигде не списаны)
    - иначе: UPDATE balance счёта from_id (- amount) и счёта to_id
      (+ amount), затем conn.commit()
    - если поймали ValueError — conn.rollback() и пробросить исключение
      дальше (re-raise)
5.2 Вызови transfer(...) с суммой БОЛЬШЕ баланса счёта-отправителя —
    поймай ValueError снаружи, напечатай сообщение.
5.3 Выведи balance обоих счетов после неудачной попытки — оба должны
    остаться БЕЗ ИЗМЕНЕНИЙ (rollback сработал).
5.4 Вызови transfer(...) ещё раз с суммой МЕНЬШЕ баланса — перевод
    должен пройти. Выведи balance обоих счетов — сумма списанного
    и зачисленного должна совпасть.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Атомарность (без кода, письменный ответ)")
print("=" * 60)
print("""
6.1 Представь, что в transfer() из задания 5 два UPDATE выполнялись бы
    БЕЗ общей транзакции — то есть после первого UPDATE (списание у
    from_id) сразу же вызывался commit(), а потом отдельным вызовом
    выполнялся второй UPDATE (зачисление to_id) со своим commit().
    Что произойдёт с деньгами, если программа упадёт (например, из-за
    обрыва сети или бага) ровно МЕЖДУ этими двумя commit()?
    Почему обёртывание обоих UPDATE в одну транзакцию с одним commit()
    в конце решает эту проблему?
    Напиши ответ ниже прямо в комментарии.
""")

# ТВОЙ ОТВЕТ ЗДЕСЬ (в комментарии):
