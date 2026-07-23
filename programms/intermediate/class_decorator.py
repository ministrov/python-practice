""" Модуль декоратора класса """

import functools
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def log_call(func: Callable[P, T]) -> Callable[P, T]:
    """ Логирует вызов"""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"[LOG] {func.__qualname__} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


class Service:
    """ Сервис (для примера декоратора класса)"""

    @log_call
    def process(self, x: float):
        return x * 2


service_a = Service()
service_a.process(10)
