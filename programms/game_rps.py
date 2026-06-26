""" Создание игры Камень Ножницы Бумага

    Запрос числа раундов:
     
        Мы запрашиваем у пользователя, сколько раундов он хочет сыграть.
        
        Основной цикл игры:

        Для каждого раунда происходит следующее: Пользователь делает свой выбор из "Камень", "Ножницы", "Бумага".
        Компьютер случайным образом выбирает свой вариант с использованием библиотеки random.
        Мы сравниваем выборы и определяем победителя раунда.
        Ведется подсчет очков для пользователя и компьютера.
        Вывод итогов игры:
        Подводим итоги после всех раундов: выводим общий счет и объявляем победителя или ничью.
"""

import random


def select_variant():
    user_select = None
    while user_select not in CHOISES:
        user_select = input("Выбери (камень/ножницы/бумага): ")
        if user_select not in CHOISES:
            print("Некорректный выбор!!!")
    return user_select


def compute_game_result(user_choice: str, computer_choice: str):
    if user_choice == computer_choice:
        print("Ничья")
        return (0, 0)
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
        (user_choice == "ножницы" and computer_choice == "бумага") or \
            (user_choice == "бумага" and computer_choice == "камень"):
        print("Ты победил")
        return (1, 0)
    else:
        print("Ты проиграл")
        return (0, 1)


def print_result(user_res: int, computer_res: int):
    print("======= Итог Игры ========")
    print(f"Твой счет: {user_res}")
    print(f"Счет компьютера: {computer_res}")

    if user_res > computer_res:
        print("Ты победил в игре")
    elif user_res < computer_res:
        print("Компьютер победил в игре")
    else:
        print("Ничья")


CHOISES = ("камень", "ножницы", "бумага")
round_count = int(input("Сколько раундов будем играть? "))
user_score = 0
computer_score = 0

for r in range(1, round_count + 1):
    print(f"\nРаунд {r}")
    user_select = select_variant()
    computer_select = random.choice(CHOISES)
    print(f"Компьютер выбрал: {computer_select}")
    [user_mode, comp_mode] = compute_game_result(user_select, computer_select)
    user_score += user_mode
    computer_score += comp_mode

print_result(user_score, computer_score)
