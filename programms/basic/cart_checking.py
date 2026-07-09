""" Цель - Реализовать функцию checkout, которая обрабатывает заказы в корзине. Обрабатывать возможные ошибки: пустая корзина,      отсутствие товара на складе и невалидный купон.
    # выбрасывает EmptyCartError, если карзина пуста
    # выбрасывает OutOfStockError, если товара нет
    # выбрасывает InvalidCouponError, если купон не "SALES20"
    # возвращает итоговую сумму заказа
"""

carts: list[tuple[list[dict[str, str | int | bool]], str | None]] = [
    ([], None),
    ([{"item": "Phone", "price": 700, "in_stock": False}], None),
    ([{"item": "Laptop", "price": 1000, "in_stock": True}], "BADCODE"),
    ([{"item": "Laptop", "price": 1000, "in_stock": True}], "SALES20"),
]

print(carts)
