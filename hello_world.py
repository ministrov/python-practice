"""Демонстрация списков, условий, match и проверки роли."""


def check_age(age: int) -> bool:
    """Вернуть True, если возраст совершеннолетний."""
    if age < 18:
        print("You are not old enough")
    elif age < 50:
        print("You are old enough")
    else:
        print("You are too old")
    return age >= 18


def describe_role(role: str) -> None:
    """Вывести описание роли."""
    match role:
        case "admin":
            print("You are an admin")
        case "user":
            print("You are a user")
        case "guest":
            print("You are a guest")
        case _:
            print("You are not an admin")


def match_your_role(role: str) -> bool:
    """Вернуть True для ролей с доступом (admin, user)."""
    match role:
        case "admin" | "user":
            return True
        case _:
            return False


def main() -> None:
    """Точка входа."""
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    numbers.append(6)
    print(numbers)

    if numbers[0] == 1:
        print("First element is 1")

    for number in numbers:
        print(number)

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age")
        return

    is_legal_age = check_age(age)
    print(age)
    print("\n")
    print("*" * 30)
    print(is_legal_age)

    print("*" * 30)
    print("Conditional Expression")
    print(is_legal_age)

    role = input("Enter your role: ")
    describe_role(role)

    is_admin = match_your_role("admin")
    print(is_admin)


if __name__ == "__main__":
    main()
