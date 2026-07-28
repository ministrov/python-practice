"""
    Практика использования протоколов в Python:

    Цель:
    Создать два типа хранилищ данных: в памяти (memory storage) и в файле (file storage).
    Использовать протоколы для стандартизации методов хранилищ.
    Протокол Storage:
    Определяет стандартизированные методы save и load.
    save(self, data: str) -> None: сохраняет данные.
    load(self) -> str: загружает данные.
    Реализация хранилищ:
    Memory Storage:
    Хранит данные в атрибуте класса.
    Методы: save, который сохраняет строку в переменную, и load, который возвращает сохраненные данные.
    File Storage:
    Хранит данные в файле data.txt.
    Методы: save, который записывает данные в файл, и load, который читает данные из файла.
    Функция useStorage:
    Принимает объект хранилища и данные.
    Использует методы save и load для записи и немедленного чтения данных.
    Возвращает прочитанные данные.
    Тестирование:
    Создаются экземпляры MemoryStorage и FileStorage.
    Получая пользовательский ввод, данные передаются в useStorage.
    Результаты сохраняются и загружаются с помощью обоих типов хранилищ.
    Проверка корректности работы путем вывода результатов и проверки содержимого файла.
    Этот пример демонстрирует, как использовать протоколы для разделения логики хранения данных между разными реализациями.
"""

from typing import Protocol


class Storage(Protocol):
    """ Протокол хранения """

    def save(self, data: str) -> None: ...
    def load(self) -> str: ...


class MemoryStorage:
    """ Хранение в памяти """

    def save(self, data: str) -> None:
        self.data = data

    def load(self):
        return getattr(self, "data", "")


class FileStorage:
    """ Хранение в файле """

    def save(self, data: str) -> None:
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write(data)

    def load(self):
        with open("data.txt", "r", encoding="utf-8") as f:
            return f.read()


def use_storage(storage: Storage, data: str):
    storage.save(data)
    return storage.load()


memory = MemoryStorage()
file_storage = FileStorage()

user_input = input("Введите данные: ")
print(use_storage(memory, user_input))
print(use_storage(file_storage, user_input))
