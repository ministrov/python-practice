# -*- coding: utf-8 -*-
"""
Блок 2.2.6: Практика — Выбор структуры данных
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ: выбери правильную структуру и реши задачу.
Совет: посмотри 11_choosing_structures_demo.py если застрял.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: Дедупликация")
print("=" * 60)
print("""
Дан список с повторяющимися email-адресами:
  emails = ["a@mail.ru", "b@mail.ru", "a@mail.ru", "c@mail.ru", "b@mail.ru"]

1.1 Убери дубли и выведи уникальные адреса (используй set)
1.2 Выведи количество уникальных адресов
1.3 Проверь, есть ли "d@mail.ru" среди уникальных
""")

# ТВОЙ КОД ЗДЕСЬ:
unique_emails = set(
    ["a@mail.ru", "b@mail.ru", "a@mail.ru", "c@mail.ru", "b@mail.ru"])
for address in unique_emails:
    print(address)
print(len(unique_emails))
print("d@mail.ru" in unique_emails)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Подсчёт частоты")
print("=" * 60)
print("""
Дан список оценок: [5, 3, 4, 5, 3, 5, 4, 2, 3, 5]

2.1 Подсчитай, сколько раз встречается каждая оценка (используй dict)
    Ожидаемый результат: {5: 4, 3: 3, 4: 2, 2: 1}

2.2 Выведи самую частую оценку
    Подсказка: max(d, key=d.get)
""")

# ТВОЙ КОД ЗДЕСЬ:
grades = [5, 3, 4, 5, 3, 5, 4, 2, 3, 5]
counts = {}
for grade in grades:  # type: ignore
    counts[grade] = counts.get(grade, 0) + 1  # type: ignore
print(counts)  # type: ignore

most_common = max(counts, key=counts.get)  # type: ignore
print(most_common)  # type: ignore

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Фиксированная запись")
print("=" * 60)
print("""
3.1 Создай tuple для описания сервера: (хост, порт, протокол)
    Например: ("localhost", 8080, "http")
    Выведи хост и порт отдельно (распаковка)

3.2 Создай список из 3 серверов (список кортежей)
    Выведи порт каждого сервера через цикл
""")

# ТВОЙ КОД ЗДЕСЬ:
server = ("localhost", 8080, "http")
host, port, protocol = server
print(host)
print(port)

servers = [
    ("localhost", 8080, "http"),
    ("example.com", 443, "https"),
    ("10.0.0.1", 22, "ssh"),
]

for host, port, protocol in servers:
    print(port)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Пересечение множеств")
print("=" * 60)
print("""
Два класса:
  class_a = {"Alice", "Bob", "Charlie", "Diana"}
  class_b = {"Bob", "Eve", "Charlie", "Frank"}

4.1 Найди студентов, которые есть в ОБОИХ классах
4.2 Найди студентов ТОЛЬКО в классе A (нет в B)
4.3 Найди всех уникальных студентов из обоих классов
""")

# ТВОЙ КОД ЗДЕСЬ:
class_a = {"Alice", "Bob", "Charlie", "Diana"}
class_b = {"Bob", "Eve", "Charlie", "Frank"}

both = class_a & class_b
print(both)

only_a = class_a - class_b
print(only_a)

everyone = class_a | class_b
print(everyone)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Словарь как база данных")
print("=" * 60)
print("""
5.1 Создай словарь из 3 товаров: {название: цена}
    Например: {"яблоко": 50, "банан": 30, "апельсин": 80}

5.2 Выведи все товары дороже 40 рублей (dict comprehension)

5.3 Добавь новый товар "груша" за 60 рублей
    Выведи итоговый словарь
""")

# ТВОЙ КОД ЗДЕСЬ:
products = {"яблоко": 50, "банан": 30, "апельсин": 80}
print(products)

expensive = {name: price for name, price in products.items() if price > 40}
# {"яблоко": 50, "апельсин": 80}
print(expensive)

products["груша"] = 60
print(products)
# {"яблоко": 50, "банан": 30, "апельсин": 80, "груша": 60}
print(products)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Список для упорядоченных данных")
print("=" * 60)
print("""
6.1 Создай список из 5 задач (строки)
    Добавь новую задачу в конец через append()
    Выведи первую и последнюю задачу

6.2 Отсортируй задачи по алфавиту и выведи
    (используй sorted(), не sort() — чтобы не менять оригинал)

6.3 Выведи только задачи длиннее 5 символов (list comprehension)
""")

# ТВОЙ КОД ЗДЕСЬ:
tasks = ["купить хлеб", "помыть посуду",
         "написать код", "позвонить маме", "сделать зарядку"]
tasks.append("прочитать книгу")
print(tasks[0])   # первая — купить хлеб
print(tasks[-1])  # последняя — прочитать книгу

sorted_tasks = sorted(tasks)
print(sorted_tasks)
print(tasks)  # остался в исходном порядке

long_tasks = [t for t in tasks if len(t) > 5]
print(long_tasks)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Правильный выбор структуры")
print("=" * 60)
print("""
Для каждой ситуации выбери структуру и напиши код:

7.1 Хранить историю сообщений в чате (порядок важен, могут повторяться)
    Создай и добавь 3 сообщения

7.2 Хранить настройки приложения (ключ -> значение)
    Создай словарь с ключами: "theme", "language", "font_size"

7.3 Хранить список заблокированных пользователей (быстрая проверка)
    Создай set и проверь, заблокирован ли пользователь "alice"
""")

# ТВОЙ КОД ЗДЕСЬ:
chat_history: list[str] = []
chat_history.append("Привет!")
chat_history.append("Как дела?")
chat_history.append("Привет!")  # повтор допустим
print(chat_history)

settings_2: dict[str, str | int] = {
    "theme": "dark",
    "language": "ru",
    "font_size": 14,
}
print(settings_2)

blocked = {"bob", "eve", "mallory"}
print("alice" in blocked)  # False

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексная задача")
print("=" * 60)
print("""
Дан список покупок с повторениями:
  shopping = ["молоко", "хлеб", "молоко", "яйца", "хлеб", "масло", "яйца", "яйца"]

8.1 Подсчитай количество каждого товара (dict)
    Ожидаемый результат: {"молоко": 2, "хлеб": 2, "яйца": 3, "масло": 1}

8.2 Найди товары, которые нужно купить больше 1 раза (dict comprehension)

8.3 Выведи уникальный список товаров в алфавитном порядке (set -> sorted list)
""")

# ТВОЙ КОД ЗДЕСЬ:
shopping = ["молоко", "хлеб", "молоко",
            "яйца", "хлеб", "масло", "яйца", "яйца"]

counts: dict[str, int] = {}
for item in shopping:
    counts[item] = counts.get(item, 0) + 1
# {"молоко": 2, "хлеб": 2, "яйца": 3, "масло": 1}
print(counts)

more_than_one = {item: n for item, n in counts.items() if n > 1}
# {"молоко": 2, "хлеб": 2, "яйца": 3}
print(more_than_one)

unique_sorted = sorted(set(shopping))
# ["масло", "молоко", "хлеб", "яйца"]
print(unique_sorted)

print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
