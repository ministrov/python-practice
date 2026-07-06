""" Заказы пользователей на курсы: id, сумма покупки, статус платежа """

from typing import TypedDict


class Order(TypedDict):
    user_id: int
    name: str
    amount: int
    status: str


orders: list[Order] = [
    {"user_id": 1, "name": "Anton", "amount": 150, "status": "paid"},
    {"user_id": 2, "name": "Oleg", "amount": 200, "status": "paid"},
    {"user_id": 3, "name": "Maria", "amount": 120, "status": "paid"},
    {"user_id": 4, "name": "Ivan", "amount": 90, "status": "paid"},
    {"user_id": 5, "name": "Olga", "amount": 300, "status": "pending"},
    {"user_id": 6, "name": "Dmitry", "amount": 100, "status": "paid"},
    {"user_id": 7, "name": "Svetlana", "amount": 500, "status": "failed"},
    {"user_id": 8, "name": "Nikita", "amount": 101, "status": "paid"},
    {"user_id": 9, "name": "Anna", "amount": 0, "status": "paid"},
    {"user_id": 10, "name": "Petr", "amount": 250, "status": "refunded"},
    {"user_id": 11, "name": "Elena", "amount": -50, "status": "paid"},
    {"user_id": 12, "name": "Sergey", "amount": 999, "status": "paid"},
]

filtered_users = list(filter(
    lambda order: order["status"] == "paid" and order["amount"] > 100, orders))
