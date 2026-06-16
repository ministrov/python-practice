"""
Микро-задача №2: is vs == и ссылки на объекты.
Запуск:  python 05_is_vs_equals_task.py
"""

# 1. ПРЕДСКАЗАНИЕ: что выведет? Сначала ПОДУМАЙ, потом раскомментируй и проверь.
print("=== Задание 1: int ===")
x = 100
y = 100
# Предсказание: x == y → True, x is y → True (интернирование маленьких чисел -5..256)
print(f"x == y: {x == y}")    # True (значения одинаковы)
print(f"x is y: {x is y}")    # True (объекты интернированы, один объект в памяти)


print("\n=== Задание 2: float ===")
f1 = 3.14
f2 = 3.14
# Предсказание: f1 == f2 → True, f1 is f2 → False (float не интернируется)
print(f"f1 == f2: {f1 == f2}")  # True (значения одинаковы)
print(f"f1 is f2: {f1 is f2}")  # False (разные объекты, интернирования нет)


print("\n=== Задание 3: список (ловушка!) ===")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(f"list_a == list_b: {list_a == list_b}")  # True (значения одинаковы)
print(f"list_a is list_b: {list_a is list_b}")  # False (разные объекты!)

# Теперь создадим ссылку:
list_c = list_a
print(f"list_c = list_a")
print(f"list_c is list_a: {list_c is list_a}")  # True (один объект!)

# И вот ловушка:
list_c[0] = 999
print(f"После list_c[0] = 999:")
print(f"list_a = {list_a}")  # [999, 2, 3] — изменился!
print(f"list_c = {list_c}")


print("\n=== Задание 4: None ===")
value = None
# Предсказание: оба True (None — синглтон, всегда один объект в памяти)
print(f"value is None: {value is None}")   # True (всегда используй `is None`)
print(f"value == None: {value == None}")   # True (работает, но не идиоматично)


print("\n=== Задание 5: Тест понимания ===")
x = [10, 20, 30]
y = [10, 20, 30]
z = x

print(f"x == y: {x == y}")  # True (значения одинаковы)
print(f"x is y: {x is y}")  # False (разные объекты в памяти)
print(f"x is z: {x is z}")  # True (z — это ссылка на x, один объект)
print(f"y is z: {y is z}")  # False (y — отдельный объект)


print("\n=== Задание 6: Почему это важно ===")
# Представь, что у тебя есть функция, которая получает список:
# def process(items):
#     items[0] = 0  # изменяем первый элемент
#
# Если ты вызовешь:
# my_list = [1, 2, 3]
# process(my_list)
#
# То my_list изменится на [0, 2, 3]!
# Это потому что функция получает ссылку на список, а не копию.
#
# Это не ошибка Python, это нормально. Просто нужно быть в курсе.
# TODO: подумай, когда это полезно, когда — ловушка?

print("\n=== Задание 6: Почему это важно ===")

def process(items): # type: ignore
    items[0] = 0

my_list = [1, 2, 3]
print(f"ДО функции: my_list = {my_list}")
process(my_list)
print(f"ПОСЛЕ функции: my_list = {my_list}")
print("Вывод: функция изменила ИСХОДНЫЙ список!")
