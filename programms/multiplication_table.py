""" 
    Задача: с помощью цикла for создать таблицу умножения от 1 до 10
"""

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i*j:4}", end="")
#     print()

# for c in "Hi":
#     print(c)

# shopping_list = ["яблоки", "молоко", "хлеб", "сыр", "масло"]

# for fruit in shopping_list:
#     print(f"{fruit} \n")

numbers: list[int] = [3, 8, 5, 12, 7, 4, 11, 6]
result: list[int] = []

# Ваш код здесь
for number in numbers:
    if number % 2 == 1:
        continue
    else:
        result.append(number)
        for num in result:
            print(num)
