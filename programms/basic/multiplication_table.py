""" 
    Задача: с помощью цикла for создать таблицу умножения от 1 до 10
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

prices = [120, 45, 310, 75, 200, 55]
summary = 0
i = 0
while len(prices) > i:
    summary += prices[i]
    i += 1
print(summary)

print(list(range(5, 10, 2)))

names = ["Антон", "Вася", "Кейт"]
for name in names:
    print(f"Привет, {name}")
