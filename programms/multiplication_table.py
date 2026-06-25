""" 
    Задача: с помощью цикла for создать таблицу умножения от 1 до 10
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

for c in "Hi":
    print(c)

shopping_list = ["яблоки", "молоко", "хлеб", "сыр", "масло"]

for fruit in shopping_list:
    print(f"{fruit} \n")
