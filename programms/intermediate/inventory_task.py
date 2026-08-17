""" Практика: закрепление темы 1 блока 2.6 (аннотации типов) на примере
    учёта товаров на складе.

    Используем только то, что уже пройдено: параметризованные
    generic-коллекции (list[X], dict[K, V], tuple), X | None, X | Y,
    вложенные generics. НЕ используем Any/Callable/Iterable/Sequence/
    TypedDict — это следующая тема, ещё не пройдена.

    Задача:
    1. Напиши total_stock_value(prices: dict[str, float],
                                 quantities: dict[str, int]) -> float
       Возвращает суммарную стоимость склада: сумма price * quantity
       по каждому товару (ключ — название товара, общий для обоих
       словарей).

    2. Напиши find_price(prices: dict[str, float], name: str) -> float | None
       Возвращает цену товара по названию, или None, если товара нет.

    3. Напиши parse_quantity(raw: str) -> int | float
       Если строка похожа на целое число — верни int, иначе float
       (например, остаток на складе может быть дробным для весовых
       товаров).

    4. Напиши restock_pairs(names: list[str], amounts: list[int]
                             ) -> list[tuple[str, int]]
       Собирает список пар (название, количество) из двух параллельных
       списков одинаковой длины.

    5. Напиши group_by_supplier(
           items: list[tuple[str, str]],
       ) -> dict[str, list[str]]
       items — список пар (поставщик, товар). Сгруппируй товары по
       поставщику: {поставщик: [товар, товар, ...]}.

    6. Проверь на примере ниже (раскомментируй и запусти).
"""

# ТВОЙ КОД ЗДЕСЬ: total_stock_value


def total_stock_value(prices: dict[str, float], quantities: dict[str, int]) -> float:
    total: float = 0.0

    for item in prices:
        total += prices[item] * quantities[item]

    return total

# ТВОЙ КОД ЗДЕСЬ: find_price


def find_price(prices: dict[str, float], name: str) -> float | None:
    return prices[name] if name in prices else None

# ТВОЙ КОД ЗДЕСЬ: parse_quantity


def parse_quantity(raw: str) -> int | float:
    if "." in raw:
        return float(raw)
    else:
        return int(raw)

# ТВОЙ КОД ЗДЕСЬ: restock_pairs


# ТВОЙ КОД ЗДЕСЬ: group_by_supplier


if __name__ == "__main__":
    prices = {"screws": 0.1, "bolts": 0.25, "hinges": 1.5}
    quantities = {"screws": 500, "bolts": 200, "hinges": 30}

    print(total_stock_value(prices, quantities))
    print(find_price(prices, "bolts"))
    print(find_price(prices, "nails"))

    print(parse_quantity("120"))
    print(parse_quantity("12.5"))

    # print(restock_pairs(["screws", "bolts"], [100, 50]))

    # print(group_by_supplier(
    #     [("AcmeCorp", "screws"), ("AcmeCorp", "bolts"), ("Best", "hinges")]
    # ))
