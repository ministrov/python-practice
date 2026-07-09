""" Нужно нормализовать пришедшие из вне данные """

users = [
    {"name": "    anton", "age": "25"},
    {"name": "Maria   ", "age": "30"},
    {"name": "  IVAN  ", "age": "  17"},
    {"name": "olga", "age": "42  "},
    {"name": "Пётр Петров", "age": "0"}
]


def normalize_data(user: dict[str, str]):
    return {
        "name": user["name"].strip().title(),
        "age": int(user["age"].strip())
    }


normalized_users = list(map(normalize_data, users))

print(normalized_users)
