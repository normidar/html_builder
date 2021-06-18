from abc import ABCMeta, abstractmethod

class TextStyle(Style,metaclass=ABCMeta):
    ...

class TextAlign(TextStyle):
    @classmethod
    def center(cls):
        cls.value = 'center'

    @classmethod
    def left(cls):
        cls.value = 'left'

    @classmethod
    def right(cls):
        cls.value = 'right'

    @classmethod
    def justify(cls):
        """实现两端对齐文本效果。"""
        cls.value = 'justify'

    @classmethod
    def inherit(cls):
        """规定应该从父元素继承 text-align 属性的值。"""
        cls.value = 'inherit'

    def __init__(self):
        self.value = 'left'

    def _get_key(self):
        return 'text-align'

    def _get_value(self):
        return self.value


