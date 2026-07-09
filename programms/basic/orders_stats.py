""" Цель задачи — вычислить общее количество проданных товаров и общую сумму заказов за день, используя данные, хранящиеся в словарях.
"""
from functools import reduce
from typing import Any


orders = [
    {"id": 1, "user": "Anton", "items": [
        {"name": "Laptop", "price": 1000},
        {"name": "Mouse", "price": 50}
    ]},
    {"id": 2, "user": "Kate", "items": [
        {"name": "Phone", "price": 700}
    ]},
    {"id": 3, "user": "Oleg", "items": [
        {"name": "Monitor", "price": 300},
        {"name": "Keyboard", "price": 100}
    ]}
]


def aggregate(acc: dict[str, Any], order: dict[str, Any]) -> dict[str, Any]:
    order_sum = sum(item["price"] for item in order["items"])
    order_count = len(order["items"])
    print(order_sum)
    print(order_count)
    return {
        "total_price": acc["total_price"] + order_sum,
        "total_items": acc["total_items"] + order_count
    }


result = reduce(aggregate, orders, {"total_price": 0, "total_items": 0})
print(result)
