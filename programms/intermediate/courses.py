""" Модуль создания курсов с помощью наследования

    1. Создать класс Курса с ценой, названием, длительностью
    2. Реальзовать методы: 
        - узнать цену
        - вывести информацию
    3. Делаем курс с AI и тренажерами
        - можно рассчитать рассрочку на срок курса

    4. Делаем курс с проектом  с параметром названия проекта
        - можно рассчмитать рассрочкку
        - можно вывести информацию опроекте
"""


class Course:
    def __init__(self, price: int, title: str, time_length: int):
        self.price = price
        self.title = title
        self.time_length = time_length

    def get_price(self) -> int:
        return self.price

    def show_info(self) -> str:
        return f"{self.price}, {self.title}, {self.time_length}"
