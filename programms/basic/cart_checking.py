""" Цель - Реализовать функцию checkout, которая обрабатывает заказы в корзине. Обрабатывать возможные ошибки: пустая корзина,      отсутствие товара на складе и невалидный купон.
    # выбрасывает EmptyCartError, если карзина пуста
    # выбрасывает OutOfStockError, если товара нет
    # выбрасывает InvalidCouponError, если купон не "SALES20"
    # возвращает итоговую сумму заказа
"""


class ShopError(Exception):
    """ Базовый класс ошибки магазина """
    pass


class OutOfStockError(ShopError):
    """ """
    pass


class EmptyCartError(ShopError):
    """"""
    pass


class InvalidCouponError(ShopError):
    """ """
    pass


carts: list[tuple[list[dict[str, str | int | bool]], str | None]] = [
    ([], None),
    ([{"item": "Phone", "price": 700, "in_stock": False}], None),
    ([{"item": "Laptop", "price": 1000, "in_stock": True}], "BADCODE"),
    ([{"item": "Laptop", "price": 1000, "in_stock": True}], "SALES20"),
]


def checkout(
    cart: list[dict[str, str | int | bool]],
    coupon: str | None = None,
) -> int:
    if not cart:
        raise EmptyCartError("Корзина пуста")
    total = 0
    for product in cart:
        if not product.get("in_stock", True):
            raise OutOfStockError(f"{product["item"]} нет в наличии")
        price = product["price"]
        if not isinstance(price, int):
            raise ShopError(f"Некорректная цена товара: {price!r}")
        total += price

    if coupon:
        if coupon != "SALES20":
            raise InvalidCouponError(f"Купон {coupon} не валиден")

    return total


for cart, coupon in carts:
    try:
        result = checkout(cart, coupon)
        print(f"Итоговая сумма {result}")
    except OutOfStockError as e:
        print(f"Ошибка: нет товара: - {e}")
    except InvalidCouponError as e:
        print(f"Ошибка: купон не действителен - {e}")
    except EmptyCartError as e:
        print(f"Пустая корзина - {e}")
    except ShopError as e:
        print(f"Другая ошибка магазина - {e}")
