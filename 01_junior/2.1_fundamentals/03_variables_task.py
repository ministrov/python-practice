# -*- coding: utf-8 -*-
"""
Блок 2.1 — Тема 2а: Практика — Переменные
═════════════════════════════════════════════

6 ПРАКТИЧЕСКИХ ЗАДАНИЙ для самостоятельного решения.
Создавай переменные, меняй их, учись правильно их называть.
"""

print("=" * 70)
print("ЗАДАНИЕ 1: Создание и использование переменных")
print("=" * 70)
print("""
1.1 Создай переменную age со значением 25
    Выведи её на печать

1.2 Создай переменную name со строкой "Alice"
    Выведи её на печать

1.3 Создай переменную temperature со значением 36.6
    Выведи её на печать
""")

# ТВ КОД ЗДЕСЬ:
age = 25
name = "Alice"
temperature = 36.6
is_admin = True
print(age)
print(name)
print(temperature)
print(is_admin)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 2: Изменение значений переменных")
print("=" * 70)
print("""
2.1 Создай переменную count = 10
    Напечатай count

2.2 Измени count на 20
    Напечатай count

2.3 Увеличь count на 5 (используй count = count + 5)
    Напечатай count
""")

# ТВ КОД ЗДЕСЬ:
count = 10
count = 20
count = count + 5
print(count)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 3: Динамическое изменение типа данных")
print("=" * 70)
print("""
3.1 Создай переменную data и присвой ей число 42
    Выведи data и тип (используй type())

3.2 Присвой data строку "hello"
    Выведи data и тип

3.3 Присвой data список [1, 2, 3]
    Выведи data и тип

Объяви: Переменная может менять тип!
""")

# ТВ КОД ЗДЕСЬ:
data = 42
print(type(data))
print(data)
data = "hello"
print(type(data))
print(data)
data = [1, 2, 3, 4]
print(type(data))
print(data)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 4: Правила именования переменных")
print("=" * 70)
print("""
4.1 Какие из этих имён ПРАВИЛЬНЫЕ, какие НЕПРАВИЛЬНЫЕ?
    a) my_var       → ПРАВИЛЬНЫЕ
    b) 2variable    → НЕПРАВИЛЬНЫЕ
    c) my-var       → НЕПРАВИЛЬНЫЕ
    d) age_2024     → ПРАВИЛЬНЫЕ
    e) for          → НЕПРАВИЛЬНЫЕ
    f) student_name → ПРАВИЛЬНЫЕ

4.2 Создай переменные с ПРАВИЛЬНЫМИ именами:
    - переменную для возраста студента
    - переменную для номера класса
    - переменную для имени учителя

    Напечатай все три
""")

# ТВ КОД ЗДЕСЬ:
student_name = "Elise"
number_of_class = 3
name_of_teacher = "Victoria"

print(student_name)
print(number_of_class)
print(name_of_teacher)

print("\n" + "=" * 70)
print("ЗАДАНИЕ 5: Стили именования")
print("=" * 70)
print("""
5.1 Переименуй переменные в SNAKE_CASE (рекомендуемый стиль):
    myAge → my_age
    studentName → student_name
    maxValue → max_value

5.2 Создай переменные:
    - обычную переменную (snake_case)
    - константу (CAPS_LOCK)

    Напечатай обе
""")

# ТВ КОД ЗДЕСЬ:
user_profile_name = "Anton"
PROMOCODE = "MYPROMOCODE"

print(user_profile_name)
print(PROMOCODE)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 6: Множественное присвоение")
print("=" * 70)
print("""
6.1 Присвой несколько переменных одновременно:
    x = y = z = 100
    Напечатай все три

6.2 Присвой разные значения:
    a, b, c = 1, 2, 3
    Напечатай все три

6.3 Обмен значений:
    p = 10
    q = 20
    p, q = q, p  (поменяй местами)
    Напечатай p и q
""")

# ТВ КОД ЗДЕСЬ:
x = y = z = 100
print(x, y, z)
a, b, c = 1, 2, 3
print(a, b, c)
p = 10
q = 20
p, q = q, p
print(p, q)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 7: Арифметические операции с переменными")
print("=" * 70)
print("""
7.1 Создай переменные a = 15 и b = 3
    Напечатай результаты всех операций:
    - Сложение (a + b)
    - Вычитание (a - b)
    - Умножение (a * b)
    - Деление (a / b)
    - Целочисленное деление (a // b)
    - Остаток от деления (a % b)
""")

# ТВ КОД ЗДЕСЬ:
a = 15
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 8: Конкатенация строк")
print("=" * 70)
print("""
8.1 Создай переменные:
    first_name = "John"
    last_name = "Doe"

8.2 Объедини их в одну переменную full_name через пробел
    Напечатай результат

8.3 Создай приветствие:
    greeting = "Hello, " + full_name + "!"
    Напечатай greeting
""")

