""" Демо модуль по базовому объектно-ориентированному программированию"""


from datetime import date


class Task:
    """ Задача """
    done: bool = False
    title: str

    def set_info(self, text: str):
        """ Установка title """
        self.title = text

    def get_info(self):
        """ Получение данных задачи """
        print("Задача")


task = Task()
task.set_info("Сделать лекцию")
print(task.get_info())


""" Пример авторизации """


class Auth:
    is_auth = False

    def login(self):
        """ Вход """
        self.is_auth = True

    def logout(self):
        """ Выход """
        self.is_auth = False


auth_service = Auth()
auth_service.login()
print(auth_service.is_auth)


class Note:
    def __init__(self) -> None:
        print("Создана новая заметка!")


note = Note()
print(note)

""" Пример статического метода """


class Book:
    """ Книга """

    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    @staticmethod
    def years_since(year: int):
        """ Метод получения возраста книги """
        return date.today().year - year


book = Book("Первая книга", 1998)
print(Book.years_since(book.year))

""" Пример декоратора @property """


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect_a = Rectangle(10, 5)
print(rect_a.height)
print(rect_a.width)
print(rect_a.area)
