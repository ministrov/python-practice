""" Домашнее задание по теме операторы

    Задача: Ввести три траты: еда, транспорт, развлечения. Вывести общую сумму и среднее - файл expences.py
"""

MAX_VALUE = 3

food = float(input("Еда: "))
transport = float(input("Транспорт: "))
entertainment = float(input("Развлечения: "))

overall_sum = food + transport + entertainment
average = overall_sum // MAX_VALUE

print(overall_sum)
print(average)