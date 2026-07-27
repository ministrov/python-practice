""" Модуль создания курсов с помощью наследования

    1. Создать класс Курса с ценой, названием, длительностью
    2. Реальзовать методы: 
        - узнать цену
        - вывести информацию
    3. Делаем курс с AI и тренажерами
        - можно рассчитать рассрочку на срок курса

    4. Делаем курс с проектом с параметром названия проекта
        - можно рассчмитать рассрочкку
        - можно вывести информацию опроекте
"""


class CreditMixin:
    """ Миксин рассчета кредита """
    price: int = 0
    course_length: float = 0

    def calculate_credit(self):
        return self.price / self.course_length


class Course:
    """ Обучающий курс """

    def __init__(self, title: str, price: int, course_length: int):
        self.price = price
        self.title = title
        self.course_length = course_length

    def get_price(self) -> int:
        return self.price

    def show_info(self) -> str:
        return (
            f"курс {self.title} по цене {self.price} "
            f"длительностью {self.course_length}"
        )


class AICourse(Course, CreditMixin):
    """ Обучающий курс по AI """
    pass


class ProjectCourse(Course, CreditMixin):
    """ Обучающий курс с проектом """

    def __init__(
        self, title: str, price: int, course_length: int, project_name: str
    ):
        super().__init__(title, price, course_length)
        self.project_name = project_name

    def get_project_info(self):
        return f"Проект: {self.project_name}"


course = ProjectCourse("Python", 10000, 2, "Калькулятор")
print(course.show_info())
print(course.get_project_info())
print(course.calculate_credit())
