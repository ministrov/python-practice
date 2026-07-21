# -*- coding: utf-8 -*-
"""
Блок 2.5.3: Практика — наследование, super(), MRO
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 05_inheritance_demo.py, если застрял с синтаксисом.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: простое наследование без переопределений")
print("=" * 60)
print("""
1.1 Создай класс Vehicle с __init__(self, brand: str) и методом
    info(self) -> str, возвращающим f"Транспорт: {brand}".
1.2 Создай класс Car(Vehicle), который ничего не переопределяет.
1.3 Создай экземпляр Car("Toyota"), напечатай info() и проверь
    isinstance(car, Vehicle) — должно быть True.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: переопределение метода (override)")
print("=" * 60)
print("""
2.1 Используя Vehicle из задания 1, создай класс Motorcycle(Vehicle)
    со своей версией info(self) -> str, возвращающей
    f"Мотоцикл: {brand}" (ПОЛНОСТЬЮ своя реализация, без super()).
2.2 Создай Motorcycle("Harley"), напечатай info() — должна вывестись
    версия Motorcycle, не Vehicle.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: super() — вызов версии родителя внутри переопределения")
print("=" * 60)
print("""
3.1 Используя Vehicle из задания 1, создай класс Truck(Vehicle) с
    info(self) -> str, который берёт результат super().info() и
    добавляет к нему " (грузовой)".
3.2 Создай Truck("Volvo"), напечатай info() — должно получиться
    "Транспорт: Volvo (грузовой)".
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: super().__init__() — дополнение конструктора родителя")
print("=" * 60)
print("""
4.1 Создай класс Person с __init__(self, name: str, age: int).
4.2 Создай класс Student(Person) с __init__(self, name: str,
    age: int, school: str), который вызывает super().__init__(name,
    age), а затем сохраняет self.school = school.
4.3 Добавь Student метод describe(self) -> str, возвращающий строку
    вида "<name>, <age> лет, учится в <school>".
4.4 Создай Student("Аня", 20, "МГУ"), напечатай describe().
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: несколько уровней наследования + super() в каждом")
print("=" * 60)
print("""
5.1 Используя Person и Student из задания 4, создай класс
    Graduate(Student) с __init__(self, name: str, age: int,
    school: str, degree: str), вызывающим super().__init__(name,
    age, school), затем сохраняющим self.degree = degree.
5.2 Переопредели describe(self) в Graduate: возьми super().describe()
    и добавь f" ({degree})".
5.3 Создай Graduate("Борис", 24, "МГТУ", "магистр"), напечатай
    describe() — должна собраться строка из ВСЕХ трёх уровней
    (Person -> Student -> Graduate).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: isinstance() и issubclass() на иерархии из 3 уровней")
print("=" * 60)
print("""
6.1 Используя Person, Student, Graduate из заданий 4-5, создай
    Graduate("Вера", 23, "СПбГУ", "бакалавр").
6.2 Проверь и напечатай: isinstance(grad, Graduate),
    isinstance(grad, Student), isinstance(grad, Person).
6.3 Проверь и напечатай: issubclass(Graduate, Person),
    issubclass(Person, Graduate) (должно быть True, True, False).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: MRO при множественном наследовании")
print("=" * 60)
print("""
7.1 Создай класс Walker с методом move(self) -> str, возвращающим
    "идёт пешком".
7.2 Создай класс Swimmer с методом move(self) -> str, возвращающим
    "плывёт".
7.3 Создай класс Triathlete(Walker, Swimmer), НЕ переопределяющий
    move().
7.4 Создай экземпляр Triathlete, напечатай move() — объясни в
    комментарии, ПОЧЕМУ вывелся именно этот результат (какой класс
    в списке родителей стоит первым).
7.5 Напечатай [cls.__name__ for cls in Triathlete.__mro__].
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: комплексное — банковские счета с наследованием")
print("=" * 60)
print("""
8.1 Создай класс Account с __init__(self, owner: str,
    balance: float = 0.0), методом deposit(self, amount: float)
    -> None (увеличивает balance) и методом describe(self) -> str,
    возвращающим f"{owner}: {balance}".
8.2 Создай класс SavingsAccount(Account) с __init__(self, owner: str,
    balance: float, interest_rate: float), вызывающим
    super().__init__(owner, balance), сохраняющим self.interest_rate.
8.3 Добавь SavingsAccount метод add_interest(self) -> None,
    увеличивающий balance на balance * interest_rate (используй
    self.deposit(...) внутри, а не self.balance += ... напрямую).
8.4 Переопредели describe(self) в SavingsAccount: возьми
    super().describe() и добавь f", ставка {interest_rate}".
8.5 Создай SavingsAccount("Олег", 1000, 0.05), вызови add_interest(),
    напечатай balance и describe().
""")

# ТВОЙ КОД ЗДЕСЬ:
