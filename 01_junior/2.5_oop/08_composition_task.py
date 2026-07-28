# -*- coding: utf-8 -*-
"""
Блок 2.5.4: Практика — композиция vs наследование
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 07_composition_demo.py, если застрял с синтаксисом.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: простая композиция — Engine внутри Car")
print("=" * 60)
print("""
1.1 Создай класс Engine с __init__(self, horsepower: int) и методом
    start(self) -> str, возвращающим f"Двигатель на {horsepower} л.с.
    заведён".
1.2 Создай класс Car с __init__(self, brand: str, engine: Engine) —
    Car ИМЕЕТ engine внутри себя (self.engine = engine), а не
    наследуется от Engine.
1.3 Добавь Car метод start(self) -> str, который делегирует вызов
    self.engine.start() и добавляет к результату f" ({self.brand})".
1.4 Создай Engine(200), затем Car("BMW", тот_же_engine), напечатай
    car.start().
""")

# ТВОЙ КОД ЗДЕСЬ:


class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Двигатель на {self.horsepower} л.с. заведён"


class Car:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine

    def start(self) -> str:
        return f"{self.engine.start()} ({self.brand})"


engine_200 = Engine(200)
bmw = Car("BMW", engine_200)
print(engine_200.start())
print(bmw.start())


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: почему это НЕ наследование — задай вопрос is-a")
print("=" * 60)
print("""
2.1 В комментарии (без кода) ответь: правда ли "Car ЕСТЬ Engine"?
    Объясни своими словами, почему тут композиция ("has-a"), а не
    наследование ("is-a") — используй пример из задания 1.
""")

# ТВОЙ КОД ЗДЕСЬ:
# Тут мы используем композицию, как я понял,
# потому что машина не является частным случаем двигателя,
# а просто его имеет внутри себя

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: стратегия — PaymentMethod внутри Order")
print("=" * 60)
print("""
3.1 Создай базовый класс PaymentMethod с методом pay(self, amount:
    float) -> str, который бросает NotImplementedError (это
    "интерфейс", сам по себе не используется).
3.2 Создай CardPayment(PaymentMethod) и CashPayment(PaymentMethod),
    каждый со своей реализацией pay(): CardPayment возвращает
    f"Оплата картой: {amount}", CashPayment — f"Оплата наличными:
    {amount}".
3.3 Создай класс Order с __init__(self, total: float, payment:
    PaymentMethod) — Order ИМЕЕТ payment внутри.
3.4 Добавь Order метод checkout(self) -> str, делегирующий вызов
    self.payment.pay(self.total).
3.5 Создай Order(1500, CardPayment()) и Order(300, CashPayment()),
    напечатай checkout() для обоих — тексты должны отличаться.
""")

# ТВОЙ КОД ЗДЕСЬ:


class PaymentMethod:
    def pay(self, amount: float) -> str:
        raise NotImplementedError(
            'это "интерфейс", сам по себе не используется')


class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата картой: {amount}"


class CashPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата наличными: {amount}"


class Order:
    def __init__(self, total: float, payment: PaymentMethod):
        self.total = total
        self.payment = payment

    def checkout(self):
        return self.payment.pay(self.total)


order_a = Order(1500, CardPayment())
order_b = Order(300, CashPayment())

print(order_a.checkout())
print(order_b.checkout())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: подмена объекта в рантайме — сила композиции")
print("=" * 60)
print("""
4.1 Используя Order и оба PaymentMethod из задания 3, создай
    order = Order(500, CashPayment()), напечатай checkout().
4.2 Присвой order.payment = CardPayment() (замени способ оплаты БЕЗ
    создания нового объекта Order), напечатай checkout() ещё раз —
    результат должен измениться. Так с наследованием сделать нельзя:
    класс объекта нельзя поменять после создания, а объект внутри —
    можно.
""")

# ТВОЙ КОД ЗДЕСЬ:
order = Order(500, CashPayment())
print(order.checkout())
order.payment = CardPayment()
print(order.checkout())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: несколько независимых частей — Invoice")
print("=" * 60)
print("""
5.1 Создай класс Customer с __init__(self, name: str, email: str).
5.2 Создай класс LineItems с __init__(self, items: list[float]) и
    методом total(self) -> float, возвращающим sum(self.items).
5.3 Создай класс Invoice с __init__(self, customer: Customer, items:
    LineItems) — Invoice ИМЕЕТ и customer, и items внутри (НЕ
    наследуется ни от одного из них).
