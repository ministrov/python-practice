""" Написать функцию calculate, которая принимает два числа и операцию +, -, *, / """


def calculate(num_1: float, num_2: float, operation: str) -> float | None | str:
    if operation == "+":
        return num_1 + num_2
    if operation == "-":
        return num_1 - num_2
    if operation == "*":
        return num_1 * num_2
    if operation == "/":
        return num_1 / num_2
    elif num_2 == 0:
        return "Ошибка в делении на 0"
