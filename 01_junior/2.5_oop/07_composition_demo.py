# -*- coding: utf-8 -*-
"""
Блок 2.5.4: Демо — композиция vs наследование
════════════════════════════════════════════════════════════════════════
Темы:
  1. Наследование = "Х ЕСТЬ разновидность Y" (is-a)
  2. Композиция = "Х ИМЕЕТ внутри Y" (has-a) — объект хранит другой
     объект и делегирует ему работу, вместо того чтобы наследоваться
  3. Когда наследование ломается: комбинации, которые не выражаются
     одной иерархией классов
  4. Композиция чинит это: поведение можно подменять в рантайме,
     не создавая новый класс на каждую комбинацию
  5. Правило: "Б — это разновидность А, или Б использует А?"
"""


# ════════════════════════════════════════════════════════════════════════
# 1. Наследование — оправдано, когда связь ДЕЙСТВИТЕЛЬНО "is-a"
# ════════════════════════════════════════════════════════════════════════

class Course:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def show_info(self) -> str:
        return f"{self.title}: {self.price}"


class AICourse(Course):
    # AICourse ЕСТЬ Course — просто разновидность с тем же "устройством"
    pass


ai_course = AICourse("Python + AI", 5000)
print(ai_course.show_info())   # Python + AI: 5000


# ════════════════════════════════════════════════════════════════════════
# 2. Наследование — ломается, когда пытаемся выразить им "has" вместо "is"
# ════════════════════════════════════════════════════════════════════════

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class DiscountedProduct(Product):
    # "товар со скидкой ЕСТЬ товар"? Работает, пока скидка ОДНА.
    def __init__(self, name: str, price: float, percent: float) -> None:
        super().__init__(name, price)
        self.percent = percent

    def final_price(self) -> float:
        return self.price * (1 - self.percent / 100)


sale_shirt = DiscountedProduct("Футболка", 1000, 20)
print(sale_shirt.final_price())   # 800.0

# Проблема: если появится вторая скидка (промокод + чёрная пятница),
# наследованием это не выразить без нового класса на КАЖДУЮ комбинацию:
# PromoDiscountedProduct, BulkPromoDiscountedProduct, ...


# ════════════════════════════════════════════════════════════════════════
# 3. То же самое через композицию — Product ИМЕЕТ стратегию скидки
# ════════════════════════════════════════════════════════════════════════

class DiscountStrategy:
    """Базовый интерфейс скидки — сам по себе не используется."""

    def apply(self, price: float) -> float:
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price


class PercentDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.percent = percent

    def apply(self, price: float) -> float:
        return price * (1 - self.percent / 100)


class SmartProduct:
    def __init__(
        self, name: str, price: float, discount: DiscountStrategy
    ) -> None:
        self.name = name
        self.price = price
        self.discount = discount   # объект ХРАНИТСЯ внутри, не наследуется

    def final_price(self) -> float:
        # делегирование: расчёт скидки поручается ОБЪЕКТУ discount,
        # а не реализуется внутри SmartProduct напрямую
        return self.discount.apply(self.price)


plain_shirt = SmartProduct("Футболка", 1000, NoDiscount())
sale_shirt_v2 = SmartProduct("Футболка", 1000, PercentDiscount(20))
print(plain_shirt.final_price())     # 1000 — NoDiscount возвращает
                                      # price как есть, без float()
print(sale_shirt_v2.final_price())   # 800.0

# Новую скидку добавляем НЕ трогая SmartProduct вообще — просто
# пишем ещё один класс DiscountStrategy. Комбинации скидок собираются
# на лету (можно даже поменять discount у существующего объекта в
# рантайме), а не требуют нового класса-наследника на каждый случай.


# ════════════════════════════════════════════════════════════════════════
# 4. Композиция из нескольких независимых частей — заказ в магазине
# ════════════════════════════════════════════════════════════════════════

class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[SmartProduct] = []

    def add(self, product: SmartProduct) -> None:
        self.items.append(product)

    def total(self) -> float:
        return sum(item.final_price() for item in self.items)


class ShippingCalculator:
    def __init__(self, rate_per_kg: float) -> None:
        self.rate_per_kg = rate_per_kg

    def cost(self, weight_kg: float) -> float:
        return weight_kg * self.rate_per_kg


class Order:
    def __init__(
        self, cart: ShoppingCart, shipping: ShippingCalculator
    ) -> None:
        self.cart = cart            # Order ИМЕЕТ корзину
        self.shipping = shipping    # Order ИМЕЕТ калькулятор доставки

    def total_with_shipping(self, weight_kg: float) -> float:
        return self.cart.total() + self.shipping.cost(weight_kg)


cart = ShoppingCart()
cart.add(plain_shirt)
cart.add(sale_shirt_v2)

order = Order(cart, ShippingCalculator(rate_per_kg=50))
print(order.total_with_shipping(weight_kg=2))
# 1000.0 + 800.0 + 2*50 = 1900.0

# Order НЕ наследуется ни от ShoppingCart, ни от ShippingCalculator —
# он их ИСПОЛЬЗУЕТ. "Заказ — это разновидность корзины"? Бессмысленно.
# Значит здесь однозначно композиция, а не наследование.


# ════════════════════════════════════════════════════════════════════════
# 5. Правило проверки: "Б — это разновидность А, или Б использует А?"
# ════════════════════════════════════════════════════════════════════════

# "AI-курс — это разновидность курса"           -> ДА  -> наследование
# "Скидка — это разновидность товара"           -> НЕТ -> композиция
# "Заказ — это разновидность корзины"           -> НЕТ -> композиция
#
# В индустрии эта мысль оформлена как принцип "Composition over
# inheritance" — по умолчанию выбирают композицию чаще, чем кажется
# новичку, потому что наследование фиксирует связь МЕЖДУ КЛАССАМИ
# намертво в момент объявления класса, а объект внутри (как discount
# у SmartProduct) можно подменить в любой момент в рантайме.
