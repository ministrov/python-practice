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


def delete_expenses(expenses: list[float], index: int) -> None:
    if index >= len(expenses) or index < 0:
        print("Неверный номер")
    else:
        expenses.pop(index)
        print("Вы удалили расход")


def get_total(expenses: list[float]) -> float:
    return sum(expenses)


def get_average(expenses: list[float]) -> float:
    if not expenses:
        return 0.0
    return sum(expenses) / len(expenses)


def print_report():
    print(f"")


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

    if choice == "3":
        info = {
            "total": get_total(expenses),
            "average": get_average(expenses)
        }
        print(f"""
                Итого: {info["total"]}
                Среднее: {info["average"]}        
            """)

    if choice == "4":
        index_value = input("Введите индекс: ")
        delete_expenses(expenses, int(index_value) - 1)

    if choice == "5":
        print("До свидания!")
        break
