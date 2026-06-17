""" Домашнее задание по теме управление потоком

    Задача: Спросить у пользователя категорию: «напиток», «суп», «десерт».
        В зависимости от выбора — предложить варианты (например:
            • напиток → «чай», «кофе», «сок»
            • суп → «борщ», «щи», «суп-пюре»
            • десерт → «торт», «мороженое», «фрукты»).

    Пользователь вводит конкретное блюдо.
    Программа с помощью match case выводит цену выбранного блюда.
"""

user_input = input("Введите блюдо: ")
meal = user_input
meal_price = 0

if meal == "напиток":
    user_input = input("Выберите напиток (чай, кофе, сок): ")
    match user_input:
        case "чай":
            meal_price = 120
            print(f"Цена выбранного блюда: {meal_price}")
        case "кофе":
            meal_price = 145
            print(f"Цена выбранного блюда: {meal_price}")
        case "сок":
            meal_price = 234
            print(f"Цена выбранного блюда: {meal_price}")
        case _:
            print("Такого напитка нет")

if meal == "суп":
    user_input = input("Выберите суп (борщ, щи, суп-пюре): ")
    match user_input:
        case "борщ":
            meal_price = 220
            print(f"Цена выбранного блюда: {meal_price}")
        case "щи":
            meal_price = 245
            print(f"Цена выбранного блюда: {meal_price}")
        case "суп-пюре":
            meal_price = 250
            print(f"Цена выбранного блюда: {meal_price}")
        case _:
            print("Такого супа нет")

if meal == "десерт":
    user_input = input("Выберите десерт (торт, мороженое, фрукты): ")
    match user_input:
        case "торт":
            meal_price = 250
            print(f"Цена выбранного блюда: {meal_price}")
        case "мороженое":
            meal_price = 300
            print(f"Цена выбранного блюда: {meal_price}")
        case "фрукты":
            meal_price = 350
            print(f"Цена выбранного блюда: {meal_price}")
        case _:
            print("Такого десерта нет")
