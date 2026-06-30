""" 
    Сделать интерактивное меню управления расходами с помощью циклов.
        Добавить расход
        Показать все расходы
        Показать сумму и средний расход
        Удалить расход по номеру
        Выход
        Пока сделать только выход
"""

expenses: list[float] = []


def add_expenses(expenses: list[float], value: str) -> None:
    expenses.append(float(value))


while True:
    print("\n ====== Меню =======")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        sum_value = input("Введите сумму: ")
        add_expenses(expenses, sum_value)
        print("Расход добавлен!")

    if choice == "5":
        print("До свидания!")
        break
