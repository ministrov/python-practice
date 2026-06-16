""" Домашнее задание по теме операторы

    Задача: Калькулятор скидки. Спросить у пользователя цену товара. Спросить процент скидки. Посчитать и вывести цену со скидкой. - файл discount.py
"""
ask_user_price = int(input("Введите цену товара: "))
ask_user_sale_percent = int(input("Введите процент скидки: "))

final_price = ask_user_price - (1 * ask_user_sale_percent) / 100

print(final_price)