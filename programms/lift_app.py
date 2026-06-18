""" Программа на подобии лифта которая принимает от
                        пользователя число -1 до 10 и выводит что это за этаж 
"""


def define_floor(num: int) -> None:
    """ Определяет какой этаж."""
    # sequences: list[int] = [2, 3, 4, 5, 6, 7, 8, 9]
    # odds: list[int] = [n for n in sequences if n % 2 == 1]
    # evens: list[int] = [n for n in sequences if n % 2 == 0]
    match num:
        case -1:
            print("Подвал, здесь находится склад.")
        case 1:
            print("Hall Reception.")
        case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            if num % 2 == 0:
                print("Офисный этаж.")
            else:
                print("Жилой этаж.")
        case 10:
            print("Технический этаж, ход запрещен.")
        case _:
            print("Такого этажа нет.")


def main() -> None:
    """ Точка входа. """
    user_input = int(input("Введите число от -1 до 10: "))
    define_floor(user_input)


if __name__ == "__main__":
    main()
