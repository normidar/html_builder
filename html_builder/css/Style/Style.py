from abc import ABCMeta, abstractmethod
from . import CssObj

class Style(CssObj,metaclass=ABCMeta):
    def _get_str(self):
        return f'{self._get_key()}:{self._get_value()};'

    @abstractmethod
    def _get_key(self):
        ...

    @abstractmethod
    def _get_value(self):
        ...
