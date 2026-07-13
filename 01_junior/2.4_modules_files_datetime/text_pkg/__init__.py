""" В text_pkg/__init__.py сделай `from .shout import shout`, чтобы
    её можно было импортировать прямо из пакета.
"""

from .shout import shout

__all__ = ["shout"]
