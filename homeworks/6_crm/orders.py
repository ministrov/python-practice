""" Модуль заказов """

from typing import Literal, TypedDict


OrderStatus = Literal["new", "in_progress", "done", "cancelled"]


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: OrderStatus
    tags: set[str]
    created_at: str
    due: str | None
    closed_at: str | None


def create_order(orders: list[Order], order: Order) -> None:
    """ Добавить новый заказ в список заказов """
    orders.append(order)


def list_orders(orders: list[Order]) -> list[Order]:
    """ Вернуть список заказов """
    return orders


def edit_order(orders: list[Order], order_id: int, updates: dict[str, object]):
    """ Изменить поля заказа по id """
    pass


def remove_order(orders: list[Order], order_id: int):
    """ Удалить заказ по id """
    pass