# ТВ КОД ЗДЕСЬ:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
greeting = "Hello, " + full_name + "!"
print(greeting)

print("\n" + "=" * 70)
print("ЗАДАНИЕ 9: Работа с индексами строк")
print("=" * 70)
print("""
9.1 Создай переменную word = "Python"
    Напечатай:
    - Первый символ (индекс 0)
    - Последний символ (индекс -1)
    - Подстроку с позиции 1 по 4 (слайс [1:4])

9.2 Выведи всю строку в обратном порядке (используй [::-1])
""")

# ТВ КОД ЗДЕСЬ:
word = "Python"
print(word[0])
print(word[-1])
print(word[1:4])
print(word[::-1])


print("\n" + "=" * 70)
print("ЗАДАНИЕ 10: Проверка типа переменной")
print("=" * 70)
print("""
10.1 Создай переменные разных типов:
    integer_var = 42
    float_var = 3.14
    string_var = "hello"
    list_var = [1, 2, 3]

10.2 Напечатай тип каждой переменной используя type()
    (Напечатай все 4 типа на отдельных строках)
""")

# ТВ КОД ЗДЕСЬ:
integer_var = 42
float_var = 3.14
string_var = "hello"
list_var = [1, 2, 3]
print(type(integer_var))
print(type(float_var))
print(type(string_var))
print(type(list_var))

print("\n" + "=" * 70)
print("ЗАДАНИЕ 11: Преобразование типов (Casting)")
print("=" * 70)
print("""
11.1 Создай переменную number = "123" (строка!)
     Преобразуй её в целое число используя int()
     Сохрани результат в переменную int_number
     Напечатай int_number и его тип

11.2 Создай переменную text = 456 (число!)
     Преобразуй её в строку используя str()
     Сохрани в переменную str_number
     Напечатай str_number и его тип

11.3 Создай переменную value = 7
     Преобразуй её в float и напечатай результат
""")

# ТВ КОД ЗДЕСЬ:
number = "123"
int_number = int(number)
print(int_number)
print(type(int_number))

text = 456
str_number = str(text)
print(str_number)
print(type(str_number))

value = 7
float_value = float(value)
print(float_value)
print(type(float_value))


print("\n" + "=" * 70)
print("ЗАДАНИЕ 12: Булевы переменные и логика")
print("=" * 70)
print("""
12.1 Создай переменные:
    is_student = True
    is_adult = False

12.2 Напечатай результаты логических операций:
    - is_student and is_adult
    - is_student or is_adult
    - not is_student

12.3 Напечатай результат сравнения: 10 > 5
""")

# ТВ КОД ЗДЕСЬ:
is_student = True
is_adult = False

print(is_student and is_adult)
print(is_student or is_adult)
print(not is_student)
print(10 > 5)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 13: F-строки для форматирования")
print("=" * 70)
print("""
13.1 Создай переменные:
    name = "Alice"
    age = 30
    city = "New York"

13.2 Используя f-string, напечатай одно предложение:
    Меня зовут {name}, мне {age} лет, я живу в {city}

13.3 Создай f-string с вычислением:
    price = 99.99
    quantity = 3
    Напечатай: Total: {price * quantity}
""")

# ТВ КОД ЗДЕСЬ:

name = "Alice"
age = 30
city = "New York"
print(f"Меня зовут {name}, мне {age} лет, я живу в {city}")

price = 99.99
quantity = 3
print(f"Total: {price * quantity}")

print("\n" + "=" * 70)
print("ЗАДАНИЕ 14: Функция len() для определения длины")
print("=" * 70)
print("""
14.1 Создай переменную text = "Programming"
     Напечатай её длину используя len()

14.2 Создай список numbers = [10, 20, 30, 40, 50]
     Напечатай количество элементов в списке

14.3 Создай пустой список empty_list = []
     Напечатай его длину

14.4 Создай переменную greeting = "Hello"
     Сравни её длину с 5 (напечатай результат len(greeting) == 5)
""")

# ТВ КОД ЗДЕСЬ:
text = "Programming"
print(len(text))

numbers = [10, 20, 30, 40, 50]
print(len(numbers))

empty_list: list[int] = []
print(len(empty_list))

greeting = "Hello"
print(len(greeting) == 5)

print("\n" + "=" * 70)
print("ЗАДАНИЕ 15: Работа с None")
print("=" * 70)
print("""
15.1 Создай переменную nothing = None
     Напечатай это значение и его тип

15.2 Создай две переменные:
    result = None
    message = "pending"

15.3 Используя условие if:
    Если result is None → напечатай "No result yet"
    Если message is None → напечатай "No message"

    (Напечатается только одна фраза, так как только result равен None)
""")

# ТВ КОД ЗДЕСЬ:

nothing = None
print(nothing)
print(type(nothing))

result: str | None = None
message: str | None = "pending"

if result is None:
  print("No result yet")

