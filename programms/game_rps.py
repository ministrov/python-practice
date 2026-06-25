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

CHOISES = ("камень", "ножницы", "бумага")
round_count = int(input("Сколько раундов будем играть? "))
user_score = 0
computer_score = 0

for r in range(1, round_count + 1):
    print(f"\nРаунд {r}")
    user_select = input("Выбери (камень/ножницы/бумага): ")
    if user_select not in CHOISES:
        print("Некорректный выбор!!!")
        exit()
    computer_select = random.choice(CHOISES)
    print(f"Компьютер выбрал: {computer_select}")

    if user_select == computer_select:
        print("Ничья")
    elif (user_select == "камень" and computer_select == "ножницы") or \
        (user_select == "ножницы" and computer_select == "бумага") or \
            (user_select == "бумага" and computer_select == "камень"):
        print("Ты победил")
        user_score += 1
    else:
        print("Ты проиграл")
        computer_score += 1

print("======= Итог Игры ========")
print(f"Твой счет: {user_score}")
print(f"Счет компьютера: {computer_score}")

if user_score > computer_score:
    print("Ты победил в игре")
elif user_score < computer_score:
    print("Компьютер победил в игре")
else:
    print("Ничья")
print(random)
# numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# random_num = random.choice(numbers)

# evens: list[int] = []

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         evens = []

# print(random_num)
# print(evens)
