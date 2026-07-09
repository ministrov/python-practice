""" Написать функцию calculate, которая принимает два числа и операцию +, -, *, / """


def calculate(num_1: float, num_2: float, operation: str) -> float | None | str:
    match operation:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "*":
            return num_1 * num_2
        case "/":
            return num_1 / num_2 if num_2 != 0 else "Ошибка в делении на 0"
        case _:
            return "Неизвестная операция"


print(calculate(10, 5, "+"))
print(calculate(10, 2, "-"))
print(calculate(10, 3, "*"))
print(calculate(10, 5, "*(*I)"))
print(calculate(10, 0, "/"))
print(calculate(40, 4, "/"))
