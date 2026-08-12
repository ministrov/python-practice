# -*- coding: utf-8 -*-
"""
Блок 2.5.7: Практика — абстракция (abc.ABC, @abstractmethod)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 13_abstraction_demo.py, если застрял с синтаксисом.
"""

from abc import ABC, abstractmethod


print("=" * 60)
print("ЗАДАНИЕ 1: базовый ABC + @abstractmethod")
print("=" * 60)
print("""
1.1 Создай абстрактный класс Animal(ABC) с абстрактным методом
    sound(self) -> str (тело метода — просто "...").
1.2 Попробуй создать Animal() напрямую, оберни в try/except TypeError
    as e, напечатай f"Ошибка: {e}".
""")

# ТВОЙ КОД ЗДЕСЬ:


class Animal(ABC):
    @abstractmethod
    def sound(self) -> str:
        ...


try:
    animal = Animal()  # type: ignore
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: конкретный наследник реализует контракт")
print("=" * 60)
print("""
2.1 Создай класс Dog(Animal), реализующий sound(self) -> str,
    возвращающий "Woof".
2.2 Создай Dog(), напечатай dog.sound().
""")

# ТВОЙ КОД ЗДЕСЬ:


class Dog(Animal):
    def sound(self) -> str:
        return "Woof"


dog = Dog()
print(dog.sound())


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: неполный наследник тоже не создаётся")
print("=" * 60)
print("""
3.1 Создай класс Cat(Animal), но НЕ переопределяй sound() (пустой
    класс, только наследующий Animal).
3.2 Попробуй создать Cat(), оберни в try/except TypeError as e,
    напечатай f"Ошибка: {e}".
""")

# ТВОЙ КОД ЗДЕСЬ:


class Cat(Animal):
    pass


try:
    cat = Cat()  # type: ignore  # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: абстрактный метод + обычный шаблонный метод")
print("=" * 60)
print("""
4.1 Создай абстрактный класс Notifier(ABC) с абстрактным методом
    send(self, message: str) -> None.
4.2 Добавь в Notifier обычный (НЕ абстрактный) метод
    notify_all(self, messages: list[str]) -> None, который вызывает
    self.send(message) для каждого сообщения из списка.
4.3 Создай класс ConsoleNotifier(Notifier), реализующий send() как
    print(f"[Console] {message}").
4.4 Создай ConsoleNotifier(), вызови notify_all(["Привет", "Пока"]).
""")

# ТВОЙ КОД ЗДЕСЬ:


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        ...

    def notify_all(self, messages: list[str]) -> None:
        for message in messages:
            self.send(message)


class ConsoleNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Console] {message}")


console_notifier = ConsoleNotifier()
console_notifier.notify_all(["Привет", "Пока"])

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: несколько абстрактных методов сразу")
print("=" * 60)
print("""
5.1 Создай абстрактный класс Employee(ABC) с ДВУМЯ абстрактными
    методами: monthly_salary(self) -> float и role(self) -> str.
5.2 Создай класс Manager(Employee), реализующий ТОЛЬКО
    monthly_salary() (role() забыт намеренно).
5.3 Попробуй создать Manager(...), оберни в try/except TypeError as e,
    напечатай f"Ошибка: {e}" — убедись, что реализации ОДНОГО из двух
    абстрактных методов недостаточно.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Employee(ABC):
    @abstractmethod
    def monthly_salary(self) -> float:
        ...

    @abstractmethod
    def role(self) -> str:
        ...


class Manager(Employee):
    def monthly_salary(self) -> float:
        return 5000.0
    # role() намеренно не реализован


try:
    manager = Manager()  # type: ignore  # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: @property + @abstractmethod")
print("=" * 60)
print("""
6.1 Создай абстрактный класс Vehicle(ABC) с абстрактным СВОЙСТВОМ
    wheels (используй @property поверх @abstractmethod).
6.2 Создай класс Motorcycle(Vehicle), реализующий wheels как
    @property, возвращающий 2.
6.3 Создай Motorcycle(), напечатай motorcycle.wheels (без скобок —
    это свойство, а не метод).
""")

# ТВОЙ КОД ЗДЕСЬ:


class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self) -> int:
        ...


class Motorcycle(Vehicle):
    @property
    def wheels(self) -> int:
        return 2


motorcycle = Motorcycle()
print(motorcycle.wheels)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: полиморфизм через список общего типа")
print("=" * 60)
print("""
7.1 Используя Animal/Dog из заданий 1-2, создай ещё Bird(Animal)
    с sound(), возвращающим "Tweet".
7.2 Собери список animals: list[Animal] из Dog() и Bird().
7.3 Пройдись циклом for по списку, напечатай animal.sound() для
    каждого — код не должен знать заранее, какой это конкретный тип.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: комплексное — платёжные стратегии")
print("=" * 60)
print("""
8.1 Создай абстрактный класс PaymentMethod(ABC) с абстрактным методом
    pay(self, amount: float) -> None.
8.2 Добавь обычный метод checkout(self, amount: float) -> None,
    печатающий f"Оформление заказа на {amount}" и вызывающий
    self.pay(amount).
8.3 Создай CardPayment(PaymentMethod) и CashPayment(PaymentMethod),
    каждый реализует pay() по-своему (печатает свой способ оплаты).
8.4 Создай список methods: list[PaymentMethod] из обоих способов,
    пройдись циклом, вызови checkout(100) для каждого.
""")

# ТВОЙ КОД ЗДЕСЬ:
