# Продвинутые функции в Python

## Предварительно
Прежде чем изучать эту часть, убедись что хорошо понимаешь основы из `basics_guide.md`

## 1. Переменное количество параметров

### *args (переменное количество позиционных аргументов)
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4)  # 10
sum_all(10, 20)      # 30
```

### **kwargs (переменное количество именованных аргументов)
```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# Вывод:
# name: Alice
# age: 30
# city: NYC
```

### Сочетание всех типов
```python
def complex_function(a, b=10, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

complex_function(1, 2, 3, 4, name="Alice", age=30)
# Вывод:
# a = 1
# b = 2
# args = (3, 4)
# kwargs = {'name': 'Alice', 'age': 30}
```

## 2. Декораторы

Функция, которая изменяет или расширяет другую функцию:

### Простой декоратор
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Привет!")

say_hello()
# Вывод:
# До вызова функции
# Привет!
# После вызова функции
```

### Декоратор с параметрами
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Привет!")

say_hello()
# Выведет "Привет!" три раза
```

### Декоратор для отслеживания времени
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция выполнилась за {end - start:.4f} секунд")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "готово"
```

## 3. Замыкания (Closures)

Внутренняя функция имеет доступ к переменным внешней функции:

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3))  # 8

add_10 = outer(10)
print(add_10(3))  # 13
```

### Практический пример: Счётчик
```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## 4. Функции высшего порядка

### Функция, которая возвращает функцию
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier(3)
print(times_3(5))  # 15
print(times_3(10))  # 30
```

### Функция, которая принимает функцию
```python
def apply_twice(func, x):
    return func(func(x))

def add_one(x):
    return x + 1

print(apply_twice(add_one, 5))  # 7
```

### Композиция функций
```python
def compose(f, g):
    return lambda x: f(g(x))

square = lambda x: x ** 2
add_one = lambda x: x + 1

# Сначала add_one, потом square
f = compose(square, add_one)
print(f(3))  # (3+1)^2 = 16
```

## 5. Встроенные функции высшего порядка

### reduce() — свернуть список в одно значение
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Эквивалентно: 1 * 2 * 3 * 4 * 5
```

### min() и max() с key параметром
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
best = max(students, key=lambda x: x[1])
print(best)  # ("Bob", 92)
```

## 6. Генераторы

Функции, которые выдают значения по одному через `yield`:

### Простой генератор
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)
# Вывод: 1, 2, 3, 4, 5
```

### Генератор Фибоначчи
```python
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)
# Вывод: 0, 1, 1, 2, 3, 5, 8
```

### Преимущества генераторов
```python
# Обычный способ (использует памяти для всех чисел)
def range_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

# Генератор (использует память только для одного числа)
def range_generator(n):
    for i in range(n):
        yield i
```

## 7. Кэширование (Memoization)

Сохранение результатов для избежания повторных вычислений:

### Ручное кэширование
```python
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    
    cache[n] = result
    return result
```

### Использование декоратора functools.lru_cache
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # очень быстро
```

## 8. Частичное применение (Partial Application)

Создание новой функции с фиксированными параметрами:

```python
from functools import partial

def multiply(a, b):
    return a * b

times_3 = partial(multiply, 3)
print(times_3(5))  # 15
print(times_3(10))  # 30
```

## 9. Распаковка аргументов

### Распаковка позиционных аргументов
```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6
```

### Распаковка именованных аргументов
```python
def greet(name, age, city):
    print(f"{name}, {age}, {city}")

info = {"name": "Alice", "age": 30, "city": "NYC"}
greet(**info)  # Alice, 30, NYC
```

## 10. Контекстные менеджеры и with

Управление ресурсами (файлы, соединения БД):

```python
# Открытие файла
with open("file.txt") as f:
    content = f.read()
# Файл автоматически закроется

# Создание собственного контекстного менеджера
class MyContext:
    def __enter__(self):
        print("Входим в контекст")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выходим из контекста")

with MyContext() as ctx:
    print("Внутри контекста")
```

## 11. Асинхронные функции (async/await)

Для работы с асинхронным кодом:

```python
import asyncio

async def fetch_data():
    print("Начинаем загрузку...")
    await asyncio.sleep(2)
    print("Загрузка завершена")
    return "данные"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

## 12. Сложные примеры

### Pipeline - цепочка операций
```python
def pipeline(value, *funcs):
    for func in funcs:
        value = func(value)
    return value

result = pipeline(
    5,
    lambda x: x * 2,    # 10
    lambda x: x + 3,    # 13
    lambda x: x ** 2    # 169
)
print(result)  # 169
```

### Валидация с функциями
```python
def validate_email(email: str) -> bool:
    return "@" in email and "." in email

def validate_password(password: str) -> bool:
    return len(password) >= 8

def validate_user(email: str, password: str) -> bool:
    validators = [
        (validate_email, email, "Email невалидный"),
        (validate_password, password, "Пароль слишком короткий")
    ]
    
    for validator, value, error_msg in validators:
        if not validator(value):
            print(error_msg)
            return False
    return True
```

## 13. Лучшие практики для продвинутых техник

1. **Декораторы** — используй для логирования, кэширования, проверки прав
2. **Генераторы** — для больших наборов данных, экономии памяти
3. **Замыкания** — для создания приватных переменных, факторий функций
4. **Функции высшего порядка** — для функционального стиля программирования
5. **Type hints** — обязательно типизируй продвинутые функции
6. **Документация** — особенно важна для сложных функций
7. **Избегай излишней сложности** — простой код лучше чем сложный и умный