if message is None:  # type: ignore[reportUnnecessaryComparison]  # намеренно: message заведомо не None
  print("No message")

print("\n" + "=" * 70)
print("ЗАДАНИЕ 16: Комбинированная практика")
print("=" * 70)
print("""
16.1 Создай переменные профиля студента:
    student_name = "Emma"
    student_id = 2024001
    gpa = 4.5
    is_active = True
    courses = ["Math", "Physics", "Chemistry"]

16.2 Напечатай следующую информацию (отдельные строки):
    - Имя и ID в одной строке: "Emma - 2024001"
    - GPA и активность: "GPA: 4.5, Active: True"
    - Количество курсов (используй len())
    - Первый курс из списка (используй индекс [0])

16.3 Создай одну строку с f-string:
    "Student Emma (ID: 2024001) studies 3 courses"
    (используй переменные внутри {})
""")

# ТВ КОД ЗДЕСЬ:
student_name = "Emma"
student_id = 2024001
gpa = 4.5
is_active = True
courses = ["Math", "Physics", "Chemistry"]

student_info = f"""
    - Имя и ID в одной строке: "{student_name} - {student_id}"
    - GPA и активность: "GPA: {gpa}, Active: {is_active}"
    - Количество курсов ({len(courses)})
    - Первый курс из списка ({courses[0]})
 """

print(student_info)

student_str = f"Student {student_name} (ID: {student_id}) studies {len(courses)} courses"

print(student_str)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 17: Константы — базовое использование")
print("=" * 70)
print("""
17.1 Создай константы (CAPS_LOCK):
    PI = 3.14159
    GRAVITY = 9.8
    MAX_USERS = 1000

17.2 Напечатай каждую константу

17.3 Используя PI, вычисли длину окружности:
    radius = 10
    circumference = 2 * PI * radius
    Напечатай результат
""")

# ТВ КОД ЗДЕСЬ:
PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 1000

print(PI)
print(GRAVITY)
print(MAX_USERS)

radius = 10
circumference = 2 * PI * radius
print(circumference)


print("\n" + "=" * 70)
print("ЗАДАНИЕ 18: Константы в расчётах")
print("=" * 70)
print("""
18.1 Создай константы для расчёта стоимости:
    PRICE_PER_UNIT = 50.0  (цена за единицу)
    TAX_RATE = 0.15        (налог 15%)
    DISCOUNT = 0.1         (скидка 10%)

18.2 Переменные для заказа:
    quantity = 4   (количество товара)

18.3 Напечатай:
    - Стоимость без налогов: quantity * PRICE_PER_UNIT
    - Стоимость после скидки: quantity * PRICE_PER_UNIT * (1 - DISCOUNT)
    - Итоговая сумма с налогом:
      total = quantity * PRICE_PER_UNIT * (1 - DISCOUNT) * (1 + TAX_RATE)
""")

# ТВ КОД ЗДЕСЬ:
PRICE_PER_UNIT = 50.0
TAX_RATE = 0.15
DISCOUNT = 0.1
quantity = 4
total = 0

print(f"- Стоимость без налогов: {quantity * PRICE_PER_UNIT}")
print(f"- Стоимость после скидки: {quantity * PRICE_PER_UNIT * (1 - DISCOUNT)}")
print(f"- Итоговая сумма с налогом: {quantity * PRICE_PER_UNIT * (1 - DISCOUNT) * (1 + TAX_RATE)}")


print("\n" + "=" * 70)
print("ЗАДАНИЕ 19: Константы и их использование")
print("=" * 70)
print("""
19.1 Создай константы для приложения:
    APP_NAME = "MyStore"
    APP_VERSION = "1.0.0"
    MAX_ATTEMPTS = 5
    TIMEOUT_SECONDS = 30
    DATABASE_URL = "localhost:5432"

19.2 Создай переменные для сессии пользователя:
    user_name = "John"
    attempts = 3

19.3 Напечатай информацию:
    - Приложение: {APP_NAME} версия {APP_VERSION}
    - Пользователь: {user_name}
    - Попыток осталось: {MAX_ATTEMPTS - attempts}
    - Соединение: {DATABASE_URL}

    (Используй f-string для вывода)
""")

# ТВ КОД ЗДЕСЬ:

APP_NAME = "MyStore"
APP_VERSION = "1.0.0"
MAX_ATTEMPTS = 5
TIMEOUT_SECONDS = 30
DATABASE_URL = "localhost:5432"

user_name = "John"
attempts = 3

user_app_info = f"""
    - Приложение: {APP_NAME} версия {APP_VERSION}
    - Пользователь: {user_name}
    - Попыток осталось: {MAX_ATTEMPTS - attempts}
    - Соединение: {DATABASE_URL}
 """

print(user_app_info)

print("\n" + "=" * 70)
print("✅ КОГДА ЗАКОНЧИШЬ, ПРОВЕРЬ ВСЕ ЗАДАНИЯ!")
print("=" * 70)
