# Основы функций в Python

## 1. Что такое функция?
Функция — это переиспользуемый блок кода, который выполняет определённую задачу.

## 2. Определение функции
```python
def имя_функции(параметры):
    """Документация функции"""
    # тело функции
    return результат
```

## 3. Основные компоненты

### Параметры и аргументы
- **Параметры** — переменные в определении функции
- **Аргументы** — значения, которые вы передаёте при вызове

```python
def greet(name):  # name — параметр
    return f"Hello, {name}!"

greet("Alice")  # "Alice" — аргумент
```

## 4. Типы параметров

### Позиционные аргументы
```python
def add(a, b):
    return a + b

add(5, 3)  # порядок важен
```

### Именованные аргументы
```python
add(b=3, a=5)  # порядок не важен
```

### Параметры по умолчанию
```python
def greet(name="Guest"):
    return f"Hello, {name}!"

greet()       # "Hello, Guest!"
greet("Bob")  # "Hello, Bob!"
```

## 5. Return (Возврат значений)

### Одно значение
```python
def double(x):
    return x * 2
```

### Несколько значений (кортеж)
```python
def get_coordinates():
    return 10, 20

x, y = get_coordinates()  # распаковка
```

### Без return (None)
```python
def greet(name):
    print(f"Hi, {name}!")
    # неявно return None
```

## 6. Область видимости (Scope)

### Локальная переменная
```python
def func():
    x = 5  # локальная переменная
    print(x)

func()  # 5
print(x)  # ошибка: x не определена
```

### Глобальная переменная
```python
x = 10  # глобальная

def func():
    print(x)  # может читать глобальную переменную

func()  # 10
```

### Ключевое слово global
```python
x = 10

def func():
    global x
    x = 20  # изменяет глобальную переменную

func()
print(x)  # 20
```

## 7. Документация (Docstring)

```python
def calculate(a, b):
    """
    Складывает два числа.
    
    Args:
        a (int): первое число
        b (int): второе число
    
    Returns:
        int: сумма двух чисел
    """
    return a + b

print(calculate.__doc__)  # выведет документацию
help(calculate)  # выведет справку
```

## 8. Типизация (Type Hints)

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## 9. Лямбда-функции (Anonymous Functions)

Короткие функции в одну строку:

```python
# Обычная функция
def double(x):
    return x * 2

# Лямбда-функция
double = lambda x: x * 2

# Часто используется с map, filter, sorted
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8]
```

## 10. Встроенные функции для работы с функциями

### map() — применить функцию к каждому элементу
```python
numbers = [1, 2, 3]
squared = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9]
```

### filter() — отфильтровать элементы
```python
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### sorted() — сортировка с функцией
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])  # по оценкам
```

## 11. Рекурсия

Функция, которая вызывает сама себя:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## 12. Практические примеры

### Проверка палиндрома
```python
def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]
```

### Поиск максимума в списке
```python
def find_max(numbers: list) -> int:
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num
```

### Подсчёт количества слов
```python
def count_words(text: str) -> int:
    return len(text.split())
```

### Инвертирование словаря
```python
def invert_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}
```

## 13. Лучшие практики

1. **Называйте функции понятно**: `calculate_average()`, не `calc()`
2. **Одна функция — одна задача**: принцип единственной ответственности
3. **Используйте docstring**: документируйте функции
4. **Избегайте побочных эффектов**: функция не должна изменять глобальное состояние без необходимости
5. **Типизируйте параметры**: используйте type hints для читаемости
6. **Обрабатывайте исключения**: используйте try-except для ошибок
7. **Проверяйте входные данные**: не доверяйте пользовательским данным
