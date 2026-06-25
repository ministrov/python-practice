""" 
    Задача: с помощью цикла for создать таблицу умножения от 1 до 10
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
