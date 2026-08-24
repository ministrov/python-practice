# -*- coding: utf-8 -*-
"""
Блок 2.8.1: Практика — основы SQL (SELECT/WHERE/JOIN/GROUP BY/ORDER BY/LIMIT)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Домен: интернет-магазин — categories (категории) и products (товары).

ВАЖНО: задание 1 создаёт connection/cursor и заполняет таблицы — все
следующие задания используют ЭТИ ЖЕ connection/cursor (не создавай новые
подключения в других заданиях).

Совет: посмотри 01_sql_basics_demo.py, если застрял — но там другой
домен (employees/departments), просто скопировать не получится.
"""

import sqlite3

print("=" * 60)
print("ЗАДАНИЕ 1: Схема и данные")
print("=" * 60)
print("""
1.1 Создай connection = sqlite3.connect(":memory:") и
    cursor = connection.cursor().
1.2 Создай таблицу categories(id INTEGER PRIMARY KEY, name TEXT NOT NULL).
1.3 Создай таблицу products(id INTEGER PRIMARY KEY, name TEXT NOT NULL,
    price REAL NOT NULL, category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)).
1.4 Наполни categories минимум 3 строками — одна из категорий должна
    остаться БЕЗ единого товара (понадобится в задании 5).
1.5 Наполни products минимум 5 строками с разными ценами — один товар
    должен иметь category_id = NULL (понадобится в задании 4).
1.6 Сделай connection.commit().
""")

# ТВОЙ КОД ЗДЕСЬ:
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")

cursor.executemany(
    "INSERT INTO categories (id, name) VALUES (?, ?)",
    [
        (1, "Электроника"),
        (2, "Книги"),
        (3, "Спорттовары")
    ]
)

cursor.executemany(
    "INSERT INTO products (id, name, price, category_id) VALUES (?, ?, ?, ?)",
    [
        (1, "Ноутбук", 79990.0, 1),
        (2, "Смартфон", 45990.0, 1),
        (3, "Python для начинающих", 1290.0, 2),
        (4, "Чистый код", 990.0, 2),
        (5, "Мышь беспроводная", 990.0, None),
    ],
)

connection.commit()

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: SELECT + WHERE")
print("=" * 60)
print("""
2.1 Выбери name и price из products, где price больше выбранного тобой
    порога (например, 500).
2.2 Выполни запрос через cursor.execute(...), напечатай
    cursor.fetchall().
""")

# ТВОЙ КОД ЗДЕСЬ:

cursor.execute("SELECT name, price FROM products WHERE price > 1500")
print(cursor.fetchall())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: ORDER BY + LIMIT")
print("=" * 60)
print("""
3.1 Выбери name и price трёх самых дорогих товаров, отсортированных по
    убыванию цены (ORDER BY ... DESC LIMIT 3).
3.2 Напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:
cursor.execute("SELECT name, price FROM products ORDER BY price DESC LIMIT 3")
print(cursor.fetchall())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: INNER JOIN")
print("=" * 60)
print("""
4.1 Выбери name товара и name его категории — только для товаров, у
    которых ЕСТЬ категория (INNER JOIN products и categories по
    products.category_id = categories.id).
4.2 Товар с category_id = NULL из задания 1.5 сюда попасть НЕ должен.
    Напечатай результат и отдельно — сколько всего строк вернулось
    (len(...)), сравни с общим количеством товаров.
""")

# ТВОЙ КОД ЗДЕСЬ:
cursor.execute("""
    SELECT products.name, categories.name
    FROM products
    INNER JOIN categories ON products.category_id = categories.id
""")

result = cursor.fetchall()
print(result)
print(f"Строк с категорией: {len(result)}")
cursor.execute("SELECT COUNT(*) FROM products")
total = cursor.fetchone()[0]
print(f"Всего товаров: {total}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: LEFT JOIN")
print("=" * 60)
print("""
5.1 Выбери name категории и name товара для ВСЕХ категорий, включая
    категорию без товаров из задания 1.4 (LEFT JOIN: FROM categories
    LEFT JOIN products ON products.category_id = categories.id).
5.2 Напечатай весь результат. Для категории без товаров name товара
    должен прийти как None — найди эту строку в выводе.
""")

# ТВОЙ КОД ЗДЕСЬ:

cursor.execute("""
    SELECT categories.name, products.name
    FROM categories
    LEFT JOIN products ON products.category_id = categories.id
""")

result = cursor.fetchall()
for row in result:
    print(row)

# отдельно найдём строку(и), где товара нет
print("\nКатегории без товаров:")
for row in result:
    category_name, product_name = row
    if product_name is None:
        print(f"  {category_name} — товаров нет")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: GROUP BY + агрегаты")
print("=" * 60)
print("""
6.1 Посчитай среднюю цену (AVG) и количество товаров (COUNT) в каждой
    категории, у которой есть хотя бы один товар — JOIN products и
    categories, GROUP BY categories.name.
6.2 Напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:
cursor.execute("""
    SELECT categories.name,
           AVG(products.price) AS avg_price,
           COUNT(products.id) AS product_count
    FROM products
    JOIN categories ON products.category_id = categories.id
    GROUP BY categories.name
""")

result = cursor.fetchall()
for row in result:
    category_name, avg_price, product_count = row
    print(f"{category_name}: средняя цена = {avg_price:.2f}, товаров = {product_count}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Комплексный запрос")
print("=" * 60)
print("""
7.1 Одним запросом: name товара + name его категории, только для
    товаров с ценой выше выбранного тобой порога, отсортировано по
    цене по убыванию, не больше 2 строк — JOIN + WHERE + ORDER BY +
    LIMIT вместе.
7.2 Напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:
price_threshold = 1000

cursor.execute("""
    SELECT products.name, categories.name, products.price
    FROM products
    JOIN categories ON products.category_id = categories.id
    WHERE products.price > ?
    ORDER BY products.price DESC
    LIMIT 2
""", (price_threshold,))

result = cursor.fetchall()
for row in result:
    product_name, category_name, price = row
    print(f"{product_name} ({category_name}): {price}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Нормализация (без кода, письменный ответ)")
print("=" * 60)
print("""
8.1 Представь, что вместо category_id в products хранили бы сразу
    category_name текстом, продублированным в каждой строке товара.
    Какое правило нормализации (1NF/2NF/3NF) это нарушает и почему?
    Что произойдёт, если категорию потребуется переименовать?
    Напиши ответ ниже прямо в комментарии.
""")

# ТВОЙ ОТВЕТ ЗДЕСЬ (в комментарии):
# Это нарушает 3НФ, так как category_name транзитивно зависит от
# category (а не от products.id напрямую) и дублируется в каждой строке.
# При переименовании категории пришлось бы обновлять все строки
# products с этим именем — иначе часть строк останется со старым
# названием (аномалия обновления).