5.4 Добавь Invoice метод summary(self) -> str, возвращающий
    f"{customer.name}: {items.total()}".
5.5 Создай Invoice с Customer("Аня", "a@mail.com") и LineItems([100,
    200, 50]), напечатай summary() — должно быть "Аня: 350".
""")

# ТВОЙ КОД ЗДЕСЬ:


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class LineItems:
    def __init__(self, items: list[float]):
        self.items = items

    def total(self) -> float:
        return sum(self.items)


class Invoice:
    def __init__(self, customer: Customer, items: LineItems):
        self.customer = customer
        self.items = items

    def summary(self):
        return f"{self.customer.name}: {self.items.total()}"


invoice_a = Invoice(Customer("Аня", "a@mail.com"), LineItems([100,
                                                              200, 50]))
print(invoice_a.summary())


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: когда наследование ВСЁ-ТАКИ уместно — контрпример")
print("=" * 60)
print("""
6.1 Создай класс Notification с __init__(self, message: str) и
    методом send(self) -> str, возвращающим f"Отправлено: {message}".
6.2 Создай EmailNotification(Notification) и SmsNotification(
    Notification) — оба ничего не переопределяют (просто разные
    типы уведомлений с ОДИНАКОВЫМ поведением).
6.3 В комментарии объясни: почему здесь наследование оправдано
    (в отличие от Order/PaymentMethod из задания 3) — какой ответ
    даёт вопрос "EmailNotification ЕСТЬ Notification?".
6.4 Создай оба класса с сообщением "Заказ отправлен", напечатай
    send() для обоих.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Notification:
    def __init__(self, message: str):
        self.message = message

    def send(self) -> str:
        return f"Отправлено: {self.message}"


class EmailNotification(Notification):
    pass


class SmsNotification(Notification):
    pass

# Потому что ответ на вопрос EmailNotification ЕСТЬ Notification? Да.
# Так как EmailNotification, является частным случаем Notification
# поэтому тут наследование, уместно


email_notification = EmailNotification("Заказ отправлен")
sms_notification = SmsNotification("Заказ отправлен")

print(email_notification.send())
print(sms_notification.send())


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: композиция ВНУТРИ иерархии наследования — миксуем оба")
print("=" * 60)
print("""
7.1 Используя PaymentMethod/CardPayment/CashPayment из задания 3,
    создай класс Product с __init__(self, name: str, price: float)
    (обычный класс, наследования пока нет).
7.2 Создай класс DigitalProduct(Product) — ЕСТЬ разновидность
    Product (наследование, is-a), с доп. атрибутом download_url:
    str в __init__.
7.3 Добавь DigitalProduct метод purchase(self, payment:
    PaymentMethod) -> str, который делегирует payment.pay(self.
    price) (композиция, has-a — PaymentMethod передаётся снаружи,
    а не наследуется).
7.4 Создай DigitalProduct("Курс Python", 2000, "http://example.com"),
    вызови purchase(CardPayment()), напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class DigitalProduct(Product):
    def __init__(self, name: str, price: float, download_url: str):
        super().__init__(name, price)
        self.download_url = download_url

    def purchase(self, payment: PaymentMethod) -> str:
        return payment.pay(self.price)


digital_product = DigitalProduct("Курс Python", 2000, "http://example.com")
print(digital_product.purchase(CardPayment()))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: комплексное — корзина + доставка + оплата без наследования")
print("=" * 60)
print("""
8.1 Используя Product из задания 7, создай класс Cart с __init__(
    self) -> None, атрибутом self.items: list[Product] = [], методом
    add(self, product: Product) -> None и методом total(self) ->
    float (сумма price всех товаров).
8.2 Создай класс Shipping с __init__(self, price: float) и методом
    cost(self) -> float, возвращающим self.price.
8.3 Создай класс Checkout с __init__(self, cart: Cart, shipping:
    Shipping, payment: PaymentMethod) — три НЕЗАВИСИМЫХ объекта
    внутри, без наследования ни от одного.
8.4 Добавь Checkout метод complete(self) -> str, который считает
    grand_total = cart.total() + shipping.cost(), затем возвращает
    результат self.payment.pay(grand_total).
8.5 Собери Cart с двумя Product, Shipping(200), CardPayment() в
    Checkout, вызови complete(), напечатай результат.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Cart:
    def __init__(self) -> None:
        self.items: list[Product] = []

    def add(self, product: Product) -> None:
        self.items.append(product)

    def total(self) -> float:
        return sum(item.price for item in self.items)
