"""
ДЕМО: Циклы — for, while, break, continue, else
Python 3.10+

Что это: способ повторить код несколько раз.
for — когда заранее знаешь, сколько повторений (список, диапазон)
while — когда повторяешь, пока выполнено условие

Правило: Python выполняет тело цикла столько раз, сколько нужно.
Запусти файл: python 11_loops_demo.py
"""

print("=" * 55)
print("1) БАЗА: for с range()")
print("=" * 55)

# range(n) — от 0 до n-1
for i in range(5):
    print(f"Итерация {i}")

# range(start, stop) — от start до stop-1
print("\nОт 2 до 5:")
for i in range(2, 5):
    print(i)

# range(start, stop, step) — с шагом
print("\nОт 0 до 10 с шагом 2:")
for i in range(0, 10, 2):
    print(i)


print("\n" + "=" * 55)
print("2) ИТЕРАЦИЯ ПО СПИСКУ")
print("=" * 55)

fruits = ["яблоко", "груша", "банан"]
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# Если нужен индекс — используй enumerate
print("\nС индексами:")
for idx, fruit in enumerate(fruits):
    print(f"[{idx}] {fruit}")


print("\n" + "=" * 55)
print("3) zip — две последовательности одновременно")
print("=" * 55)

names = ["Алиса", "Боб", "Виктор"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name}: {age} лет")

# zip останавливается на самой короткой последовательности
print("\nЕсли длины разные:")
for name, age in zip(names, [25, 30]):  # ages короче
    print(f"{name}: {age}")  # Виктор не поднимется


print("\n" + "=" * 55)
print("4) while — цикл по условию")
print("=" * 55)

count = 0
while count < 3:
    print(f"count = {count}")
    count += 1

print("Цикл завершился\n")

# while с условием — реальный пример (поиск числа)
number = 0
target = 5
while number != target:
    print(f"Ищу число {target}, текущее: {number}")
    number += 1
print(f"Нашел! number = {number}")


print("\n" + "=" * 55)
print("5) break — выход из цикла")
print("=" * 55)

for i in range(10):
    if i == 3:
        print(f"Нашли 3, выходим!")
        break  # Выход из цикла
    print(i)

print("(После break цикл завершился)\n")


print("=" * 55)
print("6) continue — перейти к следующей итерации")
print("=" * 55)

for i in range(5):
    if i == 2:
        print(f"Пропускаем 2")
        continue  # Перейти к следующей итерации
    print(f"Число {i}")

print("(continue пропустил только i=2, остальное выполнилось)\n")


print("=" * 55)
print("7) else в цикле — выполняется, если цикл завершился нормально")
print("=" * 55)

# Если цикл закончился без break — сработает else
print("Цикл БЕЗ break:")
for i in range(3):
    print(i)
else:
    print("=> Цикл закончился нормально (без break)")

print("\nЦикл С break:")
for i in range(5):
    if i == 2:
        print("Нашли 2, выходим через break")
        break
    print(i)
else:
    print("=> Этот else НЕ выполнится, потому что был break")

print("\nwhile с else:")
x = 0
while x < 3:
    print(f"x = {x}")
    x += 1
else:
    print("=> while закончился нормально")


print("\n" + "=" * 55)
print("8) ВЛОЖЕННЫЕ ЦИКЛЫ (nested loops)")
print("=" * 55)

# Таблица умножения 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j}", end="  ")
    print()  # Новая строка

print("\n" + "=" * 55)
print("ИТОГ: когда что использовать?")
print("=" * 55)
print("""
[OK] for с range(n)     — когда повторяешь n раз
[OK] for с for x in lst — когда проходишь по списку
[OK] enumerate(lst)     — когда нужны и значение, и индекс
[OK] zip(lst1, lst2)    — когда нужно связать две последовательности
[OK] while условие      — когда повторяешь ДО ТЕХ ПОР, ПОКА верно условие
[OK] break              — выход из цикла раньше (часто в while)
[OK] continue           — пропустить текущую итерацию, перейти к следующей
[OK] else в цикле       — выполнится, если цикл завершился без break
""")
