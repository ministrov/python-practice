# -*- coding: utf-8 -*-
"""
Блок 2.2.1: Практика со списками (list)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Напиши свой код и выведи результаты.

Совет: Если застрял — посмотри 01_list_demo.py, но старайся решить сам.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: Создание и индексирование")
print("=" * 60)
print("""
1.1 Создай список с 5 фруктами
    Напечатай первый элемент (индекс 0)
    Напечатай последний элемент (индекс -1)

1.2 Создай список [10, 20, 30, 40, 50]
    Напечатай элемент с индексом 2
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:

fruits: list[str] = ["apple", "banana", "cherry", "pomegranate", "orange"]
print(fruits[0])
print(fruits[-1])

numbers: list[int] = [10, 20, 30, 40, 50]
print(numbers[1])


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Срезы (slicing)")
print("=" * 60)
print("""
2.1 Создай список [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Получи срез [3, 4, 5] (элементы с индексом 2 до 5)

2.2 Из того же списка получи первые 3 элемента

2.3 Получи последние 2 элемента

2.4 Разверни весь список (от конца к началу)
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
integers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_int: list[int] = integers[2:5]
first_three_elements: list[int] = integers[:3]
last_two_elements: list[int] = integers[2:]
reversed_int: list[int] = integers[::-1]

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Методы append(), insert(), remove()")
print("=" * 60)
print("""
3.1 Создай список цветов: ["red", "green"]
    Добавь "blue" в конец (append)

3.2 Вставь "yellow" на позицию 1 (insert)

3.3 Удали "green" из списка (remove)

Выведи финальный список.
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:

colors: list[str] = ["red", "green"]
colors.append("blue")
colors.insert(1, "yellow")
colors.remove("green")

print(colors)


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Методы pop(), extend(), clear()")
print("=" * 60)
print("""
4.1 Создай список ["A", "B", "C", "D"]
    Удали последний элемент через pop()
    Выведи, что было удалено и что осталось

4.2 Создай два списка и объедини их через extend()
    list1 = [1, 2, 3]
    list2 = [4, 5]
    Выведи list1 после extend

4.3 Создай список и очисти его через clear()
    Выведи пустой список
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
letters: list[str] = ["A", "B", "C", "D"]
last_element: str = letters.pop()
print(last_element)
print(letters)

list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]
list1.extend(list2)
print(list1)

list_example: list[int] = [3, 4, 5, 6, 7]
list_example.clear()

print(list_example)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: len(), count(), index()")
print("=" * 60)
print("""
5.1 Создай список [10, 20, 30, 40]
    Найди его длину (len)

5.2 Создай список [1, 2, 2, 3, 2, 4, 2]
    Подсчитай, сколько раз встречается число 2 (count)

5.3 Из того же списка найди индекс первого вхождения числа 2 (index)
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:

list_of_numbers: list[int] = [10, 20, 30, 40]
print(len(list_of_numbers))
list_of_numbers_2: list[int] = [1, 2, 2, 3, 2, 4, 2]
count_two: int = list_of_numbers_2.count(2)
print(count_two)
print(list_of_numbers_2.index(2))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Сортировка")
print("=" * 60)
print("""
6.1 Создай список [5, 2, 9, 1, 7]
    Отсортируй его на месте (sort)
    Выведи отсортированный список

6.2 Отсортируй список в обратном порядке (sort с reverse=True)

6.3 Создай новый список и используй sorted()
    (исходный список не должен изменться)
    Выведи оба списка
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
int_numbers: list[int] = [5, 2, 9, 1, 7]
sorted_list: None = int_numbers.sort()
print(sorted_list)
reversed_list: None = int_numbers.sort(reverse=True)
print(reversed_int)
new_int_nubers: list[int] = sorted(int_numbers)
print(new_int_nubers)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Проверка принадлежности (in)")
print("=" * 60)
print("""
7.1 Создай список с именами: ["Alice", "Bob", "Charlie"]
    Проверь, есть ли "Alice" в списке (in)
    Проверь, есть ли "Diana" в списке

Выведи оба результата.
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
names: list[str] = ["Alice", "Bob", "Charlie"]
has_alice: bool = "Alice" in names
print(has_alice)
has_dima: bool = "Dima" in names
print(has_dima)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Итерация и изменяемость")
print("=" * 60)
print("""
8.1 Создай список [1, 2, 3]
    Напечатай все элементы через цикл for

8.2 Напечатай элементы с индексом (используй enumerate)

8.3 Создай список list_a = [1, 2, 3]
    Присвой list_b = list_a
    Добавь в list_a число 4 (append)
    Выведи list_a и list_b

    Вопрос: Почему list_b тоже изменилась?

8.4 Создай копию списка:
    list_c = [1, 2, 3]
    list_d = list(list_c)  # или list_d = list_c[:]
    Добавь в list_c число 4
    Выведи list_c и list_d

    Вопрос: На этот раз list_d изменилась или нет? Почему?
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
one_two_three_list: list[int] = [1, 2, 3]
for i in one_two_three_list:
    print(f"Elements: {i}")

for inx, j in enumerate(one_two_three_list):
    print(f"Index: {inx} of Element {j}")

list_a: list[int] = [1, 2, 3]
list_b: list[int] = list_a
print(list_a == list_b)
print(list_a is list_b)
list_a.append(4)
print(list_a)
print(list_b)

copy_of_list_a: list[int] = list(list_a)
copy_of_list_a.append(6)
print(copy_of_list_a)

print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
