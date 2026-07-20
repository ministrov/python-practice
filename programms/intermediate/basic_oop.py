""" Демо модуль по базовому объектно-ориентированному программированию"""


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
