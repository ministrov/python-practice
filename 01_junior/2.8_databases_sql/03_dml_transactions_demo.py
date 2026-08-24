# -*- coding: utf-8 -*-
"""
Блок 2.8.2: Демо — INSERT/UPDATE/DELETE и транзакции (COMMIT/ROLLBACK)
════════════════════════════════════════════════════════════════════════
Темы:
  0. Мост: backup+restore списка вручную ≈ ROLLBACK транзакции
  1. INSERT — добавление одной строки
  2. UPDATE — риск запроса без WHERE
  3. DELETE — риск запроса без WHERE
  4. Транзакция целиком: несколько операций как одно целое
     (ROLLBACK при ошибке на середине)
  5. connection.close() — закрывать явно
"""

import copy
import sqlite3

# ════════════════════════════════════════════════════════════════════════
# 0. Мост: backup+restore списка вручную ≈ ROLLBACK транзакции
# ════════════════════════════════════════════════════════════════════════
# Если меняешь структуру данных в несколько шагов и на середине что-то
# идёт не так — хочется откатить ВСЕ шаги, а не оставить данные в
# наполовину испорченном состоянии. Руками это выглядит так: снять
# копию ДО изменений, вернуться к ней при ошибке.

warehouse = {"apples": 10, "oranges": 5}


def transfer(
    stock: dict[str, int], from_key: str, to_key: str, amount: int
) -> None:
    """Перенести amount из from_key в to_key, откатив всё при ошибке."""
    backup = copy.deepcopy(stock)  # снимок ДО изменений = "BEGIN"
    try:
        if stock[from_key] < amount:
            raise ValueError("not enough stock")
        stock[from_key] -= amount
        stock[to_key] += amount
        # обе строки применились без ошибок = ничего откатывать не надо
        # (в SQL это соответствует неявному COMMIT)
    except ValueError:
        stock.clear()
        stock.update(backup)  # откат к снимку = "ROLLBACK"
        raise


try:
    transfer(warehouse, "apples", "oranges", 100)  # больше, чем есть
except ValueError:
    print("Перевод не удался, откатили:", warehouse)
# Перевод не удался, откатили: {'apples': 10, 'oranges': 5}
#
# В SQL движок БД делает ровно то же самое сам: между BEGIN и COMMIT
# можно выполнить несколько INSERT/UPDATE/DELETE, и если где-то
# посередине происходит ошибка — ROLLBACK отменяет ВСЕ изменения
# транзакции разом, как будто их не было. Не нужно руками писать
# copy.deepcopy() и restore — за это отвечает движок БД.


# ════════════════════════════════════════════════════════════════════════
# 1. Подготовка: таблица products с полем quantity (остаток на складе)
# ════════════════════════════════════════════════════════════════════════

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
""")

cursor.executemany(
    "INSERT INTO products (id, name, quantity) VALUES (?, ?, ?)",
    [
        (1, "Ноутбук", 5),
        (2, "Смартфон", 12),
        (3, "Наушники", 0),
    ],
)
connection.commit()


# ════════════════════════════════════════════════════════════════════════
# 2. INSERT — добавление одной строки
# ════════════════════════════════════════════════════════════════════════
# Та же команда, что и в executemany() выше, но для одной строки — без
# списка кортежей, один кортеж параметров.

cursor.execute(
    "INSERT INTO products (id, name, quantity) VALUES (?, ?, ?)",
    (4, "Клавиатура", 8),
)
connection.commit()

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())
# [(1, 'Ноутбук', 5), (2, 'Смартфон', 12), (3, 'Наушники', 0),
#  (4, 'Клавиатура', 8)]


# ════════════════════════════════════════════════════════════════════════
# 3. UPDATE — риск запроса без WHERE
# ════════════════════════════════════════════════════════════════════════
# С WHERE — меняется ровно одна (или несколько подходящих) строка.

cursor.execute(
    "UPDATE products SET quantity = quantity - 1 WHERE id = 1"
)
connection.commit()
cursor.execute("SELECT name, quantity FROM products WHERE id = 1")
print(cursor.fetchone())
# ('Ноутбук', 4)

# Без WHERE — UPDATE применится КО ВСЕМ строкам таблицы разом. Это не
# синтаксическая ошибка, поэтому опечатка "забыл WHERE" в проде — одна
# из самых частых причин испорченных данных. Демонстрация на снимке
# (не выполняем на боевых данных, только чтобы увидеть эффект):

cursor.execute("UPDATE products SET quantity = 0")  # ВСЯ таблица!
cursor.execute("SELECT name, quantity FROM products")
print(cursor.fetchall())
# [('Ноутбук', 0), ('Смартфон', 0), ('Наушники', 0), ('Клавиатура', 0)]
# Все остатки обнулились — это и есть цена забытого WHERE.

connection.rollback()  # отменяем демонстрацию, возвращаемся к commit()
cursor.execute("SELECT name, quantity FROM products")
print(cursor.fetchall())
# [('Ноутбук', 4), ('Смартфон', 12), ('Наушники', 0),
#  ('Клавиатура', 8)]


# ════════════════════════════════════════════════════════════════════════
# 4. DELETE — риск запроса без WHERE
# ════════════════════════════════════════════════════════════════════════
# Та же логика, что и у UPDATE: DELETE без WHERE удаляет ВСЕ строки.

cursor.execute("DELETE FROM products WHERE id = 3")  # "Наушники"
connection.commit()
cursor.execute("SELECT * FROM products")
print(cursor.fetchall())
# [(1, 'Ноутбук', 4), (2, 'Смартфон', 12), (4, 'Клавиатура', 8)]


# ════════════════════════════════════════════════════════════════════════
# 5. Транзакция целиком: несколько операций как одно (ROLLBACK)
# ════════════════════════════════════════════════════════════════════════
# "Продажа" ноутбука: списать 1 штуку со склада. Если остаток уходит
# в минус — вся операция должна отмениться, а не остаться наполовину
# применённой (в реальном сценарии здесь было бы ещё и INSERT в
# таблицу заказов — тут для простоты только списание остатка).


def sell(
    cur: sqlite3.Cursor,
    conn: sqlite3.Connection,
    product_id: int,
    amount: int,
) -> None:
    """Списать amount товара product_id, откатив всё при нехватке."""
    cur.execute(
        "SELECT quantity FROM products WHERE id = ?", (product_id,)
    )
    row = cur.fetchone()
    current_quantity: int = row[0]
    try:
        if current_quantity < amount:
            raise ValueError("недостаточно на складе")
        cur.execute(
            "UPDATE products SET quantity = quantity - ? WHERE id = ?",
            (amount, product_id),
        )
        conn.commit()
    except ValueError:
        conn.rollback()
        raise


try:
    sell(cursor, connection, product_id=4, amount=100)  # больше остатка
except ValueError as exc:
    print(f"Продажа отменена: {exc}")
# Продажа отменена: недостаточно на складе

cursor.execute("SELECT quantity FROM products WHERE id = 4")
print(cursor.fetchone())
# (8,) — остаток не изменился, ROLLBACK отменил UPDATE


# ════════════════════════════════════════════════════════════════════════
# 6. connection.close() — закрывать явно
# ════════════════════════════════════════════════════════════════════════
# Напоминание из раздела 7 предыдущего демо-файла: `with connection:`
# делает commit/rollback, но НЕ закрывает соединение. close() нужен
# отдельно, когда работа с этим connection полностью закончена.

connection.close()
