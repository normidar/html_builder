from abc import ABCMeta, abstractmethod
from . import Style
from html_builder.css.Color import Color

class ColorStyle(Style,metaclass=ABCMeta):
    def _get_value(self):
        return self.value


class BackgroundColor(ColorStyle):
    def __init__(self,color: Color):
        self.color = str(color)

    def _get_key(self):
        return 'background-color'
    
class ContextColor(ColorStyle):
    def __init__(self,color: Color):
        self.color = str(color)

    def _get_key(self):
        return 'color'