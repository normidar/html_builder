from abc import ABCMeta, abstractmethod


class Value(metaclass=ABCMeta):
    
    @abstractmethod
    def _get_str(self):
        ...

    def __str__(self):
        return self._get_str()