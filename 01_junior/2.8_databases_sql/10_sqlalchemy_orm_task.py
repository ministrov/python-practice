# -*- coding: utf-8 -*-
"""
Блок 2.8, тема 4b: SQLAlchemy 2.0 ORM — практика
════════════════════════════════════════════════════════════════════════
Домен: тот же, что в 08_sqlalchemy_core_task.py — customers (покупатели)
/ orders (заказы). Домен тот же нарочно (сравни, как одна и та же
задача решается через Core-функции и через ORM-классы), но API другое —
скопировать из Core-задания не получится, там были Table/insert/select
над Table-объектами, здесь — классы, Session, relationship.

БД — тот же контейнер pg-learning (см. 05_postgres_basics_demo.py):
    host=localhost, port=5432, db=learning,
    user=learning, password=learning

Справка по API — 09_sqlalchemy_orm_demo.py (DeclarativeBase, Mapped/
mapped_column, relationship, Session.add/commit, select(Model).scalars()).
"""

from typing import List

from sqlalchemy import ForeignKey, create_engine, func, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
)

print(List, func, select, Session)


class Base(DeclarativeBase):
    pass


engine = create_engine(
    "postgresql+psycopg://learning:learning@localhost:5432/learning"
)

# ════════════════════════════════════════════════════════════════════════
# Задание 1: опиши модели Customer и Order
# ════════════════════════════════════════════════════════════════════════
# Класс Customer (__tablename__ = "customers"):
#   - id: Mapped[int], mapped_column(primary_key=True)
#   - name: Mapped[str]
#   - orders: Mapped[List["Order"]] = relationship(back_populates="customer")
#
# Класс Order (__tablename__ = "orders"):
#   - id: Mapped[int], mapped_column(primary_key=True)
#   - customer_id: Mapped[int], mapped_column(ForeignKey("customers.id"))
#   - amount: Mapped[int]
#   - status: Mapped[str]
#   - customer: Mapped["Customer"] = relationship(back_populates="orders")
#
# Оба класса наследуются от Base.
#
# YOUR CODE HERE:


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    orders: Mapped[list["Order"]] = relationship(back_populates="customer")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    amount: Mapped[int]
    status: Mapped[str]
    customer: Mapped["Customer"] = relationship(back_populates="orders")


# ════════════════════════════════════════════════════════════════════════
# Задание 2: создай таблицы
# ════════════════════════════════════════════════════════════════════════
# Base.metadata.drop_all(engine), потом Base.metadata.create_all(engine).
#
# YOUR CODE HERE:

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# ════════════════════════════════════════════════════════════════════════
# Задание 3: наполни таблицы данными через Session
# ════════════════════════════════════════════════════════════════════════
# Один блок `with Session(engine) as session:`:
#   1. Создай 3 объекта Customer (свои имена), session.add_all([...]),
#      session.commit() — после commit() у каждого объекта появится .id.
#   2. Создай 6 объектов Order (по 2 на каждого customer, используя
#      customer.id как customer_id), значения status — "paid"/"pending"
#      вперемешку. session.add_all([...]), session.commit().
#
# YOUR CODE HERE:

with Session(engine) as session:
    customers: List[Customer] = [Customer(name="Anton"), Customer(
        name="Bill"), Customer(name="John")]
    session.add_all(customers)
    session.commit()
    print(customers[0].id)
    print(customers[0].name)

    orders: List[Order] = [
        Order(customer_id=customers[0].id, amount=100, status="paid"),
        Order(customer_id=customers[0].id, amount=200, status="pending"),
        Order(customer_id=customers[1].id, amount=150, status="paid"),
        Order(customer_id=customers[1].id, amount=300, status="pending"),
        Order(customer_id=customers[2].id, amount=250, status="paid"),
        Order(customer_id=customers[2].id, amount=400, status="pending"),
    ]
    session.add_all(orders)
    session.commit()
    print(orders[0].id)
    print(orders[0].status)
    print(orders[0].amount)

# ════════════════════════════════════════════════════════════════════════
# Задание 4: select(Customer) с фильтром
# ════════════════════════════════════════════════════════════════════════
# Новый `with Session(engine) as session:`. Найди Customer по имени
# (любое одно конкретное имя из задания 3, не переменная) через
# select(Customer).where(...), .scalars().one() (не .all() — здесь
# ожидается ровно один результат). Выведи customer.id и customer.name.
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 5: relationship без JOIN
# ════════════════════════════════════════════════════════════════════════
# Для того же customer из задания 4 (можно в том же `with`-блоке):
# пройдись циклом по customer.orders и выведи каждый order.amount и
# order.status. Без единого select()/JOIN — только атрибут .orders.
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 6: JOIN + WHERE через классы
# ════════════════════════════════════════════════════════════════════════
# select(Customer.name, Order.amount).join(Order).where(Order.status ==
# "paid") — выведи через session.execute(query).all().
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 7: GROUP BY + SUM через классы
# ════════════════════════════════════════════════════════════════════════
# select(Customer.name, func.sum(Order.amount)).join(Order).group_by(
# Customer.name) — общая сумма заказов на покупателя (без WHERE).
#
# YOUR CODE HERE:


# ════════════════════════════════════════════════════════════════════════
# Задание 8 (бонус): GROUP BY + ORDER BY + LIMIT через классы
# ════════════════════════════════════════════════════════════════════════
# Покупатель с наибольшим количеством заказов: func.count(Order.id),
# .join(Order), .group_by(Customer.name), .order_by(...desc()), .limit(1).
#
# YOUR CODE HERE:
