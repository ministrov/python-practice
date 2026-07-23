""" Модуль декоратора ограницивающий лимит вызова метода класса 

    Задачи:
        1. Создать декоратор limit_calls, который ограничивает количество вызовов метода.
        2. При превышении лимита вызовов вызывать исключение RuntimeError.
        3. Правильно передавать все данные, используя wrap.
"""

from functools import wraps
from typing import Callable, Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")
SelfT = TypeVar("SelfT")


def limit_calls(
    max_calls: int,
) -> Callable[
    [Callable[Concatenate[SelfT, P], T]], Callable[Concatenate[SelfT, P], T]
]:
    def decorator(
        func: Callable[Concatenate[SelfT, P], T],
    ) -> Callable[Concatenate[SelfT, P], T]:
        @wraps(func)
        def wrapper(self: SelfT, *args: P.args, **kwargs: P.kwargs) -> T:
            count_attr = f"_{func.__name__}_count"
            current: int = getattr(self, count_attr, 0)

            if current >= max_calls:
                raise RuntimeError("Call limit exceeded")
            setattr(self, count_attr, current + 1)
            print(
                f"[LOG] {func.__qualname__} called {current + 1} / {max_calls}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


class Engine:
    """ Двигатель """

    @limit_calls(max_calls=3)
    def start(self):
        """ Запуск двигателя """
        print("Двигатель запущен!")


car = Engine()

car.start()
car.start()

car.start()
car.start()
