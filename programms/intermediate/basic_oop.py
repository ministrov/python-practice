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
