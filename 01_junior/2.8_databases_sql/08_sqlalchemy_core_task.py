# -*- coding: utf-8 -*-
"""
Блок 2.8, тема 4a: SQLAlchemy 2.0 Core — практика
════════════════════════════════════════════════════════════════════════
Домен: интернет-магазин — customers (покупатели) / orders (заказы).
Домен намеренно другой, не authors/posts из демо-файла — чтобы решать
задания через понимание Core, а не копированием кода из демо.

БД — тот же контейнер pg-learning (см. 05_postgres_basics_demo.py):
    host=localhost, port=5432, db=learning,
    user=learning, password=learning

Справка по API — 07_sqlalchemy_core_demo.py (Engine, Table/MetaData,
insert/select/join/group_by, engine.begin() vs engine.connect()).
"""

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    create_engine,
    insert,
    select,
    func,
)

print(Column)
print(Integer)
print(Table)
print(String)
print(Numeric)
print(ForeignKey)
print(insert)
print(select)
print(func)

engine = create_engine(
    "postgresql+psycopg://learning:learning@localhost:5432/learning"
)
metadata = MetaData()

# ════════════════════════════════════════════════════════════════════════
# Задание 1: опиши схему через Table
# ════════════════════════════════════════════════════════════════════════
# Создай два объекта Table в этом MetaData:
#
# customers:
#   - id: Integer, primary_key=True
#   - name: String, nullable=False
#
# orders:
#   - id: Integer, primary_key=True
#   - customer_id: Integer, ForeignKey("customers.id")
#   - amount: Numeric, nullable=False   (сумма заказа)
#   - status: String, nullable=False    (значения: "paid" или "pending")
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 2: создай таблицы в БД
# ════════════════════════════════════════════════════════════════════════
# Сначала metadata.drop_all(engine) — чтобы демо было безопасно
# перезапускать (та же причина, что DROP TABLE IF EXISTS в психкопг-
# практике). Потом metadata.create_all(engine).
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 3: наполни таблицы данными
# ════════════════════════════════════════════════════════════════════════
# Через engine.begin() как контекстный менеджер (один блок с двумя
# insert() — сначала customers, потом orders, ведь orders ссылается на
# customers через customer_id):
#
# customers (4 покупателя, имена — свои):
#   например: "Анна", "Борис", "Виктор", "Галина"
#
# orders (8 заказов, распредели произвольно между покупателями, у
# каждого покупателя должен быть хотя бы один заказ):
#   customer_id, amount (любые числа), status ("paid" или "pending")
#   — сделай так, чтобы были заказы ОБОИХ статусов у разных покупателей.
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 4: select() с фильтром
# ════════════════════════════════════════════════════════════════════════
# Через engine.connect(): выбери всех customers с именем, которое ты
# использовал в задании 3 (любое одно конкретное имя, не переменная).
# Выведи результат через print(result.fetchall()).
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 5: JOIN + WHERE
# ════════════════════════════════════════════════════════════════════════
# Выбери customers.name и orders.amount для заказов со статусом "paid"
# (используй orders.c.status == "paid"). JOIN customers и orders через
# .join(). Выведи результат.
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 6: GROUP BY + агрегат (SUM)
# ════════════════════════════════════════════════════════════════════════
# Посчитай ОБЩУЮ сумму заказов (func.sum(orders.c.amount)) для каждого
# покупателя — неважно, какой статус у заказа (без WHERE). JOIN
# customers и orders, GROUP BY customers.name. Выведи имя покупателя и
# сумму.
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 7 (бонус): GROUP BY + ORDER BY + LIMIT
# ════════════════════════════════════════════════════════════════════════
# Найди покупателя с НАИБОЛЬШИМ количеством заказов (func.count(orders.c.id)):
# JOIN, GROUP BY customers.name, ORDER BY по количеству заказов по
# убыванию (.order_by(...).desc()), LIMIT 1 (.limit(1)). Выведи имя и
# количество заказов.
#
# YOUR CODE HERE:
